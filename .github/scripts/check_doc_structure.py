#!/usr/bin/env python3
"""Check (and optionally repair) the structure of localized node docs.

Eight translation defects reached docs.comfy.org because nothing compared a
translated document with its English source:

* the AI-disclaimer link is built from the node class name, which does not always
  match the directory (``CLIPMergeSimple`` versus ``ClipMergeSimple``), so the
  "Edit on GitHub" link 404s;
* section headings are written one level off (``# Inputs``, or a literal
  ``# ## Inputs``) where ``en.md`` writes ``## Inputs``;
* a section the English source has (``## Overview``) is missing;
* the translation leaked its own preamble / prompt block under the H1 (the
  pipeline's preamble detector ran while the H1 was still attached, so it read
  the title and never matched; see PR #167 and ``fix_translation_preamble.py``).

Usage:
    python docs-generation/scripts/check_doc_structure.py                     # whole tree
    python docs-generation/scripts/check_doc_structure.py --changed-only --base origin/main
    python docs-generation/scripts/check_doc_structure.py --fix               # repair, then report
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

from pathlib import Path as _Path

REPO_ROOT = _Path(__file__).resolve().parents[2]
PIPELINE_SCRIPTS = REPO_ROOT / "docs-generation" / "scripts"
if str(PIPELINE_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(PIPELINE_SCRIPTS))
try:
    from fix_translation_preamble import strip_leak as _strip_leaked_preamble
except ImportError:  # pragma: no cover - pipeline scripts missing
    _strip_leaked_preamble = None
DEFAULT_DOCS_ROOT = REPO_ROOT / "comfyui_embedded_docs" / "docs"

# Languages the documentation site publishes; other locales are translated in
# this repository too but are not rendered, so they are reported, not enforced.
ENFORCED_LANGS = ("ja", "zh", "ko")
ALL_LANGS = (
    "ja",
    "zh",
    "ko",
    "zh-TW",
    "es",
    "fr",
    "ru",
    "pt-BR",
    "ar",
    "tr",
    "fa",
)

# Localized "## Overview" headings.
OVERVIEW_HEADING = {
    "ja": "概要",
    "zh": "概述",
    "zh-TW": "概述",
    "ko": "개요",
    "es": "Descripción general",
    "fr": "Aperçu",
    "ru": "Обзор",
    "pt-BR": "Visão geral",
    "ar": "نظرة عامة",
    "tr": "Genel bakış",
    "fa": "نمای کلی",
}

FENCE_RE = re.compile(r"^\s*(```|~~~)")
H1_RE = re.compile(r"^# (.+)$")
BROKEN_HEADING_RE = re.compile(r"^# ##")
LINK_RE = re.compile(r"comfyui_embedded_docs/docs/([^/]+)/([A-Za-z-]+)\.md")


def body_start(lines: list[str]) -> int:
    """Index of the first line after the frontmatter, if any."""
    if lines and lines[0].strip() == "---":
        for index, line in enumerate(lines[1:], 1):
            if line.strip() == "---":
                return index + 1
    return 0


def count_headings(lines: list[str], start: int, level: int) -> int:
    """Count ATX headings of exactly *level*, ignoring fenced code blocks."""
    total = 0
    in_fence = False
    for line in lines[start:]:
        if FENCE_RE.match(line):
            in_fence = not in_fence
            continue
        if not in_fence and re.match(rf"^#{{{level}}} ", line):
            total += 1
    return total


def repair(text: str, doc_dir: str, lang: str, en_h2: int) -> tuple[str, list[str]]:
    """Return the repaired text plus a list of what was repaired."""
    notes: list[str] = []
    lines = text.split("\n")
    start = body_start(lines)

    for index, line in enumerate(lines):
        fixed = LINK_RE.sub(
            lambda match: f"comfyui_embedded_docs/docs/{doc_dir}/{match.group(2)}.md",
            line,
        )
        if fixed != line:
            lines[index] = fixed
            notes.append("disclaimer link points at the wrong directory")

    for index in range(start, len(lines)):
        line = lines[index]
        if BROKEN_HEADING_RE.match(line):
            lines[index] = "## " + line[4:].lstrip("# ")
            notes.append("literal '# ##' heading")
            continue
        match = H1_RE.match(line)
        if match and index > start:
            lines[index] = "## " + match.group(1)
            notes.append("section heading written as H1")

    if count_headings(lines, start, 2) == 0 and en_h2 > 0:
        for index in range(start, len(lines)):
            match = re.match(r"^(#{3,4}) (.+)$", lines[index])
            if match:
                lines[index] = "#" * (len(match.group(1)) - 1) + " " + match.group(2)
                notes.append("sections one level low")

    overview = OVERVIEW_HEADING.get(lang)
    if overview and en_h2 and count_headings(lines, start, 2) < en_h2:
        body = "\n".join(lines[start:])
        if not re.search(rf"^## .*{re.escape(overview)}", body, re.M):
            index = start
            while index < len(lines) and not lines[index].strip():
                index += 1
            if index < len(lines) and H1_RE.match(lines[index]) and count_headings(lines, start, 1) == 1:
                index += 1
                while index < len(lines) and not lines[index].strip():
                    index += 1
            if index < len(lines) and not lines[index].startswith("#"):
                lines.insert(index, f"## {overview}")
                lines.insert(index + 1, "")
                notes.append("missing localized '## Overview' heading")

    return "\n".join(lines), sorted(set(notes))


def changed_paths(base: str) -> set[Path]:
    """Files changed against *base*, as absolute paths."""
    out = subprocess.run(
        ["git", "diff", "--name-only", f"{base}...HEAD"],
        capture_output=True,
        text=True,
        check=False,
    ).stdout
    root = Path(
        subprocess.run(["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip()
    )
    return {(root / line).resolve() for line in out.split("\n") if line.strip()}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fix", action="store_true", help="repair the defects instead of only reporting")
    parser.add_argument("--changed-only", action="store_true", help="only inspect files changed against --base")
    parser.add_argument("--base", default="origin/main", help="base ref for --changed-only")
    parser.add_argument("--docs-root", default=None, help="path to comfyui_embedded_docs/docs")
    args = parser.parse_args()

    root = Path(args.docs_root) if args.docs_root else DEFAULT_DOCS_ROOT
    changed = changed_paths(args.base) if args.changed_only else None

    violations = 0
    repaired = 0
    for doc_dir in sorted(root.iterdir()):
        if not doc_dir.is_dir():
            continue
        en_path = doc_dir / "en.md"
        if not en_path.exists():
            continue
        en_lines = en_path.read_text(encoding="utf-8").split("\n")
        en_h2 = count_headings(en_lines, body_start(en_lines), 2)

        for lang in ("en", *ALL_LANGS):
            path = doc_dir / f"{lang}.md"
            if not path.exists():
                continue
            if changed is not None and path.resolve() not in changed:
                continue
            original = path.read_text(encoding="utf-8")
            updated, notes = repair(original, doc_dir.name, lang, en_h2)

            # Leaked translation preamble / prompt block under the H1.
            if _strip_leaked_preamble is not None:
                _, leaked_lines = _strip_leaked_preamble(updated, lang)
                if leaked_lines:
                    violations += 1
                    print(f"leaked preamble: {doc_dir.name}/{lang}.md "
                          f"({leaked_lines} line(s) under the H1; run "
                          f"docs-generation/scripts/fix_translation_preamble.py --apply)")
                    if args.fix:
                        cleaned, _ = _strip_leaked_preamble(updated, lang)
                        updated = cleaned
                        repaired += 1

            enforced = lang == "en" or lang in ENFORCED_LANGS
            enforced = lang == "en" or lang in ENFORCED_LANGS
            if updated != original and enforced:
                violations += 1
                label = "repaired" if args.fix else "needs repair"
                print(f"{label}: {doc_dir.name}/{lang}.md ({', '.join(notes)})")
                if args.fix:
                    path.write_text(updated, encoding="utf-8")
                    repaired += 1

            if enforced:
                lines = updated.split("\n")
                start = body_start(lines)
                gap = en_h2 - count_headings(lines, start, 2)
                if gap > 0:
                    violations += 1
                    print(f"missing {gap} section(s) present in en.md: {doc_dir.name}/{lang}.md")

    print(f"\n{repaired} repaired, {violations} defect(s) found")
    return 1 if violations and not args.fix else 0


if __name__ == "__main__":
    sys.exit(main())
