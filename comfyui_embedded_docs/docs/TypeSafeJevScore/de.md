# TypeSafe Jev (Score)

Der TypeSafe Jev (Score)-Node bewertet verbundenen Text, Bilder oder beides auf einer Skala von 1 bis 10 und vergleicht die Bewertung mit einem Schwellenwert. Verbinden Sie `result` mit einem If/Else Switch-Node, um auf die Bewertung zu reagieren, oder lesen Sie `score` aus, um die Rohbewertung zu verwenden. Dies ist ein API-Node: Er läuft auf den Servern von Comfy und erfordert ein Comfy.org-Konto mit Guthaben.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Zu verwendendes Jev-Modell. Derzeit ist nur ein Modell verfügbar: `jev-1.14.0`. | COMBO | Ja | `"jev-1.14.0"` |
| `question` | Was bewertet werden soll, auf einer Skala von 1 bis 10. Geben Sie an, wofür 1 und 10 stehen, wie im Standardwert (Standard: `Rate the technical quality of the image from 1 (worst) to 10 (best).`). | STRING | Ja | 1 bis 1000 Zeichen |
| `threshold` | `result` ist true, wenn die Bewertung mindestens diesem Wert entspricht (Standard: 5.0). | FLOAT | Ja | 1.0 bis 10.0 (Schritt 0.1) |
| `images` | Die Bilder, auf die sich die Frage bezieht. Insgesamt bis zu 32 Bilder; eine gebündelte Eingabe zählt pro Bild einmal. Die lange Seite jedes Bildes wird durch die Gesamtzahl der Bilder begrenzt: 1568 px bei bis zu 4 Bildern, 1024 px bei bis zu 8, 768 px bei bis zu 16 und 512 px bei bis zu 32, sodass ein größerer Batch den Detailgrad in jedem Bild verringern kann. | AUTOGROW | Nein | 0 bis 32 Bilder |
| `text` | Der Text, auf den sich die Frage bezieht, beispielsweise ein Prompt oder eine LLM-Antwort. | STRING | Nein | 0 bis 3000 Zeichen |

**Hinweise:**

- Verbinden Sie Text oder mindestens ein Bild; der Node gibt einen Fehler aus, wenn beides leer ist.
- Die Bewertung wird von 1 bis 10 angegeben, und `result` ist true, wenn sie mindestens `threshold` entspricht.
- Die Abrechnung erfolgt tokenbasiert; das Preisabzeichen am Node zeigt den ungefähren Preis pro 1 Mio. Token an.

## Ausgaben

| Ausgabe-Name | Beschreibung | Datentyp |
| --- | --- | --- |
| `result` | True, wenn `score` mindestens `threshold` entspricht. | BOOLEAN |
| `score` | Die Bewertung von 1 (schlechteste) bis 10 (beste). | FLOAT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevScore/de.md)

---
**Source fingerprint (SHA-256):** `7e1970e903d2099ab3d7481a758c5291e87614b9eaf116d0ced6a1bcd36dc126`
