# ClipSave

Der `CLIPSave`-Node speichert ein CLIP-Textencoder-Modell im SafeTensors-Format auf der Festplatte. Er ist für fortgeschrittene Workflows zum Zusammenführen von Modellen konzipiert und trennt das CLIP-Modell automatisch anhand seiner internen Struktur in seine Komponenten (wie CLIP-L, CLIP-G oder T5XXL) auf, wobei jede Komponente als separate Datei gespeichert wird.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `clip` | Das zu speichernde CLIP-Modell. | CLIP | Ja | - |
| `filename_prefix` | Der Präfixpfad und Dateiname für die gespeicherte(n) Datei(en). Der Node hängt einen Komponentensuffix (z. B. `_clip_l`, `_clip_g`) und einen Zähler an, um eindeutige Dateinamen zu erstellen (Standard: `clip/ComfyUI`). | STRING | Ja | - |
| `prompt` | Die Workflow-Prompt-Informationen, die als Metadaten in der Ausgabedatei gespeichert werden. Dieser Parameter ist in der UI ausgeblendet. | PROMPT | Nein | - |
| `extra_pnginfo` | Zusätzliche Metadaten, die als Schlüssel-Wert-Paare in der Ausgabedatei gespeichert werden. Dieser Parameter ist in der UI ausgeblendet. | EXTRA_PNGINFO | Nein | - |

## Ausgaben

Dieser Node hat keine Ausgabeverbindungen. Er speichert die verarbeiteten Dateien direkt im Verzeichnis `ComfyUI/output/`. Die gespeicherten Dateien enthalten Metadaten (das Format ist auf "pt" gesetzt, zusammen mit dem Workflow-Prompt und etwaigen zusätzlichen PNG-Informationen), sofern ComfyUI nicht mit dem Argument `--disable-metadata` gestartet wird.

### Details zu gespeicherten Dateien

Der Node analysiert das State Dictionary des CLIP-Modells und speichert separate SafeTensors-Dateien für jede erkannte Komponente. Die Komponente wird anhand des Präfixes ihrer Parameterschlüssel identifiziert. Die folgenden Präfixe werden geprüft:

- `clip_l.` (CLIP-L-Textencoder)
- `clip_g.` (CLIP-G-Textencoder)
- `clip_h.` (CLIP-H-Textencoder)
- `t5xxl.` (T5-XXL-Textencoder)
- `pile_t5xl.` (Pile-T5-XL-Textencoder)
- `mt5xl.` (mT5-XL-Textencoder)
- `umt5xxl.` (UMT5-XXL-Textencoder)
- `t5base.` (T5-Base-Textencoder)
- `gemma2_2b.` (Gemma 2 2B-Textencoder)
- `llama.` (LLaMA-Textencoder)
- `hydit_clip.` (Hydit-CLIP-Textencoder)
- Leeres Präfix (andere CLIP-Komponenten)

Für jede erkannte Komponente erstellt der Node eine Datei mit dem Namen `{filename_prefix}_{counter:05}_.safetensors`, wobei das Komponentenpräfix an das Dateinamenpräfix angehängt wird (z. B. `clip/ComfyUI_clip_l_00001_.safetensors`). Das Präfix `transformer.` wird beim Speichern aus den Parameterschlüsseln entfernt.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipSave/de.md)

---
**Source fingerprint (SHA-256):** `4ab9171e4245b10f738f78bac8a5b564c0957dde352e207ec3f9865e4fac0cab`
