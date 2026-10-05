#!/usr/bin/env python3
"""Detect and remove leaked translation preambles / prompt blocks from localized node docs.

Root cause (fixed separately in batch_translate_docs.strip_ai_preamble): the
translation step called the preamble detector while the H1 was still attached, and
the detector only inspected the first non-empty line, so it read the title and never
matched. Everything the model prepended under the H1 shipped to the site.

Five shapes leak, all sitting between the H1 and the real overview:

  A  preamble sentence      ``Вот перевод документации на русский язык:``
                            ``以下が翻訳結果です。`` / ``Voici la traduction …``
  B  whole prompt block     expert-role line + rules heading + numbered rules +
                            a "please translate the following" line
  C  descriptive sentence   ``هذا هو توثيق عقدة … المترجم إلى العربية، مع الالتزام بقواعد الترجمة.``
  D  displaced disclaimer   the AI disclaimer repeated directly under the H1 while the
                            proper one sits at the bottom (compose_document appends it)
  E  leftover separator     a bare ``---`` left where a preamble used to be

Removal is conservative: a region qualifies only when it starts immediately under the
H1, ends at the first real content line, and contains at least one STRONG marker
(role line, rules heading, please-translate line, preamble/descriptive sentence, or a
disclaimer that also exists near the bottom). A plain bullet list under the H1 is
never removed on its own.

Usage:
    python docs-generation/scripts/fix_translation_preamble.py --dry-run
    python docs-generation/scripts/fix_translation_preamble.py --apply
    python docs-generation/scripts/fix_translation_preamble.py --apply --langs ar,tr
    python docs-generation/scripts/fix_translation_preamble.py --check-only --changed-only --base origin/main
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS_ROOT = REPO_ROOT.parent / "comfyui_embedded_docs" / "docs"

# Shape A / C: "here is the translation …" openers, per language
PREAMBLE_SENTENCES: dict[str, list[str]] = {
    "zh": [r"^以下是您要求的", r"^以下是为您翻译", r"^以下是翻译结果", r"^这是.*?翻译",
           r"^以下是将", r"^以下是.*?译文", r"^这是.*?译文"],
    "zh-TW": [r"^以下是您要求的", r"^以下是为您翻譯", r"^以下是翻譯結果", r"^以下是將",
              r"^這是.*?翻譯"],
    "ja": [r"^以下が翻訳", r"^翻訳結果", r"^以下に.*?翻訳", r"^以下は、指定された",
           r"^以下は.*?翻訳した", r"^以下が日本語訳"],
    "ko": [r"^다음은.*?번역", r"^번역 결과", r"^다음은 제공된", r"^요청하신 번역",
           r"^아래는.*?번역"],
    "ru": [r"^Вот перевод", r"^Перевод документаци", r"^Ниже приведен перевод",
           r"^Ниже представлен перевод"],
    "es": [r"^Aquí está la traducción", r"^Esta es la traducción", r"^Traducción de",
           r"^A continuación.*?traducción"],
    "fr": [r"^Voici la traduction", r"^Voici le document", r"^Traduction de",
           r"^Voici la version"],
    "ar": [r"^هذه هي الترجمة", r"^إليك الترجمة", r"^هذا هو المستند", r"^فيما يلي الترجمة",
           r"^بالتأكيد، إليك الترجمة", r"^هذا هو توثيق", r"^هذا توثيق"],
    "tr": [r"^İşte çeviri", r"^Çeviri sonucu", r"^Aşağıda.*?çevir", r"^Bu, ComfyUI",
           r"^Elbette"],
    "pt-BR": [r"^Aqui está a tradução", r"^Esta é a tradução", r"^A seguir.*?tradução"],
    "fa": [r"^این ترجمه", r"^در زیر ترجمه", r"^ترجمه زیر", r"^در ادامه ترجمه"],
}

# Shape B openers: expert-role lines
ROLE_LINES = [
    r"^أنت خبير في الترجمة", r"^أنت مترجم", r"^You are an expert translator",
    r"^あなたは", r"^당신은", r"^Ты .*?переводчик", r"^Вы .*?переводчик",
    r"^Sen .*?çevirmen", r"^Vous êtes", r"^Eres un experto", r"^你是一位", r"^你是一名",
    r"^ComfyUI düğüm belgelerini", r"^Como tradutor",
]

# Shape B: rules headings
RULES_HEADINGS = [
    "قواعد الترجمة", "قواعد ترجمه", "翻訳ルール", "翻译规则", "翻譯規則", "번역 규칙",
    "Правила перевода", "правила перевода", "Translation rules", "Çeviri kuralları",
    "Reglas de traducción", "Règles de traduction", "قوانین ترجمه", "翻譯規則：",
]

# Shape B: closing instruction line
PLEASE_LINES = [
    "الرجاء ترجمة", "لطفاً ترجمه", "translate the following", "traduisez le texte suivant",
    "翻訳してください", "다음을 번역", "переведите следующий", "aşağıdaki metni çevir",
    "traduce el siguiente", "请翻译以下", "請翻譯以下", "please translate",
    "الرجاء ترجمة الوثيقة", "traduza o seguinte",
]

COMPILED_SENTENCES = {lang: [re.compile(p) for p in pats] for lang, pats in PREAMBLE_SENTENCES.items()}
ROLE_RE = re.compile("|".join(ROLE_LINES), re.I)
PLEASE_RE = re.compile("|".join(re.escape(p) for p in PLEASE_LINES), re.I)
RULES_HEADING_RE = re.compile(
    "^#{1,4}\\s*(" + "|".join(re.escape(h) for h in RULES_HEADINGS) + ")\\s*[:：]?\\s*$", re.I)

# disclaimer link text in any shipped language ("Edit on GitHub")
DISCLAIMER_LINK_RE = re.compile(
    r"(Edit on GitHub|تحرير على GitHub|GitHub で編集|GitHub에서 편집|在 GitHub 上编辑|"
    r"在 GitHub 上編輯|Редактировать на GitHub|GitHub'ta düzenle|Editar en GitHub|"
    r"Modifier sur GitHub|ویرایش در GitHub)", re.I)
DISCLAIMER_MARK_RE = re.compile(
    r"(AI-generated|تم إنشاؤه|تم إنشاء|AI 生成|AI가 생성|AI에 의해 생성|Создано ИИ|"
    r"generado por IA|généré par IA|AI によって生成|تولید شده توسط هوش مصنوعی|AI tarafından)", re.I)


def _disclaimer_in_tail(lines: list[str]) -> bool:
    """True when a proper disclaimer exists in the last lines (so a top copy is a duplicate)."""
    tail = "\n".join(lines[-8:])
    return bool(DISCLAIMER_LINK_RE.search(tail) and DISCLAIMER_MARK_RE.search(tail))


def _is_marker(line: str, lang: str, in_block: bool, top_disclaimer_is_dup: bool) -> str | None:
    s = line.strip()
    if not s:
        return "blank"
    if RULES_HEADING_RE.match(s):
        return "rules-heading"
    if ROLE_RE.search(s):
        return "role"
    if PLEASE_RE.search(s):
        return "please"
    if any(p.search(s) for p in COMPILED_SENTENCES.get(lang, [])):
        return "sentence"
    if s in ("---", "***", "___"):
        return "hr"
    if in_block and re.match(r"^\d+\.\s", s):
        return "rule-item"
    if in_block and re.match(r"^[-*]\s", s):
        return "rule-bullet"
    # shape D: the disclaimer repeated under the H1 (proper one lives at the bottom)
    if top_disclaimer_is_dup and DISCLAIMER_LINK_RE.search(s):
        return "disclaimer"
    return None


STRONG = {"rules-heading", "role", "please", "sentence"}


def strip_leak(text: str, lang: str) -> tuple[str, int]:
    """Return (cleaned_text, lines_removed)."""
    lines = text.split("\n")
    h1_idx = next((i for i, l in enumerate(lines) if l.startswith("# ")), None)
    if h1_idx is None:
        return text, 0

    dup_disclaimer = _disclaimer_in_tail(lines)
    start = h1_idx + 1
    end = start
    kinds: list[str | None] = []
    strong_found = False
    for i in range(start, len(lines)):
        kind = _is_marker(lines[i], lang, in_block=any(k for k in kinds), top_disclaimer_is_dup=dup_disclaimer)
        if kind is None:
            break
        # a real section heading that is not the rules heading means the body began
        if lines[i].strip().startswith("## ") and kind != "rules-heading":
            break
        if kind in STRONG:
            strong_found = True
        if kind == "disclaimer":
            strong_found = True
        kinds.append(kind)
        end = i + 1

    non_blank_kinds = [k for k in kinds if k != "blank"]
    if not kinds or not strong_found or not non_blank_kinds:
        return text, 0

    removed = end - start
    tail = lines[end:]
    while tail and not tail[0].strip():
        tail.pop(0)
    cleaned = lines[: h1_idx + 1] + [""] + tail
    return "\n".join(cleaned), removed + 1


def iter_docs(langs: list[str] | None, changed_only: bool, base: str):
    if changed_only:
        out = subprocess.run(
            ["git", "diff", "--name-only", f"{base}...HEAD", "--", "comfyui_embedded_docs/docs/"],
            capture_output=True, text=True, check=True,
        ).stdout
        paths = [REPO_ROOT.parent / p for p in out.splitlines() if p.strip().endswith(".md")]
    else:
        paths = sorted(DOCS_ROOT.rglob("*.md"))
    for p in paths:
        lang = p.stem
        if lang == "en":
            continue
        if langs and lang not in langs:
            continue
        if p.exists():
            yield p, lang


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true", help="write the cleaned files")
    ap.add_argument("--dry-run", action="store_true", help="report only (default)")
    ap.add_argument("--check-only", action="store_true",
                    help="exit 1 when leakage exists (CI gate), never write")
    ap.add_argument("--langs", default=None, help="comma-separated language filter")
    ap.add_argument("--changed-only", action="store_true", help="only files changed vs --base")
    ap.add_argument("--base", default="origin/main")
    args = ap.parse_args()

    langs = args.langs.split(",") if args.langs else None
    total_files = total_lines = 0
    per_lang: dict[str, int] = {}

    for path, lang in iter_docs(langs, args.changed_only, args.base):
        text = path.read_text(encoding="utf-8", errors="ignore")
        cleaned, removed = strip_leak(text, lang)
        if not removed:
            continue
        total_files += 1
        total_lines += removed
        per_lang[lang] = per_lang.get(lang, 0) + 1
        if args.apply and not args.check_only:
            path.write_text(cleaned, encoding="utf-8")

    for lang in sorted(per_lang, key=lambda l: -per_lang[l]):
        print(f"  {lang:7} {per_lang[lang]:4} files")
    verb = "fixed" if (args.apply and not args.check_only) else "found"
    print(f"\n{verb}: {total_files} files, {total_lines} leaked lines")
    if args.check_only and total_files:
        print("\nLeaked preamble / prompt block detected. Run with --apply to clean.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
