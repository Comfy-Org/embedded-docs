#!/usr/bin/env python3
"""Localize English residue in the Range column of translated node docs.

Why residue exists (three pipeline causes, all fixed or covered here):

1. ``config/translation_config.json`` tells the model, in every language, that
   "Range column values: numbers, \\"auto\\", option names - do not translate". The
   rule is too broad, so the model leaves the *whole* cell in English, prose
   included ("Multiline text", "Any value", "Video file", "9 options").
2. ``fix_range_residue.py`` post-processes only ``X to Y``, ``(step: N)`` and
   Yes/No. It has no prose handling, and its ``de``/``he``/``it`` token maps
   (added when those languages joined) were never applied at scale - those three
   languages hold 1287 of the 1872 residue cells.
3. No CI gate compares a translated Range cell with its English source, so the
   residue ships silently and only a human contributor notices a handful of it.

This script closes (2): it localizes the mechanical patterns with per-language
token maps and the recurring prose phrases with a dictionary, using the
conventions already present in the corpus (extracted, not invented).

Cells that are literals - option ids in backticks, quoted values, all-caps file
format lists (``GLB<br>GLTF<br>OBJ``) and placeholders (``-``, ``—``, ``N/A``) -
are deliberately left alone.

Usage:
    python docs-generation/scripts/fix_range_locale.py --dry-run
    python docs-generation/scripts/fix_range_locale.py --apply
    python docs-generation/scripts/fix_range_locale.py --apply --langs de,he,it
    python docs-generation/scripts/fix_range_locale.py --check-only --changed-only --base origin/main
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DOCS_ROOT = REPO_ROOT.parent / "comfyui_embedded_docs" / "docs"

RANGE_HEADERS = {
    "range", "范围", "範圍", "範囲", "범위", "диапазон", "rango", "plage", "faixa",
    "نطاق", "aralık", "محدوده", "bereich", "טווח", "intervallo",
}
PLACEHOLDERS = {"", "-", "—", "–", "N/A", "n/a", "na", "None", "none"}

# Literal tokens that stay in English: file formats, codecs, colour names, option ids.
FORMAT_TOKENS = {
    "glb", "gltf", "fbx", "obj", "stl", "usdz", "3mf", "ply", "splat", "splatany",
    "spz", "ksplat", "bmp", "dpx", "hdr", "jpeg", "jpg", "open_exr", "png", "targa",
    "tiff", "webp", "mp4", "mov", "webm", "gif", "avif", "heic", "wav", "mp3", "flac",
    "true", "false", "yes", "no", "none", "any", "mixamo", "blender", "3dsmax",
    "red", "green", "blue", "white", "black", "gray", "grey", "alpha",
    "3mf", "blender", "3dsmax", "bake_scale", "bake", "rigify", "up", "down",
    "left", "right", "max_resolution", "max_audio_frames", "audio_frames_per_second",
    "x", "y", "z", "w",
}

# Connectives and unit words, taken from the corpus conventions.
TOKENS: dict[str, dict[str, str]] = {
    "zh":     {"to": "到", "step": "步长", "default": "默认", "or": "或", "min": "最小", "max": "最大", "options": "个选项", "upto": "最多", "unlimited": "无限制", "images": "张图像", "seconds": "秒", "videos": "个视频", "clips": "段", "characters": "个字符"},
    "zh-TW":  {"to": "至", "step": "步進值", "default": "預設", "or": "或", "min": "最小", "max": "最大", "options": "個選項", "upto": "最多", "unlimited": "無限制", "images": "張影像", "seconds": "秒", "videos": "個影片", "clips": "段", "characters": "個字元"},
    "ja":     {"to": "～", "step": "ステップ", "default": "デフォルト", "or": "または", "min": "最小", "max": "最大", "options": "個のオプション", "upto": "最大", "unlimited": "無制限", "images": "枚の画像", "seconds": "秒", "videos": "本の動画", "clips": "個のクリップ", "characters": "文字"},
    "ko":     {"to": " ~ ", "step": "단계", "default": "기본값", "or": "또는", "min": "최소", "max": "최대", "options": "개 옵션", "upto": "최대", "unlimited": "무제한", "images": "개 이미지", "seconds": "초", "videos": "개 동영상", "clips": "개 클립", "characters": "자"},
    "ru":     {"to": "до", "step": "шаг", "default": "по умолчанию", "or": "или", "min": "мин.", "max": "макс.", "options": "вариантов", "upto": "до", "unlimited": "без ограничений", "images": "изображений", "seconds": "секунд", "videos": "видео", "clips": "клипов", "characters": "символов"},
    "de":     {"to": "bis", "step": "Schritt", "default": "Standard", "or": "oder", "min": "Min.", "max": "Max.", "options": "Optionen", "upto": "bis zu", "unlimited": "unbegrenzt", "images": "Bilder", "seconds": "Sekunden", "videos": "Videos", "clips": "Clips", "characters": "Zeichen"},
    "fr":     {"to": "à", "step": "pas", "default": "par défaut", "or": "ou", "min": "min.", "max": "max.", "options": "options", "upto": "jusqu'a", "unlimited": "illimité", "images": "images", "seconds": "secondes", "videos": "vidéos", "clips": "clips", "characters": "caractères"},
    "es":     {"to": "a", "step": "paso", "default": "predeterminado", "or": "o", "min": "mín.", "max": "máx.", "options": "opciones", "upto": "hasta", "unlimited": "ilimitado", "images": "imágenes", "seconds": "segundos", "videos": "videos", "clips": "clips", "characters": "caracteres"},
    "it":     {"to": "a", "step": "passo", "default": "predefinito", "or": "o", "min": "min.", "max": "max.", "options": "opzioni", "upto": "fino a", "unlimited": "illimitato", "images": "immagini", "seconds": "secondi", "videos": "video", "clips": "clip", "characters": "caratteri"},
    "pt-BR":  {"to": "a", "step": "passo", "default": "padrão", "or": "ou", "min": "mín.", "max": "máx.", "options": "opções", "upto": "até", "unlimited": "ilimitado", "images": "imagens", "seconds": "segundos", "videos": "vídeos", "clips": "clipes", "characters": "caracteres"},
    "ar":     {"to": "إلى", "step": "خطوة", "default": "افتراضي", "or": "أو", "min": "الحد الأدنى", "max": "الحد الأقصى", "options": "خيارات", "upto": "حتى", "unlimited": "غير محدود", "images": "صور", "seconds": "ثوانٍ", "videos": "فيديوهات", "clips": "مقاطع", "characters": "حرفًا"},
    "tr":     {"to": "ile", "step": "adım", "default": "varsayılan", "or": "veya", "min": "min.", "max": "maks.", "options": "seçenek", "upto": "en fazla", "unlimited": "sınırsız", "images": "görsel", "seconds": "saniye", "videos": "video", "clips": "klip", "characters": "karakter"},
    "fa":     {"to": "تا", "step": "گام", "default": "پیش‌فرض", "or": "یا", "min": "حداقل", "max": "حداکثر", "options": "گزینه", "upto": "حداکثر", "unlimited": "نامحدود", "images": "تصویر", "seconds": "ثانیه", "videos": "ویدیو", "clips": "کلیپ", "characters": "نویسه"},
    "he":     {"to": "עד", "step": "צעד", "default": "ברירת מחדל", "or": "או", "min": "מינימום", "max": "מקסימום", "options": "אפשרויות", "upto": "עד", "unlimited": "ללא הגבלה", "images": "תמונות", "seconds": "שניות", "videos": "סרטונים", "clips": "קטעים", "characters": "תווים"},
}

# Recurring prose cells, translated per language following the corpus.
PROSE: dict[str, str] = {
    "Multiline text": "multiline_text",
    "Single image": "single_image",
    "Free text": "free_text",
    "Any text": "any_text",
    "Any value": "any_value",
    "Any string": "any_string",
    "Any integer": "any_integer",
    "Single mesh": "single_mesh",
    "Image": "image",
    "Video file": "video_file",
    "Text": "text",
    "Multiple options available": "multiple_options",
    "Any 3D format": "any_3d_format",
    "Any": "any_value",
    "Text (multiline)": "multiline_text",
    "multiline, dynamic prompts enabled": "multiline_dynamic",
    "Tripo task ID": "task_id",
}
PROSE_I18N: dict[str, dict[str, str]] = {
    "multiline_text": {"zh": "多行文本", "zh-TW": "多行文字", "ja": "複数行テキスト", "ko": "여러 줄 텍스트", "ru": "Многострочный текст", "de": "Mehrzeiliger Text", "fr": "Texte multiligne", "es": "Texto multilínea", "it": "Testo multiriga", "pt-BR": "Texto multilinha", "ar": "نص متعدد الأسطر", "tr": "Çok satırlı metin", "fa": "متن چندخطی", "he": "טקסט רב-שורתי"},
    "single_image": {"zh": "单张图像", "zh-TW": "單張圖片", "ja": "単一画像", "ko": "단일 이미지", "ru": "Одно изображение", "de": "Einzelbild", "fr": "Image unique", "es": "Imagen única", "it": "Immagine singola", "pt-BR": "Imagem única", "ar": "صورة واحدة", "tr": "Tek görüntü", "fa": "تک تصویر", "he": "תמונה בודדת"},
    "free_text": {"zh": "自由文本", "zh-TW": "自由文字", "ja": "自由テキスト", "ko": "자유 텍스트", "ru": "Свободный текст", "de": "Freitext", "fr": "Texte libre", "es": "Texto libre", "it": "Testo libero", "pt-BR": "Texto livre", "ar": "نص حر", "tr": "Serbest metin", "fa": "متن آزاد", "he": "טקסט חופשי"},
    "any_text": {"zh": "任意文本", "zh-TW": "任意文字", "ja": "任意のテキスト", "ko": "임의 텍스트", "ru": "Любой текст", "de": "Beliebiger Text", "fr": "Texte quelconque", "es": "Texto cualquiera", "it": "Testo qualsiasi", "pt-BR": "Qualquer texto", "ar": "أي نص", "tr": "Herhangi bir metin", "fa": "هر متنی", "he": "טקסט כלשהו"},
    "any_value": {"zh": "任意值", "zh-TW": "任意值", "ja": "任意の値", "ko": "임의 값", "ru": "Любое значение", "de": "Beliebiger Wert", "fr": "Valeur quelconque", "es": "Valor cualquiera", "it": "Qualsiasi valore", "pt-BR": "Qualquer valor", "ar": "أي قيمة", "tr": "Herhangi bir değer", "fa": "هر مقدار", "he": "ערך כלשהו"},
    "any_string": {"zh": "任意字符串", "zh-TW": "任意字串", "ja": "任意の文字列", "ko": "임의 문자열", "ru": "Любая строка", "de": "Beliebige Zeichenkette", "fr": "Chaîne quelconque", "es": "Cadena cualquiera", "it": "Stringa qualsiasi", "pt-BR": "Qualquer string", "ar": "أي سلسلة", "tr": "Herhangi bir dize", "fa": "هر رشته", "he": "מחרוזת כלשהי"},
    "any_integer": {"zh": "任意整数", "zh-TW": "任意整數", "ja": "任意の整数", "ko": "임의 정수", "ru": "Любое целое число", "de": "Beliebige Ganzzahl", "fr": "Entier quelconque", "es": "Entero cualquiera", "it": "Intero qualsiasi", "pt-BR": "Qualquer inteiro", "ar": "أي عدد صحيح", "tr": "Herhangi bir tamsayı", "fa": "هر عدد صحیح", "he": "מספר שלם כלשהו"},
    "single_mesh": {"zh": "单个网格", "zh-TW": "單一網格", "ja": "単一メッシュ", "ko": "단일 메시", "ru": "Один меш", "de": "Einzelnes Mesh", "fr": "Maillage unique", "es": "Malla única", "it": "Mesh singola", "pt-BR": "Malha única", "ar": "شبكة واحدة", "tr": "Tek mesh", "fa": "تک مش", "he": "מש בודד"},
    "image": {"zh": "图像", "zh-TW": "影像", "ja": "画像", "ko": "이미지", "ru": "Изображение", "de": "Bild", "fr": "Image", "es": "Imagen", "it": "Immagine", "pt-BR": "Imagem", "ar": "صورة", "tr": "Görüntü", "fa": "تصویر", "he": "תמונה"},
    "video_file": {"zh": "视频文件", "zh-TW": "影片檔案", "ja": "動画ファイル", "ko": "동영상 파일", "ru": "Видеофайл", "de": "Videodatei", "fr": "Fichier vidéo", "es": "Archivo de vídeo", "it": "File video", "pt-BR": "Arquivo de vídeo", "ar": "ملف فيديو", "tr": "Video dosyası", "fa": "فایل ویدیو", "he": "קובץ וידאו"},
    "text": {"zh": "文本", "zh-TW": "文字", "ja": "テキスト", "ko": "텍스트", "ru": "Текст", "de": "Text", "fr": "Texte", "es": "Texto", "it": "Testo", "pt-BR": "Texto", "ar": "نص", "tr": "Metin", "fa": "متن", "he": "טקסט"},
    "multiline_dynamic": {"zh": "多行文本，可启用动态提示词", "zh-TW": "多行文字，可啟用動態提示詞", "ja": "複数行テキスト（動的プロンプト有効）", "ko": "여러 줄 텍스트, 동적 프롬프트 활성화", "ru": "Многострочный текст с поддержкой динамических промптов", "de": "Mehrzeiliger Text, dynamische Prompts aktiviert", "fr": "Texte multiligne, invites dynamiques activées", "es": "Texto multilínea, prompts dinámicos habilitados", "it": "Testo multiriga, prompt dinamici abilitati", "pt-BR": "Texto multilinha, prompts dinâmicos ativados", "ar": "نص متعدد الأسطر مع تفعيل المطالبات الديناميكية", "tr": "Çok satırlı metin, dinamik istemler etkin", "fa": "متن چندخطی، اعلان‌های پویا فعال", "he": "טקסט רב-שורתי, הנחיות דינמיות מופעלות"},
    "task_id": {"zh": "Tripo 任务 ID", "zh-TW": "Tripo 任務 ID", "ja": "Tripo タスク ID", "ko": "Tripo 작업 ID", "ru": "ID задачи Tripo", "de": "Tripo-Aufgaben-ID", "fr": "ID de tâche Tripo", "es": "ID de tarea de Tripo", "it": "ID attività Tripo", "pt-BR": "ID da tarefa Tripo", "ar": "معرّف مهمة Tripo", "tr": "Tripo görev kimliği", "fa": "شناسه وظیفه Tripo", "he": "מזהה משימת Tripo"},
    "multiple_options": {"zh": "多个可用选项", "zh-TW": "多個可用選項", "ja": "複数のオプションがあります", "ko": "여러 옵션 사용 가능", "ru": "Доступно несколько вариантов", "de": "Mehrere Optionen verfügbar", "fr": "Plusieurs options disponibles", "es": "Varias opciones disponibles", "it": "Diverse opzioni disponibili", "pt-BR": "Várias opções disponíveis", "ar": "تتوفر خيارات متعددة", "tr": "Birden çok seçenek mevcut", "fa": "چندین گزینه موجود است", "he": "אפשרויות מרובות זמינות"},
    "any_3d_format": {"zh": "任意 3D 格式", "zh-TW": "任意 3D 格式", "ja": "任意の 3D 形式", "ko": "모든 3D 형식", "ru": "Любой 3D-формат", "de": "Beliebiges 3D-Format", "fr": "Tout format 3D", "es": "Cualquier formato 3D", "it": "Qualsiasi formato 3D", "pt-BR": "Qualquer formato 3D", "ar": "أي صيغة 3D", "tr": "Herhangi bir 3D formatı", "fa": "هر قالب 3D", "he": "כל פורמט 3D"},
}

NUM = r"(\d+(?:\.\d+)?)"
STEP_RE = re.compile(r"\(step\s*:?\s*([0-9.eE+-]+)\)")
DEFAULT_RE = re.compile(r"\bdefault\s*:\s*")
TRUE_OR_FALSE_RE = re.compile(r"\b(True|true)\s+or\s+(False|false)\b")
TO_RE = re.compile(rf"{NUM}\s+to\s+({NUM}|[A-Z][A-Z0-9_]+)")
UNIT_RE = re.compile(r"\b(images|seconds|videos|clips|characters)\b")


def needs_translation(cell: str) -> bool:
    """True when the cell still holds English a translator must localize.

    Cells that are only numbers, backticked/quoted literals, placeholders or bare
    digits joined by a dash need no translation and must not be reported.
    """
    c = cell.strip()
    if c in PLACEHOLDERS:
        return False
    bare = re.sub(r"`[^`]*`|\"[^\"]*\"", "", c)
    bare = re.sub(r"<br\s*/?>", " ", bare, flags=re.I)
    bare = re.sub(r"0x[0-9A-Fa-f]+", " ", bare)          # hex literals
    bare = re.sub(r"\b[A-Z][A-Z0-9_]{2,}\b", " ", bare)  # MAX_RESOLUTION style ids
    bare = re.sub(r"[\d.,:;+\-–—~/\\()\s]+", " ", bare)
    words = re.findall(r"[A-Za-z0-9_]+", bare)
    words = [w for w in words if len(w) >= 2 and not w.isdigit()]
    words = [w for w in words if w.lower() not in FORMAT_TOKENS]
    if not words:
        return False
    return True


def is_literal(cell: str) -> bool:
    c = cell.strip()
    if c in PLACEHOLDERS:
        return True
    bare = re.sub(r"`[^`]*`|\"[^\"]*\"", "", c)
    bare = re.sub(r"<br\s*/?>", " ", bare, flags=re.I)
    words = re.findall(r"[A-Za-z]{2,}", bare)
    if words and all(w.isupper() for w in words):
        return True          # GLB<br>GLTF<br>OBJ, MODEL_TASK_ID ...
    if words and {w.lower() for w in words} <= {"true", "false", "yes", "no"}:
        return True          # pure boolean literals
    return False


def localize(cell: str, lang: str) -> tuple[str, str] | None:
    """Return (new_cell, kind) or None when nothing to do."""
    tok = TOKENS.get(lang)
    if not tok:
        return None
    c = cell.strip()
    if is_literal(c):
        return None

    # 1. exact prose phrase
    key = PROSE.get(c)
    if key:
        tr = PROSE_I18N[key].get(lang)
        if tr:
            return tr, "prose"

    out = c
    # 2. mechanical rewrites
    out = STEP_RE.sub(lambda m: f"({tok['step']}: {m.group(1)})" if lang not in ("ja", "fr", "ko") else f"({tok['step']} {m.group(1)})", out)
    out = DEFAULT_RE.sub(f"{tok['default']}: ", out)
    # trailing bare "Any" inside an option list (e.g. "GLB<br>FBX<br>OBJ<br>Any")
    out = re.sub(r"(<br\s*/?>)\s*Any\s*$", lambda m: m.group(1) + PROSE_I18N["any_value"].get(lang, "Any"), out, flags=re.I)
    out = TRUE_OR_FALSE_RE.sub(lambda m: f"{m.group(1)} {tok['or']} {m.group(2)}", out)
    out = re.sub(r"\bmin\s*:?\s+", tok["min"] + " ", out)
    out = re.sub(r"\bmax\s*:?\s+", tok["max"] + " ", out)
    out = re.sub(r"\b(Default|default)\s*:", tok["default"] + ":", out)
    out = re.sub(r"(,\s*)step\s*:?\s*", lambda m: m.group(1) + tok["step"] + ": ", out)
    out = re.sub(r"\(default\)", "(" + tok["default"] + ")", out)
    out = re.sub(r"\bdefault\s+(\d)", tok["default"] + r" \1", out)
    # identifier-to-identifier range, e.g. "-MAX_RESOLUTION to MAX_RESOLUTION"
    out = re.sub(r"\b([A-Z][A-Z0-9_]+)\s+to\s+([A-Z][A-Z0-9_]+)\b",
                 lambda m: m.group(1) + " " + tok["to"] + " " + m.group(2), out)
    out = re.sub(r"<br\s*/?>\s*Any 3D format", lambda m: m.group(0).replace("Any 3D format", PROSE_I18N["any_3d_format"].get(lang, "Any 3D format")), out)
    def _to(m):
        a, b = m.group(1), m.group(2)
        if lang == "tr":
            return f"{a} ile {b} arası"
        if lang == "ru":
            return f"от {a} до {b}"
        return f"{a} {tok['to']} {b}"
    out = TO_RE.sub(_to, out)
    out = re.sub(r"(\d+)\s+options\b",
                 lambda m: m.group(1) + " " + tok.get("options", "options"), out)
    out = re.sub(r"\bUp to\s+(\d+)",
                 lambda m: tok.get("upto", "Up to") + " " + m.group(1), out)
    # localize a unit word only when it directly follows a number
    out = re.sub(
        r"(\d+)\s+(images|seconds|videos|clips|characters)\b",
        lambda m: m.group(1) + " " + tok.get(m.group(2), m.group(2)),
        out,
    )

    # 3. prose phrases that survive inside a larger cell, e.g. after the mechanical
    # pass turned "Any integer (default: 0)" into "Any integer (默认: 0)".
    for phrase, key in sorted(PROSE.items(), key=lambda kv: -len(kv[0])):
        if len(phrase) < 4:
            continue
        tr = PROSE_I18N[key].get(lang)
        if not tr or tr == phrase:
            continue
        out = re.sub(r"\b" + re.escape(phrase) + r"\b", tr, out)

    if out != c:
        return out, "mechanical" if out != c else None
    return None


def parse_tables(path: Path) -> list[dict]:
    """Parse every markdown table: its Range column index and its data rows.

    Rows are matched between `en` and a translation by table position, not by
    parameter name: translations sometimes rename the parameter (``ckpt_name``
    became ``Checkpoint名称``) or drop the backticks, which made name-based
    matching miss those rows entirely.
    """
    if not path.exists():
        return []
    tables: list[dict] = []
    current: dict | None = None
    header_seen = False
    for line in path.read_text(encoding="utf-8", errors="ignore").split("\n"):
        s = line.strip()
        if not s.startswith("|"):
            current, header_seen = None, False
            continue
        cells = [x.strip() for x in s.split("|")[1:-1]]
        if all(set(x) <= {"-", ":", " ", "|", "—"} for x in cells):
            continue
        if current is None:
            current = {"range_idx": None, "rows": []}
            tables.append(current)
            header_seen = False
        if not header_seen:
            for i, x in enumerate(cells):
                if x.strip().strip("*`").lower() in RANGE_HEADERS:
                    current["range_idx"] = i
                    break
            header_seen = True
            continue
        current["rows"].append(cells)
    return [t for t in tables if t["range_idx"] is not None]


def range_cells(path: Path) -> list[tuple[int, int, str]]:
    """[(table_index, row_index, range_cell)] for every row with a Range column."""
    out = []
    for ti, t in enumerate(parse_tables(path)):
        ri = t["range_idx"]
        for rj, cells in enumerate(t["rows"]):
            if ri < len(cells):
                out.append((ti, rj, cells[ri]))
    return out


def apply_replacements(text: str, replacements: dict[tuple[int, int], str]) -> str:
    """Rewrite Range cells addressed by (table_index, row_index)."""
    out: list[str] = []
    ti = -1
    range_idx = None
    header_seen = False
    rj = -1
    for line in text.split("\n"):
        s = line.strip()
        if not s.startswith("|"):
            range_idx, header_seen = None, False
            out.append(line)
            continue
        cells = [x.strip() for x in s.split("|")[1:-1]]
        if all(set(x) <= {"-", ":", " ", "|", "—"} for x in cells):
            out.append(line)
            continue
        if not header_seen:
            ti += 1
            rj = -1
            range_idx = None
            for i, x in enumerate(cells):
                if x.strip().strip("*`").lower() in RANGE_HEADERS:
                    range_idx = i
                    break
            header_seen = True
            out.append(line)
            continue
        rj += 1
        key = (ti, rj)
        if range_idx is not None and range_idx < len(cells) and key in replacements:
            cells[range_idx] = replacements[key]
            out.append("| " + " | ".join(cells) + " |")
        else:
            out.append(line)
    return "\n".join(out)


def changed_paths(base: str) -> set[Path]:
    out = subprocess.run(
        ["git", "diff", "--name-only", f"{base}...HEAD", "--", "comfyui_embedded_docs/docs/"],
        capture_output=True, text=True, check=True, cwd=REPO_ROOT.parent,
    ).stdout
    return {(REPO_ROOT.parent / p).resolve() for p in out.splitlines() if p.strip()}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--check-only", action="store_true", help="exit 1 when residue exists (CI gate)")
    ap.add_argument("--langs", default=None, help="comma-separated language filter")
    ap.add_argument("--changed-only", action="store_true")
    ap.add_argument("--base", default="origin/main")
    args = ap.parse_args()

    langs = set(args.langs.split(",")) if args.langs else None
    changed = changed_paths(args.base) if args.changed_only else None

    per_lang: dict[str, int] = {}
    unknown: dict[str, int] = {}
    total = 0

    for node_dir in sorted(DOCS_ROOT.iterdir()):
        if not node_dir.is_dir():
            continue
        en_cells = range_cells(node_dir / "en.md")
        if not en_cells:
            continue
        for path in sorted(node_dir.glob("*.md")):
            lang = path.stem
            if lang == "en" or (langs and lang not in langs):
                continue
            if changed is not None and path.resolve() not in changed:
                continue
            tr_cells = {(t, r): c for t, r, c in range_cells(path)}
            pending: dict[tuple[int, int], str] = {}
            for t, r, en_cell in en_cells:
                key = (t, r)
                if key not in tr_cells:
                    continue
                if tr_cells[key] != en_cell:
                    continue          # already localized (or differs - not our business)
                if not needs_translation(en_cell):
                    continue          # numbers, quoted option ids, placeholders: nothing to localize
                res = localize(en_cell, lang)
                if res and res[0] != en_cell:
                    pending[key] = res[0]
                elif not res:
                    unknown[en_cell] = unknown.get(en_cell, 0) + 1
            if not pending:
                continue
            total += len(pending)
            per_lang[lang] = per_lang.get(lang, 0) + len(pending)
            if args.apply and not args.check_only:
                text = path.read_text(encoding="utf-8")
                path.write_text(apply_replacements(text, pending), encoding="utf-8")

    for lang in sorted(per_lang, key=lambda l: -per_lang[l]):
        print(f"  {lang:7} {per_lang[lang]:4} cells")
    verb = "fixed" if (args.apply and not args.check_only) else "found"
    print(f"\n{verb}: {total} Range cells across {sum(per_lang.values()) and len(per_lang)} languages")
    if unknown:
        print(f"\nneeds a dictionary entry ({len(unknown)} distinct):")
        for cell, n in sorted(unknown.items(), key=lambda x: -x[1])[:12]:
            print(f"  {n:4}x  {cell[:70]}")
    if args.check_only and total:
        print(f"\nUntranslated Range residue detected: {total} cells. "
              f"Run with --apply to localize.")
        return 1
    if args.check_only and unknown:
        # Not fatal: the tail needs human judgement (option-id lists vs prose).
        print(f"::warning::{len(unknown)} English Range cell(s) need a dictionary "
              f"entry or manual translation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
