# Kandinsky5ImageToVideo

Der Node Kandinsky5ImageToVideo bereitet Konditionierungs- und Latent-Daten für die Videogenerierung mit dem Kandinsky-Modell vor. Er erstellt ein leeres Video-Latent in der angeforderten Breite, Höhe, Länge und Batch-Größe und kann optional ein Startbild kodieren, um die Anfangsframes des generierten Videos zu steuern, indem die positive und negative Konditionierung aktualisiert wird.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `positive` | Die positiven Konditionierungs-Prompts zur Steuerung der Videogenerierung. | CONDITIONING | Ja | N/A |
| `negative` | Die negativen Konditionierungs-Prompts, um die Videogenerierung von bestimmten Konzepten wegzulenken. | CONDITIONING | Ja | N/A |
| `vae` | Das VAE-Modell, das verwendet wird, um das optionale Startbild in den latenten Raum zu kodieren. | VAE | Ja | N/A |
| `width` | Die Breite des Ausgabevideos in Pixeln (Standard: 768). | INT | Ja | 16 bis 16384 (Schritt 16) |
| `height` | Die Höhe des Ausgabevideos in Pixeln (Standard: 512). | INT | Ja | 16 bis 16384 (Schritt 16) |
| `length` | Die Anzahl der Frames im Video (Standard: 121). | INT | Ja | 1 bis 16384 (Schritt 4) |
| `batch_size` | Die Anzahl der gleichzeitig zu generierenden Videosequenzen (Standard: 1). | INT | Ja | 1 bis 4096 |
| `start_image` | Ein optionales Startbild oder ein Batch von Frames. Falls angegeben, wird es kodiert und verwendet, um den verrauschten Anfang der Ausgabe-Latents des Modells zu ersetzen. | IMAGE | Nein | N/A |

**Hinweis:** Wenn eine `start_image` bereitgestellt wird, wird sie automatisch mithilfe bilinearer Interpolation an die angegebene `width` und `height` angepasst. Es werden nur die ersten `length` Frames des Bild-Batches zur Kodierung verwendet; alle weiteren Frames werden ignoriert. Wenn der Bild-Batch weniger als `length` Frames enthält, werden nur diese Frames verwendet. Es werden nur die RGB-Kanäle des Bildes kodiert. Das kodierte Latent wird dann sowohl in die `positive`- als auch in die `negative`-Konditionierung eingespeist, um das anfängliche Erscheinungsbild des Videos zu steuern, und die sauberen kodierten Frames ersetzen den verrauschten Anfang der Ausgabe-Latents des Modells.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Die modifizierte positive Konditionierung, aktualisiert mit kodierten Startbilddaten, wenn eine `start_image` bereitgestellt wird. | CONDITIONING |
| `negative` | Die modifizierte negative Konditionierung, aktualisiert mit kodierten Startbilddaten, wenn eine `start_image` bereitgestellt wird. | CONDITIONING |
| `latent` | Leeres Video-Latent. Ein mit Nullen gefüllter Latent-Tensor, geformt für die angegebenen Dimensionen. | LATENT |
| `cond_latent` | Saubere kodierte Startbilder, die verwendet werden, um den verrauschten Anfang der Modell-Ausgabe-Latents zu ersetzen. Leer, wenn keine `start_image` bereitgestellt wird. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kandinsky5ImageToVideo/de.md)

---
**Source fingerprint (SHA-256):** `7212f0ea912578d3b72dddf1333a20054a881e3f22c2b8abd9645fc21e75a08b`
