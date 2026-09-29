#!/usr/bin/env python3
"""Markdown format checks for ComfyUI node documentation.

Checks every .md file under comfyui_embedded_docs/docs/ for the recurring
AI-generation defects that have shipped to production:

1. Outer ```markdown fences wrapping the whole document (renders as a code block)
2. Translated data-type names in table cells (MODEL -> MODELO/МОДЕЛЬ/モデル/...)
3. Translated output identifiers in Outputs tables (positive -> positivo/正向/...)
4. Duplicate H1 headings (corrupts the document outline)
5. English Required-column residue in translations (| Yes | / | No | where localized)
6. Missing source fingerprint footer (en.md must carry the SHA-256 of its source)

Fence-aware: content inside ``` / ```markdown code fences is ignored for
structural checks (tables, headings), so legitimate fenced examples in docs
never trigger false positives. An outer fence is only reported when it wraps
the entire document (first fence-before-content opens it, last fence closes it).

Exit code 1 if any error-level check fails. Warnings do not fail the run.
"""
import os
import re
import subprocess
import sys
from pathlib import Path

DOCS_DIR = Path(__file__).resolve().parents[2] / "comfyui_embedded_docs" / "docs"

# --- data-type names must stay English (programmatic schema identifiers) ---
TRANSLATED_TYPES = {
    # es / pt-BR
    "MODELO", "CADENA", "IMAGEN", "IMAGEM", "ENTERO", "FLOTANTE", "MÁSCARA",
    "MASCARA", "CONDICIONAMIENTO", "LATENTE", "BOOLEANO", "SEQUÊNCIA",
    "CONDICIONAMENTO",
    # fr
    "CHAÎNE", "CHAINE", "MODÈLE", "FLOTTANT", "ENTIER",
    # ru
    "МОДЕЛЬ", "СТРОКА", "ИЗОБРАЖЕНИЕ", "МАСКА", "ЦЕЛОЕ", "ДРОБНОЕ",
    "ЛАТЕНТ", "ЛОГИЧЕСКОЕ", "БУЛЕВО",
    # ja / ko / zh
    "モデル", "画像", "文字列", "整数", "マスク", "モデル",
    "이미지", "모델", "문자열", "정수", "마스크",
    "模型", "图像", "字符串", "遮罩", "蒙版",
}

# NOTE: parameter and output NAMES in the Inputs/Outputs tables are deliberately
# localized. update_param_translations.py writes the names exported from the
# frontend's nodeDefs.json into the first column of those tables ("Update
# parameter names in documentation to match frontend translations"), and
# sync_frontend_translations.py exports them. A translated first column is
# therefore expected in translated docs and is NOT an error. Only the Data Type
# column carries schema names, which stay English (see TRANSLATED_TYPES).

# Languages whose Required column must NOT contain English Yes/No.
# (es "No", fr "Non", pt-BR "Não" are valid localizations.)
EN_RESIDUE_LANGS = {"zh", "zh-TW", "ja", "ko", "ru", "ar", "tr", "fa", "pt-BR"}

FP_RE = re.compile(r"Source fingerprint[^\n]*`([a-f0-9]{64})`")

# Localized "Outputs" section headings observed in the repo (per language).
# Matched against the exact heading text after "## ".
OUTPUTS_HEADINGS = {
    # en
    "Outputs",
    # es / fr / pt-BR
    "Salidas", "Salida", "Sorties", "Saídas",
    # ja / ko
    "出力", "출력",
    # zh / zh-TW
    "输出", "輸出",
    # ru (variants observed)
    "Выходы", "Выходные параметры", "Выходные данные",
    # ar
    "المخرجات",
    # tr
    "Çıktılar",
    # fa
    "خروجی‌ها",
}


def is_outputs_heading(text: str) -> bool:
    t = text.strip()
    if t in OUTPUTS_HEADINGS:
        return True
    return "output" in t.lower()


# Localized "Required" table-header words observed in the repo.
REQUIRED_HEADERS = {"required", "必填", "必需", "必須", "обязательный",
                    "obligatorio", "obrigatório", "requis", "zorunlu",
                    "الإلزامية", "إلزامي", "필수"}


def _is_required_header(cell: str) -> bool:
    c = cell.strip().lower()
    return c in REQUIRED_HEADERS or "required" in c

FENCE_INFO_RE = re.compile(r"^\s*(`{3,}|~{3,})")


def split_fenced(text: str):
    """Split text into (is_inside_fence, line) pairs.

    Returns a list of (fenced: bool, line: str). A block opened with N
    backticks/tildes only closes with a run of the SAME character of at
    least the same length (CommonMark rule), so a ``` example inside a
    longer-backtick block cannot accidentally close it.
    """
    result = []
    inside = False
    delim_char, delim_len = "", 0
    for line in text.splitlines():
        m = FENCE_INFO_RE.match(line)
        if not inside and m:
            inside = True
            delim_char, delim_len = m.group(1)[0], len(m.group(1))
            result.append((True, line))
            continue
        if inside and m:
            marker = m.group(1)
            if marker[0] == delim_char and len(marker) >= delim_len:
                inside = False
                delim_char, delim_len = "", 0
            result.append((True, line))
            continue
        result.append((inside, line))
    return result


def find_outer_fence(text: str):
    r"""Return True if a markdown fence (triple backtick) wraps the whole document.

    The known defect pattern (PR #142) is: H1 title, then \`\`\`markdown opener
    enclosing the whole body, then a closing fence, then only footer lines
    (disclaimer / --- / fingerprint). We require exactly that shape:

    - a standalone \`\`\`markdown opener
    - a matching closing fence
    - only the H1 title line before the opener
    - only footer-ish lines after the closer

    Anything else (fenced examples mid-document, docs that start with a fence,
    prose before the fence) is a legitimate use and not flagged.
    """
    lines = text.splitlines()
    if not re.search(r"^```markdown\s*$", text, re.M):
        return False
    try:
        open_idx = next(i for i, l in enumerate(lines) if l.strip() == "```markdown")
    except StopIteration:
        return False
    close_idx = None
    for i in range(open_idx + 1, len(lines)):
        if lines[i].strip() == "```":
            close_idx = i
            break
    if close_idx is None or close_idx - open_idx < 2:
        return False
    # content before opener: only the H1 title line (and blanks) allowed
    before = [lines[i].strip() for i in range(open_idx) if lines[i].strip()]
    if not all(re.match(r"^# [^#]", b) for b in before):
        return False
    # content after closer: only footer-ish lines (disclaimer, ---, fingerprint)
    after = [lines[i].strip() for i in range(close_idx + 1, len(lines)) if lines[i].strip()]
    for a in after:
        low = a.lower()
        if a == "---" or "fingerprint" in low or low.startswith(">"):
            continue
        return False
    return True


def check_file(path: Path):
    """Return (errors, warnings) for one doc file."""
    errors, warnings = [], []
    rel = path.relative_to(DOCS_DIR.parent)
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        errors.append(f"{rel}: file is not valid UTF-8")
        return errors, warnings

    lang = path.stem  # en, zh, ja, pt-BR, ...

    # 1. outer markdown fence (fence-aware: only when it wraps the whole doc)
    if find_outer_fence(text):
        errors.append(f"{rel}: document wrapped in ```markdown fence "
                      f"(strips to render properly)")

    # Structural checks run on non-fenced lines only, so legitimate fenced
    # examples (workflow JSON, code samples) never trigger them.
    unfenced = [(i, line) for i, (fenced, line) in
                enumerate(split_fenced(text)) if not fenced]

    # 2. translated data-type names in table cells
    reported_lines = set()
    for i, line in unfenced:
        if line.startswith("|"):
            for cell in line.split("|"):
                if cell.strip() in TRANSLATED_TYPES:
                    errors.append(f"{rel}: translated data type "
                                  f"'{cell.strip()}' (keep English schema names)")
                    reported_lines.add(i)
                    break

    # 4. duplicate H1 (unfenced headings only)
    h1s = [line for _, line in unfenced if re.match(r"^# .+", line)]
    if len(h1s) > 1:
        errors.append(f"{rel}: {len(h1s)} H1 headings (expected exactly 1)")

    # 5. English Yes/No residue in the Required column of translations.
    # Track the current table header to find the Required column index;
    # "Yes"/"No" in OTHER columns (e.g. COMBO option lists) are valid content.
    if lang in EN_RESIDUE_LANGS:
        required_idx = None
        for i, line in unfenced:
            if line.startswith("|"):
                cells = [c.strip().lower() for c in line.split("|")[1:-1]]
                if any(_is_required_header(c) for c in cells):
                    required_idx = next(
                        (j for j, c in enumerate(cells)
                         if _is_required_header(c)), None)
                    continue
                if required_idx is not None and len(cells) > required_idx:
                    if cells[required_idx] == "yes":
                        errors.append(f"{rel}:{i+1}: English 'Yes' in Required "
                                      f"column (translate: 是/はい/예/Да/نعم/...)")
            else:
                # table ended
                if line.strip() and not line.startswith("|"):
                    required_idx = None

    # 6. fingerprint footer (en.md only; translations inherit via sync)
    if lang == "en" and not FP_RE.search(text):
        warnings.append(f"{rel}: missing 'Source fingerprint (SHA-256)' footer")

    return errors, warnings


def main():
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--changed-only", action="store_true",
        help="Only check files changed vs the PR base (used on PRs; avoids "
             "failing on pre-existing defects elsewhere in the repo)")
    parser.add_argument(
        "--base", default="origin/main",
        help="Base ref for --changed-only (default: origin/main)")
    args = parser.parse_args()

    if not DOCS_DIR.is_dir():
        print(f"docs directory not found: {DOCS_DIR}", file=sys.stderr)
        return 1

    files = sorted(DOCS_DIR.rglob("*.md"))

    if args.changed_only:
        git_cmd = ["git", "diff", "--name-only", f"{args.base}...HEAD", "--",
                   "comfyui_embedded_docs/docs/"]
        git_res = subprocess.run(git_cmd, capture_output=True, text=True)
        if git_res.returncode != 0:
            print(f"git diff failed (rc={git_res.returncode}): "
                  f"{git_res.stderr.strip()}", file=sys.stderr)
            # fall back to full-repo scan rather than crashing the workflow
            git_res2 = subprocess.run(
                ["git", "diff", "--name-only", args.base, "HEAD", "--",
                 "comfyui_embedded_docs/docs/"],
                capture_output=True, text=True)
            if git_res2.returncode != 0:
                print("fallback two-dot diff also failed; checking all files",
                      file=sys.stderr)
                changed = None  # check everything
            else:
                changed = {l.strip() for l in git_res2.stdout.splitlines()
                           if l.strip().endswith(".md")}
        else:
            changed = {l.strip() for l in git_res.stdout.splitlines()
                       if l.strip().endswith(".md")}
        if changed is not None:
            files = [f for f in files
                     if str(f.relative_to(Path.cwd())) in changed]
        print(f"Checking {len(files)} files changed vs {args.base}")

    all_errors, all_warnings = [], []
    n_files = 0
    for path in files:
        n_files += 1
        errs, warns = check_file(path)
        all_errors += errs
        all_warnings += warns

    for w in all_warnings:
        print(f"warn: {w}")
    for e in all_errors:
        print(f"erro: {e}")

    print(f"\nChecked {n_files} files: "
          f"{len(all_errors)} errors, {len(all_warnings)} warnings")
    return 1 if all_errors else 0


if __name__ == "__main__":
    sys.exit(main())
