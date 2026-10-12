# WanCameraImageToVideo

Der Node WanCameraImageToVideo bereitet Konditionierungs- und Latent-Daten für die kameragesteuerte Videogenerierung aus Bildern vor. Er nimmt positive und negative Konditionierungs-Prompts sowie optionale Eingaben wie ein Startbild, eine CLIP-Vision-Ausgabe und Kamerabedingungen entgegen und gibt aktualisierte Konditionierung plus einen leeren Latent-Tensor aus, der von einem Videomodell gefüllt werden kann.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `positive` | Positive Konditionierungs-Prompts für die Videogenerierung | CONDITIONING | Ja | - |
| `negative` | Negative Konditionierungs-Prompts, die bei der Videogenerierung vermieden werden sollen | CONDITIONING | Ja | - |
| `vae` | VAE-Modell zum Kodieren von Bildern in den Latent-Raum | VAE | Ja | - |
| `width` | Ausgabevideo-Breite in Pixeln (Standard: 832, Schritt: 16) | INT | Ja | 16 bis MAX_RESOLUTION |
| `height` | Ausgabevideo-Höhe in Pixeln (Standard: 480, Schritt: 16) | INT | Ja | 16 bis MAX_RESOLUTION |
| `length` | Anzahl der Frames in der Videosequenz (Standard: 81, Schritt: 4) | INT | Ja | 1 bis MAX_RESOLUTION |
| `batch_size` | Anzahl der gleichzeitig zu generierenden Videos (Standard: 1) | INT | Ja | 1 bis 4096 |
| `clip_vision_output` | Optionale CLIP-Vision-Ausgabe für zusätzliche Konditionierung | CLIP_VISION_OUTPUT | Nein | - |
| `start_image` | Optionales Startbild zur Initialisierung der Videosequenz. Wenn angegeben, werden nur die ersten `length` Frames verwendet, und das Bild wird skaliert, um der angegebenen `width` und `height` zu entsprechen. Die ersten Frames der Sequenz werden in den latenten Raum kodiert und eine Maske wird angewendet, um die Startframes mit generiertem Inhalt zu überblenden. | IMAGE | Nein | - |
| `camera_conditions` | Optionale Kamera-Embedding-Bedingungen für die Videogenerierung. Wenn angegeben, werden diese Bedingungen sowohl auf die positive als auch auf die negative Konditionierung angewendet. | WAN_CAMERA_EMBEDDING | Nein | - |

**Hinweis:** Wenn `start_image` angegeben wird, setzt der Node die Werte `concat_latent_image` und `concat_mask` sowohl bei der `positive`- als auch bei der `negative`-Konditionierung. Die Parameter `camera_conditions` und `clip_vision_output` sind optional, aber wenn sie angegeben werden, verändern sie die Konditionierung sowohl für die positiven als auch für die negativen Prompts.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Modifizierte positive Konditionierung mit angewendeten Kamerabedingungen, CLIP-Vision-Ausgabe und/oder Startbilddaten | CONDITIONING |
| `negative` | Modifizierte negative Konditionierung mit angewendeten Kamerabedingungen, CLIP-Vision-Ausgabe und/oder Startbilddaten | CONDITIONING |
| `latent` | Leere Video-Latent-Repräsentation zur Verwendung mit Videomodellen. Der Latent-Tensor hat die Dimensionen [batch_size, 16, frames, height/8, width/8], wobei frames als ((length - 1) // 4) + 1 berechnet wird. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraImageToVideo/de.md)

---
**Source fingerprint (SHA-256):** `467a82be0dfd6ac1c3b2dd2a6cb02e0d0749de4536a7fbdb000456b817b20ebb`
