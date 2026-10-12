# EmptyHiDreamO1LatentImage

Dieser Node erstellt ein leeres Latent-Bild im Pixelraum für das HiDream-O1-Image-Modell. Er erzeugt einen leeren Tensor aus Nullen, der als Ausgangspunkt für die Bilderzeugung dient, wobei die Abmessungen durch die Eingaben `width`, `height` und `batch_size` definiert werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `width` | Die Breite des Latent-Bilds in Pixeln. Standard: 2048. Der Wert muss ein Vielfaches von 32 sein. Das Modell wurde mit etwa 4 Megapixeln trainiert; niedrigere Auflösungen können die Qualität merklich verringern. | INT | Ja | 64 bis 4096 (Schritt: 32) |
| `height` | Die Höhe des Latent-Bilds in Pixeln. Standard: 2048. Der Wert muss ein Vielfaches von 32 sein. Das Modell wurde mit etwa 4 Megapixeln trainiert; niedrigere Auflösungen können die Qualität merklich verringern. | INT | Ja | 64 bis 4096 (Schritt: 32) |
| `batch_size` | Die Anzahl der Latent-Bilder, die in einem einzelnen Batch erzeugt werden sollen. Standard: 1. | INT | Ja | 1 bis 64 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `samples` | Ein mit Nullen gefüllter Tensor, der das leere Latent-Bild repräsentiert, mit der Form (batch_size, 3, height, width). | LATENT |

## Hinweise

- Das HiDream-O1-Image-Modell wurde mit ungefähr 4 Megapixeln trainiert. Die Verwendung deutlich niedrigerer Auflösungen kann zu einer merklich verringerten Bildqualität führen.
- Zu den trainierten Auflösungen gehören: 2048x2048, 2304x1728, 1728x2304, 2560x1440, 1440x2560, 2496x1664, 1664x2496, 3104x1312, 1312x3104, 2304x1792, 1792x2304.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHiDreamO1LatentImage/de.md)

---
**Source fingerprint (SHA-256):** `7412639e261512d9174e60009143c8c06c354e2a20ada7271837d72053426be5`
