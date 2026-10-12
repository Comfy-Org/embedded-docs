# LTXVImgToVideo

LTXVImgToVideo wandelt ein Eingabebild in eine latente Videorepräsentation für Videogenerierungsmodelle um. Es skaliert das Bild auf die angeforderte Breite und Höhe, kodiert es mit dem VAE und platziert die kodierten Frames am Anfang eines mit Nullen gefüllten Latents in Video-Größe. Die Stärkesteuerung bestimmt, wie viel vom ursprünglichen Bildinhalt während der Videogenerierung erhalten bleibt und wie viel verändert wird.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `positive` | Positive Konditionierungs-Prompts zur Steuerung der Videogenerierung | CONDITIONING | Ja | - |
| `negative` | Negative Konditionierungs-Prompts, um bestimmte Elemente im Video zu vermeiden | CONDITIONING | Ja | - |
| `vae` | VAE-Modell, das zum Kodieren des Eingabebilds in den latenten Raum verwendet wird | VAE | Ja | - |
| `image` | Eingabebild, das in Video-Frames umgewandelt werden soll | IMAGE | Ja | - |
| `width` | Breite des Ausgabevideos in Pixeln (Standard: 768, Schritt: 32) | INT | Ja | 64 bis MAX_RESOLUTION |
| `height` | Höhe des Ausgabevideos in Pixeln (Standard: 512, Schritt: 32) | INT | Ja | 64 bis MAX_RESOLUTION |
| `length` | Anzahl der Frames im generierten Video (Standard: 97, Schritt: 8) | INT | Ja | 9 bis MAX_RESOLUTION |
| `batch_size` | Anzahl der gleichzeitig zu generierenden Videos (Standard: 1) | INT | Ja | 1 bis 4096 |
| `strength` | Steuerung, wie viel vom ursprünglichen Bildinhalt in den ersten Frames des generierten Videos erhalten bleibt. Ein Wert von 1.0 bewahrt das Originalbild vollständig, während 0.0 maximale Modifikation ermöglicht (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |

Hinweis: `width` und `height` ändern sich in Schritten von 32 Pixeln, und `length` ändert sich in Schritten von 8 Frames, was der Video-Latent-Kompression entspricht (32x in den räumlichen Dimensionen und 8x in der zeitlichen Dimension). Das Video-Latent enthält ((length - 1) // 8) + 1 Frames. Das Eingabebild wird mit bilinearer Skalierung und mittigem Zuschneiden auf `width` x `height` skaliert, und nur die ersten drei Kanäle werden zur Kodierung verwendet.

## Ausgaben

| Name der Ausgabe | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Die positive Konditionierung, die unverändert für die Verwendung mit dem generierten Latent durchgereicht wird | CONDITIONING |
| `negative` | Die negative Konditionierung, die unverändert für die Verwendung mit dem generierten Latent durchgereicht wird | CONDITIONING |
| `latent` | Latente Videorepräsentation, die die kodierten Bild-Frames und eine Rauschmaske enthält, die steuert, wie stark die Konditionierung während der Videogenerierung angewendet wird | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideo/de.md)

---
**Source fingerprint (SHA-256):** `4ebc7f80b4d9ac3329e3349c7048885de22b827b5bdd102976687afd7e07a16b`
