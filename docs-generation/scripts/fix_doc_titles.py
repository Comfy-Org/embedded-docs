#!/usr/bin/env python3
"""
Fix missing, duplicate, or incorrect H1 titles in existing node documentation.

Titles are set from frontend nodeDefs display_name (locale → English → class name),
not from AI. Preserves disclaimer and SHA footer on each file.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import runtime  # noqa: F401
from lib.doc_disclaimer import strip_ai_disclaimer
from lib.doc_title import (
    HashMode,
    analyze_title_issues,
    fix_document_title,
    load_node_translations,
)
from lib.hash_footer import (
    extract_english_source_fingerprint_hex,
    load_node_source_sha256,
    strip_source_hash_footer,
)
from lib.paths import TRANSLATION_CONFIG, embedded_docs_dir, load_dotenv

load_dotenv()

DOCS_PATH = embedded_docs_dir()
DOC_LANGS = ["en", "zh", "zh-TW", "es", "fr", "ja", "ko", "ru", "ar", "tr", "pt-BR", "fa"]


def resolve_en_source_hex(node_name: str, hash_mode: HashMode) -> Optional[str]:
    """SHA hex for update mode: ai_input → en.md on disk."""
    if hash_mode != "update":
        return None
    from_ai = load_node_source_sha256(node_name)
    if from_ai:
        return from_ai
    en_path = DOCS_PATH / node_name / "en.md"
    if en_path.is_file():
        return extract_english_source_fingerprint_hex(en_path.read_text(encoding="utf-8"))
    return None


def load_translation_config() -> Dict[str, Any]:
    if not TRANSLATION_CONFIG.is_file():
        return {}
    with open(TRANSLATION_CONFIG, encoding="utf-8") as f:
        return json.load(f)


def iter_doc_files(
    node_filter: Optional[str] = None,
    lang_filter: Optional[str] = None,
) -> List[Tuple[Path, str, str]]:
    if not DOCS_PATH.is_dir():
        return []

    out: List[Tuple[Path, str, str]] = []
    for node_dir in sorted(DOCS_PATH.iterdir(), key=lambda p: p.name.lower()):
        if not node_dir.is_dir():
            continue
        if node_filter and node_dir.name != node_filter:
            continue
        langs = [lang_filter] if lang_filter else DOC_LANGS
        for lang in langs:
            md = node_dir / f"{lang}.md"
            if md.is_file():
                out.append((md, node_dir.name, lang))
    return out


def fix_file(
    path: Path,
    node_name: str,
    lang: str,
    translations: Dict[str, Any],
    lang_config: Dict[str, Any],
    dry_run: bool,
    hash_mode: HashMode,
    en_source_hex: Optional[str],
) -> Tuple[bool, List[str]]:
    original = path.read_text(encoding="utf-8")
    body = strip_ai_disclaimer(strip_source_hash_footer(original))
    issues = analyze_title_issues(body, node_name, lang, translations)
    if not issues:
        return False, []

    if not dry_run:
        path.write_text(
            fix_document_title(
                original,
                node_name,
                lang,
                translations,
                lang_config,
                hash_mode=hash_mode,
                en_source_hex=en_source_hex,
            ),
            encoding="utf-8",
        )
    return True, issues


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Fix H1 titles in existing node docs (frontend display_name)"
    )
    parser.add_argument("--mode", choices=("test", "all"), default="all")
    parser.add_argument("--count", type=int, default=20, help="Max files in test mode")
    parser.add_argument("--node", type=str, help="Only this node folder")
    parser.add_argument("--lang", type=str, choices=DOC_LANGS, help="Only this language")
    parser.add_argument("--dry-run", action="store_true", help="Report only, do not write")
    parser.add_argument(
        "--hash-mode",
        choices=("preserve", "update"),
        default="preserve",
        help=(
            "preserve: keep original disclaimer + SHA footer unchanged (default); "
            "update: rewrite disclaimer and sync SHA from en.md / ai_input"
        ),
    )
    args = parser.parse_args()
    hash_mode: HashMode = args.hash_mode

    if not DOCS_PATH.is_dir():
        print(f"❌ Docs directory not found: {DOCS_PATH}")
        return 1

    translations = load_node_translations()
    if not translations:
        print(
            "⚠️  Warning: data/node_translations.json not found or empty.\n"
            "   Titles will fall back to class names. Run:\n"
            "   python3 scripts/sync_frontend_translations.py <frontend_path> --export"
        )

    lang_config = load_translation_config()
    files = iter_doc_files(args.node, args.lang)
    if args.mode == "test":
        files = files[: args.count]

    print("=" * 80)
    print("Fix document titles (frontend display_name)")
    print("=" * 80)
    print(f"Docs: {DOCS_PATH}")
    print(f"Files to scan: {len(files)}")
    print(f"Mode: {'dry-run' if args.dry_run else 'write'}")
    print(f"Hash: {hash_mode}")
    print("=" * 80)
    print()

    fixed_count = 0
    skipped_count = 0
    issue_totals: Dict[str, int] = {}
    en_hash_cache: Dict[str, Optional[str]] = {}

    for path, node_name, lang in files:
        en_hex: Optional[str] = None
        if hash_mode == "update":
            if node_name not in en_hash_cache:
                en_hash_cache[node_name] = resolve_en_source_hex(node_name, hash_mode)
            en_hex = en_hash_cache[node_name]

        changed, issues = fix_file(
            path,
            node_name,
            lang,
            translations,
            lang_config,
            args.dry_run,
            hash_mode,
            en_hex,
        )
        if changed:
            fixed_count += 1
            labels = ", ".join(issues)
            action = "would fix" if args.dry_run else "fixed"
            print(f"✅ {action}: {node_name}/{lang}.md  ({labels})")
            for code in issues:
                issue_totals[code] = issue_totals.get(code, 0) + 1
        else:
            skipped_count += 1

    print()
    print("=" * 80)
    print("Summary")
    print("=" * 80)
    print(f"{'Would fix' if args.dry_run else 'Fixed'}: {fixed_count}")
    print(f"OK (no change): {skipped_count}")
    if issue_totals:
        print("Issues addressed:")
        for code, n in sorted(issue_totals.items()):
            print(f"  - {code}: {n}")
    print("=" * 80)
    return 0


if __name__ == "__main__":
    sys.exit(main())
