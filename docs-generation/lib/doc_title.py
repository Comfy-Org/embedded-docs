"""Inject node display-name headings from frontend translations (not AI)."""

from __future__ import annotations

import json
import re
from functools import lru_cache
from typing import Any, Dict, Literal, Optional

HashMode = Literal["preserve", "update"]

from lib.paths import NODE_TRANSLATIONS

# Level-1 heading: single `#`, not `##` or deeper.
_H1_RE = re.compile(r"^#(?!#)")


@lru_cache(maxsize=1)
def load_node_translations() -> Dict[str, Any]:
    """Load exported frontend nodeDefs translations (data/node_translations.json)."""
    if not NODE_TRANSLATIONS.is_file():
        return {}
    try:
        with open(NODE_TRANSLATIONS, encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, OSError):
        return {}


def _display_name_for_lang(
    data: Dict[str, Any],
    lang: str,
    node_name: str,
) -> str:
    lang_data = data.get(lang, {})
    if not isinstance(lang_data, dict):
        return ""
    node_data = lang_data.get(node_name)
    if not isinstance(node_data, dict):
        return ""
    return str(node_data.get("display_name", "")).strip()


def get_node_display_name(
    node_name: str,
    lang: str = "en",
    translations: Optional[Dict[str, Any]] = None,
) -> str:
    """
    Return display name from frontend nodeDefs.

    Fallback order:
    1. Target language ``display_name``
    2. English ``display_name`` (when target lang is missing)
    3. ComfyUI class name (``node_name``)
    """
    data = translations if translations is not None else load_node_translations()

    if lang != "en":
        localized = _display_name_for_lang(data, lang, node_name)
        if localized:
            return localized

    english = _display_name_for_lang(data, "en", node_name)
    if english:
        return english

    return node_name


def _is_h1_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    if not _H1_RE.match(stripped):
        return False
    return bool(re.match(r"^#(?!#)\s*\S", stripped))


def extract_leading_h1_title(content: str) -> Optional[str]:
    """Return the text of the first leading level-1 heading, or None."""
    lines = content.split("\n")
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1
    if i >= len(lines) or not _is_h1_line(lines[i]):
        return None
    m = re.match(r"^#(?!#)\s*(.+)$", lines[i].strip())
    return m.group(1).strip() if m else None


def count_leading_h1_lines(content: str) -> int:
    """Count consecutive level-1 headings at the start of the document."""
    lines = content.split("\n")
    i = 0
    count = 0
    while True:
        while i < len(lines) and not lines[i].strip():
            i += 1
        if i < len(lines) and _is_h1_line(lines[i]):
            count += 1
            i += 1
            continue
        break
    return count


def analyze_title_issues(
    body: str,
    node_name: str,
    lang: str = "en",
    translations: Optional[Dict[str, Any]] = None,
) -> list[str]:
    """
    Detect title problems: missing, duplicate, or mismatch vs frontend display_name.
    """
    issues: list[str] = []
    n = count_leading_h1_lines(body)
    expected = get_node_display_name(node_name, lang, translations)

    if n == 0:
        issues.append("missing")
    if n > 1:
        issues.append("duplicate")

    current = extract_leading_h1_title(body)
    if n >= 1 and current != expected:
        issues.append("mismatch")

    return issues


def title_needs_fix(
    body: str,
    node_name: str,
    lang: str = "en",
    translations: Optional[Dict[str, Any]] = None,
) -> bool:
    return bool(analyze_title_issues(body, node_name, lang, translations))


def strip_leading_h1(content: str) -> str:
    """Remove all consecutive leading level-1 markdown headings."""
    lines = content.split("\n")
    i = 0
    while i < len(lines):
        while i < len(lines) and not lines[i].strip():
            i += 1
        if i < len(lines) and _is_h1_line(lines[i]):
            i += 1
            continue
        break
    return "\n".join(lines[i:]).lstrip("\n")


def ensure_doc_title(
    body: str,
    node_name: str,
    lang: str = "en",
    translations: Optional[Dict[str, Any]] = None,
) -> str:
    """
    Prepend ``# {display_name}`` to the document body.
    Strips any existing leading H1(s) first so AI-generated titles are replaced.
    """
    clean = strip_leading_h1(body.strip())
    title = get_node_display_name(node_name, lang, translations)
    if not clean:
        return f"# {title}\n"
    return f"# {title}\n\n{clean}"


def fix_document_title(
    original_content: str,
    node_name: str,
    lang: str,
    translations: Optional[Dict[str, Any]] = None,
    lang_config: Optional[dict] = None,
    hash_mode: HashMode = "preserve",
    en_source_hex: Optional[str] = None,
) -> str:
    """
    Rebuild a markdown file with corrected H1.

    hash_mode:
      - ``preserve``: keep original disclaimer + SHA footer bytes unchanged
      - ``update``: rewrite disclaimer and sync SHA from ``en_source_hex`` / en.md / ai_input
    """
    from lib.doc_disclaimer import (
        assemble_document_with_metadata_suffix,
        compose_document,
        create_en_disclaimer,
        create_translated_disclaimer,
        extract_metadata_suffix,
        strip_ai_disclaimer,
    )
    from lib.hash_footer import (
        extract_english_source_fingerprint_hex,
        format_source_hash_footer,
        load_node_source_sha256,
        strip_source_hash_footer,
    )

    body = strip_ai_disclaimer(strip_source_hash_footer(original_content))
    fixed_body = ensure_doc_title(body, node_name, lang, translations)

    if hash_mode == "preserve":
        suffix = extract_metadata_suffix(original_content)
        return assemble_document_with_metadata_suffix(fixed_body, suffix)

    if en_source_hex:
        src_fp = en_source_hex
    elif lang == "en":
        src_fp = (
            load_node_source_sha256(node_name)
            or extract_english_source_fingerprint_hex(original_content)
        )
    else:
        src_fp = None

    if lang == "en":
        disclaimer = create_en_disclaimer(node_name)
    else:
        disclaimer = create_translated_disclaimer(lang, node_name, lang_config or {})

    footer = format_source_hash_footer(src_fp) if src_fp else ""
    return compose_document(fixed_body, disclaimer, footer)
