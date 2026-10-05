#!/usr/bin/env python3
"""Batch-fix Range-column localization residue ('X to N', '(step: N)') in
translated files, using per-language token maps. Also localizes 'Yes'/'No'
Required tokens missed by AI retranslation. Skips en.md.
"""
import re, json, os, sys

DOCS = "/Users/linmoumou/Documents/embedded-docs/comfyui_embedded_docs/docs"
LANG_MAP = {
    "zh":     {"to": "到",   "step": "步长"},
    "zh-TW":  {"to": "至",   "step": "步進值"},
    "ja":     {"to": "〜",   "step": "ステップ"},
    "ko":     {"to": " ~ ",  "step": "단계"},
    "ru":     {"to": "до",   "step": "шаг"},
    "ar":     {"to": "إلى",  "step": "خطوة"},
    "tr":     {"to": None,   "step": "adım"},   # tr handled specially
    "es":     {"to": "a",    "step": "paso"},
    "fr":     {"to": "à",    "step": "pas"},
    "pt-BR":  {"to": "a",    "step": "passo"},
    "fa":     {"to": "تا",   "step": "گام"},
}
REQ_MAP = {
    "zh": ("是", "否"), "zh-TW": ("是", "否"), "ja": ("はい", "いいえ"),
    "ko": ("예", "아니요"), "ru": ("Да", "Нет"), "ar": ("نعم", "لا"),
    "tr": ("Evet", "Hayır"), "pt-BR": ("Sim", "Não"), "fa": ("بله", "خیر"),
    "es": ("Sí", "No"), "fr": ("Oui", "Non"),
}

range_pat = re.compile(r'(\d+(?:\.\d+)?) to (\d+(?:\.\d+)?)')
step_pat  = re.compile(r'\(step:?\s*([0-9.]+)\)|\(step ([0-9.]+)\)')
yes_row   = re.compile(r'^(\| `[^`]+` \|.*\| [A-Z_]+ \| )Yes( \|.*\|)$')
# NOTE: 2 groups -> \g<1> req/opt \g<2>

def fix_tr_range(s):
    # tr: "X to Y arası" pattern: "0 to 100" -> "0 ile 100 arası"
    return re.sub(r'(\d+(?:\.\d+)?) to (\d+(?:\.\d+)?)', r'\1 ile \2 arası', s)

def process_file(path, lang):
    txt = open(path).read()
    m = LANG_MAP[lang]
    orig = txt
    n_fix = 0
    # Range 'to'
    if m["to"] is None:  # tr
        txt2 = fix_tr_range(txt)
    else:
        txt2 = range_pat.sub(r'\1 ' + m["to"] + r' \2', txt)
    if txt2 != txt: n_fix += len(range_pat.findall(txt)); txt = txt2
    # step
    if lang == "ja":
        txt2 = step_pat.sub(r'（ステップ \1\2）', txt)
    elif lang == "zh-TW":
        txt2 = step_pat.sub(r'（步進值：\1\2）', txt)
    elif lang == "ko":
        txt2 = step_pat.sub(r'(단계: \1\2)', txt)
    elif lang == "ru":
        txt2 = step_pat.sub(r'(шаг: \1\2)', txt)
    elif lang == "ar":
        txt2 = step_pat.sub(r'(خطوة: \1\2)', txt)
    elif lang == "tr":
        txt2 = step_pat.sub(r'(adım: \1\2)', txt)
    elif lang == "es":
        txt2 = step_pat.sub(r'(paso: \1\2)', txt)
    elif lang == "fr":
        txt2 = step_pat.sub(r'(pas: \1\2)', txt)
    elif lang == "pt-BR":
        txt2 = step_pat.sub(r'(passo: \1\2)', txt)
    elif lang == "fa":
        txt2 = step_pat.sub(r'(گام: \1\2)', txt)
    else:  # zh
        txt2 = step_pat.sub(r'（步长：\1\2）', txt)
    if txt2 != txt:
        n_fix += len(step_pat.findall(txt)); txt = txt2
    # Required residue: '| Yes |' -> localized (only for rows whose en counterpart is Yes)
    if '| Yes |' in txt:
        req, opt = REQ_MAP[lang]
        lines = txt.splitlines()
        en_lines = open(path.replace(f"/{lang}.md", "/en.md")).read().splitlines()
        # align rows by index among param-shaped rows
        ROWT = re.compile(r'^\| `[^`]+` \| .*\| ([A-Z_]+) \| ([^|]+) \|')
        en_rows = [(i, ROWT.match(l).group(2).strip()) for i, l in enumerate(en_lines) if ROWT.match(l)]
        tr_rows = []
        for i, l in enumerate(lines):
            mt = ROWT.match(l)
            if mt:
                tr_rows.append((i, mt.group(2).strip()))
        if len(en_rows) == len(tr_rows):
            for (ti, tok), (ei, etok) in zip(tr_rows, en_rows):
                if tok == "Yes" and etok == "Yes":
                    lines[ti] = yes_row.sub(r'\g<1>' + req + r'\g<2>', lines[ti])
                elif tok == "Yes" and etok == "No":
                    lines[ti] = yes_row.sub(r'\g<1>' + opt + r'\g<2>', lines[ti])
            txt = "\n".join(lines) + ("\n" if txt.endswith("\n") else "")
    if txt != orig:
        open(path, "w").write(txt)
    return n_fix

def main():
    nodes = json.load(open(sys.argv[1]))["nodes"]
    langs = sys.argv[2].split(",") if len(sys.argv) > 2 else list(LANG_MAP)
    total = {}
    for lang in langs:
        fixes = 0
        files = 0
        for n in nodes:
            p = f"{DOCS}/{n}/{lang}.md"
            if os.path.isfile(p):
                f = process_file(p, lang)
                if f:
                    fixes += f
                    files += 1
        total[lang] = (files, fixes)
        print(f"{lang}: {files} files fixed, {fixes} residue tokens")
    print(json.dumps(total))

if __name__ == "__main__":
    main()
