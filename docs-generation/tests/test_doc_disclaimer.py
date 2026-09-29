#!/usr/bin/env python3
"""Unit tests for lib.doc_disclaimer directory resolution."""

import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from lib import doc_disclaimer as dd  # noqa: E402


class ResolveDocDirTests(unittest.TestCase):
    def test_exact_directory_wins(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "ClipSave").mkdir()
            self.assertEqual(dd.resolve_doc_dir("ClipSave", tmp), "ClipSave")

    def test_class_name_resolves_to_renamed_directory(self):
        # Migrations renamed directories to title case; the node class name that
        # the generator passes still has to produce a working link.
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "ClipMergeSimple").mkdir()
            self.assertEqual(dd.resolve_doc_dir("CLIPMergeSimple", tmp), "ClipMergeSimple")
            self.assertEqual(dd.resolve_doc_dir("clipmergesimple", tmp), "ClipMergeSimple")

    def test_unknown_name_falls_back(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(dd.resolve_doc_dir("NotANode", tmp), "NotANode")

    def test_disclaimer_link_uses_resolved_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            (Path(tmp) / "ClipSetLastLayer").mkdir()
            en = dd.create_en_disclaimer("CLIPSetLastLayer", tmp)
            ja = dd.create_translated_disclaimer("ja", "CLIPSetLastLayer", {}, tmp)
            self.assertIn("docs/ClipSetLastLayer/en.md", en)
            self.assertIn("docs/ClipSetLastLayer/ja.md", ja)
            self.assertNotIn("CLIPSetLastLayer", en)
            self.assertNotIn("CLIPSetLastLayer", ja)


if __name__ == "__main__":
    unittest.main()
