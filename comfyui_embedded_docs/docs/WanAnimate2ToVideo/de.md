# WanAnimate2ToVideo

WanAnimate2ToVideo animiert eine Figur aus einem Referenzbild, indem Gesichtsausdrücke, Körperbewegungen und Handgesten aus einem separaten Pose-Video übertragen werden. Er erstellt die Conditioning-Daten und einen Start-Latent, den ein Videogenerierungs-Sampler verwendet, um die Animation zu erzeugen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `positive` | Das positive Conditioning für die Videogenerierung. | CONDITIONING | Ja | N/A |
| `negative` | Das negative Conditioning für die Videogenerierung. | CONDITIONING | Ja | N/A |
| `vae` | Der VAE, der zum Kodieren des Referenzbilds und der Videoframes in den Latent-Raum verwendet wird. | VAE | Ja | N/A |
| `width` | Breite des Ausgabevideos in Pixeln. (Standard: 832) | INT | Ja | 16 bis MAX_RESOLUTION (Schritt 16) |
| `height` | Höhe des Ausgabevideos in Pixeln. (Standard: 480) | INT | Ja | 16 bis MAX_RESOLUTION (Schritt 16) |
| `length` | Anzahl der zu generierenden Frames. (Standard: 81) | INT | Ja | 1 bis MAX_RESOLUTION (Schritt 4) |
| `batch_size` | Anzahl der gleichzeitig zu generierenden Videos. (Standard: 1) | INT | Ja | 1 bis 4096 |
| `reference_image` | Die zu animierende Figur. Wenn sie weggelassen wird, wird ein schwarzes Bild verwendet. | IMAGE | Nein | N/A |
| `pose_video` | Das Video, dessen Bewegung auf die Referenzfigur übertragen wird. Wenn es weniger Frames als `length` hat, wird der letzte Frame wiederholt, um die fehlenden Frames aufzufüllen. | IMAGE | Nein | N/A |
| `clip_vision_output` | CLIP-Vision des Referenzbilds. | CLIP_VISION_OUTPUT | Nein | N/A |
| `positive_pose` | Prompt für den Pose-Video-Zweig, der die Bewegung statt der Figur beschreibt. Standardmäßig `positive`. Wird sowohl für den Cond- als auch für den Uncond-Durchlauf verwendet. | CONDITIONING | Nein | N/A |
| `clip_vision_output_pose` | CLIP-Vision des ersten Frames des Pose-Videos. Standardmäßig `clip_vision_output`. | CLIP_VISION_OUTPUT | Nein | N/A |
| `continue_motion` | Vorherige Bewegungssequenz, von der aus für zeitliche Konsistenz fortgesetzt wird. Nur der letzte Frame dieser Sequenz wird als Start-Bewegungsframe verwendet. | IMAGE | Nein | N/A |
| `video_frame_offset` | Frames, zu denen im Pose-Video vorgespult werden soll. Beim Erweitern mit dem `video_frame_offset`-Ausgang des vorherigen Nodes verbinden. (Standard: 0) | INT | Ja | 0 bis MAX_RESOLUTION |
| `pose_strength` | Skaliert den Einfluss des Pose-Videos auf die Bewegung. 1.0 ist das trainierte Verhalten; darunter wird die Befolgung abgeschwächt, darüber verstärkt. 0.0 dämpft ihn, entfernt ihn aber nicht vollständig. (Standard: 1.0) | FLOAT | Ja | 0.00 bis 10.00 (Schritt 0.01) |
| `pose_start_percent` | Sampling-Prozentsatz, bei dem der Pose-Einfluss beginnt. Außerhalb des Fensters wird der Pose-Zweig vollständig übersprungen, was diese Schritte zusätzlich beschleunigt. (Standard: 0.0) | FLOAT | Ja | 0.00 bis 1.00 (Schritt 0.01) |
| `pose_end_percent` | Sampling-Prozentsatz, bei dem der Pose-Einfluss endet. Die Bewegung wird größtenteils früh festgelegt, daher kann z. B. 0.7 feine Details lockern, während die Choreografie beibehalten wird. (Standard: 1.0) | FLOAT | Ja | 0.00 bis 1.00 (Schritt 0.01) |
| `reference_image_strength` | Skaliert, wie stark generierte Frames den Latent-Frame des Referenzbilds berücksichtigen. Unter 1.0 wird die Bindung an Identität/Erscheinungsbild gelockert (z. B. damit der Prompt das Erscheinungsbild neu gestalten kann), darüber wird sie gegen Drift gestrafft. (Standard: 1.0) | FLOAT | Ja | 0.00 bis 10.00 (Schritt 0.01) |

**Hinweise zur Validierung:**

- `pose_start_percent` darf nicht größer als `pose_end_percent` sein; andernfalls löst der Node einen ValueError aus.
- Wenn `pose_video` angegeben ist, muss seine Frame-Anzahl größer als `video_frame_offset` sein; andernfalls löst der Node einen ValueError aus.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `positive` | Positives Conditioning für das Sampling, mit angehängtem Referenzbild, Maske und optionalen Pose-Daten. | CONDITIONING |
| `negative` | Negatives Conditioning für das Sampling, mit demselben Referenzbild, derselben Maske und optionalen Pose-Daten. | CONDITIONING |
| `latent` | Mit Nullen gefüllter Start-Latent für den Video-Sampler; die ersten `trim_latent` Frames sollten vor der Dekodierung entfernt werden. | LATENT |
| `trim_latent` | Anzahl der Latent-Frames, die vor der Dekodierung entfernt werden sollten. | INT |
| `trim_image` | Anzahl der überlappenden Bild-Frames beim Erweitern eines Videos. | INT |
| `video_frame_offset` | Frames, zu denen im Pose-Video vorgespult werden soll; entspricht dem angepassten Eingabe-Offset plus der Anzahl der generierten Frames. | INT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimate2ToVideo/de.md)

---
**Source fingerprint (SHA-256):** `7e1f497983ab63a68e5ef5439b3ef4e9295f79f78530c9dc5de16a8238475f05`
