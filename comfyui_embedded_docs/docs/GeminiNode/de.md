# Google Gemini

Dieser Node ermöglicht es Benutzern, mit den Gemini-KI-Modellen von Google zu interagieren, um Textantworten zu generieren. Sie können verschiedene Eingabetypen bereitstellen, darunter Text, Bilder, Audio, Video und Dateien, die als Kontext für das Modell dienen, damit es relevantere und aussagekräftigere Antworten generieren kann. Der Node übernimmt die gesamte API-Kommunikation und das Parsen der Antworten automatisch.

**Hinweis:** Dieser Node ist im Quellcode als veraltet markiert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Texteingaben für das Modell, die zur Generierung einer Antwort verwendet werden. Sie können detaillierte Anweisungen, Fragen oder Kontext für das Modell angeben. Standard: leerer String. | STRING | Ja | - |
| `model` | Das Gemini-Modell, das zur Generierung von Antworten verwendet werden soll. Standard: gemini-3-1-pro. | COMBO | Ja | "gemini-2.5-pro"<br>"gemini-2.5-flash"<br>"gemini-3-pro-preview"<br>"gemini-3-1-pro"<br>"gemini-3-1-flash-lite" |
| `seed` | Wenn der Seed auf einen bestimmten Wert festgelegt wird, bemüht sich das Modell nach besten Kräften, bei wiederholten Anfragen dieselbe Antwort zu liefern. Eine deterministische Ausgabe ist nicht garantiert. Außerdem können Änderungen am Modell oder an Parametereinstellungen wie der Temperatur selbst bei Verwendung desselben Seed-Werts zu Abweichungen bei der Antwort führen. Standardmäßig wird ein zufälliger Seed-Wert verwendet. Standard: 42. | INT | Ja | 0 to 18446744073709551615 |
| `images` | Optionale Bilder, die als Kontext für das Modell verwendet werden. Um mehrere Bilder einzubinden, können Sie den Batch Images Node verwenden. Standard: Keine. | IMAGE | Nein | - |
| `audio` | Optionales Audio, das als Kontext für das Modell verwendet werden soll. Standard: Keine. | AUDIO | Nein | - |
| `video` | Optionales Video, das als Kontext für das Modell verwendet werden soll. Standard: Keine. | VIDEO | Nein | - |
| `files` | Optionale Datei(en), die als Kontext für das Modell verwendet werden. Akzeptiert Eingaben vom Node „Gemini Generate Content Input Files“. Standard: Keine. | GEMINI_INPUT_FILES | Nein | - |
| `system_prompt` | Grundlegende Anweisungen, die das Verhalten einer KI vorgeben. Standard: leerer String. Dies ist ein erweiterter Parameter. | STRING | Nein | - |

Alle verbundenen Bilder werden als Kontext verwendet. Wenn mehr als 10 Bilder bereitgestellt werden, werden die ersten 10 als Dateireferenzen hochgeladen und die übrigen Bilder inline an die API gesendet.

Der Node verwendet den ausgewählten Modellnamen wie in der Liste angegeben; einige Einträge werden intern ihren aktuellen API-Modellbezeichnern zugeordnet, bevor die Anfrage gesendet wird.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `STRING` | Die vom Gemini-Modell generierte Textantwort. Wenn das Modell keinen Text erzeugt, gibt der Node „Empty response from Gemini model...“ zurück. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNode/de.md)

---
**Source fingerprint (SHA-256):** `d1c53a5d80182085a36302867c8875df696adec6aaea9a9519a21bd6b9543d8f`
