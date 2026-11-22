# TypeSafe Jev (Yes/No)

Der Node TypeSafe Jev (Yes/No) stellt eine Ja-oder-Nein-Frage zu verbundenem Text, Bildern oder beidem und gibt die Antwort als booleschen Wert zurück. Verbinden Sie `result` mit einem If/Else Switch-Node, um den Workflow zu steuern, oder lesen Sie `probability` aus, um darauf zu reagieren, wie sicher sich das Modell ist. Dies ist ein API-Node: Er läuft auf den Servern von Comfy und erfordert ein Comfy.org-Konto mit Guthaben.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Zu verwendendes Jev-Modell. Derzeit ist nur ein Modell verfügbar: `jev-1.14.0`. | COMBO | Ja | `"jev-1.14.0"` |
| `question` | Die Ja-oder-Nein-Frage, die der verbundene Text und die Bilder beantworten. Formulieren Sie sie so, dass „Ja“ der Fall ist, auf den Sie reagieren möchten; bei mehreren Bild-Sockets verwenden Sie deren Namen, zum Beispiel `Does image_2 show the same person as image_1?` (Standard: `Is there a person in the image?`). | STRING | Ja | 1 bis 1000 Zeichen |
| `threshold` | Die Antwort lautet „Ja“, wenn die Wahrscheinlichkeit für „Ja“ mindestens diesem Wert entspricht (Standard: 0.5). | FLOAT | Ja | 0.01 bis 0.99 (Schritt: 0.01) |
| `images` | Die Bilder, auf die sich die Frage bezieht. Insgesamt bis zu 32 Bilder; eine gebündelte Eingabe zählt pro Bild einmal. Die lange Seite jedes Bildes wird durch die Gesamtzahl der Bilder begrenzt: 1568 px bei bis zu 4 Bildern, 1024 px bei bis zu 8, 768 px bei bis zu 16 und 512 px bei bis zu 32, sodass ein größerer Stapel den Detailgrad in jedem Bild verringern kann. | AUTOGROW | Nein | 0 bis 32 Bilder |
| `text` | Der Text, auf den sich die Frage bezieht, etwa ein Prompt oder eine LLM-Antwort. | STRING | Nein | 0 bis 3000 Zeichen |

**Hinweise:**

- Verbinden Sie Text oder mindestens ein Bild; der Node gibt einen Fehler aus, wenn beides leer ist.
- `result` ist true, wenn `probability` mindestens `threshold` entspricht, und `answer` liefert dasselbe Urteil als `yes` oder `no`.
- Die Abrechnung erfolgt tokenbasiert; das Preis-Badge am Node zeigt den ungefähren Preis pro 1 Mio. Tokens.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `result` | Die Antwort als boolescher Wert: true, wenn die Wahrscheinlichkeit für „Ja“ mindestens `threshold` entspricht. | BOOLEAN |
| `answer` | Die Antwort als Text `yes` oder `no`. | STRING |
| `probability` | Wahrscheinlichkeit für „Ja“, von 0 (definitiv nein) bis 1 (definitiv ja). | FLOAT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevYesNo/de.md)

---
**Source fingerprint (SHA-256):** `e8c7de5558c61e7c9058b28104a72d8d8961165983d02d63a5c9078c40855385`
