#!/usr/bin/env python3
"""
One-time migration for embedded-docs markdown files:

1. Move AI disclaimer blockquote from top to bottom (before SHA footer if present).
2. Reorder parameter / output tables so Description is the second column.

Usage:
  python3 migrate_docs_format.py --dry-run          # preview changes
  python3 migrate_docs_format.py                  # apply to all docs
  python3 migrate_docs_format.py --node KSampler  # single node
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import runtime  # noqa: F401
from lib.doc_disclaimer import (
    compose_document,
    create_en_disclaimer,
    create_translated_disclaimer,
    strip_ai_disclaimer,
)
from lib.hash_footer import (
    SOURCE_HASH_FOOTER_RE,
    extract_english_source_fingerprint_hex,
    format_source_hash_footer,
    strip_source_hash_footer,
)
from lib.paths import TRANSLATION_CONFIG, default_embedded_docs_path, embedded_docs_dir, load_dotenv

load_dotenv()

DOCS_PATH = embedded_docs_dir()

# Header cell (normalized) -> role for column reordering
_DESCRIPTION_HINTS = (
    "description",
    "descripción",
    "descripcion",
    "descrição",
    "descricao",
    "beschreibung",
    "описание",
    "açıklama",
    "aciklama",
    "descriere",
    "描述",
    "说明",
    "說明",
    "説明",
    "설명",
    "الوصف",
    "توضیح",
    "توضیحات",
    "descrição da função",
    "descripción de la función",
    "function description",
    "descrição da função",
)

_TABLE_ROW_RE = re.compile(r"^\s*\|")
_SEPARATOR_RE = re.compile(r"^\s*\|?[\s:\-|]+\|?\s*$")


def _normalize_header(cell: str) -> str:
    return re.sub(r"\s+", " ", cell.strip().lower())


def _parse_table_cells(line: str) -> Optional[List[str]]:
    if not _TABLE_ROW_RE.match(line):
        return None
    inner = line.strip()
    if inner.startswith("|"):
        inner = inner[1:]
    if inner.endswith("|"):
        inner = inner[:-1]
    return [c.strip() for c in inner.split("|")]


def _is_separator_row(line: str) -> bool:
    cells = _parse_table_cells(line)
    if not cells:
        return False
    return all(re.fullmatch(r":?-{2,}:?", c.strip()) or not c.strip() for c in cells)


def _description_col_index(headers: List[str]) -> Optional[int]:
    for i, cell in enumerate(headers):
        norm = _normalize_header(cell)
        if any(h in norm for h in _DESCRIPTION_HINTS):
            return i
    return None


def _reorder_table_row(cells: List[str], order: List[int]) -> str:
    padded = cells + [""] * (max(order) + 1 - len(cells))
    reordered = [padded[i] if i < len(padded) else "" for i in order]
    return "| " + " | ".join(reordered) + " |"


def _migrate_table_block(lines: List[str]) -> Tuple[List[str], bool]:
    """Reorder one markdown table so column 1 is Description (column 0 unchanged)."""
    if len(lines) < 2:
        return lines, False
    headers = _parse_table_cells(lines[0])
    if not headers or len(headers) < 3:
        return lines, False

    desc_idx = _description_col_index(headers)
    if desc_idx is None or desc_idx == 1:
        return lines, False

    order = [0, desc_idx] + [i for i in range(len(headers)) if i not in (0, desc_idx)]
    out: List[str] = [_reorder_table_row(headers, order)]

    i = 1
    if i < len(lines) and _is_separator_row(lines[i]):
        out.append("| " + " | ".join(["---"] * len(order)) + " |")
        i += 1

    changed = True
    while i < len(lines):
        line = lines[i]
        if not _TABLE_ROW_RE.match(line):
            break
        if _is_separator_row(line):
            i += 1
            continue
        cells = _parse_table_cells(line)
        if cells:
            out.append(_reorder_table_row(cells, order))
        else:
            out.append(line)
        i += 1

    return out, changed


def migrate_tables(content: str) -> Tuple[str, int]:
    """Reorder all tables where Description is not already the second column."""
    lines = content.split("\n")
    out: List[str] = []
    i = 0
    tables_changed = 0

    while i < len(lines):
        line = lines[i]
        headers = _parse_table_cells(line)
        if headers and len(headers) >= 3 and _description_col_index(headers) is not None:
            block = [line]
            j = i + 1
            while j < len(lines) and (_TABLE_ROW_RE.match(lines[j]) or not lines[j].strip()):
                if _TABLE_ROW_RE.match(lines[j]):
                    block.append(lines[j])
                elif not lines[j].strip() and block:
                    break
                j += 1
            migrated, changed = _migrate_table_block(block)
            out.extend(migrated)
            if changed:
                tables_changed += 1
            i = i + len(block)
            continue
        out.append(line)
        i += 1

    return "\n".join(out), tables_changed


def _load_translation_config() -> Dict[str, dict]:
    if not TRANSLATION_CONFIG.exists():
        return {}
    with open(TRANSLATION_CONFIG, encoding="utf-8") as f:
        return json.load(f)


def _disclaimer_for_lang(node_name: str, lang: str, lang_config: Dict[str, dict]) -> str:
    if lang == "en":
        return create_en_disclaimer(node_name)
    if lang in lang_config:
        return create_translated_disclaimer(lang, node_name, lang_config[lang])
    return create_en_disclaimer(node_name).replace("/en.md", f"/{lang}.md")


def _extract_footer(content: str) -> str:
    m = SOURCE_HASH_FOOTER_RE.search(content)
    return m.group(0) if m else ""


def migrate_file(
    path: Path,
    node_name: str,
    lang: str,
    lang_config: Dict[str, dict],
) -> Tuple[bool, str]:
    """
    Returns (changed, summary).
    """
    original = path.read_text(encoding="utf-8")
    footer_hex = extract_english_source_fingerprint_hex(original)
    footer = format_source_hash_footer(footer_hex) if footer_hex else _extract_footer(original)

    body = strip_ai_disclaimer(strip_source_hash_footer(original))
    body, table_count = migrate_tables(body)

    disclaimer = _disclaimer_for_lang(node_name, lang, lang_config)
    new_content = compose_document(body, disclaimer, footer)

    if new_content == original:
        return False, "unchanged"

    path.write_text(new_content, encoding="utf-8")
    parts = ["disclaimer→bottom"]
    if table_count:
        parts.append(f"tables={table_count}")
    return True, ", ".join(parts)


def iter_doc_files(docs_path: Path, node_filter: Optional[str] = None) -> List[Tuple[Path, str, str]]:
    """Yield (path, node_name, lang_code)."""
    if not docs_path.exists():
        return []
    out: List[Tuple[Path, str, str]] = []
    for node_dir in sorted(docs_path.iterdir()):
        if not node_dir.is_dir():
            continue
        if node_filter and node_dir.name != node_filter:
            continue
        for md in sorted(node_dir.glob("*.md")):
            out.append((md, node_dir.name, md.stem))
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description="Migrate embedded-docs: disclaimer to bottom + table columns")
    parser.add_argument("--dry-run", action="store_true", help="Preview only; do not write files")
    parser.add_argument("--node", type=str, help="Migrate a single node directory")
    parser.add_argument(
        "--docs-path",
        type=Path,
        default=DOCS_PATH,
        help=f"Docs root (default: {DOCS_PATH})",
    )
    args = parser.parse_args()
    docs_path = args.docs_path

    if not docs_path.exists():
        print(f"ERROR: docs path not found: {docs_path}")
        return 1

    lang_config = _load_translation_config()
    files = iter_doc_files(docs_path, args.node)
    if not files:
        print("No markdown files found.")
        return 1

    changed_files = 0
    unchanged_files = 0
    tables_total = 0
    errors: List[str] = []

    print(f"Migrating {len(files)} file(s) under {docs_path} (dry_run={args.dry_run})")

    for path, node_name, lang in files:
        try:
            original = path.read_text(encoding="utf-8")
            footer_hex = extract_english_source_fingerprint_hex(original)
            footer = format_source_hash_footer(footer_hex) if footer_hex else _extract_footer(original)
            body = strip_ai_disclaimer(strip_source_hash_footer(original))
            body, table_count = migrate_tables(body)
            disclaimer = _disclaimer_for_lang(node_name, lang, lang_config)
            new_content = compose_document(body, disclaimer, footer)

            if new_content == original:
                unchanged_files += 1
                continue

            tables_total += table_count
            changed_files += 1
            rel = path.relative_to(docs_path)
            had_top = original.lstrip().startswith(">")
            print(f"  {'[dry-run] ' if args.dry_run else ''}✓ {rel} (tables={table_count}, was_top_disclaimer={had_top})")

            if not args.dry_run:
                path.write_text(new_content, encoding="utf-8")
        except Exception as e:
            errors.append(f"{path}: {e}")

    print()
    print("=" * 60)
    print(f"Changed:   {changed_files}")
    print(f"Unchanged: {unchanged_files}")
    print(f"Tables reordered (total): {tables_total}")
    if errors:
        print(f"Errors:    {len(errors)}")
        for err in errors[:20]:
            print(f"  - {err}")
        return 1
    if args.dry_run and changed_files:
        print("\nRe-run without --dry-run to apply.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
