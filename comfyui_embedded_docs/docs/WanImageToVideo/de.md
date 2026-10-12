# WanImageToVideo

Der WanImageToVideo-Node bereitet Conditioning- und Latent-Repräsentationen für die Videogenerierung vor. Er erstellt einen leeren latenten Raum für das Video und kann optional ein Startbild und eine CLIP-Vision-Ausgabe einbeziehen, um die Generierung zu steuern. Sowohl die positiven als auch die negativen Conditioning-Eingaben werden mit den bereitgestellten Bild- und Vision-Daten aktualisiert.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `positive` | Positive Conditioning-Eingabe, die zur Steuerung der Generierung verwendet wird | CONDITIONING | Ja | - |
| `negative` | Negative Conditioning-Eingabe, die zur Steuerung der Generierung verwendet wird | CONDITIONING | Ja | - |
| `vae` | VAE-Modell, das verwendet wird, um Bilder in den latenten Raum zu kodieren | VAE | Ja | - |
| `width` | Breite des generierten Videos (Standard: 832, Schritt: 16) | INT | Ja | 16 bis MAX_RESOLUTION |
| `height` | Höhe des generierten Videos (Standard: 480, Schritt: 16) | INT | Ja | 16 bis MAX_RESOLUTION |
| `length` | Anzahl der Frames im Video (Standard: 81, Schritt: 4) | INT | Ja | 1 bis MAX_RESOLUTION |
| `batch_size` | Anzahl der Videos, die in einem Batch generiert werden (Standard: 1) | INT | Ja | 1 bis 4096 |
| `clip_vision_output` | Optionale CLIP-Vision-Ausgabe, die als zusätzliches Conditioning zu den positiven und negativen Eingaben hinzugefügt wird | CLIP_VISION_OUTPUT | Nein | - |
| `start_image` | Optionales Startbild, das zum Initialisieren des Videos verwendet wird. Wenn angegeben, wird es auf die festgelegte `width` und `height` skaliert und an den Anfang der Frame-Sequenz gesetzt; alle Frames über `length` hinaus werden ignoriert. Die verbleibenden Frames werden mit neutralen Grauwerten (0,5) gefüllt, sofern `ref_pad_image` nicht angegeben ist. | IMAGE | Nein | - |
| `ref_pad_image` | Optionales Referenzbild, dessen erster Frame das neutrale graue Padding der Frame-Sequenz ersetzt. Es wird auf die festgelegte `width` und `height` skaliert, und nur das erste Bild des Batches wird verwendet. Wirkt nur, wenn auch `start_image` angegeben ist. | IMAGE | Nein | - |

**Hinweis:** Wenn `start_image` angegeben ist, wird die Frame-Sequenz mit dem VAE kodiert und eine Maske auf das Conditioning angewendet. Die Maske wird für die Frames, die vom Startbild abgedeckt werden, auf 0 und für die verbleibenden Frames auf 1 gesetzt, sodass die Generierung vom bereitgestellten Bild aus fortgesetzt wird. Während der Kodierung werden nur die ersten drei Farbkanäle (RGB) des Bildes verwendet. Sowohl das positive als auch das negative Conditioning erhalten dasselbe verkettete latente Bild, die Maske und (falls angegeben) die CLIP-Vision-Ausgabe. Wenn `ref_pad_image` zusammen mit `start_image` angegeben wird, wird dessen erster Frame auf `width` und `height` skaliert und in die RGB-Kanäle der Padding-Frames geschrieben, bevor das Startbild darübergelegt wird, sodass das Padding das Referenzbild statt einer einfarbigen grauen Fläche enthält. Dies ist Anti-Drift-Padding im SVI-Stil, das von Modellen wie ID-V2V verwendet wird.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Positives Conditioning, aktualisiert mit den Bild- und Vision-Daten | CONDITIONING |
| `negative` | Negatives Conditioning, aktualisiert mit den Bild- und Vision-Daten | CONDITIONING |
| `latent` | Leerer latenter Tensor, bereit für die Videogenerierung, mit Form [batch_size, 16, ((length-1)//4)+1, height//8, width//8] | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideo/de.md)

---
**Source fingerprint (SHA-256):** `3000c1c816d2c123fc5bc46ea1f193c52c0f81a2f8c4a9110d8a4fa909185aea`
