# WanFirstLastFrameToVideo

Der Node WanFirstLastFrameToVideo bereitet die Konditionierung für die Videogenerierung vor, indem er ein Startframe und ein Endframe mit Text-Prompts kombiniert. Er kodiert die Frame-Bilder in den latenten Raum, erstellt eine Maske, die dem Videomodell mitteilt, welche Frames bereits bekannt sind, und hängt CLIP-Vision-Merkmale an, wenn diese bereitgestellt werden. Der Node gibt aktualisierte positive und negative Konditionierung sowie ein leeres Latent aus, das die Größe und Länge des zu generierenden Videos definiert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `positive` | Positive Textkonditionierung, die zur Steuerung der Videogenerierung verwendet wird. | CONDITIONING | Ja | - |
| `negative` | Negative Textkonditionierung, die zur Steuerung der Videogenerierung verwendet wird. | CONDITIONING | Ja | - |
| `vae` | VAE-Modell, das verwendet wird, um die kombinierten Frame-Bilder in den latenten Raum zu kodieren. | VAE | Ja | - |
| `width` | Breite des generierten Videos in Pixeln (Standard: 832, Schritt: 16). | INT | Ja | 16 bis MAX_RESOLUTION |
| `height` | Höhe des generierten Videos in Pixeln (Standard: 480, Schritt: 16). | INT | Ja | 16 bis MAX_RESOLUTION |
| `length` | Anzahl der Frames in der Videosequenz (Standard: 81, Schritt: 4). | INT | Ja | 1 bis MAX_RESOLUTION |
| `batch_size` | Anzahl der auf einmal zu generierenden Videos (Standard: 1). | INT | Ja | 1 bis 4096 |
| `clip_vision_start_image` | Aus dem Startbild extrahierte CLIP-Vision-Merkmale. Wenn sowohl Start- als auch Ende-CLIP-Vision-Eingaben bereitgestellt werden, werden ihre Merkmale kombiniert. | CLIP_VISION_OUTPUT | Nein | - |
| `clip_vision_end_image` | Aus dem Endbild extrahierte CLIP-Vision-Merkmale. Wenn sowohl Start- als auch Ende-CLIP-Vision-Eingaben bereitgestellt werden, werden ihre Merkmale kombiniert. | CLIP_VISION_OUTPUT | Nein | - |
| `start_image` | Startframe-Bild für die Videosequenz. Seine ersten `length` Frames werden verwendet und auf `width` × `height` skaliert. | IMAGE | Nein | - |
| `end_image` | Endframe-Bild für die Videosequenz. Seine letzten `length` Frames werden verwendet und auf `width` × `height` skaliert. | IMAGE | Nein | - |

**Hinweis:** Wenn mindestens eines von `start_image` oder `end_image` bereitgestellt wird, erstellt der Node eine kombinierte Framesequenz, in der die Start- und Endframes eingefügt werden und die übrigen Frames einen neutralen grauen Platzhalter (0.5) verwenden. Eine Maske markiert die gefüllten Bereiche als bekannt und die Platzhalterbereiche als unbekannt, sodass das Videomodell die dazwischenliegenden Frames generieren kann. Wenn ein Startbild bereitgestellt wird, erstreckt sich der bekannte Bereich zusätzlich 3 Frames über das Bild hinaus. Dasselbe kodierte Frame-Bild und dieselbe Maske werden sowohl an die `positive`- als auch an die `negative`-Konditionierung angehängt. Wenn beide CLIP-Vision-Eingaben bereitgestellt werden, werden ihre Hidden States konkateniert; wenn nur eine bereitgestellt wird, wird sie allein verwendet. Die latente Videolänge wird aus `length` nach temporaler Kompression abgeleitet: `((length - 1) // 4) + 1`.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Positive Konditionierung mit angehängtem kodiertem Frame-Bild, angehängter Maske und (falls bereitgestellt) angehängten CLIP-Vision-Merkmalen. | CONDITIONING |
| `negative` | Negative Konditionierung mit angehängtem kodiertem Frame-Bild, angehängter Maske und (falls bereitgestellt) angehängten CLIP-Vision-Merkmalen. | CONDITIONING |
| `latent` | Leerer latenter Tensor (alle Nullen), geformt für die angegebene Batch-Größe, Videolänge und Auflösung. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFirstLastFrameToVideo/de.md)

---
**Source fingerprint (SHA-256):** `0072e441cb80334c3c961d1bbf2d081c78bc38ed1eacca840c577a2d01b36f05`
