#!/usr/bin/env python3
"""Unit tests for scripts.sync_to_comfy_docs normalization helpers.

Covers the CodeRabbit review fixes: inline-code stashing, curly-brace
escaping, whitespace-preserving < escaping, description extraction
(image/table skipping, e.g. protection), acronym-preserving labels,
and non-destructive nav purge.
"""

import os
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(REPO_ROOT / "scripts"))

os.environ.setdefault("TARGET_DOCS", str(REPO_ROOT / ".." / "docs"))
os.environ.setdefault("COMFYUI_PATH", "")

from scripts import sync_to_comfy_docs as sc  # noqa: E402


class SegToLabelTests(unittest.TestCase):
    def test_title_cases_underscores(self):
        self.assertEqual(sc._seg_to_label("custom_sampling"), "Custom Sampling")

    def test_preserves_acronyms(self):
        self.assertEqual(sc._seg_to_label("SDXL"), "SDXL")
        self.assertEqual(sc._seg_to_label("API_node"), "API Node")
        self.assertEqual(sc._seg_to_label("bfl_flux"), "Bfl Flux")


class NormalizeMdxTests(unittest.TestCase):
    def test_inline_code_preserved(self):
        out = sc._normalize_mdx_content("Use `x <= 10` for limits.")
        self.assertIn("`x <= 10`", out)
        self.assertNotIn("&lt;=", out.split("`")[1])

    def test_fenced_code_preserved_verbatim(self):
        out = sc._normalize_mdx_content("```python\nif x <= 10: print({1})\n```")
        self.assertIn("if x <= 10: print({1})", out)

    def test_curly_braces_escaped_in_prose(self):
        out = sc._normalize_mdx_content("The bbox {x, y} syntax.")
        self.assertIn("&#123;x, y&#125;", out)

    def test_curly_braces_not_escaped_in_code(self):
        out = sc._normalize_mdx_content("```json\n{\"a\": 1}\n```")
        self.assertIn('{"a": 1}', out)

    def test_whitespace_after_lt_preserved(self):
        out = sc._normalize_mdx_content("text < more")
        self.assertIn("text &lt; more", out)

    def test_paired_mintlify_component_kept(self):
        out = sc._normalize_mdx_content("<Note>\nHeads up.\n</Note>")
        self.assertIn("<Note>", out)
        self.assertIn("</Note>", out)

    def test_orphaned_closing_tag_escaped(self):
        out = sc._normalize_mdx_content("text </Note> more")
        self.assertIn("&lt;/Note>", out)


class DescriptionExtractionTests(unittest.TestCase):
    def test_skips_image_and_table_lines(self):
        content = "![img](x.png)\n\n| A | B |\n|---|---|\n\nThis is the first sentence. Second sentence."
        desc = sc.get_description_from_content(content)
        self.assertTrue(desc.startswith("This is the first sentence."))

    def test_does_not_cut_abbreviations(self):
        desc = sc.get_description_from_content("This is a test e.g. with abbreviations. Second sentence.")
        self.assertTrue(desc.startswith("This is a test e.g."))

    def test_cjk_sentence_break(self):
        desc = sc.get_description_from_content("这是第一句话。第二句话。")
        self.assertEqual(desc, "这是第一句话。")

    def test_truncation_aligned_to_180(self):
        long = "Word " * 100
        desc = sc.get_description_from_content(long)
        self.assertLessEqual(len(desc), 180)


class PurgeNavTests(unittest.TestCase):
    def _fake_locale(self):
        """Point the en locale's builtin_dir at a temp dir with a real .mdx file."""
        tmp = tempfile.TemporaryDirectory()
        self.addCleanup(tmp.cleanup)
        builtin_dir = Path(tmp.name) / "built-in-nodes"
        builtin_dir.mkdir()
        (builtin_dir / "CLIPTextEncodeControlnet.mdx").write_text("---\n---\n", encoding="utf-8")
        orig = sc.LOCALE_CONFIGS[0]["builtin_dir"]
        sc.LOCALE_CONFIGS[0]["builtin_dir"] = builtin_dir
        self.addCleanup(lambda: sc.LOCALE_CONFIGS[0].__setitem__("builtin_dir", orig))
        # Drop any cached listing for the original dir so the fake dir is used
        sc._locale_mdx_names.cache_clear()
        return builtin_dir

    def test_replaces_canonical_when_mdx_exists(self):
        self._fake_locale()
        nav = [{
            "group": "Nodes",
            "pages": [
                "built-in-nodes/ClipTextEncodeControlnet",
                "built-in-nodes/KSampler",
            ],
        }]
        sc._purge_noncanonical_nav_pages(nav)
        keys = sc.collect_page_keys(nav)
        self.assertIn("built-in-nodes/CLIPTextEncodeControlnet", keys)
        self.assertNotIn("built-in-nodes/ClipTextEncodeControlnet", keys)
        self.assertIn("built-in-nodes/KSampler", keys)

    def test_keeps_unknown_key_without_mdx(self):
        self._fake_locale()
        nav = [{"group": "Nodes", "pages": ["built-in-nodes/NonexistentNodeXYZ"]}]
        sc._purge_noncanonical_nav_pages(nav)
        keys = sc.collect_page_keys(nav)
        self.assertIn("built-in-nodes/NonexistentNodeXYZ", keys)


class FrontmatterTests(unittest.TestCase):
    def test_concrete_description_used(self):
        fm = sc.build_frontmatter("Canny", "Extract all edge lines from photos.")
        self.assertIn("Extract all edge lines from photos.", fm)
        self.assertNotIn("Complete documentation for the Canny node", fm)

    def test_template_fallback_when_empty(self):
        fm = sc.build_frontmatter("Canny", "")
        self.assertIn("Complete documentation for the Canny node", fm)


if __name__ == "__main__":
    unittest.main()
