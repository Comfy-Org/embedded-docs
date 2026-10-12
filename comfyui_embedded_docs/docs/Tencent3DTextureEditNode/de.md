# Tencent3DTextureEditNode

Dieser Node verwendet die Tencent Hunyuan3D API, um die Texturen eines 3D-Modells zu bearbeiten. Sie stellen ein 3D-Modell und eine Textbeschreibung der gewünschten Änderungen bereit, und der Node gibt eine neue Version des Modells zurück, bei der die Texturen gemäß Ihrem Prompt neu gezeichnet wurden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `model_3d` | 3D-Modell im FBX-Format. Das Modell sollte weniger als 100000 Flächen haben. | FILE3D | Ja | FBX, Any |
| `prompt` | Beschreibt die Texturbearbeitung. Unterstützt bis zu 1024 UTF-8-Zeichen. | STRING | Ja |  |
| `seed` | Seed steuert, ob der Node erneut ausgeführt werden soll; die Ergebnisse sind unabhängig vom Seed nicht deterministisch. (Standard: 0) | INT | Nein | 0 to 2147483647 |

**Hinweis:** Die Eingabe `model_3d` muss eine Datei im FBX-Format sein. Andere 3D-Dateiformate werden von diesem Node nicht unterstützt. Der Parameter `prompt` ist erforderlich und muss zwischen 1 und 1024 Zeichen lang sein.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `GLB` | Das verarbeitete 3D-Modell im GLB-Format. | FILE3D |
| `OBJ` | Das verarbeitete 3D-Modell im OBJ-Format. | FILE3D |
| `texture_image` | Das neu generierte Texturbild für das 3D-Modell. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Tencent3DTextureEditNode/de.md)

---
**Source fingerprint (SHA-256):** `eedddc8bd47a4af6e45a516f2817e7c1dded575d9e28ea9b66a1d7a39b93526c`
