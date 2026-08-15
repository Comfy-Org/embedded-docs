#!/usr/bin/env python3
"""Regression tests for update_param_translations section detection.

Covers the H3-subheading bug (PR #128): '### Common Inputs' / '### <Model>
Inputs' subheadings start with '##' and must NOT close the Inputs/Outputs
section. Only H2 (## X) headings toggle sections.
"""

import os
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(REPO_ROOT / "scripts"))

from scripts import update_param_translations as upt  # noqa: E402


def _make_doc(lang_heading, subheadings, rows_after_each):
    """Build a doc with H2 heading, H3 subheadings and table rows.

    lang_heading: localized H2 heading (e.g. "Entradas")
    subheadings: list of H3 headings
    rows_after_each: list of table-row lists, one per subheading
    """
    lines = [f"## {lang_heading}", ""]
    for sub, rows in zip(subheadings, rows_after_each):
        lines.append(f"### {sub}")
        lines.append("")
        for r in rows:
            lines.append(r)
        lines.append("")
    return "\n".join(lines)


class InputsSectionDetectionTests(unittest.TestCase):
    def _write_and_update(self, content, node="TestNode", lang="es"):
        """Write content to a temp doc and run update_doc_with_translations."""
        d = {
            lang: {
                node: {
                    "inputs": {
                        "model": {"name": "modelo"},
                        "seed": {"name": "semilla"},
                        "prompt": {"name": "prueba"},
                    },
                    "outputs": {},
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
                path, node, lang, d
            )
            final = open(path, encoding="utf-8").read()
        finally:
            os.unlink(path)
        return updated, changes, final

    def test_rows_under_h3_subheadings_are_translated(self):
        """Rows under '### Common Inputs' must be translated (H3 must not close section)."""
        content = _make_doc(
            "Entradas",
            ["Entradas comunes", "Entradas del modelo"],
            [
                ["| `model` | desc | COMBO | Sí |"],
                ["| `seed` | desc | INT | Sí |"],
            ],
        )
        updated, changes, final = self._write_and_update(content)
        self.assertTrue(updated)
        self.assertIn("`modelo`", final)
        self.assertIn("`semilla`", final)
        # The H3 headings themselves must remain untouched
        self.assertIn("### Entradas comunes", final)
        self.assertIn("### Entradas del modelo", final)

    def test_following_h2_ends_input_section(self):
        """A subsequent H2 (e.g. Salidas) must close the Inputs section so
        rows under it are NOT treated as inputs."""
        content = _make_doc(
            "Entradas",
            ["Entradas comunes"],
            [["| `model` | desc | COMBO | Sí |"]],
        )
        # Append an Outputs H2 with a row that happens to contain `model`
        content += "## Salidas\n\n| `model` | output desc | VIDEO |\n"
        updated, changes, final = self._write_and_update(content)
        self.assertTrue(updated)
        # Inputs row translated
        self.assertIn("| `modelo` | desc | COMBO | Sí |", final)
        # Outputs row must keep the raw name (only Inputs table is scoped)
        self.assertIn("| `model` | output desc | VIDEO |", final)

    def test_no_h3_rows_skipped_when_multiple_model_sections(self):
        """Multiple per-model H3 sections, all rows must be translated."""
        content = _make_doc(
            "Inputs",
            ["Common Inputs", "Model A Inputs", "Model B Inputs"],
            [
                ["| `model` | common | COMBO | Yes |"],
                ["| `seed` | A | INT | Yes |"],
                ["| `prompt` | B | STRING | Yes |"],
            ],
        )
        updated, changes, final = self._write_and_update(content, lang="en")
        self.assertTrue(updated)
        self.assertIn("`modelo`", final)
        self.assertIn("`semilla`", final)
        self.assertIn("`prueba`", final)

    def test_english_h2_inputs_detected(self):
        """English '## Inputs' heading must open the section."""
        content = _make_doc(
            "Inputs",
            ["Common Inputs"],
            [["| `model` | desc | COMBO | Yes |"]],
        )
        updated, changes, final = self._write_and_update(content, lang="en")
        self.assertTrue(updated)
        self.assertIn("`modelo`", final)


if __name__ == "__main__":
    unittest.main()
