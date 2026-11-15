#!/usr/bin/env python3
"""Lint embedded-docs node pages for defects that surface as bot findings on the
weekly docs sync PR.

Classes covered (all seen on Comfy-Org/docs#2364):

1. scaffolding_leak   a translation instruction survived in a localized file
                      ("Por favor traduce ...", "以下が翻訳結果です", "번역 결과입니다",
                      "请翻译以下内容") and becomes the page description.
2. note_before_intro  the body opens with a `>` note before any overview
                      paragraph, so `get_description_from_content()` returns the
                      note as the description (Tripo 7-day retention notice).
3. missing_overview   a localized file has no overview paragraph before its
                      first `## ` section while the English file has one.
4. import_recovery    a node whose inputs require a task-specific id
                      (SEGMENT_TASK_ID / RIG_TASK_ID / MULTIVIEW_TASK_ID) tells
                      readers to recover from an expired task with
                      "Tripo: Import Model", which only returns MODEL_TASK_ID.

Usage:
  python3 docs-generation/scripts/lint_localized_node_docs.py            # full corpus
  python3 docs-generation/scripts/lint_localized_node_docs.py --lang ko  # one language
  python3 docs-generation/scripts/lint_localized_node_docs.py --node TripoMeshCompleteNode
Exit code 1 when anything is found, so it can gate a pipeline run.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2] / "comfyui_embedded_docs" / "docs"
LANGS = ["ar", "de", "es", "fa", "fr", "he", "it", "ja", "ko", "pt-BR", "ru", "tr", "zh", "zh-TW"]

SCAFFOLD = [
    re.compile(r"por favor,? traduce", re.I),
    re.compile(r"please translate", re.I),
    re.compile(r"以下が翻訳結果です"),
    re.compile(r"번역\s*결과입니다"),
    re.compile(r"请翻译|以下是翻译结果"),
    re.compile(r"traduci il seguente", re.I),
    re.compile(r"übersetze den folgenden", re.I),
    re.compile(r"traduce el siguiente", re.I),
]

TASK_SPECIFIC_INPUT = re.compile(r"(SEGMENT_TASK_ID|RIG_TASK_ID|MULTIVIEW_TASK_ID)")
IMPORT_ADVICE = re.compile(r"Import Model", re.I)


def body_lines(text: str):
    return text.splitlines()


# Words that turn a nearby "Import Model" mention into a warning instead of advice.
NEGATION_CUES = (
    "no ", "not ", "never", "nunca", "jamais", "nicht", "kein", "non ", "não", "nao",
    "никогда", "не ", "لا ", "لم ", "לא ", "al ", "asla", "hiçbir", "بدون", "negar",
)


def _negated_before(line: str, pos: int, window: int = 32) -> bool:
    """True when a negation cue sits in the run-up to the mention at ``pos``."""
    head = line[max(0, pos - window):pos].lower()
    return any(cue in head for cue in NEGATION_CUES)


def check_file(path: Path, lang: str, en_text: str | None):
    text = path.read_text(encoding="utf-8")
    lines = body_lines(text)
    findings = []

    for i, line in enumerate(lines, 1):
        for pat in SCAFFOLD:
            if pat.search(line):
                findings.append(("scaffolding_leak", i, line.strip()[:100]))

    # First description candidate after the H1, using the same skip rules as
    # get_description_from_content() in sync_to_comfy_docs.py: headings, images,
    # table rows and disclaimers are not prose, so a note that follows an image is
    # still the line the description is built from.
    body_start = 0
    for i, line in enumerate(lines):
        if line.startswith("# "):
            body_start = i + 1
            break
    first_candidate = None
    for i in range(body_start, len(lines)):
        s = lines[i].strip()
        if not s:
            continue
        if s.startswith("#") or s.startswith("![") or s.startswith("|"):
            continue
        first_candidate = (i + 1, s)
        break
    if first_candidate and first_candidate[1].startswith(">"):
        findings.append(("note_before_intro", first_candidate[0], first_candidate[1][:100]))

    if en_text is not None and lang != "en":
        def pre_section_paragraph(text: str) -> bool:
            ls = text.splitlines()
            start = next((i for i, l in enumerate(ls) if l.startswith("# ")), -1) + 1
            # a page with no H2 at all still has an overview: the section boundary is EOF
            first_h2 = next((i for i, l in enumerate(ls) if l.startswith("## ")), len(ls))
            body = ls[start:first_h2]
            return any(l.strip() and not l.strip().startswith(("#", ">", "|", "!", "```")) for l in body)

        if pre_section_paragraph(en_text) and not pre_section_paragraph(text):
            first_h2 = next((i for i, l in enumerate(lines) if l.startswith("## ")), None)
            findings.append(("missing_overview", (first_h2 or 0) + 1,
                             "English page has an overview paragraph, this one opens straight into a section"))

    if IMPORT_ADVICE.search(text) and TASK_SPECIFIC_INPUT.search(text):
        # Pages that warn readers *against* Import Model mention it in the same breath,
        # so only an affirmative recommendation counts.
        if any(not _negated_before(line, m.start()) for line in lines
               for m in IMPORT_ADVICE.finditer(line)):
            findings.append(("import_recovery", 0, "Import Model suggested while the node needs a task-specific id"))
    return findings


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--lang")
    ap.add_argument("--node")
    args = ap.parse_args()

    langs = [args.lang] if args.lang else LANGS
    total = 0
    for node_dir in sorted(ROOT.iterdir()):
        if not node_dir.is_dir():
            continue
        if args.node and node_dir.name != args.node:
            continue
        en = node_dir / "en.md"
        en_text = en.read_text(encoding="utf-8") if en.exists() else None
        for lang in langs:
            f = node_dir / f"{lang}.md"
            if not f.exists():
                continue
            for kind, line, detail in check_file(f, lang, en_text):
                total += 1
                print(f"{kind:18s} {node_dir.name}/{lang}.md:{line}  {detail}")
    print(f"\n{total} finding(s)")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
