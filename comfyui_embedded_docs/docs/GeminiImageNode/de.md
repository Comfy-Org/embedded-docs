# Nano Banana (Google Gemini Image)

Der GeminiImage-Node erzeugt Text- und Bildantworten von den Gemini-KI-Modellen von Google. Er ermöglicht die Bereitstellung multimodaler Eingaben, einschließlich Text-Prompts, Bildern und Dateien, um kohärente Text- und Bildausgaben zu erzeugen. Der Node übernimmt die gesamte API-Kommunikation und das Antwortparsing mit den neuesten Gemini-Modellen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Eingabetyp | Standard | Bereich |
| --- | --- | --- | --- | --- | --- |
| `prompt` | Text-Prompt für die Generierung | STRING | erforderlich | "" | - |
| `model` | Das Gemini-Modell, das zur Generierung von Antworten verwendet wird | COMBO | erforderlich | gemini_2_5_flash_image_preview | Verfügbare Gemini-Modelle<br>Optionen extrahiert aus dem GeminiImageModel-Enum |
| `seed` | Wenn der Seed auf einen bestimmten Wert festgelegt wird, unternimmt das Modell größte Anstrengungen, um bei wiederholten Anfragen dieselbe Antwort zu liefern. Deterministische Ausgabe ist nicht garantiert. Außerdem können Änderungen am Modell oder an Parametereinstellungen wie der Temperatur selbst bei Verwendung desselben Seed-Werts Variationen in der Antwort verursachen. Standardmäßig wird ein zufälliger Seed-Wert verwendet | INT | erforderlich | 42 | 0 bis 18446744073709551615 |
| `images` | Optionale(s) Bild(er), die als Kontext für das Modell verwendet werden. Um mehrere Bilder einzubinden, können Sie den Node Batch Images verwenden | IMAGE | optional | None | - |
| `files` | Optionale Datei(en), die als Kontext für das Modell verwendet werden. Akzeptiert Eingaben vom Node Gemini Generate Content Input Files | GEMINI_INPUT_FILES | optional | None | - |

*Hinweis: Der Node enthält verborgene Parameter (`auth_token`, `comfy_api_key`, `unique_id`), die automatisch vom System verarbeitet werden und keine Benutzereingabe erfordern.*

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `IMAGE` | Die vom Gemini-Modell generierte Bildantwort | IMAGE |
| `STRING` | Die vom Gemini-Modell generierte Textantwort | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiImageNode/de.md)
