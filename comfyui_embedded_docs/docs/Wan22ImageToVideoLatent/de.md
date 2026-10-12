# Wan22ImageToVideoLatent

Wan22ImageToVideoLatent erstellt Video-Latentdarstellungen aus Bildern. Es generiert einen leeren Video-Latentraum mit der angegebenen Breite, Höhe, Frame-Länge und Batch-Größe und kann optional eine Startbildsequenz in die Anfangs-Frames kodieren. Wenn ein Startbild bereitgestellt wird, kodiert der Node es in den latenten Raum und erstellt eine entsprechende Noise-Maske, die markiert, welche Bereiche während der Generierung entrauscht werden sollen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `vae` | Das VAE-Modell, das verwendet wird, um das Startbild in den latenten Raum zu kodieren | VAE | Ja | - |
| `width` | Die Breite des Ausgabevideos in Pixeln (Standard: 1280, Schritt: 32) | INT | Ja | 32 bis MAX_RESOLUTION |
| `height` | Die Höhe des Ausgabevideos in Pixeln (Standard: 704, Schritt: 32) | INT | Ja | 32 bis MAX_RESOLUTION |
| `length` | Die Anzahl der Frames in der Videosequenz (Standard: 49, Schritt: 4) | INT | Ja | 1 bis MAX_RESOLUTION |
| `batch_size` | Die Anzahl der zu generierenden Video-Latents (Standard: 1) | INT | Ja | 1 bis 4096 |
| `start_image` | Optionale Startbildsequenz, die in die Anfangs-Frames des Video-Latents kodiert wird (verwendet die ersten `length` Frames) | IMAGE | Nein | - |

**Hinweis:** Wenn `start_image` angegeben wird, wird die Bildsequenz auf die Ziel-`width` und `height` hochskaliert, mit dem VAE kodiert und in die ersten Frames des Latents eingesetzt. Die Noise-Maske für diese Frames wird auf 0 gesetzt (beibehalten), während die übrigen Frames einen Maskenwert von 1 haben (zu entrauschen). Das Latent hat immer 48 Kanäle, räumliche Dimensionen von `height / 16` mal `width / 16` und eine zeitliche Dimension von `((length - 1) // 4) + 1`. `width` und `height` müssen durch 16 teilbar sein (erzwungen durch den Schritt von 32), und `length` erhöht die zeitliche Dimension in Schritten von 4.

Wenn `start_image` nicht angegeben wird, wird ein vollständig leeres Latent ohne Noise-Maske zurückgegeben, und die Eingabe `batch_size` wird nicht auf dieses leere Latent angewendet.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `samples` | Die generierte Video-Latentdarstellung, für jedes Element im Batch wiederholt | LATENT |
| `noise_mask` | Die Noise-Maske, die angibt, welche Bereiche entrauscht werden sollen (Wert 1) und welche das kodierte Startbild beibehalten (Wert 0) | LATENT |

Beide Felder werden zusammen in einer einzigen LATENT-Ausgabe zurückgegeben.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22ImageToVideoLatent/de.md)

---
**Source fingerprint (SHA-256):** `3d05980641eeef2e86df7a845aa8b2bd703882db98fe71adef2746ab34a9d717`
