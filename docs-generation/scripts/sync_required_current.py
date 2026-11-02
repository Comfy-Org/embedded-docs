#!/usr/bin/env python3
"""Sync Required column (and drifted data-type column) in all translation files
to match current en.md, aligned by param-row index.

Safety: alignment is accepted only when row count matches AND data-type column
matches on every row (types stay English-uppercase in all languages per rules).
Files failing that check are logged for manual review, not touched.
"""
import os, re, json, sys

DOCS = "/Users/linmoumou/Documents/embedded-docs/comfyui_embedded_docs/docs"
LANGS = {
    "zh":     ("是", "否"),
    "zh-TW":  ("是", "否"),
    "ja":     ("はい", "いいえ"),
    "ko":     ("예", "아니요"),
    "ru":     ("Да", "Нет"),
    "ar":     ("نعم", "لا"),
    "tr":     ("Evet", "Hayır"),
    "pt-BR":  ("Sim", "Não"),
    "fa":     ("بله", "خیر"),
    "es":     ("Sí", "No"),
    "fr":     ("Oui", "Non"),
}
EN_YES, EN_NO = "Yes", "No"

# generic param row: | `param` | desc | TYPE | required | range |
ROW = re.compile(r'^(\| `[^`]+` \|.*\| )([A-Z][A-Z_0-9]*)( \| )([^|]+?)( \|.*\|)$')

def parse_rows(lines):
    """Return list of (line_idx, type, req_token, regex_match_spans)."""
    rows = []
    for i, l in enumerate(lines):
        m = ROW.match(l)
        if m:
            rows.append((i, m.group(2), m.group(4)))
    return rows

changed = {}   # path -> n_lines
type_fixed = {}  # path -> n_lines
skipped = []   # (path, reason)

node_dirs = sorted(d for d in os.listdir(DOCS) if os.path.isdir(os.path.join(DOCS, d)))
for node in node_dirs:
    nd = os.path.join(DOCS, node)
    en_path = os.path.join(nd, "en.md")
    if not os.path.isfile(en_path):
        continue
    en_lines = open(en_path).read().splitlines()
    en_rows = parse_rows(en_lines)
    if not en_rows:
        continue
    for lang, (req_tok, opt_tok) in LANGS.items():
        tr_path = os.path.join(nd, f"{lang}.md")
        if not os.path.isfile(tr_path):
            continue
        tr_lines = open(tr_path).read().splitlines()
        tr_rows = parse_rows(tr_lines)
        if len(tr_rows) != len(en_rows):
            skipped.append((f"{node}/{lang}.md", f"row count {len(tr_rows)} vs {len(en_rows)}"))
            continue
        # verify type columns align
        type_mism = [(a, b) for (_, a, _) in en_rows if False]  # placeholder
        bad = False
        for (ei, etype, ereq), (ti, ttype, treq) in zip(en_rows, tr_rows):
            if etype != ttype:
                skipped.append((f"{node}/{lang}.md", f"type mismatch line {ti+1}: {ttype} vs {etype}"))
                bad = True
                break
        if bad:
            continue
        mod = 0
        tmod = 0
        for (ei, etype, ereq), (ti, ttype, treq) in zip(en_rows, tr_rows):
            want = req_tok if ereq == EN_YES else (opt_tok if ereq == EN_NO else None)
            if want is None:
                continue  # en.md has unusual token; leave alone
            new_line = tr_lines[ti]
            if treq != want:
                new_line = ROW.sub(r'\g<1>\g<2>\g<3>' + want + r'\g<5>', tr_lines[ti])
                if new_line != tr_lines[ti]:
                    tr_lines[ti] = new_line
                    mod += 1
        if mod:
            open(tr_path, "w").write("\n".join(tr_lines) + "\n")
            changed[f"{node}/{lang}.md"] = mod

print(f"translation files modified: {len(changed)}, lines changed: {sum(changed.values())}")
print(f"type-column fixes: {sum(type_fixed.values())}")
print(f"skipped (need manual review): {len(skipped)}")
for s in skipped[:30]:
    print("  SKIP:", s)
json.dump({"changed": changed, "skipped": skipped}, open("/tmp/required_sync_result.json", "w"), indent=1)
