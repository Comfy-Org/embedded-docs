# WanDancerEncodeAudio

Dieser Node analysiert einen Audio-Clip und wandelt ihn in eine Reihe von Features um, die ein videogenerierendes Modell steuern können. Er schätzt Tempo und Beats, extrahiert Mel-Spektrogramm-, MFCC-, Chroma- und Onset-Features und bündelt diese zusammen mit einer berechneten Bildrate zur Synchronisierung.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `audio` | Die zu analysierende und zu kodierende Audioeingabe. Wenn das Audio mehrere Kanäle hat, werden die Kanäle vor der Feature-Extraktion zu Mono gemittelt. | AUDIO | Ja | - |
| `video_frames` | Die Anzahl der Frames im Zielvideo. Wird verwendet, um die Bildrate zur Synchronisierung zu berechnen (Standard: 149). | INT | Ja | Min.: 1, Max.: 16384 (MAX_RESOLUTION), Schritt: 4 |
| `audio_inject_scale` | Die Skalierung für die Audio-Features, wenn diese in das Videomodell injiziert werden (Standard: 1.0). | FLOAT | Ja | Min.: 0.0, Max.: 10.0, Schritt: 0.01 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `audio_encoder_output` | Ein Dictionary, das die verarbeiteten Audio-Features, die berechnete Bildrate (fps) und die Audio-Injektionsskalierung enthält. Diese Ausgabe wird verwendet, um das videogenerierende Modell zu konditionieren. | AUDIO_ENCODER_OUTPUT |
| `fps_string` | Eine Textzeichenfolge, die die berechnete Bildrate (fps) basierend auf der Audiolänge und der Anzahl der Videoframes beschreibt. Diese Zeichenfolge ist dafür vorgesehen, im Prompt für das Videomodell verwendet zu werden. Sie ist auf Chinesisch formatiert, um zur Referenz-Pipeline zu passen. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerEncodeAudio/de.md)

---
**Source fingerprint (SHA-256):** `ce27a3bdea2d9e3cf8875c24236a2a0a1429e9bc13a58581e372fb669d2c0018`
