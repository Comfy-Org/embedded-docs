#!/usr/bin/env python3
"""Regression coverage for scanner-compatible documentation extraction."""
import sys
import textwrap
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from generate_docs import NodeInfoExtractor


class SchemaExtractionTests(unittest.TestCase):
    def extractor(self, source):
        extractor = NodeInfoExtractor(Path('unused.py'))
        extractor.content = textwrap.dedent(source)
        return extractor

    def test_schema_id_spellings(self):
        for declaration, argument in [
            ('', 'node_id="Target",'),
            ('NODE_ID = "Target"', 'node_id=cls.NODE_ID,'),
            ('NodeId = "Target"', ''),
        ]:
            with self.subTest(declaration=declaration):
                e = self.extractor(f'''
                    class DifferentClass:
                        {declaration}
                        @classmethod
                        def define_schema(cls):
                            return IO.Schema({argument} inputs=[IO.Image.Input(
                                "image")], outputs=[IO.Image.Output()])
                ''')
                info = e.extract_new_api_node('Target')
                self.assertEqual(info['class_name'], 'DifferentClass')
                self.assertEqual([i['name'] for i in info['inputs']], ['image'])
                self.assertEqual(info['outputs'], [{'type': 'IMAGE', 'name': 'IMAGE'}])

    def test_inherited_schema_and_super_mutation(self):
        source = '''
            class Base:
                NODE_ID = "Base"
                @classmethod
                def define_schema(cls):
                    return io.Schema(node_id=cls.NODE_ID, inputs=[io.Image.Input("image")])
            class Child(Base):
                NODE_ID = "Target"
        '''
        for suffix in ['', '''
    @classmethod
    def define_schema(cls):
        schema = super().define_schema()
        schema.node_id = "Target"
        return schema
''']:
            with self.subTest(suffix=suffix):
                e = self.extractor(source)
                e.content += suffix
                info = e.extract_new_api_node('Target')
                self.assertEqual(info['class_name'], 'Child')
                self.assertEqual([i['name'] for i in info['inputs']], ['image'])

    def test_factory_and_shared_input_helper(self):
        e = self.extractor('''
            def shared_inputs():
                return [IO.String.Input("prompt")]
            def _cloud_schema(node_id, inputs):
                return IO.Schema(node_id=node_id, inputs=inputs)
            class Cloud:
                @classmethod
                def define_schema(cls):
                    return _cloud_schema("Target", shared_inputs())
        ''')
        self.assertEqual(e.extract_new_api_node('Target')['inputs'][0]['name'], 'prompt')

    def test_classic_registry_alias_and_named_inputs(self):
        e = self.extractor('''
            class CombineHooks:
                @classmethod
                def INPUT_TYPES(cls):
                    inputs = {"hooks": ("HOOKS",)}
                    return {"required": inputs}
            NODE_CLASS_MAPPINGS = {"CombineHooks2": CombineHooks}
        ''')
        info = e.extract_classic_node('CombineHooks2')
        self.assertEqual(info['node_name'], 'CombineHooks2')
        self.assertEqual(info['class_name'], 'CombineHooks')
        self.assertEqual(info['inputs'][0]['name'], 'hooks')

    def test_literal_fast_path_is_preserved(self):
        e = self.extractor('''
            class Target:
                def define_schema(cls):
                    return io.Schema(node_id="Target", inputs=[io.Image.Input("image")])
        ''')
        with patch.object(e, '_extract_resolved_schema', side_effect=AssertionError('fallback')):
            self.assertEqual(e.extract_new_api_node('Target')['inputs'][0]['name'], 'image')

    def test_classic_nodeid_alias(self):
        e = self.extractor('''
            class CombineHooks:
                NodeId = "CombineHooks2"
                @classmethod
                def INPUT_TYPES(cls):
                    return {"optional": {"hooks": ("HOOKS",)}}
        ''')
        info = e.extract_classic_node('CombineHooks2')
        self.assertEqual(info['class_name'], 'CombineHooks')
        self.assertEqual(info['inputs'][0]['name'], 'hooks')


if __name__ == '__main__':
    unittest.main()
