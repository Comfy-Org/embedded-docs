#!/usr/bin/env python3
"""Language-inventory tests: a supported locale must reach every consumer.

The locale list lives in several places -- ``config/translation_config.json``,
the CLI workflow, the per-script language lists, the localized section
headings and the repo checkers in ``.github/scripts``. A locale added to only
some of them fails silently: ``prepare_translation.py`` accepts it (it is
config-driven), but the Outputs-section guard, the frontend parameter export
or the structure checker never see it.

These tests fail whenever those inventories disagree, so adding a locale is a
one-command check and the config stays the single source of truth.
"""

from __future__ import annotations

import importlib.util
import json
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent          # docs-generation/
REPO = REPO_ROOT.parent                                     # repository root
sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(REPO_ROOT / "scripts"))

import main as cli  # noqa: E402
from lib.doc_disclaimer import create_translated_disclaimer  # noqa: E402
from scripts import batch_translate_docs as btd  # noqa: E402
from scripts import fix_doc_titles as fdt  # noqa: E402
from scripts import fix_translation_preamble as ftp  # noqa: E402
from scripts import sync_frontend_translations as sft  # noqa: E402
from scripts import update_param_translations as upt  # noqa: E402

CONFIG_PATH = REPO_ROOT / "config" / "translation_config.json"
with open(CONFIG_PATH, encoding="utf-8") as fh:
    CONFIG = json.load(fh)
LANGS = list(CONFIG)                    # zh, es, fr, ... de, he, it
NEW_LANGS = ("de", "he", "it")
REQUIRED_ENTRY_FIELDS = {
    "name", "heading_overview", "heading_inputs", "heading_outputs",
    "disclaimer", "prompt_template",
}


def _load_checker(filename: str, name: str):
    """Import a checker from .github/scripts (not an importable package)."""
    spec = importlib.util.spec_from_file_location(
        name, REPO / ".github" / "scripts" / filename
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


cds = _load_checker("check_doc_structure.py", "check_doc_structure")
cmf = _load_checker("check_md_format.py", "check_md_format")


class ConfigTests(unittest.TestCase):
    def test_new_locales_are_configured(self):
        for lang in NEW_LANGS:
            self.assertIn(lang, CONFIG, f"{lang} missing from translation_config.json")

    def test_every_entry_is_complete(self):
        for lang, entry in CONFIG.items():
            with self.subTest(lang=lang):
                self.assertEqual(REQUIRED_ENTRY_FIELDS, set(entry))
                for field in ("name", "heading_overview", "heading_inputs",
                              "heading_outputs", "disclaimer", "prompt_template"):
                    self.assertTrue(entry[field].strip(), f"{lang}.{field} is empty")
                for placeholder in ("{heading_overview}", "{heading_inputs}",
                                    "{heading_outputs}"):
                    self.assertIn(placeholder, entry["prompt_template"])


class PipelineInventoryTests(unittest.TestCase):
    def test_cli_language_list_matches_config(self):
        self.assertEqual(set(cli.LANGUAGES), set(CONFIG))
        self.assertEqual(len(cli.LANGUAGES), len(CONFIG))

    def test_cli_has_display_names_for_every_language(self):
        self.assertLessEqual(set(cli.LANGUAGES), set(cli.LANG_NAMES))

    def test_script_language_lists_match_config(self):
        # Compare as sets: the config and the scripts order the same locales
        # differently (zh-TW before/after es) and the order carries no meaning.
        self.assertEqual(set(sft.SUPPORTED_LANGS), {"en", *LANGS})
        self.assertEqual(set(upt.SUPPORTED_LANGS), set(LANGS))
        self.assertEqual(set(fdt.DOC_LANGS), {"en", *LANGS})

        # scan_missing_nodes declares its list inside a method, so compare the
        # literal the method uses instead of importing an attribute.
        source = (REPO_ROOT / "scripts" / "scan_missing_nodes.py").read_text(encoding="utf-8")
        literal = "languages = ['en', " + ", ".join(f"'{lang}'" for lang in cli.LANGUAGES) + "]"
        self.assertIn(literal, source)

    def test_doc_disclaimer_has_a_label_per_locale(self):
        # The English "Edit on GitHub" label is the fallback for a locale that
        # has no entry, so its presence means the locale was never added.
        for lang, entry in CONFIG.items():
            with self.subTest(lang=lang):
                disclaimer = create_translated_disclaimer(lang, "KSampler", entry)
                self.assertNotIn("Edit on GitHub", disclaimer)
                self.assertIn(entry["disclaimer"], disclaimer)

    def test_preamble_strippers_cover_every_locale(self):
        # A locale with no patterns lets a leaked LLM preamble reach the docs.
        self.assertLessEqual(set(CONFIG), set(btd._PREAMBLE_PATTERNS))
        self.assertLessEqual(set(CONFIG), set(ftp.PREAMBLE_SENTENCES))


class LocalizedHeadingTests(unittest.TestCase):
    EN_DOC = (
        "# KSampler\n\n"
        "## Outputs\n\n"
        "| Name | Data Type | Description |\n"
        "|------|-----------|-------------|\n"
        "| `positive` | CONDITIONING | Positive conditioning |\n"
    )

    def test_outputs_section_detected_for_every_locale(self):
        """The Outputs guard keys off the localized heading, so each locale's
        ``heading_outputs`` must be matched by the detection regex."""
        for lang, entry in CONFIG.items():
            translated = (
                f"## {entry['heading_outputs']}\n\n"
                "| Name | Data Type | Description |\n"
                "|------|-----------|-------------|\n"
                "| `translated` | CONDITIONING | translated |\n"
            )
            with self.subTest(lang=lang):
                out = btd._fix_output_names_in_translation(translated, self.EN_DOC)
                self.assertIn("| `positive` |", out,
                              f"'## {entry['heading_outputs']}' did not open the Outputs section")
                rows, _ = upt.extract_table_rows(translated, "outputs")
                self.assertIsNotNone(rows, f"'## {entry['heading_outputs']}' not found")

    def test_inputs_section_detected_for_every_locale(self):
        for lang, entry in CONFIG.items():
            content = (
                f"## {entry['heading_inputs']}\n\n"
                "| Name | Data Type | Description |\n"
                "|------|-----------|-------------|\n"
                "| `image` | IMAGE | translated |\n"
            )
            with self.subTest(lang=lang):
                rows, _ = upt.extract_table_rows(content, "inputs")
                self.assertIsNotNone(rows, f"'## {entry['heading_inputs']}' not found")


class RepoCheckerInventoryTests(unittest.TestCase):
    def test_structure_checker_covers_every_locale(self):
        self.assertEqual(set(cds.ALL_LANGS), set(CONFIG))
        for lang, entry in CONFIG.items():
            with self.subTest(lang=lang):
                self.assertIn(lang, cds.OVERVIEW_HEADING)
        for lang in NEW_LANGS:
            self.assertEqual(cds.OVERVIEW_HEADING[lang], CONFIG[lang]["heading_overview"])

    def test_format_checker_knows_every_outputs_heading(self):
        for lang, entry in CONFIG.items():
            with self.subTest(lang=lang):
                self.assertIn(entry["heading_outputs"], cmf.OUTPUTS_HEADINGS)
        self.assertLessEqual(set(NEW_LANGS), cmf.EN_RESIDUE_LANGS)


if __name__ == "__main__":
    unittest.main()
