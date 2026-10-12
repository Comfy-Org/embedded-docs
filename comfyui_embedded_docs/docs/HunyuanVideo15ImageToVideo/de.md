# HunyuanVideo15ImageToVideo

Der Node HunyuanVideo15ImageToVideo bereitet Konditionierungs- und Latent-Raum-Daten für die Videogenerierung auf Basis des HunyuanVideo 1.5-Modells vor. Er erstellt eine anfängliche latente Repräsentation für eine Videosequenz und kann optional ein Startbild oder eine CLIP-Vision-Ausgabe integrieren, um den Generierungsprozess zu steuern.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `positive` | Die positiven Konditionierungs-Prompts, die beschreiben, was das Video enthalten soll. | CONDITIONING | Ja | - |
| `negative` | Die negativen Konditionierungs-Prompts, die beschreiben, was das Video vermeiden soll. | CONDITIONING | Ja | - |
| `vae` | Das VAE-Modell (Variational Autoencoder), das verwendet wird, um das Startbild in den latenten Raum zu kodieren. | VAE | Ja | - |
| `width` | Die Breite der Ausgabe-Videoframes in Pixeln. Muss durch 16 teilbar sein. (Standard: 848) | INT | Ja | 16 bis MAX_RESOLUTION, Schritt: 16 |
| `height` | Die Höhe der Ausgabe-Videoframes in Pixeln. Muss durch 16 teilbar sein. (Standard: 480) | INT | Ja | 16 bis MAX_RESOLUTION, Schritt: 16 |
| `length` | Die Gesamtzahl der Frames in der Videosequenz. Die Werte erhöhen sich in Schritten von 4, beginnend bei 1 (1, 5, 9, 13, ...). (Standard: 33) | INT | Ja | 1 bis MAX_RESOLUTION, Schritt: 4 |
| `batch_size` | Die Anzahl der Videosequenzen, die in einem einzelnen Batch generiert werden sollen. (Standard: 1) | INT | Ja | 1 bis 4096 |
| `start_image` | Ein optionales Startbild zur Initialisierung der Videogenerierung. Falls angegeben, wird es kodiert und zur Konditionierung der ersten Frames verwendet. Es werden nur die ersten `length` Frames des Bildes verwendet. | IMAGE | Nein | - |
| `clip_vision_output` | Optionale CLIP-Vision-Einbettungen, um zusätzliche visuelle Konditionierung für die Generierung bereitzustellen. | CLIP_VISION_OUTPUT | Nein | - |

**Hinweis:** Wenn ein `start_image` angegeben wird, wird es automatisch unter Verwendung bilinearer Interpolation an die angegebene `width` und `height` angepasst. Die ersten `length` Frames des Bild-Batches werden verwendet, und nur die ersten 3 Farbkanäle jedes Frames werden kodiert. Das kodierte Bild wird dann sowohl zur `positive`- als auch zur `negative`-Konditionierung als `concat_latent_image` mit einer entsprechenden `concat_mask` hinzugefügt. Die Maske wird für die vom Startbild abgedeckten Frames auf 0.0 und für die verbleibenden Frames auf 1.0 gesetzt. Wenn ein `clip_vision_output` angegeben wird, wird es ebenfalls sowohl zur `positive`- als auch zur `negative`-Konditionierung hinzugefügt.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Die modifizierte positive Konditionierung, die nun das kodierte Startbild oder die CLIP-Vision-Ausgabe enthalten kann. | CONDITIONING |
| `negative` | Die modifizierte negative Konditionierung, die nun das kodierte Startbild oder die CLIP-Vision-Ausgabe enthalten kann. | CONDITIONING |
| `latent` | Ein leerer latenter Tensor mit Dimensionen, die für die angegebene Batchgröße, Videolänge, Breite und Höhe konfiguriert sind. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15ImageToVideo/de.md)

---
**Source fingerprint (SHA-256):** `dbedf7f378ae9613c8f47fe9876a4576c815055b4cdb6bf687b7575fcd7ea80a`
