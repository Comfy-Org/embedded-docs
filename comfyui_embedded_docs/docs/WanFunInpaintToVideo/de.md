# WanFunInpaintToVideo

Der WanFunInpaintToVideo-Node bereitet Conditioning- und Latent-Daten für die Video-Generierung im Inpainting-Stil vor, wobei ein optionales Startbild und Endbild verwendet werden, um das Ergebnis zu steuern. Er funktioniert, indem er die bereitgestellten Conditioning-, VAE- und Bildframes durch dieselbe Logik leitet, die für die Video-Generierung mit erstem und letztem Frame verwendet wird, und gibt aktualisiertes Conditioning plus ein leeres Latent für das Sampling zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `positive` | Positive Conditioning-Prompts für die Video-Generierung | CONDITIONING | Ja | - |
| `negative` | Negative Conditioning-Prompts, die bei der Video-Generierung vermieden werden sollen | CONDITIONING | Ja | - |
| `vae` | VAE-Modell, das zum Kodieren und Dekodieren der Videoframes verwendet wird | VAE | Ja | - |
| `width` | Ausgabevideobreite in Pixeln (Standard: 832, Schritt: 16) | INT | Ja | 16 bis MAX_RESOLUTION |
| `height` | Ausgabevideohöhe in Pixeln (Standard: 480, Schritt: 16) | INT | Ja | 16 bis MAX_RESOLUTION |
| `length` | Anzahl der Frames in der Videosequenz (Standard: 81, Schritt: 4) | INT | Ja | 1 bis MAX_RESOLUTION |
| `batch_size` | Anzahl der Videos, die in einem Batch generiert werden (Standard: 1) | INT | Ja | 1 bis 4096 |
| `clip_vision_output` | Optionale CLIP-Vision-Ausgabe, die als Conditioning für das Startbild verwendet wird | CLIP_VISION_OUTPUT | Nein | - |
| `start_image` | Optionales Startbild (Frame) für die Video-Generierung | IMAGE | Nein | - |
| `end_image` | Optionales Endbild (Frame) für die Video-Generierung | IMAGE | Nein | - |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Verarbeitete positive Conditioning-Ausgabe | CONDITIONING |
| `negative` | Verarbeitete negative Conditioning-Ausgabe | CONDITIONING |
| `latent` | Generierte Latent-Repräsentation des Videos | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunInpaintToVideo/de.md)

---
**Source fingerprint (SHA-256):** `70b58e961c5df12f94183245ce320197439b2505b47d0bb3ff643b25c9fe6175`
