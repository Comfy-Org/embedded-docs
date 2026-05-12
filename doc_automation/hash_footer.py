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

from node_source_extract import class_source_from_contextual_bundle

DOC_AUTOMATION_PATH = Path(__file__).resolve().parent
AI_INPUT_PATH = DOC_AUTOMATION_PATH / "ai_input"

SOURCE_HASH_FOOTER_RE = re.compile(
    r"\n---\s*\n\*\*Source fingerprint \(SHA-256\):\*\*\s*`[a-fA-F0-9]{64}`\s*$",
    re.MULTILINE,
)


def strip_source_hash_footer(markdown_body: str) -> str:
    """Remove trailing source fingerprint footer (e.g. before translation)."""
    return SOURCE_HASH_FOOTER_RE.sub("", markdown_body.rstrip()).rstrip()


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
