#!/usr/bin/env python3
"""Mechanically sync Required-column Yes->No flips from en.md commit ed0975a95
into all 11 translation files, aligned by table row index.

Only flips rows where en.md currently has '| No |' in the Required column AND
the pre-commit (ed0975a95^) en.md had '| Yes |' on the same row. Translation
files get their localized required-token -> optional-token in column 4.
"""
import subprocess, re, json, sys

REPO = "/Users/linmoumou/Documents/embedded-docs"
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
    # es: Yes->"Sí", No->"No" (optional token same as English)
    "es":     ("Sí", "No"),
    # fr: "Oui" -> "Non"
    "fr":     ("Oui", "Non"),
}

def run(cmd):
    return subprocess.run(cmd, cwd=REPO, capture_output=True, text=True).stdout

# 1. Extract per-file row-index flips from ed0975a95 using two full file versions
flips = {}  # en_path -> set of table-row indices (0-based within the Inputs table rows)
diff = run(["git", "diff", "ed0975a95^", "ed0975a95", "--", "comfyui_embedded_docs/docs/*/en.md"])
cur = None
old_rows_idx = {}  # per-file: current row index counter for '-' side
# Simpler: load both versions of each file, walk Inputs table rows, compare Required col
names = run(["git", "diff", "--name-only", "ed0975a95^", "ed0975a95", "--", "comfyui_embedded_docs/docs/*/en.md"]).split()

ROW = re.compile(r'^\| `([^`]+)` \|.*\| [A-Z_]+ \| (Yes|No) \|')
def table_rows(text):
    """Return list of (param, required) for rows in Inputs tables, keyed by row order."""
    rows = []
    for l in text.splitlines():
        m = ROW.match(l)
        if m:
            rows.append((m.group(1), m.group(2)))
    return rows

for en in names:
    old = run(["git", "show", f"ed0975a95^:{en}"])
    new = run(["git", "show", f"ed0975a95:{en}"])
    # map by param name occurrence index (params can repeat across tables? use per-table walk)
    old_rows = table_rows(old)
    new_rows = table_rows(new)
    if len(old_rows) != len(new_rows):
        print(f"WARN row count mismatch {en}: {len(old_rows)} vs {len(new_rows)}", file=sys.stderr)
    fl = set()
    for i, ((op, oreq), (np_, nreq)) in enumerate(zip(old_rows, new_rows)):
        if oreq == "Yes" and nreq == "No":
            fl.add(i)
    if fl:
        flips[en] = fl

print(f"files with flips: {len(flips)}, total flip row indices: {sum(len(v) for v in flips.values())}")

# 2. Apply to translation files
opt_re = re.compile(r'^(\| `[^`]+` \|.*\| [A-Z_]+ \| )(Sí|Oui|はい|예|Да|نعم|Evet|Sim|بله)( \|.*\|)$')

changed_files = 0
changed_lines = 0
skipped = []
for en, fl in flips.items():
    dirp = en.rsplit("/", 1)[0]
    for lang, (req_tok, opt_tok) in LANGS.items():
        path = f"{dirp}/{lang}.md"
        try:
            with open(f"{REPO}/{path}") as f:
                lines = f.read().splitlines(keepends=False)
        except FileNotFoundError:
            skipped.append(path)
            continue
        # collect table row indices (same ROW regex; required token is localized)
        trow = re.compile(r'^(\| `[^`]+` \|.*\| [A-Z_]+ \| )(' + re.escape(req_tok) + r')( \|.*\|)$')
        idx = -1
        mod = 0
        for i, l in enumerate(lines):
            m = ROW.match(l) or (l.startswith('| `') and '| MODEL |' in l or True)
            # count only rows matching the generic param-row shape in *any* table
            if re.match(r'^\| `[^`]+` \| .*\| [A-Z_]+ \|', l):
                idx += 1
                if idx in fl and req_tok in l:
                    nl = trow.sub(r'\g<1>' + opt_tok + r'\g<3>', l)
                    if nl != l:
                        lines[i] = nl
                        mod += 1
        if mod:
            with open(f"{REPO}/{path}", "w") as f:
                f.write("\n".join(lines) + "\n")
            changed_files += 1
            changed_lines += mod

print(f"translation files modified: {changed_files}, lines flipped: {changed_lines}")
print(f"missing translation files (skipped): {len(skipped)}: {skipped[:5]}")
