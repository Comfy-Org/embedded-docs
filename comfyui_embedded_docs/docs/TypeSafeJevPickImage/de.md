# TypeSafe Jev (Pick Image)

Der TypeSafe Jev (Pick Image)-Node wählt ein Bild aus einem Stapel aus. Verbinden Sie denselben Bildstapel mit Get Image from Batch zusammen mit `index`, um das ausgewählte Bild zu behalten, oder lesen Sie `confidence`, um zu entscheiden, ob die Auswahl gut genug ist. Dies ist ein API-Node: Er läuft auf den Servern von Comfy und erfordert ein Comfy.org-Konto mit Guthaben.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Zu verwendendes Jev-Modell. Derzeit ist nur ein Modell verfügbar: `jev-1.14.0`. | COMBO | Ja | `"jev-1.14.0"` |
| `question` | Welches Bild ausgewählt werden soll. Verbinden Sie den Prompt mit `text`, um das Bild auszuwählen, das am besten dazu passt (Standard: `Which image best matches the prompt in text? If there is no text, which image has the best quality?`). | STRING | Ja | 1 bis 1000 Zeichen |
| `images` | Die Bilder, aus denen gewählt werden soll. Eine Stapel-Eingabe zählt einmal pro Bild, sodass jedes Bild im Stapel ein Kandidat ist. Die lange Seite jedes Bildes wird vor dem Hochladen durch die Größe des Stapels begrenzt: 1568 px für bis zu 4 Bilder, 1024 px für bis zu 8, 768 px für bis zu 16 und 512 px für bis zu 32, sodass ein größerer Stapel den Detailgrad jedes Bildes verringern kann. | IMAGE | Ja | 2 bis 32 Bilder |
| `text` | Der Text, auf den sich die Frage bezieht, beispielsweise der Prompt, aus dem die Bilder erstellt wurden. | STRING | Nein | 0 bis 3000 Zeichen |

**Hinweise:**

- Der Node gibt einen Fehler aus, wenn weniger als 2 oder mehr als 32 Bilder verbunden sind.
- `index` zählt ab 0, was der Position entspricht, die Get Image from Batch erwartet.
- Die Abrechnung erfolgt tokenbasiert; das Preisabzeichen auf dem Node zeigt den ungefähren Tarif pro 1M Tokens.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
| --- | --- | --- |
| `index` | Position des ausgewählten Bildes im Stapel, beginnend bei 0. | INT |
| `confidence` | Wie sicher Jev ist, von 0 (kein eindeutiger Gewinner) bis 1 (sicher). | FLOAT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevPickImage/de.md)

---
**Source fingerprint (SHA-256):** `432ee9ba69ebc0b452de4b52e94abdc56a65dc694a463a3654efb62b172c7b93`
