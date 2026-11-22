# TypeSafe Jev (Yes/No)

Der TypeSafe Jev (Ja/Nein)-Node stellt eine Ja-oder-Nein-Frage zu verbundenem Text, Bildern oder beidem und gibt die Antwort als booleschen Wert zurück. Verbinden Sie `result` mit einem If/Else Switch-Node, um den Workflow zu verzweigen, oder lesen Sie `probability`, um auf die Sicherheit des Modells zu reagieren. Dies ist ein API-Node und erfordert ein Comfy.org-Konto und einen API-Schlüssel.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Range |
| --- | --- | --- | --- | --- |
| `model` | Zu verwendendes Jev-Modell. Derzeit ist nur ein Modell verfügbar: `jev-1.14.0`. | COMBO | Ja | `"jev-1.14.0"` |
| `question` | Die Ja-oder-Nein-Frage, die der verbundene Text und die Bilder beantworten. Formulieren Sie sie so, dass „Ja“ der Fall ist, auf den Sie reagieren; verwenden Sie bei mehreren Bild-Sockets deren Namen, zum Beispiel `Does image_2 show the same person as image_1?` (Standard: `Is there a person in the image?`). | STRING | Ja | 1 bis 1000 Zeichen |
| `threshold` | Die Antwort ist „Ja“, wenn die Wahrscheinlichkeit für „Ja“ mindestens diesem Wert entspricht (Standard: 0.5). | FLOAT | Ja | 0.01 bis 0.99 (Schritt: 0.01) |
| `images` | Die Bilder, auf die sich die Frage bezieht. Insgesamt bis zu 32 Bilder; eine gebatchte Eingabe zählt pro Bild einmal, und mehr als 4 Bilder werden in einer kleineren Größe gesendet. | AUTOGROW | Nein | 0 bis 32 Bilder |
| `text` | Der Text, auf den sich die Frage bezieht, etwa ein Prompt oder eine LLM-Antwort. | STRING | Nein | 0 bis 3000 Zeichen |

**Hinweise:**

- Verbinden Sie Text oder mindestens ein Bild; der Node löst einen Fehler aus, wenn beides leer ist.
- `result` ist true, wenn `probability` mindestens `threshold` entspricht, und `answer` liefert dasselbe Urteil als `yes` oder `no`.
- Die Abrechnung erfolgt tokenbasiert; das Preisabzeichen auf dem Node zeigt den ungefähren Satz pro 1 Mio. Tokens.

## Ausgaben

| Output Name | Beschreibung | Datentyp |
| --- | --- | --- |
| `result` | Die Antwort als boolescher Wert: true, wenn die Wahrscheinlichkeit für „Ja“ mindestens `threshold` entspricht. | BOOLEAN |
| `answer` | Die Antwort als Text `yes` oder `no`. | STRING |
| `probability` | Wahrscheinlichkeit für „Ja“, von 0 (definitiv nein) bis 1 (definitiv ja). | FLOAT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevYesNo/de.md)

---
**Source fingerprint (SHA-256):** `e8c7de5558c61e7c9058b28104a72d8d8961165983d02d63a5c9078c40855385`
