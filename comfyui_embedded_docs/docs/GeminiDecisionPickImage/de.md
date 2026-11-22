# Google Gemini Decision (Pick Image)

Wählt das beste Bild aus einem Batch aus. Verbinden Sie `index` mit Get Image from Batch, um das ausgewählte Bild beizubehalten, sodass der Rest des Workflows nur mit der Auswahl weiterläuft.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Zu verwendendes Modell (Standard: `"gemini-decision-1"`). | COMBO | Ja | `"gemini-decision-1"` |
| `question` | Frage zur Bildauswahl (Standard: "Which image best matches the prompt in text? If there is no text, which image has the best quality?"). | STRING | Ja | 1 bis 5000 Zeichen |
| `images` | Die Bilder zur Auswahl, als Batch oder als einzelner Batch von Frames. | IMAGE | Ja | 2 bis 64 Bilder |
| `text` | Text, auf den sich die Frage bezieht, z. B. der Prompt, aus dem die Bilder erstellt wurden, bis zu 20000 Zeichen. | STRING | Nein | Bis zu 20000 Zeichen |

Der Node benötigt 2 bis 64 Bilder und löst bei einem einzelnen Bild einen Fehler aus. Verbinden Sie `text`, wenn die Auswahl einem Prompt statt allein der Bildqualität folgen soll.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `index` | Position des ausgewählten Bildes im Batch, beginnend bei 0. | INT |
| `confidence` | Konfidenz der Auswahl, zwischen 0 und 1. | FLOAT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionPickImage/de.md)

---
**Source fingerprint (SHA-256):** `55eb604923cb66b42f23f37d0c710a97033cc2c5d95880d45397bba10e44dab0`
