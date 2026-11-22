# HeyGen Decision (Yes/No)

Stellen Sie eine Ja/Nein-Frage zu dem Text, den Bildern, dem Audio oder dem Video, das Sie verbinden, und erhalten Sie einen booleschen Wert, auf dem Sie weiterleiten können. Verbinden Sie `result` mit einem If/Else-Switch-Node, um zwischen zwei Pfaden zu wählen, und lesen Sie `answer` und `probability`, um zu sehen, wie eindeutig die Antwort war.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `Modell` | Zu verwendendes Modell. `heygen-decision-1-turbo` ist schneller und kostengünstiger als `heygen-decision-1` (Standard: `"heygen-decision-1"`). | COMBO | Ja | `"heygen-decision-1"`<br>`"heygen-decision-1-turbo"` |
| `Frage` | Die Ja/Nein-Frage zu dem, was verbunden ist, bis zu 5000 Zeichen. Formulieren Sie sie so, dass „Ja“ dem Fall entspricht, auf den Sie reagieren möchten (Standard: „Is there a person in the image?“). | STRING | Ja | 1 bis 5000 Zeichen |
| `Schwellenwert` | Wahrscheinlichkeit für „Ja“, ab der `result` true wird; eindeutige Antworten liegen nahe bei 0 oder 1 (Standard: 0.5). | FLOAT | Ja | 0.01 bis 0.99 (Schritt 0.01) |
| `Bilder` | Bilder, zu denen die Frage gestellt wird, insgesamt bis zu 4, wobei jeder Frame eines Batches mitzählt. Sie werden über die Sockets hinweg in der Reihenfolge `image_1` bis `image_4` nummeriert. | IMAGE | Nein | Bis zu 4 Bilder |
| `audio_1` | Audio, zu dem die Frage gestellt wird, bis zu 30 Minuten. | AUDIO | Nein | Bis zu 30 Minuten |
| `video_1` | Video, zu dem die Frage gestellt wird, bis zu 60 Sekunden. | VIDEO | Nein | Bis zu 60 Sekunden |
| `Text` | Text, auf den sich die Frage bezieht, etwa ein Prompt oder eine LLM-Antwort, bis zu 20000 Zeichen. | STRING | Nein | Bis zu 20000 Zeichen |

Verbinden Sie mindestens eines von `text`, `images`, `audio_1` oder `video_1` und verweisen Sie innerhalb der Frage über den Socket-Namen darauf, zum Beispiel „Zeigt image_2 dieselbe Person wie image_1?“.

## Ausgaben

| Output Name | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `result` | True, wenn die Wahrscheinlichkeit für „Ja“ `threshold` erreicht, andernfalls false. | BOOLEAN |
| `answer` | Das Urteil als String `"yes"` oder `"no"`, wobei derselbe `threshold` wie bei `result` gilt. | STRING |
| `probability` | Wahrscheinlichkeit für „Ja“ zwischen 0 und 1. | FLOAT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenDecisionYesNo/de.md)

---
**Source fingerprint (SHA-256):** `5a6a606d5c6ef62eb3424bd54a0da3dc177da7d0acf4b5c235a62b78ad8d2df1`
