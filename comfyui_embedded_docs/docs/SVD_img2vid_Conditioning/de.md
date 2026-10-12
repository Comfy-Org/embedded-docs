# SVD_img2vid_Conditioning

Der Node SVD_img2vid_Conditioning bereitet Conditioning-Daten für die Videogenerierung mit Stable Video Diffusion vor. Er nimmt ein Ausgangsbild entgegen und verarbeitet es durch CLIP-Vision- und VAE-Encoder, um positive und negative Conditioning-Paare sowie einen leeren Latent-Raum für die Videogenerierung zu erzeugen. Dieser Node richtet die notwendigen Parameter für die Steuerung von Bewegung, Bildrate und Augmentierungsstufen im generierten Video ein.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `clip_vision` | CLIP-Vision-Modell zum Kodieren des Eingabebilds | CLIP_VISION | Ja | - |
| `init_image` | Ausgangsbild, das als Startpunkt für die Videogenerierung verwendet wird | IMAGE | Ja | - |
| `vae` | VAE-Modell zum Kodieren des Bilds in den Latent-Raum | VAE | Ja | - |
| `width` | Breite des Ausgabevideos (Standard: 1024, Schritt: 8) | INT | Ja | 16 bis MAX_RESOLUTION |
| `height` | Höhe des Ausgabevideos (Standard: 576, Schritt: 8) | INT | Ja | 16 bis MAX_RESOLUTION |
| `video_frames` | Anzahl der im Video zu generierenden Frames (Standard: 14) | INT | Ja | 1 bis 4096 |
| `motion_bucket_id` | Steuert den Umfang der Bewegung im generierten Video (Standard: 127) | INT | Ja | 1 bis 1023 |
| `fps` | Bilder pro Sekunde für das generierte Video (Standard: 6) | INT | Ja | 1 bis 1024 |
| `augmentation_level` | Grad der Rausch-Augmentierung, der auf das Eingabebild angewendet wird (Standard: 0.0, Schritt: 0.01) | FLOAT | Ja | 0.0 bis 10.0 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Positive Conditioning-Daten, die Bild-Embeddings und Videoparameter enthalten | CONDITIONING |
| `negative` | Negative Conditioning-Daten mit auf Null gesetzten Embeddings und Videoparametern | CONDITIONING |
| `latent` | Leerer Latent-Raum-Tensor, bereit für die Videogenerierung | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SVD_img2vid_Conditioning/de.md)

---
**Source fingerprint (SHA-256):** `33b295b6f2e459852aaa95d9dca26c724aa2e9ad0f884a1c7760766530a00a09`
