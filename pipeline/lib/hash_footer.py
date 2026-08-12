"""
Shared helpers for the optional SHA-256 footer on en.md (node class body only).
Fingerprints match ``NodeVersionTracker`` / ``prepare_ai_input`` after contextual extraction:
the saved ``ai_input/*/source_code.py`` may include preamble + cross-file context, but the
hash is computed on the node class definition alone.
"""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Optional

from lib.node_source_extract import class_source_from_contextual_bundle
from lib.paths import AI_INPUT_DIR

AI_INPUT_PATH = AI_INPUT_DIR

SOURCE_HASH_FOOTER_RE = re.compile(
    r"\n---\s*\n\*\*Source fingerprint \(SHA-256\):\*\*\s*`[a-fA-F0-9]{64}`\s*$",
    re.MULTILINE,
)

# Same label as in ``format_source_hash_footer`` / en.md (keep ASCII so translations stay comparable).
ENGLISH_SOURCE_FINGERPRINT_HEX_RE = re.compile(
    r"\*\*Source fingerprint \(SHA-256\):\*\*\s*`([a-fA-F0-9]{64})`",
)


def strip_source_hash_footer(markdown_body: str) -> str:
    """Remove trailing source fingerprint footer (e.g. before translation)."""
    return SOURCE_HASH_FOOTER_RE.sub("", markdown_body.rstrip()).rstrip()


def extract_english_source_fingerprint_hex(markdown_body: str) -> Optional[str]:
    """Parse the English footer line left by ``batch_generate_docs``; returns lowercase hex or None."""
    m = ENGLISH_SOURCE_FINGERPRINT_HEX_RE.search(markdown_body)
    if not m:
        return None
    h = m.group(1).lower()
    if len(h) == 64 and all(c in "0123456789abcdef" for c in h):
        return h
    return None


def strip_trailing_fingerprint_section(markdown_body: str) -> str:
    """Drop a trailing ``---`` block that contains a SHA-256 hex in backticks (any localized heading)."""
    body = markdown_body.rstrip()
    idx = body.rfind("\n---")
    if idx == -1:
        return markdown_body
    tail = body[idx:]
    if re.search(r"`[a-fA-F0-9]{64}`", tail):
        return body[:idx].rstrip()
    return markdown_body


def load_node_source_sha256(node_name: str) -> Optional[str]:
    """SHA-256 (hex, UTF-8) of the node ``class`` body — same scope as ``basic_info.version_info.source_hash``."""

    node_dir = AI_INPUT_PATH / node_name
    basic = node_dir / "basic_info.json"
    if basic.exists():
        try:
            with open(basic, encoding="utf-8") as f:
                data = json.load(f)
            h = (data.get("version_info") or {}).get("source_hash")
            if isinstance(h, str) and len(h) == 64:
                lc = h.lower()
                if all(c in "0123456789abcdef" for c in lc):
                    return lc
        except (json.JSONDecodeError, OSError, TypeError):
            pass
    src_file = node_dir / "source_code.py"
    if src_file.exists():
        try:
            text = src_file.read_text(encoding="utf-8")
            body = class_source_from_contextual_bundle(text)
            return hashlib.sha256(body.encode("utf-8")).hexdigest()
        except OSError:
            pass
    return None


def format_source_hash_footer(sha256_hex: str) -> str:
    return f"\n\n---\n**Source fingerprint (SHA-256):** `{sha256_hex}`\n"
