# Google Gemini Decision (Score)

Bewerten Sie den Text, die Bilder, das Audio oder das Video, das Sie verbinden, auf einer Skala von 1 bis 10 und erhalten Sie die Punktzahl sowie einen booleschen Wert, der bei einem von Ihnen festgelegten Schwellenwert umschlägt. Verwenden Sie dies zum Filtern oder Sortieren von Ausgaben, beispielsweise um nur Bilder zu behalten, die mindestens 7 Punkte erreichen, und verbinden Sie `result` mit einem If/Else Switch-Node, um darauf zu reagieren. Ein Lauf bewertet das, was Sie verbinden, als Ganzes; das Filtern einzelner Bilder bedeutet daher, sie einzeln zu bewerten.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Zu verwendendes Modell (Standard: `"gemini-decision-1"`). | COMBO | Ja | `"gemini-decision-1"` |
| `question` | Was bewertet werden soll, wobei anzugeben ist, was 1 und 10 bedeuten (Standard: "Rate the technical quality of the image from 1 (worst) to 10 (best)."). | STRING | Ja | 1 bis 5000 Zeichen |
| `threshold` | `result` ist true, wenn die Punktzahl mindestens diesem Wert entspricht. Saubere, scharfe Bilder erreichen etwa 7 bis 8, stark beschädigte etwa 3 bis 5 (Standard: 6.0). | FLOAT | Ja | 1.0 bis 10.0 (Schritt: 0.1) |
| `images` | Zu bewertende Bilder, bis zu 16 über die erweiterbaren Slots (`image_1` ... `image_16`). Ein gebündeltes Bild zählt einmal pro enthaltenem Bild. | IMAGE | Nein | Bis zu 16 Bilder |
| `audio` | Zu bewertender Audioclip. | AUDIO | Nein | - |
| `video` | Zu bewertender Videoclip. | VIDEO | Nein | - |
| `text` | Text, auf den sich die Frage bezieht, etwa ein Prompt oder eine LLM-Antwort, bis zu 20000 Zeichen. | STRING | Nein | Bis zu 20000 Zeichen |

Verbinden Sie mindestens eines von `text`, `images`, `audio` oder `video`; der Node gibt einen Fehler aus, wenn nichts zu bewerten ist. Bei mehreren Bildern benennen Sie diese innerhalb der Frage als `image_1`, `image_2` und so weiter.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `result` | True, wenn die Punktzahl mindestens `threshold` entspricht, andernfalls false. | BOOLEAN |
| `score` | Die Bewertung von 1 bis 10. | FLOAT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionScore/de.md)

---
**Source fingerprint (SHA-256):** `9b0a68cc7f29b1d4d23e23e051a008f34932aac6d1fe1a16e45a0e70b4df412f`
