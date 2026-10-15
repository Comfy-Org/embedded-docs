# Get Image/Video Latent Size

Liest ein Bild- oder Video-Latent und gibt dessen Breite, Höhe, Frame-Anzahl und Batch-Größe zurück, sodass die Geometrie wiederverwendet werden kann, ohne das Latent zu dekodieren. Verwenden Sie ihn, um Rauschmasken zu dimensionieren, Auflösungen auszurichten oder Überlappungen beim Kacheln eines Samplers zu ermitteln. Die gemessenen Werte werden außerdem direkt am Node angezeigt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `latent` | Das zu untersuchende Bild- oder Video-Latent. Enthält das Latent mehrere Streams, wird der erste gemessen. | LATENT | Ja | - |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `width` | Die Breite des Latents, in Latent-Zellen statt in Pixeln. | INT |
| `height` | Die Höhe des Latents, in Latent-Zellen statt in Pixeln. | INT |
| `frames` | Die Anzahl der Frames im Latent. Bild-Latents haben einen einzelnen Frame. | INT |
| `batch_size` | Die Anzahl der Latents im Batch. | INT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetLatentSize/de.md)

---
**Source fingerprint (SHA-256):** `f75b3347cb1853b035b0bb283d5487ab1532d561d66d3cae3c67f54bf693d31a`
