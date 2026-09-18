#!/usr/bin/env python3
"""Finalize an agent-written en.md body: validate, inject title/disclaimer/fingerprint, save.

Workflow (daily cron, agent-authored English):
    1. python3 scripts/scan_missing_nodes.py                 # script: which nodes changed (hash)
    2. agent reads ai_input/<Node>/{source_code.py,basic_info.json}
       plus the existing en.md, writes the NEW en.md body to a file
    3. python3 scripts/save_agent_doc.py --node <Node> --body /tmp/<Node>.md [--dry-run]
    4. python3 scripts/batch_translate_docs.py --lang <L> --node-list <Node> --force
                                                              # script: 11-language translation

The agent writes prose only (H1 omitted). This script owns every mechanical part:
title from the frontend display_name, the AI-generated disclaimer, and the
SHA-256 source fingerprint footer, so hand-written docs stay byte-compatible
with the pipeline format.

Validation before saving (fail fast, never write a broken doc):
  - body must contain "## Inputs" and "## Outputs" tables
  - every Inputs row must look like `| `name` | desc | TYPE | Yes/No | range |`
  - data types must be English schema identifiers (MODEL, IMAGE, ...)
  - no markdown code fences wrapping the document
  - exactly one H1 after title injection

Exit code 0 = saved (or dry-run OK), 1 = validation failed, nothing written.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from lib.doc_disclaimer import compose_document, create_en_disclaimer, strip_ai_disclaimer
from lib.doc_title import ensure_doc_title, strip_leading_h1
from lib.hash_footer import (
    format_source_hash_footer,
    load_node_source_sha256,
    strip_source_hash_footer,
)
from lib.paths import default_embedded_docs_path

DOCS_OUTPUT_PATH = default_embedded_docs_path() / "comfyui_embedded_docs" / "docs"

# schema identifiers that must remain English in the Data Type column
VALID_TYPES = {
    "MODEL", "MODEL_PATCH", "IMAGE", "MASK", "LATENT", "CONDITIONING", "CLIP", "VAE",
    "STRING", "INT", "FLOAT", "BOOLEAN", "COMBO", "DYNAMIC_COMBO", "AUDIO", "VIDEO",
    "BOUNDING_BOX", "FILE3D", "FILE3DGLB", "FILE3DFBX", "PROMPT", "EXTRA_PNGINFO",
    "WEBCAM", "GUIDER", "SAMPLER", "SIGMAS", "NOISE", "ANY", "PK_HOOK", "MESH",
    "AUTO_TRIGGER", "IC_LORA_PARAMETERS", "MODEL_TASK_ID", "IMAGE_TASK_ID",
}

ROW_RE = re.compile(r"^\|")
FENCE_LINE_RE = re.compile(r"^\s*(`{3,}|~{3,})")


def has_outer_fence(body: str) -> bool:
    """True when a fence wraps the whole body (any info string: ```, ```md, ```markdown).

    Inner fenced blocks are legitimate body content and are allowed; only a
    wrapper around the entire body is rejected.
    """
    lines = [l for l in body.splitlines() if l.strip()]
    if len(lines) < 2:
        return False
    first, last = lines[0].strip(), lines[-1].strip()
    opens = FENCE_LINE_RE.match(lines[0]) is not None
    closes = FENCE_LINE_RE.match(lines[-1]) is not None and last in ("```", "~~~") \
        or last.startswith("```") or last.startswith("~~~")
    return opens and closes


def validate(body: str, node_name: str) -> list[str]:
    """Return a list of problems; empty means the body is saveable."""
    problems: list[str] = []

    if has_outer_fence(body):
        problems.append("body is wrapped in a code fence (strip the outer fence)")

    if "## Inputs" not in body:
        problems.append("missing '## Inputs' section")
    if "## Outputs" not in body:
        problems.append("missing '## Outputs' section")

    # Inputs table: parameter rows must carry an English data type and Yes/No
    in_inputs = False
    in_outputs = False
    input_rows = output_rows = 0
    for line in body.splitlines():
        s = line.strip()
        if s.startswith("## "):
            in_inputs = s.startswith("## Inputs")
            in_outputs = "output" in s.lower()
            continue
        if not s.startswith("|") or s.startswith("|---") or re.match(r"^\|[\s:\-|]+\|$", s):
            continue
        cells = [c.strip() for c in s.split("|")[1:-1]]
        if in_inputs:
            if cells and cells[0].lower() in ("parameter", "参数"):
                continue  # header
            input_rows += 1
            if len(cells) < 5:
                problems.append(f"inputs row has {len(cells)} cells, expected 5: {s[:80]}")
                continue
            name, _desc, dtype, required = cells[0], cells[1], cells[2], cells[3]
            if not name.startswith("`") or not name.endswith("`"):
                problems.append(f"input name not backticked: {name!r}")
            if dtype.strip() not in VALID_TYPES:
                problems.append(f"input {name} has non-schema data type: {dtype!r}")
            if required not in ("Yes", "No"):
                problems.append(f"input {name} Required must be Yes/No, got {required!r}")
        elif in_outputs:
            if cells and "output name" in cells[0].lower():
                continue
            output_rows += 1
            if len(cells) < 3:
                problems.append(f"outputs row has {len(cells)} cells, expected 3: {s[:80]}")

    if input_rows == 0:
        problems.append("no input parameter rows found")
    if output_rows == 0:
        problems.append("no output rows found")

    h1s = re.findall(r"^# .+", body, re.M)
    if h1s:
        problems.append(
            f"{len(h1s)} H1 heading(s) in body (the script injects the title; "
            f"write the body without any H1)")

    return problems


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--node", required=True, help="Node name (docs/<Node>/)")
    ap.add_argument("--body", required=True, help="Path to the agent-written markdown body")
    ap.add_argument("--dry-run", action="store_true", help="Validate and print, do not write")
    args = ap.parse_args()

    node = args.node
    body_path = Path(args.body)
    if not body_path.exists():
        print(f"❌ body file not found: {body_path}", file=sys.stderr)
        return 1
    body = strip_source_hash_footer(strip_ai_disclaimer(body_path.read_text(encoding="utf-8")))

    problems = validate(body, node)
    if problems:
        print(f"❌ validation failed for {node}:")
        for p in problems:
            print(f"   - {p}")
        return 1

    sha = load_node_source_sha256(node)
    if not sha:
        print(f"⚠️  no source hash for {node}: saving without fingerprint footer")
        footer = ""
    else:
        footer = format_source_hash_footer(sha)

    final = compose_document(
        ensure_doc_title(strip_leading_h1(body), node, "en"),
        create_en_disclaimer(node),
        footer,
    )

    doc_dir = DOCS_OUTPUT_PATH / node
    doc_file = doc_dir / "en.md"
    if args.dry_run:
        print(f"✅ {node}: validation passed ({len(final)} bytes) [dry-run, not written]")
        print("-" * 70)
        print(final)
        return 0

    doc_dir.mkdir(parents=True, exist_ok=True)
    doc_file.write_text(final, encoding="utf-8")
    print(f"✅ {node}: en.md saved ({len(final)} bytes, fingerprint {'yes' if footer else 'none'})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
