# TextEncodeMageFlowEdit

## Übersicht

Dieser Node kodiert eine Bearbeitungsanweisung (Prompt) zusammen mit einem oder mehreren Referenzbildern für das Mage-Flow-Edit-Modell. Er skaliert alle Referenzbilder auf die Zielausgabeauflösung, kodiert sie in den Latentraum, wenn ein VAE bereitgestellt wird, und hängt die Referenz-Latents an die Conditioning-Ausgabe an. Außerdem wird ein leerer Latent-Tensor mit den korrekten Dimensionen für das Sampling erzeugt, wodurch sichergestellt wird, dass die Größe immer mit der Ausgabebreite und -höhe übereinstimmt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `clip` | Das CLIP-Modell, das zum Tokenisieren und Kodieren der Text-Prompts verwendet wird. | CLIP | Ja | |
| `prompt` | Die anzuwendende Bearbeitungsanweisung (Positiv-Prompt). | STRING | Ja | mehrzeilig, dynamische Prompts aktiviert |
| `negative_prompt` | Der Negativ-Prompt, von dem weggesteuert werden soll. Standard: leerer String (verwendet intern ein Leerzeichen, wenn leer). Wird im erweiterten Bereich der UI angezeigt. | STRING | Nein | mehrzeilig, dynamische Prompts aktiviert |
| `vae` | VAE-Modell zum Kodieren von Referenzbildern in den Latentraum. Wenn nicht bereitgestellt, werden keine Referenz-Latents an das Conditioning angehängt. | VAE | Nein | |
| `images` | Referenzbild(er), die bearbeitet werden sollen. Alle Referenzen werden vor der Kodierung auf die Ausgabeauflösung skaliert. | IMAGE (autogrow) | Nein | Bis zu 16 Bilder (benannt `image_1`…`image_16`), mindestens 0 |
| `width` | Ausgabebreite in Pixeln. Wenn auf 0 gesetzt, wird die Breite des ersten Referenzbilds verwendet. Wird immer auf ein Vielfaches von 16 abgerundet. Standard: 0. | INT | Ja | 0 bis 8192 (Schritt 16) |
| `height` | Ausgabehöhe in Pixeln. Gleiches Fallback-Verhalten wie bei der Breite. Standard: 0. | INT | Ja | 0 bis 8192 (Schritt 16) |
| `batch_size` | Anzahl der zu erzeugenden Latent-Samples. Standard: 1. | INT | Ja | 1 bis 4096 |

**Hinweise zu Parameterabhängigkeiten:**
- Wenn `width` und/oder `height` 0 sind und keine Referenzbilder bereitgestellt werden, fallen sie jeweils auf 1024 zurück.
- Wenn nur einer der Werte `width` oder `height` 0 ist, wird die fehlende Dimension vom ersten Referenzbild übernommen, während die explizit gesetzte Dimension beibehalten wird.
- Der Parameter `vae` ist optional; Referenz-Latents werden nur erzeugt und an das Conditioning angehängt, wenn ein VAE verbunden ist.
- Das Feld `negative_prompt` ist optional – wenn es leer bleibt, wird intern ein einzelnes Leerzeichen als Negativtext verwendet.
- Für das Text-Conditioning wird jedes Referenzbild so skaliert, dass seine längste Kante höchstens 384 Pixel beträgt, was der Vorverarbeitung beim Training entspricht. Der VAE-Kodierungszweig skaliert stattdessen alle Referenzen auf die volle Ausgabeauflösung.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `positive` | Conditioning-Ausgabe, die die Token des Positiv-Prompts sowie (falls ein VAE bereitgestellt wurde) die kodierten Referenz-Latents enthält. | CONDITIONING |
| `negative` | Conditioning-Ausgabe, die die Token des Negativ-Prompts sowie dieselben Referenz-Latents enthält (falls VAE bereitgestellt). | CONDITIONING |
| `latent` | Ein leerer Latent-Tensor mit der Form `[batch_size, 128, height÷16, width÷16]` zur Verwendung als initiales Rauschen während des Samplings. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeMageFlowEdit/de.md)

---
**Source fingerprint (SHA-256):** `880d8856b7f6e656bc68ca953fbf892898d05bc5d65290ae3bf7a4405ee09be3`
