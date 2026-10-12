# WanDancerVideo

Der WanDancerVideo-Node bereitet Konditionierungsdaten und einen leeren latenten Tensor für die Videogenerierung mit dem WanDancer-Modell vor. Er hängt optionale Startbilder, Masken, CLIP-Vision-Einbettungen und Audio-Merkmale an die positive und negative Konditionierung an, damit sie das generierte Video steuern können.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `positive` | Die positive Konditionierung zur Steuerung der Videogenerierung. | CONDITIONING | Ja |  |
| `negative` | Die negative Konditionierung zur Steuerung der Videogenerierung. | CONDITIONING | Ja |  |
| `vae` | Das VAE, das zum Kodieren des Startbilds in den latenten Raum verwendet wird. | VAE | Ja |  |
| `width` | Die Breite des generierten Videos in Pixeln (Standard: 480). | INT | Ja | 16 bis MAX_RESOLUTION (Schritt: 16) |
| `height` | Die Höhe des generierten Videos in Pixeln (Standard: 832). | INT | Ja | 16 bis MAX_RESOLUTION (Schritt: 16) |
| `length` | Die Anzahl der Frames im generierten Video. Sollte für WanDancer 149 bleiben (Standard: 149). | INT | Ja | 1 bis MAX_RESOLUTION (Schritt: 4) |
| `clip_vision_output` | Die CLIP-Vision-Einbettungen für den ersten Frame. | CLIP_VISION_OUTPUT | Nein |  |
| `clip_vision_output_ref` | Die CLIP-Vision-Einbettungen für das Referenzbild. | CLIP_VISION_OUTPUT | Nein |  |
| `start_image` | Das/die Startbild(er), die kodiert werden sollen; kann eine beliebige Anzahl von Frames umfassen. | IMAGE | Nein |  |
| `mask` | Bildkonditionierungsmaske für das/die Startbild(er). Weiß bleibt erhalten, Schwarz wird generiert. Wird für lokale Generierungen verwendet. | MASK | Nein |  |
| `audio_encoder_output` | Eine Audio-Encoder-Ausgabe, die Audio-Merkmale, Framerate und Inject-Scale-Werte bereitstellt; diese werden, wenn die Ausgabe angegeben wird, an die Konditionierung angehängt. | AUDIO_ENCODER_OUTPUT | Nein |  |

### Hinweise zum Parameterverhalten

- `start_image` ist optional. Wenn angegeben, wird es auf `width` und `height` skaliert, vom `vae` kodiert und sowohl an die positive als auch an die negative Konditionierung angehängt. Wenn `start_image` mehr Frames als `length` enthält, werden die zusätzlichen Frames verworfen. Wenn es weniger Frames enthält, werden die fehlenden Frames mit Nullwerten aufgefüllt.
- `mask` wirkt sich nur aus, wenn auch `start_image` angegeben ist. Weiße Bereiche bleiben erhalten, schwarze Bereiche werden generiert.
- `clip_vision_output_ref` wirkt sich nur aus, wenn auch `clip_vision_output` angegeben ist.
- `audio_encoder_output` hängt, wenn angegeben, Audio-Einbettungen, Framerate und Injection-Scale sowohl an die positive als auch an die negative Konditionierung an.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Die positive Konditionierung mit allen angehängten Startbild-Latents, Masken, CLIP-Vision- oder Audiodaten. | CONDITIONING |
| `negative` | Die negative Konditionierung mit allen angehängten Startbild-Latents, Masken, CLIP-Vision- oder Audiodaten. | CONDITIONING |
| `latent` | Ein leerer latenter Tensor in der Größe für die angeforderte Videolänge, -höhe und -breite. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerVideo/de.md)

---
**Source fingerprint (SHA-256):** `086a0ec361cf7f7ae7ce9505b55d31d92b025c6c7c9cde192009e6664011ad05`
