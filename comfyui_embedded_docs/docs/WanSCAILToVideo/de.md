# WanSCAILToVideo

Der Node WanSCAILToVideo bereitet die Konditionierung und einen leeren Latent-Raum für die Videogenerierung mit den SCAIL- und SCAIL-2-Videomodellen vor. Er verarbeitet optionale Eingaben wie Referenzbilder, Pose-Videos, CLIP-Vision-Ausgaben, farbige Identitätsmasken und vorherige Frame-Chunks und bettet sie in die positive und negative Konditionierung ein. Der Node gibt die geänderte Konditionierung und einen leeren Latent-Tensor mit den angegebenen Videoabmessungen aus, der zum Sampling bereit ist.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `positive` | Die positive Konditionierungseingabe. | CONDITIONING | Ja | - |
| `negative` | Die negative Konditionierungseingabe. | CONDITIONING | Ja | - |
| `vae` | Das VAE-Modell, das zum Kodieren von Bildern und Video-Frames verwendet wird. | VAE | Ja | - |
| `width` | Die Breite des Ausgabevideos in Pixeln (Standard: 512). Werte haben eine Schrittweite von 32. | INT | Ja | 32 bis MAX_RESOLUTION |
| `height` | Die Höhe des Ausgabevideos in Pixeln (Standard: 896). Werte haben eine Schrittweite von 32. | INT | Ja | 32 bis MAX_RESOLUTION |
| `length` | Die Anzahl der Frames im Video (Standard: 81). Werte haben eine Schrittweite von 4. | INT | Ja | 1 bis MAX_RESOLUTION |
| `batch_size` | Die Anzahl der Videos, die in einem Batch generiert werden (Standard: 1). | INT | Ja | 1 bis 4096 |
| `pose_video` | Video, das zur Pose-Konditionierung verwendet wird. Wird auf die halbe Auflösung des Hauptvideos herunterskaliert. | IMAGE | Nein | - |
| `pose_video_mask` | Nur SCAIL-2. Farbiges SAM3-Maskenvideo pro Identität mit derselben Auflösung wie `pose_video`. | IMAGE | Nein | - |
| `replacement_mode` | Nur SCAIL-2. False = Animationsmodus (`pose_video_mask` sollte schwarzen Hintergrund haben). True = Ersetzungsmodus (`pose_video_mask` sollte weißen Hintergrund haben). (Standard: False) | BOOLEAN | Nein | - |
| `pose_strength` | Stärke des Pose-Latents. (Standard: 1.0) | FLOAT | Ja | 0.0 bis 10.0 |
| `pose_start` | Startschritt der Pose-Konditionierung. (Standard: 0.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `pose_end` | Endschritt der Pose-Konditionierung. (Standard: 1.0) | FLOAT | Ja | 0.0 bis 1.0 |
| `reference_image` | Referenzbild. Das erste Bild ist die primäre Referenz (auf die alle Identitäten zusammengesetzt werden). SCAIL-2: Zusätzliche Batch-Bilder werden als zusätzliche Ansichten verwendet (Rückansicht, Nahaufnahme, verdeckter Hintergrund), wobei jedes eine passende `reference_image_mask` in der Farbe dieser Identität benötigt. | IMAGE | Nein | - |
| `reference_image_mask` | Nur SCAIL-2. Farbige Referenzmaske, Batch passend zu `reference_image` (erste = primäre Referenzmaske, Rest = Identitätsmasken für das zusätzliche `reference_image`). | IMAGE | Nein | - |
| `clip_vision_output` | CLIP-Vision-Merkmale zur Konditionierung. Das Modell ist mit Stretch-Resize auf das Seitenverhältnis trainiert. | CLIP_VISION_OUTPUT | Nein | - |
| `video_frame_offset` | Kumulatives Ausgabeframe, an dem dieser Chunk beginnt. Verbinden Sie es mit der `video_frame_offset`-Ausgabe des vorherigen Chunks. (Standard: 0) | INT | Ja | 0 bis MAX_RESOLUTION |
| `previous_frame_count` | Anzahl der Endframes von `previous_frames`, die verankert werden. SCAIL-2 wurde mit 5 trainiert (81-Frame-Chunks, 76-Frame-Schritt). (Standard: 5). Werte haben eine Schrittweite von 4. | INT | Ja | 1 bis MAX_RESOLUTION |
| `previous_frames` | Nur SCAIL-2. Vollständig dekodierte Ausgabe des vorherigen Chunks. Nur die letzten `previous_frame_count` werden als Erweiterungsanker verwendet. | IMAGE | Nein | - |

**Hinweis:** Die Eingaben `pose_video` und `pose_video_mask` werden gemeinsam auf die kürzere der beiden gekürzt und nur für die ersten `length` Frames verarbeitet. Wenn eine der Eingaben kürzer oder gleich `video_frame_offset` ist, wird sie vollständig ignoriert. Das `pose_video` wird vor der Kodierung auf die halbe Auflösung des Hauptvideos herunterskaliert, und das kodierte Pose-Latent wird mit `pose_strength` multipliziert und nur zwischen den Zeitschritten `pose_start` und `pose_end` auf die Konditionierung angewendet. Wenn `pose_video_mask` angegeben ist, wird das farbige Maskenvideo auf halbe Auflösung herunterskaliert und in eine 28-Kanal-Driving-Maske umgewandelt, die sowohl zur positiven als auch zur negativen Konditionierung hinzugefügt wird.

**Hinweis:** Wenn `reference_image` angegeben ist, wird jedes Bild im Batch einzeln in ein Latent kodiert und sowohl in die positive als auch in die negative Konditionierung eingebettet. Das erste Bild ist die primäre Referenz; zusätzliche Bilder werden als zusätzliche Ansichten verwendet, wobei jedes eine passende `reference_image_mask` benötigt. `reference_image_mask` wird nur verwendet, wenn auch `reference_image` angegeben ist; wenn beide angegeben sind, wird außerdem eine 28-Kanal-Referenzmaske, die die Referenzframes an Identitäten bindet, aus den Masken erstellt und zur Konditionierung hinzugefügt. Im Ersetzungsmodus (`replacement_mode=True`) wird das Referenzbild unter Verwendung der Referenzbildmaske als Alpha-Matte auf einen schwarzen Hintergrund zusammengesetzt. Wenn `clip_vision_output` angegeben ist, wird es sowohl auf die positive als auch auf die negative Konditionierung angewendet.

**Hinweis:** Wenn `previous_frames` angegeben ist, werden nur die letzten `previous_frame_count` Frames als Erweiterungsanker verwendet, und `video_frame_offset` wird entsprechend angepasst (um die Anzahl der verankerten Frames reduziert, auf 0 begrenzt). Die verankerten Frames werden kodiert und in den Anfang des Ausgabe-Latents geschrieben, und eine Rauschmaske wird eingefügt, damit diese Frames während der Generierung unverändert bleiben.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `positive` | Die geänderte positive Konditionierung, die möglicherweise eingebettete Referenzbild-Latents, CLIP-Vision-Ausgabe, Pose-Video-Latents, Driving-Masken, Referenzmasken oder vorherige Frame-Latents enthält. | CONDITIONING |
| `negative` | Die geänderte negative Konditionierung, die möglicherweise eingebettete Referenzbild-Latents, CLIP-Vision-Ausgabe, Pose-Video-Latents, Driving-Masken, Referenzmasken oder vorherige Frame-Latents enthält. | CONDITIONING |
| `latent` | Ein leerer Latent-Tensor der Form `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]`. Wenn `previous_frames` angegeben ist, wird das Latent teilweise mit kodierten vorherigen Frames gefüllt und eine Rauschmaske wird eingefügt. | LATENT |
| `video_frame_offset` | Angepasster Offset + Länge. Für die sequenzielle Videogenerierung mit dem nächsten Chunk verbinden. | INT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSCAILToVideo/de.md)

---
**Source fingerprint (SHA-256):** `4a1a2201dfa94bd2f1330db02ec18a5e0a6aae9e9ac5ae97d456b7af1aa84b7b`
