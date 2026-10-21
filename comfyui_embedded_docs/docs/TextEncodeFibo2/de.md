# TextEncodeFibo2

Kodiert einen Fibo-2.0-Prompt in eine Konditionierung und ein passendes leeres Latent. Der Prompt ist entweder Klartext oder eine strukturierte JSON-Bildbeschreibung; bei verbundenen Bildern wird er zur Bearbeitungsanweisung oder zu einer JSON-Bildbeschreibung des Ergebnisses mit einem `edit_instruction`-Schlüssel, und die Bilder dienen als Referenz-Latents für beide Ausgaben, wenn eine VAE verbunden ist. Sampeln Sie die Ausgabe `latent`; ihre Größe entspricht der Größe, auf die die Bilder zugeschnitten werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `clip` | Der Fibo-2.0-Textencoder, mit dem der Prompt tokenisiert und kodiert wird. | CLIP | Ja | - |
| `prompt` | Die Bildbeschreibung, aus der generiert werden soll, bzw. die Bearbeitungsanweisung, wenn Bilder verbunden sind. Verweisen Sie auf die Bilder als `<image_1>`, `<image_2>` und so weiter. Eine JSON-Bildbeschreibung des erwarteten Ergebnisses funktioniert ebenfalls, wobei die Änderung im Schlüssel `edit_instruction` beschrieben wird. | STRING | Ja | - |
| `negative_prompt` | Bildbeschreibung, von der weggeführt werden soll, kodiert als negative Konditionierung. Ein leerer Wert entspricht der Null-Caption, mit der Fibo 2.0 für Classifier-Free-Guidance trainiert wurde (Standard: leer). | STRING | Ja | - |
| `vae` | VAE, mit der die Bilder in Referenz-Latents kodiert werden. Ohne sie konditionieren die Bilder nur die Textkodierung. | VAE | Nein | - |
| `images` | Zu bearbeitende Bilder, bis zu 16. Ein einzelnes Bild wird skaliert und mittig auf die Größe des Ergebnisses zugeschnitten, da die Bearbeitung pixelgenau damit übereinstimmt; mehrere Bilder werden jeweils auf ihre eigene trainierte Größe skaliert. | IMAGE | Nein | 0 bis 16 Bilder |
| `width` | Breite des Ergebnisses, abgerundet auf ein Vielfaches von 16. 0 verwendet die Größe, mit der Fibo 2.0 für das Seitenverhältnis des ersten Bildes trainiert wurde, etwa 1 Megapixel, oder 1024 ohne Bilder (Standard: 0). | INT | Ja | 0 bis 16384 (Schritt 16) |
| `height` | Höhe des Ergebnisses, abgerundet auf ein Vielfaches von 16. 0 verwendet die Größe, mit der Fibo 2.0 für das Seitenverhältnis des ersten Bildes trainiert wurde, etwa 1 Megapixel, oder 1024 ohne Bilder (Standard: 0). | INT | Ja | 0 bis 16384 (Schritt 16) |
| `batch_size` | Anzahl der im Batch zu erzeugenden Latents (Standard: 1). | INT | Ja | 1 bis 4096 |

Die Referenz-Latents werden an beide Ausgaben angehängt, sodass die Bilder mit der Konditionierung mitgeführt werden und nicht nur mit dem positiven Zweig. Wenn die VAE nicht verbunden ist, werden die Bilder nur vom Textencoder gesehen und es werden keine Referenz-Latents hinzugefügt.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Konditionierung des Prompts, mit den Referenz-Latents, wenn eine VAE und Bilder verbunden sind. | CONDITIONING |
| `negative` | Konditionierung von `negative_prompt`, nur Text, mit denselben Referenz-Latents. | CONDITIONING |
| `latent` | Leeres Latent in der angeforderten Größe, bereit zum Sampeln. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeFibo2/de.md)

---
**Source fingerprint (SHA-256):** `f400d041a3dd224e30c0fa2acc803e3de11d6c10654bde122e8d569fa1cd1d79`
