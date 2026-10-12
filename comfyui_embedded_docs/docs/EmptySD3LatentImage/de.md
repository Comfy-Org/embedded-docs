# EmptySD3LatentImage

EmptySD3LatentImage erstellt ein leeres (ausschließlich aus Nullen bestehendes) latentes Bild im Layout, das Stable Diffusion 3-Modelle erwarten. Da das Latent leer ist, wird es normalerweise als Ausgangspunkt verwendet, den ein Generierungsworkflow mit einem Bild füllt. Die gewählte Breite und Höhe bestimmen die Größe des endgültigen Bildes.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `width` | Die Breite des latenten Bildes in Pixeln (Standard: 1024). Werte werden in Schritten von 16 erhöht. | INT | Ja | 16 to MAX_RESOLUTION (step: 16) |
| `height` | Die Höhe des latenten Bildes in Pixeln (Standard: 1024). Werte werden in Schritten von 16 erhöht. | INT | Ja | 16 to MAX_RESOLUTION (step: 16) |
| `batch_size` | Die Anzahl der im Batch zu generierenden latenten Bilder (Standard: 1). | INT | Ja | 1 to 4096 |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `LATENT` | Ein latenter Tensor, der leere (ausschließlich aus Nullen bestehende) Samples im SD3-kompatiblen Format enthält. Der Tensor hat 16 Kanäle, ist relativ zu `width` und `height` um den Faktor 8 herunterskaliert und weist ein räumliches Downscale-Verhältnis von 8 auf. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptySD3LatentImage/de.md)

---
**Source fingerprint (SHA-256):** `694ede56f43e3f3889b4d23e636fa6b33b490bcbd214584557f0dc883fa0a32d`
