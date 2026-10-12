# WanInfiniteTalkToVideo

WanInfiniteTalkToVideo generiert Videosequenzen aus einer Audio-Eingabe. Es verwendet ein Videodiffusionsmodell, das auf Audio-Merkmale konditioniert ist, die aus einem oder zwei Sprechern extrahiert wurden, um eine latente Repräsentation eines Talking-Head-Videos zu erzeugen. Der Node kann eine neue Sequenz generieren oder eine bestehende erweitern, wobei vorherige Frames als Bewegungskontext verwendet werden.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `mode` | Der Audio-Eingabemodus. `single_speaker` verwendet eine Audio-Eingabe. `two_speakers` aktiviert die zusätzliche Audio-Eingabe und die im Abschnitt „Eingaben für zwei Sprecher“ aufgeführten Masken. | DYNAMIC_COMBO | Ja | `"single_speaker"`<br>`"two_speakers"` |
| `model` | Das Basis-Videodiffusionsmodell. | MODEL | Ja | - |
| `model_patch` | Der Modell-Patch, der Audio-Projektionsschichten enthält. | MODEL_PATCH | Ja | - |
| `positive` | Die positive Konditionierung zur Steuerung der Generierung. | CONDITIONING | Ja | - |
| `negative` | Die negative Konditionierung zur Steuerung der Generierung. | CONDITIONING | Ja | - |
| `vae` | Die VAE, die zum Kodieren von Bildern in den und aus dem latenten Raum verwendet wird. | VAE | Ja | - |
| `width` | Die Breite des Ausgabevideos in Pixeln. Muss durch 16 teilbar sein. (Standard: 832) | INT | Ja | 16 - MAX_RESOLUTION (step 16) |
| `height` | Die Höhe des Ausgabevideos in Pixeln. Muss durch 16 teilbar sein. (Standard: 480) | INT | Ja | 16 - MAX_RESOLUTION (step 16) |
| `length` | Die Anzahl der zu generierenden Frames. (Standard: 81) | INT | Ja | 1 - MAX_RESOLUTION (step 4) |
| `clip_vision_output` | Optionale CLIP-Vision-Ausgabe für zusätzliche Konditionierung. | CLIP_VISION_OUTPUT | Nein | - |
| `start_image` | Optionales Startbild zum Initialisieren der Videosequenz. | IMAGE | Nein | - |
| `audio_encoder_output_1` | Die primäre Audio-Encoder-Ausgabe, die Merkmale für den ersten Sprecher enthält. | AUDIO_ENCODER_OUTPUT | Ja | - |
| `motion_frame_count` | Anzahl der vorherigen Frames, die als Bewegungskontext verwendet werden. (Standard: 9; erweiterter Parameter) | INT | Ja | 1 - 33 (step 1) |
| `audio_scale` | Ein Skalierungsfaktor, der auf die Audio-Konditionierung angewendet wird. (Standard: 1.0) | FLOAT | Ja | -10.0 - 10.0 (step 0.01) |
| `previous_frames` | Optionale vorherige Video-Frames, von denen aus erweitert wird. Die letzten `motion_frame_count` Frames werden als Bewegungskontext verwendet. | IMAGE | Nein | - |

### Eingaben für zwei Sprecher

Die Eingaben in diesem Abschnitt werden angezeigt, wenn `mode` auf `"two_speakers"` gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `audio_encoder_output_2` | Die zweite Audio-Encoder-Ausgabe, die Merkmale für den zweiten Sprecher enthält. | AUDIO_ENCODER_OUTPUT | Nein | - |
| `mask_1` | Maske für den ersten Sprecher, erforderlich bei Verwendung von zwei Audio-Eingaben. | MASK | Nein | - |
| `mask_2` | Maske für den zweiten Sprecher, erforderlich bei Verwendung von zwei Audio-Eingaben. | MASK | Nein | - |

**Parametereinschränkungen:**

- Wenn `mode` auf `"two_speakers"` gesetzt ist, sind `audio_encoder_output_2`, `mask_1` und `mask_2` für die Einrichtung mit zwei Sprechern erforderlich.
- Wenn `audio_encoder_output_2` bereitgestellt wird, müssen auch sowohl `mask_1` als auch `mask_2` bereitgestellt werden.
- Wenn sowohl `mask_1` als auch `mask_2` bereitgestellt werden, muss auch `audio_encoder_output_2` bereitgestellt werden.
- Wenn `previous_frames` bereitgestellt wird, muss es mindestens so viele Frames enthalten, wie durch `motion_frame_count` angegeben.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `model` | Das gepatchte Modell mit angewendeter Audio-Konditionierung. | MODEL |
| `positive` | Die positive Konditionierung, möglicherweise mit zusätzlichem Kontext wie einem Startbild oder einer CLIP-Vision-Ausgabe modifiziert. | CONDITIONING |
| `negative` | Die negative Konditionierung, möglicherweise mit zusätzlichem Kontext modifiziert. | CONDITIONING |
| `latent` | Die generierte Videosequenz im latenten Raum. | LATENT |
| `trim_image` | Die Anzahl der Frames vom Beginn des Bewegungskontexts, die beim Erweitern einer Sequenz abgeschnitten werden sollten. Entspricht `motion_frame_count`, wenn `previous_frames` bereitgestellt wird, andernfalls 0. | INT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanInfiniteTalkToVideo/de.md)

---
**Source fingerprint (SHA-256):** `b7359490c1de86d9c82122bc227295b3b7f8a3493f629365ae0f22f9f34d9a66`
