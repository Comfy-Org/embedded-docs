#!/usr/bin/env python3
"""Regression tests for the translation pipeline fixes.

Covers:
- batch_translate_docs._fix_output_names_in_translation: EN output names must
  align to translated rows by data-row index even when blank/intro lines or
  non-backtick rows appear inside the Outputs section.
- update_param_translations.update_doc_with_translations(dry_run=True): must
  never write to disk.
- update_param_translations Outputs-section detection for Persian (fa).
"""

import os
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from scripts import batch_translate_docs as btd  # noqa: E402
from scripts import update_param_translations as upt  # noqa: E402


class FixOutputNamesTests(unittest.TestCase):
    EN_DOC = (
        "# KSampler\n\n"
        "## Outputs\n\n"
        "| Name | Data Type | Description |\n"
        "|------|-----------|-------------|\n"
        "| `positive` | CONDITIONING | Positive conditioning |\n"
        "| `negative` | CONDITIONING | Negative conditioning |\n"
        "| `latent` | LATENT | Denoised latent |\n"
    )

    def test_translated_names_replaced_by_row_index(self):
        translated = (
            "## 输出\n\n"
            "| 名称 | 数据类型 | 描述 |\n"
            "|------|-----------|-------------|\n"
            "| `正向` | CONDITIONING | 正向条件 |\n"
            "| `负向` | CONDITIONING | 负向条件 |\n"
            "| `潜空间` | LATENT | 去噪后的潜空间 |\n"
        )
        out = btd._fix_output_names_in_translation(translated, self.EN_DOC)
        self.assertIn("| `positive` |", out)
        self.assertIn("| `negative` |", out)
        self.assertIn("| `latent` |", out)
        self.assertNotIn("`正向`", out)

    def test_intro_line_inside_section_does_not_misalign_rows(self):
        """A non-table line between heading and table must not shift the index."""
        translated = (
            "## 输出\n\n"
            "以下是该节点的输出：\n\n"
            "| 名称 | 数据类型 | 描述 |\n"
            "|------|-----------|-------------|\n"
            "| `正向` | CONDITIONING | 正向条件 |\n"
            "| `负向` | CONDITIONING | 负向条件 |\n"
            "| `潜空间` | LATENT | 去噪后的潜空间 |\n"
        )
        out = btd._fix_output_names_in_translation(translated, self.EN_DOC)
        self.assertIn("| `positive` | CONDITIONING | 正向条件 |", out)
        self.assertIn("| `negative` | CONDITIONING | 负向条件 |", out)
        self.assertIn("| `latent` | LATENT | 去噪后的潜空间 |", out)

    def test_separator_like_row_does_not_count_as_data_row(self):
        translated = (
            "## 输出\n\n"
            "| 名称 | 数据类型 | 描述 |\n"
            "|------|-----------|-------------|\n"
            "| `正向` | CONDITIONING | 正向条件 |\n"
            "| `负向` | CONDITIONING | 负向条件 |\n"
            "| `潜空间` | LATENT | 去噪后的潜空间 |\n"
        )
        out = btd._fix_output_names_in_translation(translated, self.EN_DOC)
        rows = [l for l in out.split("\n") if l.strip().startswith("| `")]
        self.assertEqual(
            [r.split("`")[1] for r in rows], ["positive", "negative", "latent"]
        )

    def test_no_outputs_section_returns_content_unchanged(self):
        translated = "## 输出\n\n没有表格。\n"
        en = "# Node\n\n## Outputs\n\nNo table here.\n"
        self.assertEqual(
            btd._fix_output_names_in_translation(translated, en), translated
        )


class DryRunTests(unittest.TestCase):
    def _translations(self, node, lang):
        return {
            lang: {
                node: {
                    "inputs": {"seed": {"name": "semilla"}},
                    "outputs": {},
                }
            }
        }

    def test_dry_run_does_not_write(self):
        content = (
            "## Entradas\n\n"
            "| Parameter | Description | Type |\n"
            "|-----------|-------------|------|\n"
            "| `seed` | desc | INT |\n"
        )
        with tempfile.NamedTemporaryFile(
            "w", suffix=".md", delete=False, encoding="utf-8"
        ) as f:
            f.write(content)
            path = f.name
        try:
            updated, changes = upt.update_doc_with_translations(
                path, "TestNode", "es", self._translations("TestNode", "es"),
                dry_run=True,
            )
            self.assertTrue(updated)
            self.assertTrue(changes)
            # File on disk must be untouched
            self.assertEqual(Path(path).read_text(encoding="utf-8"), content)
        finally:
            os.unlink(path)

    def test_persian_outputs_section_detected(self):
        """'## خروجی‌ها' must open the Outputs section for fa docs."""
        content = (
            "## خروجی‌ها\n\n"
            "| Name | Type |\n"
            "|------|------|\n"
            "| `old_name` | IMAGE |\n"
        )
        translations = {
            "fa": {
                "TestNode": {
                    "inputs": {},
                    "outputs": {"0": {"name": "new_name"}},
                }
            }
        }
        with tempfile.NamedTemporaryFile(
            "w", suffix=".md", delete=False, encoding="utf-8"
        ) as f:
            f.write(content)
            path = f.name
        try:
            updated, changes = upt.update_doc_with_translations(
                path, "TestNode", "fa", translations
            )
            final = Path(path).read_text(encoding="utf-8")
        finally:
            os.unlink(path)
        self.assertTrue(updated)
        self.assertIn("`new_name`", final)


class ConcurrencyTests(unittest.TestCase):
    def test_all_success(self):
        nodes = [f"Node{i}" for i in range(10)]
        results, aborted = btd.translate_nodes_concurrently(
            nodes, concurrency=4, process_fn=lambda n: "success"
        )
        self.assertFalse(aborted)
        self.assertEqual(sorted(results["success"]), sorted(nodes))
        self.assertEqual(results["failed"], [])

    def test_circuit_breaker_trips_on_consecutive_failures(self):
        nodes = [f"Node{i}" for i in range(20)]
        results, aborted = btd.translate_nodes_concurrently(
            nodes,
            concurrency=1,  # deterministic ordering for the breaker test
            process_fn=lambda n: "failed",
            max_consecutive_failures=5,
        )
        self.assertTrue(aborted)
        # Breaker trips after 5 failures; with concurrency=1 nothing beyond
        # the in-flight task can complete, so we must see far fewer than 20.
        self.assertLess(len(results["failed"]), 20)

    def test_success_resets_consecutive_failure_counter(self):
        # Fail 4x, succeed, fail 4x: never 5 in a row -> no abort.
        outcomes = {"a": "failed", "b": "failed", "c": "failed", "d": "failed",
                    "e": "success", "f": "failed", "g": "failed", "h": "failed",
                    "i": "failed"}
        results, aborted = btd.translate_nodes_concurrently(
            list(outcomes), concurrency=1, process_fn=lambda n: outcomes[n],
            max_consecutive_failures=5,
        )
        self.assertFalse(aborted)
        self.assertEqual(len(results["failed"]), 8)
        self.assertEqual(results["success"], ["e"])


if __name__ == "__main__":
    unittest.main()
