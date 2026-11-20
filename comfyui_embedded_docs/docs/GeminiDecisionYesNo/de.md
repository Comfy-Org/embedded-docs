# Google Gemini Decision (Yes/No)

Stellen Sie eine Ja/Nein-Frage zu dem Text, den Bildern, dem Audio oder dem Video, das Sie verbinden, und erhalten Sie einen booleschen Wert, auf den Sie verzweigen können. Verbinden Sie `result` mit einem If/Else-Switch-Node, um den Lauf auf einen von zwei Pfaden zu schicken, und lesen Sie `answer` und `probability`, wenn Sie sehen möchten, warum das Modell so geantwortet hat.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Zu verwendendes Modell (Standard: `"gemini-decision-1"`). | COMBO | Ja | `"gemini-decision-1"` |
| `question` | Die Ja/Nein-Frage zu dem, was verbunden ist, bis zu 5000 Zeichen. Formulieren Sie sie so, dass „Ja“ der Fall ist, auf den Sie reagieren (Standard: "Is there a person in the image?"). | STRING | Ja | 1 bis 5000 Zeichen |
| `threshold` | Wahrscheinlichkeit für „Ja“, ab der `result` wahr wird. Eindeutige Ja-Antworten erreichen etwa 0.85 bis 0.92, daher weist 0.9 oder mehr viele davon zurück (Standard: 0.5). | FLOAT | Ja | 0.01 bis 0.99 (Schritt: 0.01) |
| `images` | Bilder, nach denen gefragt werden soll, bis zu 16 über die erweiterbaren Slots (`image_1` ... `image_16`). Ein gebatchtes Bild zählt einmal pro Bild. | IMAGE | Nein | Bis zu 16 Bilder |
| `audio` | Audioclip, nach dem gefragt werden soll. | AUDIO | Nein | - |
| `video` | Videoclip, nach dem gefragt werden soll. | VIDEO | Nein | - |
| `text` | Text, auf den sich die Frage bezieht, z. B. ein Prompt oder eine LLM-Antwort, bis zu 20000 Zeichen. | STRING | Nein | Bis zu 20000 Zeichen |

Verbinden Sie mindestens eines von `text`, `images`, `audio` oder `video`; der Node löst einen Fehler aus, wenn es nichts zu betrachten gibt. Benennen Sie bei mehreren Bildern diese in der Frage `image_1`, `image_2` und so weiter.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `result` | Die Antwort als boolescher Wert: true für „Ja“, false für „Nein“. | BOOLEAN |
| `answer` | Die Antwort als Zeichenfolge `"yes"` oder `"no"`. | STRING |
| `probability` | Wahrscheinlichkeit für „Ja“ zwischen 0 und 1. | FLOAT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionYesNo/de.md)

---
**Source fingerprint (SHA-256):** `0339031baf5648609b82526bed97ce8744986878bcbb706dcd3aa79a7370d83f`
