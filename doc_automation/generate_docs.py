#!/usr/bin/env python3
"""
Auto-extract information from ComfyUI node source code and generate basic documentation
"""

import os
import re
import ast
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
import inspect
from dotenv import load_dotenv

# Load environment variables
env_path = Path(__file__).parent.parent / '.env'
load_dotenv(env_path)

# Get paths from environment variables
COMFYUI_PATH = Path(os.getenv('COMFYUI_PATH'))
EMBEDDED_DOCS_PATH = Path(os.getenv('EMBEDDED_DOCS_PATH'))
DOCS_PATH = EMBEDDED_DOCS_PATH / "comfyui_embedded_docs" / "docs"


class NodeInfoExtractor:
    """Node information extractor"""
    
    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.content = ""
        self.node_info = {}
        
    def read_file(self):
        """Read file content"""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                self.content = f.read()
            return True
        except Exception as e:
            print(f"❌ Unable to read file {self.file_path}: {e}")
            return False
    
    def extract_new_api_node(self, node_name: str) -> Optional[Dict[str, Any]]:
        """Extract new API (io.Schema) node information"""
        try:
            # Find Schema definition corresponding to node_id
            pattern = rf'node_id\s*=\s*["\']({re.escape(node_name)})["\']'
            match = re.search(pattern, self.content)
            if not match:
                return None
            
            # Find corresponding define_schema method
            schema_start = match.start()
            lines_before = self.content[:schema_start].split('\n')
            
            # Find class definition
            class_name = None
            for line in reversed(lines_before):
                class_match = re.search(r'class\s+(\w+)', line)
                if class_match:
                    class_name = class_match.group(1)
                    break
            
            if not class_name:
                return None
            
            # Extract Schema content
            info = {
                'node_name': node_name,
                'class_name': class_name,
                'type': 'new_api',
                'inputs': [],
                'outputs': [],
                'category': None,
                'description': None
            }
            
            # Extract category
            category_match = re.search(r'category\s*=\s*["\']([^"\']+)["\']', self.content[schema_start:schema_start+2000])
            if category_match:
                info['category'] = category_match.group(1)
            
            # Extract inputs
            inputs_section = re.search(r'inputs\s*=\s*\[(.*?)\]', self.content[schema_start:schema_start+3000], re.DOTALL)
            if inputs_section:
                inputs_text = inputs_section.group(1)
                info['inputs'] = self._parse_io_schema_inputs(inputs_text)
            
            # Extract outputs
            outputs_section = re.search(r'outputs\s*=\s*\[(.*?)\]', self.content[schema_start:schema_start+2000], re.DOTALL)
            if outputs_section:
                outputs_text = outputs_section.group(1)
                info['outputs'] = self._parse_io_schema_outputs(outputs_text)
            
            return info
            
        except Exception as e:
            print(f"⚠️  Failed to extract new API node {node_name} information: {e}")
            return None
    
    def _parse_io_schema_inputs(self, inputs_text: str) -> List[Dict[str, Any]]:
        """Parse io.Schema inputs"""
        inputs = []
        
        # Match various Input types
        # e.g.: io.Clip.Input("clip")
        # io.String.Input("tags", multiline=True, default="xxx")
        # io.Float.Input("strength", default=1.0, min=0.0, max=10.0)
        
        input_patterns = [
            r'io\.(\w+)\.Input\(["\']([^"\']+)["\']([^)]*)\)',
        ]
        
        for pattern in input_patterns:
            for match in re.finditer(pattern, inputs_text):
                data_type = match.group(1).upper()
                param_name = match.group(2)
                params_str = match.group(3)
                
                input_info = {
                    'name': param_name,
                    'type': data_type,
                    'required': True,
                    'default': None,
                    'min': None,
                    'max': None,
                    'step': None,
                    'multiline': False,
                    'tooltip': None
                }
                
                # Extract parameters
                if 'default' in params_str:
                    default_match = re.search(r'default\s*=\s*([^,)]+)', params_str)
                    if default_match:
                        input_info['default'] = default_match.group(1).strip()
                
                if 'min' in params_str:
                    min_match = re.search(r'min\s*=\s*([^,)]+)', params_str)
                    if min_match:
                        input_info['min'] = min_match.group(1).strip()
                
                if 'max' in params_str:
                    max_match = re.search(r'max\s*=\s*([^,)]+)', params_str)
                    if max_match:
                        input_info['max'] = max_match.group(1).strip()
                
                if 'step' in params_str:
                    step_match = re.search(r'step\s*=\s*([^,)]+)', params_str)
                    if step_match:
                        input_info['step'] = step_match.group(1).strip()
                
                if 'multiline=True' in params_str:
                    input_info['multiline'] = True
                
                if 'tooltip' in params_str:
                    tooltip_match = re.search(r'tooltip\s*=\s*["\']([^"\']+)["\']', params_str)
                    if tooltip_match:
                        input_info['tooltip'] = tooltip_match.group(1)
                
                inputs.append(input_info)
        
        return inputs
    
    def _parse_io_schema_outputs(self, outputs_text: str) -> List[Dict[str, Any]]:
        """Parse io.Schema outputs"""
        outputs = []
        
        # Match io.XXX.Output()
        output_pattern = r'io\.(\w+)\.Output\(\)'
        
        for match in re.finditer(output_pattern, outputs_text):
            data_type = match.group(1).upper()
            outputs.append({
                'type': data_type,
                'name': data_type  # Default to using type as name
            })
        
        return outputs
    
    def extract_classic_node(self, class_name: str) -> Optional[Dict[str, Any]]:
        """Extract classic node (INPUT_TYPES) information"""
        try:
            # Parse using AST
            tree = ast.parse(self.content)
            
            for node in ast.walk(tree):
                if isinstance(node, ast.ClassDef) and node.name == class_name:
                    info = {
                        'node_name': class_name,
                        'class_name': class_name,
                        'type': 'classic',
                        'inputs': [],
                        'outputs': [],
                        'category': None,
                        'description': None,
                        'class_docstring': ast.get_docstring(node),  # Extract class docstring
                        'return_names': []
                    }
                    
                    # Find various class attributes
                    for item in node.body:
                        if isinstance(item, ast.FunctionDef) and item.name == 'INPUT_TYPES':
                            info['inputs'] = self._parse_classic_input_types(item)
                        
                        elif isinstance(item, ast.Assign):
                            # Find RETURN_TYPES
                            for target in item.targets:
                                if isinstance(target, ast.Name) and target.id == 'RETURN_TYPES':
                                    info['outputs'] = self._parse_classic_return_types(item.value)
                                
                                # Find RETURN_NAMES
                                elif isinstance(target, ast.Name) and target.id == 'RETURN_NAMES':
                                    info['return_names'] = self._parse_classic_return_names(item.value)
                                
                                # Find CATEGORY
                                elif isinstance(target, ast.Name) and target.id == 'CATEGORY':
                                    if isinstance(item.value, ast.Constant):
                                        info['category'] = item.value.value
                                
                                # Find DESCRIPTION
                                elif isinstance(target, ast.Name) and target.id == 'DESCRIPTION':
                                    if isinstance(item.value, ast.Constant):
                                        info['description'] = item.value.value
                    
                    return info
            
            return None
            
        except Exception as e:
            print(f"⚠️  Failed to extract classic node {class_name} information: {e}")
            return None
    
    def _parse_classic_input_types(self, func_node: ast.FunctionDef) -> List[Dict[str, Any]]:
        """Parse INPUT_TYPES method - extract using regular expressions"""
        inputs = []
        
        # Find INPUT_TYPES method source code
        func_start = func_node.lineno
        func_end = func_node.end_lineno
        source_lines = self.content.split('\n')
        func_source = '\n'.join(source_lines[func_start-1:func_end])
        
        # Extract required and optional parameters
        for section in ['required', 'optional']:
            section_pattern = rf'"{section}"\s*:\s*\{{([^}}]*?)\}}'
            section_match = re.search(section_pattern, func_source, re.DOTALL)
            
            if section_match:
                section_content = section_match.group(1)
                # Extract each parameter
                param_pattern = r'"([^"]+)"\s*:\s*\((.*?)\)'
                
                for param_match in re.finditer(param_pattern, section_content, re.DOTALL):
                    param_name = param_match.group(1)
                    param_config = param_match.group(2)
                    
                    # Extract data type (first element)
                    type_match = re.search(r'IO\.(\w+)', param_config)
                    data_type = type_match.group(1).upper() if type_match else 'STRING'
                    
                    input_info = {
                        'name': param_name,
                        'type': data_type,
                        'required': (section == 'required'),
                        'default': None,
                        'min': None,
                        'max': None,
                        'step': None,
                        'options': None,
                        'multiline': False,
                        'tooltip': None
                    }
                    
                    # Extract values from config dictionary
                    if 'default' in param_config:
                        default_match = re.search(r'"default"\s*:\s*([^,}\n]+)', param_config)
                        if default_match:
                            input_info['default'] = default_match.group(1).strip().strip('"')
                    
                    if 'min' in param_config:
                        min_match = re.search(r'"min"\s*:\s*([^,}\n]+)', param_config)
                        if min_match:
                            input_info['min'] = min_match.group(1).strip()
                    
                    if 'max' in param_config:
                        max_match = re.search(r'"max"\s*:\s*([^,}\n]+)', param_config)
                        if max_match:
                            input_info['max'] = max_match.group(1).strip()
                    
                    if 'step' in param_config:
                        step_match = re.search(r'"step"\s*:\s*([^,}\n]+)', param_config)
                        if step_match:
                            input_info['step'] = step_match.group(1).strip()
                    
                    if 'options' in param_config:
                        options_match = re.search(r'"options"\s*:\s*\[([^\]]+)\]', param_config)
                        if options_match:
                            input_info['options'] = options_match.group(1).strip()
                    
                    if 'multiline' in param_config:
                        input_info['multiline'] = 'True' in param_config
                    
                    if 'tooltip' in param_config:
                        tooltip_match = re.search(r'"tooltip"\s*:\s*"([^"]*)"', param_config)
                        if tooltip_match:
                            input_info['tooltip'] = tooltip_match.group(1)
                    
                    inputs.append(input_info)
        
        return inputs
    
    def _parse_classic_return_types(self, value_node: ast.expr) -> List[Dict[str, Any]]:
        """Parse RETURN_TYPES"""
        outputs = []
        
        if isinstance(value_node, ast.Tuple):
            for elt in value_node.elts:
                if isinstance(elt, ast.Constant):
                    outputs.append({
                        'type': elt.value,
                        'name': elt.value
                    })
                elif isinstance(elt, ast.Attribute):
                    # Handle IO.IMAGE format
                    if isinstance(elt.value, ast.Name) and elt.value.id == 'IO':
                        outputs.append({
                            'type': elt.attr.upper(),
                            'name': elt.attr.upper()
                        })
        
        return outputs
    
    def _parse_classic_return_names(self, value_node: ast.expr) -> List[str]:
        """Parse RETURN_NAMES"""
        names = []
        
        if isinstance(value_node, ast.Tuple):
            for elt in value_node.elts:
                if isinstance(elt, ast.Constant):
                    names.append(elt.value)
        
        return names


class DocumentGenerator:
    """Documentation generator"""
    
    def __init__(self, node_info: Dict[str, Any]):
        self.info = node_info
    
    def generate_markdown(self) -> str:
        """Generate Markdown documentation"""
        doc_parts = []
        
        # 1. Function description (placeholder)
        doc_parts.append(self._generate_description())
        doc_parts.append("")
        
        # 2. How it works (placeholder)
        doc_parts.append("## How It Works")
        doc_parts.append("")
        doc_parts.append(self._generate_how_it_works())
        doc_parts.append("")
        
        # 3. Input parameters
        if self.info.get('inputs'):
            doc_parts.append("## Inputs")
            doc_parts.append("")
            doc_parts.append(self._generate_inputs_table())
            doc_parts.append("")
        
        # 4. Output results
        if self.info.get('outputs'):
            doc_parts.append("## Outputs")
            doc_parts.append("")
            doc_parts.append(self._generate_outputs_table())
            doc_parts.append("")
        
        return "\n".join(doc_parts)
    
    def _generate_description(self) -> str:
        """Generate function description"""
        node_name = self.info['node_name']
        category = self.info.get('category', 'utility')
        
        # Basic description template
        return f"This node performs operations in the {category} category. [Description to be added]"
    
    def _generate_how_it_works(self) -> str:
        """Generate how it works explanation"""
        return "[Detailed explanation of how this node works to be added]"
    
    def _generate_inputs_table(self) -> str:
        """Generate input parameters table"""
        if not self.info.get('inputs'):
            return ""
        
        lines = [
            "| Parameter | Data Type | Input Type | Default | Range | Description |",
            "|-----------|-----------|------------|---------|-------|-------------|"
        ]
        
        for inp in self.info['inputs']:
            param_name = f"`{inp['name']}`"
            data_type = inp['type']
            input_type = "Multiline text" if inp.get('multiline') else "Widget"
            default = inp.get('default', '-')
            
            # Build range
            range_str = '-'
            if inp.get('min') is not None and inp.get('max') is not None:
                range_str = f"{inp['min']} - {inp['max']}"
                if inp.get('step'):
                    range_str += f" (step: {inp['step']})"
            
            description = inp.get('tooltip', '[Description to be added]')
            
            lines.append(f"| {param_name} | {data_type} | {input_type} | {default} | {range_str} | {description} |")
        
        return "\n".join(lines)
    
    def _generate_outputs_table(self) -> str:
        """Generate output results table"""
        if not self.info.get('outputs'):
            return ""
        
        lines = [
            "| Output Name | Data Type | Description |",
            "|-------------|-----------|-------------|"
        ]
        
        for idx, out in enumerate(self.info['outputs'], 1):
            output_name = f"`{out['name']}`"
            data_type = out['type']
            description = "[Description to be added]"
            
            lines.append(f"| {output_name} | {data_type} | {description} |")
        
        return "\n".join(lines)
    


def generate_doc_for_node(node_name: str, file_path: Path, node_type: str) -> bool:
    """Generate documentation for a single node"""
    print(f"📝 Processing node: {node_name}")
    
    # 1. Extract node information
    extractor = NodeInfoExtractor(file_path)
    if not extractor.read_file():
        return False
    
    if node_type == 'new_api':
        node_info = extractor.extract_new_api_node(node_name)
    else:
        node_info = extractor.extract_classic_node(node_name)
    
    if not node_info:
        print(f"   ⚠️  Unable to extract node information")
        return False
    
    # 2. Generate documentation
    generator = DocumentGenerator(node_info)
    markdown_content = generator.generate_markdown()
    
    # 3. Save documentation
    doc_dir = DOCS_PATH / node_name
    doc_dir.mkdir(parents=True, exist_ok=True)
    
    doc_file = doc_dir / "en.md"
    with open(doc_file, 'w', encoding='utf-8') as f:
        f.write(markdown_content)
    
    print(f"   ✅ Documentation generated: {doc_file}")
    
    # 4. Save extracted raw information (for debugging)
    info_file = doc_dir / "_node_info.json"
    with open(info_file, 'w', encoding='utf-8') as f:
        json.dump(node_info, f, indent=2, ensure_ascii=False)
    
    return True


def main():
    """Main function"""
    import sys

    print("=" * 80)
    print("ComfyUI Node Documentation Auto-Generation Tool")
    print("=" * 80)
    print()

    # Read missing nodes report
    report_file = Path(__file__).parent / "missing_nodes_report.json"
    if not report_file.exists():
        print("❌ missing_nodes_report.json not found. Please run scan_missing_nodes.py first.")
        return

    with open(report_file, 'r', encoding='utf-8') as f:
        report = json.load(f)

    missing_nodes = report['missing_nodes']
    print(f"📊 Total missing node documentations: {len(missing_nodes)}\n")

    # Parse options from command line arguments
    nodes_to_process = []

    if len(sys.argv) > 1:
        mode = sys.argv[1]
        if mode == 'all':
            nodes_to_process = missing_nodes
        elif mode == 'test':
            count = int(sys.argv[2]) if len(sys.argv) > 2 else 10
            nodes_to_process = missing_nodes[:count]
        elif mode == 'node':
            if len(sys.argv) < 3:
                print("❌ Please specify node name: python3 generate_docs.py node <node_name>")
                return
            node_name = sys.argv[2]
            nodes_to_process = [n for n in missing_nodes if n['name'] == node_name]
            if not nodes_to_process:
                print(f"❌ Node not found: {node_name}")
                return
        else:
            print("❌ Invalid argument")
            print("Usage:")
            print("  python3 generate_docs.py test [count]    # Generate docs for first N nodes (default 10)")
            print("  python3 generate_docs.py all             # Generate docs for all missing nodes")
            print("  python3 generate_docs.py node <name>     # Generate docs for the specified node")
            return
    else:
        # Default: generate docs for the first 5 missing nodes for testing
        print("💡 Default test mode: generating docs for the first 5 missing nodes")
        print("   Use argument: test [count] | all | node <name>")
        print()
        nodes_to_process = missing_nodes[:5]

    print()
    print(f"🚀 Starting to generate documentation for {len(nodes_to_process)} nodes...")
    print()

    # Generate documentation
    success_count = 0
    failed_count = 0

    for node in nodes_to_process:
        node_name = node['name']
        file_path = COMFYUI_PATH / node['file']
        node_type = node['type']

        try:
            if generate_doc_for_node(node_name, file_path, node_type):
                success_count += 1
            else:
                failed_count += 1
        except Exception as e:
            print(f"   ❌ Generation failed: {e}")
            failed_count += 1

        print()

    # Summary
    print("=" * 80)
    print("📊 Generation completed")
    print("=" * 80)
    print(f"✅ Success: {success_count}")
    print(f"❌ Failed: {failed_count}")
    print()


if __name__ == "__main__":
    main()

