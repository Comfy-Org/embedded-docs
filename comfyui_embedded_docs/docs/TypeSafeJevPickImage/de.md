# TypeSafe Jev (Pick Image)

Der TypeSafe Jev (Pick Image)-Node wählt ein Bild aus einem Batch aus. Verbinden Sie `index` mit Get Image from Batch, um das ausgewählte Bild zu behalten, oder lesen Sie `confidence`, um zu entscheiden, ob die Auswahl gut genug ist. Dies ist ein API-Node und erfordert ein Comfy.org-Konto und einen API-Schlüssel.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Zu verwendendes Jev-Modell. Derzeit ist nur ein Modell verfügbar: `jev-1.14.0`. | COMBO | Ja | `"jev-1.14.0"` |
| `question` | Welches Bild ausgewählt werden soll. Verbinden Sie den Prompt mit `text`, um das Bild auszuwählen, das am besten dazu passt (Standard: `Which image best matches the prompt in text? If there is no text, which image has the best quality?`). | STRING | Ja | 1 bis 1000 Zeichen |
| `images` | Die Bilder, aus denen ausgewählt werden soll. Eine Batch-Eingabe zählt einmal pro Bild, sodass jedes Bild im Batch ein Kandidat ist. | IMAGE | Ja | 2 bis 32 Bilder |
| `text` | Der Text, auf den sich die Frage bezieht, z. B. der Prompt, aus dem die Bilder erstellt wurden. | STRING | Nein | 0 bis 3000 Zeichen |

**Hinweise:**

- Der Node löst einen Fehler aus, wenn weniger als 2 oder mehr als 32 Bilder verbunden sind.
- `index` zählt ab 0; dies ist die Position, die Get Image from Batch erwartet.
- Die Abrechnung erfolgt tokenbasiert; das Preis-Badge am Node zeigt den ungefähren Satz pro 1 Mio. Token.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `index` | Position des ausgewählten Bildes im Batch, beginnend bei 0. | INT |
| `confidence` | Wie sicher sich Jev ist, von 0 (kein klarer Gewinner) bis 1 (sicher). | FLOAT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevPickImage/de.md)

---
**Source fingerprint (SHA-256):** `432ee9ba69ebc0b452de4b52e94abdc56a65dc694a463a3654efb62b172c7b93`
