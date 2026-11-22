# Google Gemini Decision (Choice)

Wählen Sie eine Ihrer eigenen Optionen für den Text, die Bilder, das Audio oder das Video aus, das Sie verbinden, und erhalten Sie die gewählte Option, ihre Position und eine Konfidenz zurück. Verbinden Sie `choice` mit einem Branch-Node, dessen Eingaben dieselben Optionsnamen tragen, oder leiten Sie anhand von `option_index` weiter. Ein Branch-Node akzeptiert höchstens 32 Eingaben, daher sollten Sie größere Optionssätze mit `option_index` weiterleiten.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model` | Zu verwendendes Modell (Standard: `"gemini-decision-1"`). | COMBO | Ja | `"gemini-decision-1"` |
| `question` | Die Frage, die die Optionen beantworten, bis zu 5000 Zeichen (Standard: "What style is the image?"). | STRING | Ja | 1 bis 5000 Zeichen |
| `options` | Eine Option pro Zeile, genau wie eingegeben verwendet, jeweils bis zu 128 Zeichen. Fügen Sie eine Option wie `other` für Eingaben hinzu, die zu keiner von ihnen passen (Standard: `photo`, `illustration`, `3d render`, `anime`, `sketch`, `other`). | STRING | Ja | 2 bis 255 Optionen |
| `images` | Zu klassifizierende Bilder, bis zu 16 über die erweiterbaren Slots (`image_1` ... `image_16`). Bei einem Batch zählt jedes Bild einzeln. | IMAGE | Nein | Bis zu 16 Bilder |
| `audio` | Zu klassifizierender Audioclip. | AUDIO | Nein | - |
| `video` | Zu klassifizierender Videoclip. | VIDEO | Nein | - |
| `text` | Text, auf den sich die Frage bezieht, z. B. ein Prompt oder eine LLM-Antwort, bis zu 20000 Zeichen. | STRING | Nein | Bis zu 20000 Zeichen |

Geben Sie mindestens 2 und höchstens 255 Optionen an und listen Sie keine davon doppelt auf; andernfalls löst der Node einen Fehler aus. Verbinden Sie mindestens eines von `text`, `images`, `audio` oder `video` und benennen Sie mehrere Bilder innerhalb der Frage als `image_1`, `image_2` usw.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `choice` | Die gewählte Option, genau wie in `options` geschrieben. | STRING |
| `option_index` | Position der gewählten Option in `options`, beginnend bei 0. | INT |
| `confidence` | Konfidenz der Auswahl, zwischen 0 und 1. | FLOAT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionChoice/de.md)

---
**Source fingerprint (SHA-256):** `200c63a9197cd95ba0a21da88c5f3117014b37b0651541094a775219381afe43`
