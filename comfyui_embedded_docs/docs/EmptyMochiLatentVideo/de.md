# EmptyMochiLatentVideo

EmptyMochiLatentVideo erzeugt einen leeren latenten Video-Tensor mit den von Ihnen angegebenen Abmessungen. Er generiert eine mit Nullen gefüllte latente Darstellung, die als Ausgangspunkt für Workflows zur Videogenerierung verwendet werden kann. Mit diesem Node können Sie Breite, Höhe, Länge und Batch-Größe des latenten Video-Tensors festlegen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `width` | Die Breite des latenten Videos in Pixeln (Standard: 848, Werte erhöhen sich in Schritten von 16) | INT | Ja | 16 bis MAX_RESOLUTION |
| `height` | Die Höhe des latenten Videos in Pixeln (Standard: 480, Werte erhöhen sich in Schritten von 16) | INT | Ja | 16 bis MAX_RESOLUTION |
| `length` | Die Anzahl der Frames im latenten Video (Standard: 25, Werte erhöhen sich in Schritten von 6, beginnend bei 7) | INT | Ja | 7 bis MAX_RESOLUTION |
| `batch_size` | Die Anzahl der latenten Videos, die in einem Batch erzeugt werden sollen (Standard: 1) | INT | Nein | 1 bis 4096 |

**Hinweis:** Die tatsächlichen latenten Abmessungen werden als width/8 und height/8 berechnet, die zeitliche Dimension wird als `((length - 1) // 6) + 1` berechnet, und der Tensor hat 12 Kanäle. Da `length` in Schritten von 6 ab 7 fortschreitet, sind gültige Werte 7, 13, 19, 25 und so weiter.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `samples` | Ein leerer latenter Video-Tensor mit den angegebenen Abmessungen, der ausschließlich Nullen enthält | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMochiLatentVideo/de.md)

---
**Source fingerprint (SHA-256):** `1774e1b54b429a946172ba9f609b433d99c0ca2ced2d9e0e3b0b85c82e5141b2`
