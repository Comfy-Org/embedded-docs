#!/usr/bin/env python3
"""Review fixes for PR #149 (coderabbitai comments) + stale constraint sync (2026-09-17)."""
import os

DOCS = "/Users/linmoumou/Documents/embedded-docs/comfyui_embedded_docs/docs/OpenAIGPTImage1"

def patch(path, old, new, must=True):
    with open(path, encoding="utf-8") as f:
        content = f.read()
    if old not in content:
        if must:
            print(f"NOT FOUND in {path}: {old[:60]}")
        return False
    content = content.replace(old, new)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"PATCHED {os.path.basename(path)}")
    return True

# --- Comment 1 (ar.md:3): Arabic deprecation wording ---
patch(f"{DOCS}/ar.md", "موسومة كمتقادمة", "موسومة بأنها مهملة")

# --- Comment 2 (tr.md:31): Turkish thousands separators ---
patch(f"{DOCS}/tr.md", "655,360 ile 8,294,400", "655.360 ile 8.294.400")

# --- Comment 3 (zh.md:16): plain Chinese mask wording ---
patch(f"{DOCS}/zh.md", "用于内补绘制的可选蒙版", "用于修复的可选蒙版")

# --- Stale constraint sync: PR #16366 made transparent bg supported for gpt-image-2,
#     but en.md line 32 + 8 translations still say it is NOT supported. Remove the line.
#     ja/ar were already regenerated without it? No: ja.md and ar.md still have it (line 32).
stale_lines = {
    "en.md":    "- Transparent background is not supported for the `gpt-image-2` model.\n",
    "zh.md":    "- `gpt-image-2` 模型不支持透明背景。\n",
    "zh-TW.md": "- `gpt-image-2` 模型不支援透明背景。\n",
    "ja.md":    "- `gpt-image-2` モデルでは透明な背景はサポートされていません。\n",
    "ko.md":    "- `gpt-image-2` 모델에서는 투명 배경이 지원되지 않습니다.\n",
    "ru.md":    "- Прозрачный фон не поддерживается для модели `gpt-image-2`.\n",
    "tr.md":    "- `gpt-image-2` modeli için saydam arka plan desteklenmez.\n",
    "ar.md":    "- الخلفية الشفافة غير مدعومة لنموذج `gpt-image-2`.\n",
    "es.md":    "- El fondo transparente no es compatible con el modelo `gpt-image-2`.\n",
    "fr.md":    "- L'arrière-plan transparent n'est pas pris en charge par le modèle `gpt-image-2`.\n",
    "pt-BR.md": "- O fundo transparente não é suportado pelo modelo `gpt-image-2`.\n",
    "fa.md":    "- پس‌زمینه شفاف برای مدل `gpt-image-2` پشتیبانی نمی‌شود.\n",
}
for fname, line in stale_lines.items():
    path = f"{DOCS}/{fname}"
    with open(path, encoding="utf-8") as f:
        content = f.read()
    if line in content:
        content = content.replace(line, "")
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"REMOVED stale constraint: {fname}")
    else:
        print(f"already clean: {fname}")
