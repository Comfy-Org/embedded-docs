#!/usr/bin/env python3
"""Batch-fix Range column localization residue in OpenAI node translations (2026-09-17)."""
import re, os, glob

DOCS = "/Users/linmoumou/Documents/embedded-docs/comfyui_embedded_docs/docs"
NODES = ["OpenAIGPTImage1", "OpenAIGPTImageNodeV2"]

# Per-language replacements applied only to Range column content (last | ... | cell containing " to ")
LANG_MAP = {
    "zh":      [(" to ", " 到 "), (", step ", "，步长 "), ("(step ", "(步长 "), ("step ", "步长 ")],
    "zh-TW":   [(" to ", " 至 "), (", step ", "，步進值 "), ("(step ", "(步進值 "), ("step ", "步進值 ")],
    "ja":      [(" to ", "〜"), (", step ", "、ステップ "), ("(step ", "(ステップ "), ("step ", "ステップ ")],
    "ko":      [(" to ", " ~ "), (", step ", ", 단계 "), ("(step ", "(단계 "), ("step ", "단계 ")],
    "ru":      [(" to ", " до "), (", step ", ", шаг "), ("(step ", "(шаг "), ("step ", "шаг ")],
    "ar":      [(" to ", " إلى "), (", step ", ", خطوة "), ("(step ", "(خطوة "), ("step ", "خطوة ")],
    "tr":      [(" to ", " ile "), (", step ", ", adım "), ("(step ", "(adım "), ("step ", "adım ")],
    "es":      [(" to ", " a "), (", step ", ", paso "), ("(step ", "(paso "), ("step ", "paso ")],
    "fr":      [(" to ", " à "), (", step ", ", pas "), ("(step ", "(pas "), ("step ", "pas ")],
    "pt-BR":   [(" to ", " a "), (", step ", ", passo "), ("(step ", "(passo "), ("step ", "passo ")],
    "fa":      [(" to ", " تا "), (", step ", ", گام "), ("(step ", "(گام "), ("step ", "گام ")],
}

def fix_range_cell(cell, repls):
    out = cell
    for a, b in repls:
        out = out.replace(a, b)
    return out

total = 0
for node in NODES:
    for lang, repls in LANG_MAP.items():
        path = os.path.join(DOCS, node, f"{lang}.md")
        if not os.path.exists(path):
            print(f"MISSING {path}")
            continue
        with open(path, encoding="utf-8") as f:
            lines = f.readlines()
        changed = False
        for i, line in enumerate(lines):
            # table row with pipes, and Range cell contains ' to ' followed by digit
            if line.startswith("|") and re.search(r"\|[^|]*\b to [0-9]", line):
                parts = line.split("|")
                # find cell(s) containing " to <digit>"
                for j, p in enumerate(parts):
                    if re.search(r"\b to [0-9]", p) or "step " in p or "(step " in p:
                        newp = fix_range_cell(p, repls)
                        if newp != p:
                            parts[j] = newp
                            changed = True
                if changed:
                    lines[i] = "|".join(parts)
        if changed:
            with open(path, "w", encoding="utf-8") as f:
                f.writelines(lines)
            total += 1
            print(f"FIXED {path}")
print(f"\nTotal files fixed: {total}")
