# Google Gemini Decision (Yes/No)

Stellen Sie eine Ja/Nein-Frage zum Text, zu den Bildern, zum Audio oder zum Video, das Sie verbinden, und erhalten Sie einen booleschen Wert, auf den Sie weiterleiten können. Verbinden Sie `result` mit einem If/Else-Switch-Node, um den Lauf auf einen von zwei Pfaden zu schicken, und lesen Sie `answer` und `probability`, wenn Sie sehen möchten, warum das Modell so geantwortet hat.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `Modell` | Zu verwendendes Modell (Standard: `"gemini-decision-1"`). | COMBO | Ja | `"gemini-decision-1"` |
| `Frage` | Die Ja/Nein-Frage zu dem, was verbunden ist, bis zu 5000 Zeichen. Formulieren Sie sie so, dass „Ja“ der Fall ist, auf den Sie reagieren möchten (Standard: "Is there a person in the image?"). | STRING | Ja | 1 bis 5000 Zeichen |
| `Schwellenwert` | Wahrscheinlichkeit für „Ja“, ab der `result` wahr wird. Eindeutige Ja-Antworten erreichen etwa 0.85 bis 0.92, daher lehnt 0.9 oder mehr viele davon ab (Standard: 0.5). | FLOAT | Ja | 0.01 bis 0.99 (Schritt: 0.01) |
| `Bilder` | Bilder, zu denen die Frage gestellt wird, bis zu 16 über die erweiterbaren Slots (`image_1` ... `image_16`). Ein gebündeltes Bild zählt pro Bild einmal. | IMAGE | Nein | Bis zu 16 Bilder |
| `Audio` | Audioclip, zu dem die Frage gestellt wird. | AUDIO | Nein | - |
| `Video` | Videoclip, zu dem die Frage gestellt wird. | VIDEO | Nein | - |
| `Text` | Text, auf den sich die Frage bezieht, etwa ein Prompt oder eine LLM-Antwort, bis zu 20000 Zeichen. | STRING | Nein | Bis zu 20000 Zeichen |

Verbinden Sie mindestens eines von `text`, `images`, `audio` oder `video`; der Node meldet einen Fehler, wenn es nichts zu betrachten gibt. Benennen Sie bei mehreren Bildern diese innerhalb der Frage als `image_1`, `image_2` und so weiter: Ein Batch wird Bild für Bild entpackt, sodass die Nummern einzelne Frames über die Slots hinweg in Verbindungsreihenfolge zählen.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `result` | Wahr, wenn die Wahrscheinlichkeit für „Ja“ den Wert `threshold` erreicht, andernfalls falsch. | BOOLEAN |
| `answer` | Das Urteil als Zeichenkette `"yes"` oder `"no"`, wobei derselbe `threshold` wie bei `result` gilt. | STRING |
| `probability` | Wahrscheinlichkeit für „Ja“ zwischen 0 und 1. | FLOAT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionYesNo/de.md)

---
**Source fingerprint (SHA-256):** `0339031baf5648609b82526bed97ce8744986878bcbb706dcd3aa79a7370d83f`
