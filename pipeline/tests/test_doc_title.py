#!/usr/bin/env python3
"""Unit tests for lib.doc_title."""

import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from lib import doc_title as dt  # noqa: E402


class DocTitleTests(unittest.TestCase):
    def setUp(self):
        dt.load_node_translations.cache_clear()

    def test_strip_leading_h1_single(self):
        body = "# Old Title\n\nOverview text.\n\n## Inputs\n"
        self.assertEqual(dt.strip_leading_h1(body), "Overview text.\n\n## Inputs\n")

    def test_strip_leading_h1_multiple_and_no_space(self):
        body = "# First\n#Second\n\n# Third\n\nOverview.\n"
        self.assertEqual(dt.strip_leading_h1(body), "Overview.\n")

    def test_strip_leading_h1_preserves_h2(self):
        body = "## Not a title\n\nOverview.\n"
        self.assertEqual(dt.strip_leading_h1(body), body)

    def test_ensure_doc_title_fallback_to_node_name(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "node_translations.json"
            path.write_text("{}", encoding="utf-8")
            with patch.object(dt, "NODE_TRANSLATIONS", path):
                dt.load_node_translations.cache_clear()
                out = dt.ensure_doc_title("Overview paragraph.", "KSampler", "en")
                self.assertEqual(out, "# KSampler\n\nOverview paragraph.")

    def test_get_node_display_name_from_frontend(self):
        translations = {
            "en": {"KSampler": {"display_name": "KSampler (Advanced)"}},
            "zh": {"KSampler": {"display_name": "K采样器（高级）"}},
        }
        self.assertEqual(
            dt.get_node_display_name("KSampler", "zh", translations),
            "K采样器（高级）",
        )

    def test_get_node_display_name_falls_back_to_english(self):
        translations = {
            "en": {"KSampler": {"display_name": "KSampler (Advanced)"}},
            "zh": {},
        }
        self.assertEqual(
            dt.get_node_display_name("KSampler", "zh", translations),
            "KSampler (Advanced)",
        )

    def test_get_node_display_name_falls_back_to_class_name(self):
        translations = {"en": {}, "zh": {}}
        self.assertEqual(
            dt.get_node_display_name("UnknownNode", "zh", translations),
            "UnknownNode",
        )

    def test_analyze_title_issues(self):
        translations = {"en": {"KSampler": {"display_name": "KSampler (Advanced)"}}}
        body = "Overview only.\n"
        self.assertEqual(
            dt.analyze_title_issues(body, "KSampler", "en", translations),
            ["missing"],
        )
        body_dup = "# A\n# B\n\nOverview.\n"
        issues = dt.analyze_title_issues(body_dup, "KSampler", "en", translations)
        self.assertIn("duplicate", issues)
        self.assertIn("mismatch", issues)

    def test_fix_document_title_preserve_hash(self):
        footer = "\n\n---\n**Source fingerprint (SHA-256):** `abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234abcd1234`\n"
        disclaimer = "> AI note [Edit on GitHub](https://example.com)\n"
        original = "# Wrong\n\nBody text.\n\n" + disclaimer + footer
        translations = {"en": {"KSampler": {"display_name": "KSampler (Advanced)"}}}
        out = dt.fix_document_title(
            original, "KSampler", "en", translations, hash_mode="preserve"
        )
        self.assertIn("# KSampler (Advanced)", out)
        self.assertIn("Body text.", out)
        self.assertIn("abcd1234abcd1234", out)
        self.assertIn("AI note", out)

    def test_ensure_doc_title_replaces_ai_h1(self):
        translations = {"en": {"CLIPTextEncode": {"display_name": "CLIP Text Encode"}}}
        body = "# AI Guessed Title\n\nDoes encoding.\n"
        out = dt.ensure_doc_title(body, "CLIPTextEncode", "en", translations)
        self.assertEqual(out, "# CLIP Text Encode\n\nDoes encoding.")


if __name__ == "__main__":
    unittest.main()
