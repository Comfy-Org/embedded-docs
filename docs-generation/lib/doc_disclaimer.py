"""AI disclaimer helpers for generated and translated node documentation."""

from __future__ import annotations

from lib.hash_footer import strip_source_hash_footer

# Substrings that identify the AI disclaimer blockquote (any supported language).
_DISCLAIMER_MARKERS = (
    "AI-generated",
    "AI generated",
    "AI 生成",
    "AI によって生成",
    "AI에 의해 생성",
    "generada por IA",
    "générée par IA",
    "gerada por IA",
    "с помощью ИИ",
    "الذكاء الاصطناعي",
    "yapay zeka",
    "هوش مصنوعی",
    "Edit on GitHub",
    "GitHub で編集",
    "GitHub에서 편집",
    "在 GitHub 上编辑",
    "在 GitHub 上編輯",
    "Editar en GitHub",
    "Modifier sur GitHub",
    "Редактировать на GitHub",
)

_EDIT_LINK_HINTS = (
    "edit on github",
    "github.com",
    "github で",
    "github에서",
    "github 上",
    "github'da",
)


def is_disclaimer_line(line: str) -> bool:
    """True if this line is the AI disclaimer blockquote."""
    s = line.strip()
    if not s.startswith(">"):
        return False
    low = s.lower()
    if any(h in low for h in _EDIT_LINK_HINTS):
        return True
    return any(marker in s for marker in _DISCLAIMER_MARKERS)


def strip_ai_disclaimer(content: str) -> str:
    """Remove AI disclaimer blockquote(s) from the top or bottom of a markdown body."""
    body = strip_source_hash_footer(content).strip()
    lines = body.split("\n")

    i = 0
    while i < len(lines):
        if not lines[i].strip():
            i += 1
            continue
        if is_disclaimer_line(lines[i]):
            i += 1
            while i < len(lines) and not lines[i].strip():
                i += 1
            continue
        break
    lines = lines[i:]

    while lines:
        if not lines[-1].strip():
            lines.pop()
            continue
        if is_disclaimer_line(lines[-1]):
            lines.pop()
            while lines and not lines[-1].strip():
                lines.pop()
            continue
        break

    return "\n".join(lines).rstrip()


def create_en_disclaimer(node_name: str) -> str:
    github_link = (
        f"https://github.com/Comfy-Org/embedded-docs/blob/main/"
        f"comfyui_embedded_docs/docs/{node_name}/en.md"
    )
    return (
        "> This documentation was AI-generated. If you find any errors or have suggestions "
        f"for improvement, please feel free to contribute! [Edit on GitHub]({github_link})"
    )


def create_translated_disclaimer(target_lang: str, node_name: str, lang_config: dict) -> str:
    github_link = (
        f"https://github.com/Comfy-Org/embedded-docs/blob/main/"
        f"comfyui_embedded_docs/docs/{node_name}/{target_lang}.md"
    )
    disclaimer_text = lang_config.get("disclaimer", "This documentation was AI-generated.")
    edit_text = {
        "zh": "在 GitHub 上编辑",
        "es": "Editar en GitHub",
        "fr": "Modifier sur GitHub",
        "ja": "GitHub で編集",
        "ko": "GitHub에서 편집",
        "ru": "Редактировать на GitHub",
        "zh-TW": "在 GitHub 上編輯",
        "ar": "تحرير على GitHub",
        "tr": "GitHub'da Düzenle",
        "pt-BR": "Editar no GitHub",
        "fa": "ویرایش در GitHub",
    }.get(target_lang, "Edit on GitHub")
    return f"> {disclaimer_text} [{edit_text}]({github_link})"


def compose_document(body: str, disclaimer: str, footer: str = "") -> str:
    """Assemble markdown: main content, disclaimer at bottom, optional hash footer last."""
    clean = strip_ai_disclaimer(body)
    out = f"{clean.rstrip()}\n\n{disclaimer.strip()}"
    if footer:
        out += footer if footer.startswith("\n") else f"\n{footer}"
    if not out.endswith("\n"):
        out += "\n"
    return out


def extract_metadata_suffix(original: str) -> str:
    """
    Return trailing disclaimer + SHA footer from *original*, unchanged.

    Used when fixing doc titles without altering hash or disclaimer formatting.
    """
    from lib.hash_footer import SOURCE_HASH_FOOTER_RE

    text = original.rstrip()
    footer = ""
    footer_m = SOURCE_HASH_FOOTER_RE.search(text)
    if footer_m:
        footer = text[footer_m.start():]
        text = text[:footer_m.start()].rstrip()

    lines = text.split("\n")
    disc_start = len(lines)
    i = len(lines) - 1
    while i >= 0:
        if not lines[i].strip():
            i -= 1
            continue
        if is_disclaimer_line(lines[i]):
            disc_start = i
            while disc_start > 0:
                prev = lines[disc_start - 1]
                if is_disclaimer_line(prev):
                    disc_start -= 1
                elif not prev.strip():
                    disc_start -= 1
                else:
                    break
            break
        break

    parts: list[str] = []
    if disc_start < len(lines):
        disc = "\n".join(lines[disc_start:]).strip()
        if disc:
            parts.append(disc)
    if footer:
        parts.append(footer.lstrip("\n"))
    return "\n\n".join(parts)


def assemble_document_with_metadata_suffix(body: str, metadata_suffix: str) -> str:
    """Join main body with an unchanged disclaimer + footer suffix."""
    out = body.rstrip()
    if metadata_suffix.strip():
        out += "\n\n" + metadata_suffix.strip()
    if not out.endswith("\n"):
        out += "\n"
    return out
