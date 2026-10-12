# WanAnimateToVideo

WanAnimateToVideo bereitet Conditioning-Daten und ein initiales Latent für die Generierung animierter Videos mit Wan vor, wobei Eingaben wie ein Referenzbild, Pose, Gesicht, Hintergrund und optionale Bewegung aus einem vorherigen Chunk verwendet werden. Es unterstützt außerdem die Generierung längerer Videos in Chunks, indem ein `video_frame_offset`-Wert gelesen und aktualisiert wird. Dieser Node ist als experimentell gekennzeichnet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `positive` | Positives Conditioning, um die Generierung in Richtung gewünschter Inhalte zu steuern. | CONDITIONING | Ja | - |
| `negative` | Negatives Conditioning, um die Generierung von unerwünschten Inhalten wegzulenken. | CONDITIONING | Ja | - |
| `vae` | VAE-Modell, das zum Codieren von Bild- und Videoeingaben in den latenten Raum verwendet wird. | VAE | Ja | - |
| `width` | Breite des generierten Videos in Pixeln (Standard: 832, Schritt: 16). | INT | Ja | 16 bis MAX_RESOLUTION |
| `height` | Höhe des generierten Videos in Pixeln (Standard: 480, Schritt: 16). | INT | Ja | 16 bis MAX_RESOLUTION |
| `length` | Anzahl der zu generierenden Frames (Standard: 77, Schritt: 4). | INT | Ja | 1 bis MAX_RESOLUTION |
| `batch_size` | Anzahl der Videos, die in einem Batch generiert werden (Standard: 1). | INT | Ja | 1 bis 4096 |
| `clip_vision_output` | Optionale CLIP-Vision-Ausgabe, die sowohl zum positiven als auch zum negativen Conditioning hinzugefügt wird. | CLIP_VISION_OUTPUT | Nein | - |
| `reference_image` | Referenzbild, das als Ausgangspunkt für das Erscheinungsbild des generierten Videos verwendet wird. Wenn nicht angegeben, wird ein schwarzes Bild verwendet. | IMAGE | Nein | - |
| `face_video` | Videoeingabe, die Vorgaben für Gesichtsausdrücke liefert. Sie wird intern auf 512x512 angepasst und auf den Bereich -1.0 bis 1.0 skaliert. | IMAGE | Nein | - |
| `pose_video` | Videoeingabe, die Pose- und Bewegungsvorgaben liefert. | IMAGE | Nein | - |
| `continue_motion_max_frames` | Maximale Anzahl von Frames, die aus einer vorherigen Bewegungssequenz übernommen werden (Standard: 5, Schritt: 4). | INT | Ja | 1 bis MAX_RESOLUTION |
| `background_video` | Hintergrundvideo, das verwendet wird, um die Nicht-Charakter-Bereiche der Frames zu füllen. | IMAGE | Nein | - |
| `character_mask` | Maske, die Charakterbereiche definiert und verwendet wird, um den Charakter vom Hintergrund zu trennen. | MASK | Nein | - |
| `continue_motion` | Vorherige Bewegungs-Frames, von denen fortgesetzt wird, um die zeitliche Konsistenz mit früher generierten Chunks zu wahren. | IMAGE | Nein | - |
| `video_frame_offset` | Die Anzahl der Frames, um die in allen Eingabevideos vorgespult wird. Wird verwendet, um längere Videos chunkweise zu generieren. Verbinden Sie mit der `video_frame_offset`-Ausgabe des vorherigen Nodes, um ein Video zu verlängern. (Standard: 0, Schritt: 1) | INT | Ja | 0 bis MAX_RESOLUTION |

**Parametereinschränkungen:**

- Wenn `continue_motion` angegeben wird, werden nur dessen letzte `continue_motion_max_frames` Frames verwendet.
- Eingabevideos (`face_video`, `pose_video`, `background_video`, `character_mask`) werden vor der Verwendung um `video_frame_offset` versetzt. Wenn der Offset größer oder gleich der Frame-Anzahl der Eingabe ist, wird diese Eingabe ignoriert, außer bei einer `character_mask` mit nur einem Frame.
- Wenn `character_mask` nur einen Frame hat, wird dieser Frame für jeden Frame der Ausgabe wiederholt.
- Wenn `pose_video` kürzer als `length` ist, wird sein letzter Frame wiederholt, um die verbleibenden Frames zu füllen; die Ausgabelänge wird nicht geändert.
- Wenn `clip_vision_output` angegeben wird, wird es sowohl zum positiven als auch zum negativen Conditioning hinzugefügt.
- Wenn `reference_image` nicht angegeben wird, wird ein schwarzes Bild (alle Werte null) als Standardreferenz verwendet.
- Wenn `continue_motion` nicht angegeben wird, werden die anfänglichen Bewegungs-Frames mit konstant grauen Frames (Intensität 0,5) gefüllt.
- Wenn `continue_motion` verwendet wird, wird `video_frame_offset` um die Anzahl der übernommenen Frames reduziert, bevor der nächste Chunk-Offset berechnet wird, damit überlappende Frames nicht zweimal verarbeitet werden.
- `background_video` füllt die Bewegungs-Frames nach dem Referenz-Bewegungsabschnitt; es ersetzt weder das Referenzbild noch die übernommenen `continue_motion`-Frames.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `positive` | Modifiziertes positives Conditioning mit zusätzlichem Videokontext, einschließlich CLIP-Vision-Ausgabe, Pose-Video-Latent, Gesichtsvideo-Pixeln, konkateniertem latenten Bild und konkatenierter Maske. | CONDITIONING |
| `negative` | Modifiziertes negatives Conditioning mit zusätzlichem Videokontext, einschließlich CLIP-Vision-Ausgabe, Pose-Video-Latent, leeren Gesichtspixeln, konkateniertem latenten Bild und konkatenierter Maske. | CONDITIONING |
| `latent` | Initialer Latent-Tensor (alle Samples null) für das generierte Video mit der Form `[batch_size, 16, latent_length + trim_latent, latent_height, latent_width]`. | LATENT |
| `trim_latent` | Anzahl der latenten Frames, die vom Anfang des Latents abgeschnitten werden, entsprechend den Referenzbild-Frames. | INT |
| `trim_image` | Anzahl der Bild-Frames, die vom Anfang abgeschnitten werden, entsprechend den Referenz-Bewegungs-Frames. | INT |
| `video_frame_offset` | Aktualisierter Frame-Offset, der für den nächsten Chunk verwendet werden soll, basierend auf dem Eingabe-Offset und der Anzahl der verarbeiteten Frames. | INT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimateToVideo/de.md)

---
**Source fingerprint (SHA-256):** `a95bae4c7ae4ddc8a95bc9dafa2ca920b1d2166802615189537dce16949bfc03`
