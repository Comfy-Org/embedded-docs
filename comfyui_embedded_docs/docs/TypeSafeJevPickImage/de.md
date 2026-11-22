# TypeSafe Jev (Pick Image)

Der Node TypeSafe Jev (Pick Image) wählt ein Bild aus einem Batch aus. Verbinden Sie denselben Bild-Batch zusammen mit `index` mit Get Image from Batch, um das ausgewählte Bild zu behalten, oder lesen Sie `confidence`, um zu entscheiden, ob die Auswahl gut genug ist. Dies ist ein API-Node: Er läuft auf den Servern von Comfy und erfordert ein Comfy.org-Konto mit Guthaben.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das zu verwendende Jev-Modell. Derzeit ist nur ein Modell verfügbar: `jev-1.14.0`. | COMBO | Ja | `"jev-1.14.0"` |
| `question` | Welches Bild ausgewählt werden soll. Verbinden Sie den Prompt mit `text`, um das Bild auszuwählen, das am besten dazu passt (Standard: `Which image best matches the prompt in text? If there is no text, which image has the best quality?`). | STRING | Ja | 1 bis 1000 Zeichen |
| `images` | Die Bilder, aus denen gewählt werden soll. Eine Batch-Eingabe zählt einmal pro Bild, sodass jedes Bild im Batch ein Kandidat ist. Die lange Seite jedes Bildes wird vor dem Upload durch die Batch-Größe begrenzt: 1568 px bei bis zu 4 Bildern, 1024 px bei bis zu 8, 768 px bei bis zu 16 und 512 px bei bis zu 32, sodass ein größerer Batch weniger Details in jedem Bild bedeutet. | IMAGE | Ja | 2 bis 32 Bilder |
| `text` | Der Text, auf den sich die Frage bezieht, etwa der Prompt, aus dem die Bilder erzeugt wurden. | STRING | Nein | 0 bis 3000 Zeichen |

**Hinweise:**

- Der Node gibt einen Fehler aus, wenn weniger als 2 oder mehr als 32 Bilder verbunden sind.
- `index` zählt ab 0; dies ist die Position, die Get Image from Batch erwartet.
- Die Abrechnung erfolgt tokenbasiert; das Preis-Badge am Node zeigt den ungefähren Preis pro 1 Mio. Tokens.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `index` | Position des ausgewählten Bildes im Batch, beginnend bei 0. | INT |
| `confidence` | Wie sicher Jev ist, von 0 (kein klarer Gewinner) bis 1 (sicher). | FLOAT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevPickImage/de.md)

---
**Source fingerprint (SHA-256):** `432ee9ba69ebc0b452de4b52e94abdc56a65dc694a463a3654efb62b172c7b93`
