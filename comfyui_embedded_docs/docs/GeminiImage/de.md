# GeminiImage

Der GeminiImage-Node erzeugt Text- und Bildantworten aus den Gemini-KI-Modellen von Google. Sie können multimodale Eingaben wie Text-Prompts, Bilder und Dateien bereitstellen, um kohärente Text- und Bildausgaben zu erstellen. Der Node übernimmt die gesamte API-Kommunikation und Antwortverarbeitung mit den neuesten Gemini-Modellen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Eingabetyp | Standard | Bereich |
| --- | --- | --- | --- | --- | --- |
| `prompt` | Text-Prompt für die Generierung | STRING | erforderlich | "" | - |
| `model` | Das Gemini-Modell, das zur Generierung von Antworten verwendet wird. | COMBO | erforderlich | gemini_2_5_flash_image_preview | `gemini_2_5_flash_image_preview`<br>`gemini_2_5_pro_exp_03_25`<br>`gemini_2_0_flash_exp_image_generation` |
| `seed` | Wenn der Seed auf einen bestimmten Wert festgelegt ist, bemüht sich das Modell, bei wiederholten Anfragen die gleiche Antwort zu liefern. Eine deterministische Ausgabe ist nicht garantiert. Außerdem können Änderungen am Modell oder an Parametereinstellungen wie der Temperatur selbst bei Verwendung desselben Seed-Werts zu Abweichungen in der Antwort führen. Standardmäßig wird ein zufälliger Seed-Wert verwendet. | INT | erforderlich | 42 | 0 bis 18446744073709551615 |
| `images` | Optionales Bild bzw. optionale Bilder, die als Kontext für das Modell verwendet werden. Um mehrere Bilder einzubeziehen, können Sie den Batch Images-Node verwenden. | IMAGE | optional | None | - |
| `files` | Optionale Datei(en), die als Kontext für das Modell verwendet werden. Akzeptiert Eingaben vom Node Gemini Generate Content Input Files. | GEMINI_INPUT_FILES | optional | None | - |

**Hinweis:** Der Node enthält versteckte Parameter (`auth_token`, `comfy_api_key`, `unique_id`), die automatisch vom System verarbeitet werden und keine Benutzereingabe erfordern.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
| --- | --- | --- |
| `IMAGE` | Die generierte Bildantwort vom Gemini-Modell | IMAGE |
| `STRING` | Die generierte Textantwort vom Gemini-Modell | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImage/de.md)

---
**Source fingerprint (SHA-256):** `bf55ec4f5a869a6bc5a15366f55f86ad25f9498c14056acc80951d3637bf08f2`
