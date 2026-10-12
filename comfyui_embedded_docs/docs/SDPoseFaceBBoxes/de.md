# SDPose Gesichts-Begrenzungsrahmen

Der Node SDPoseFaceBBoxes verarbeitet Pose-Keypoint-Daten, um Bounding-Boxen um menschliche Gesichter zu erkennen und zu erzeugen. Er analysiert die 2D-Gesichts-Keypoints für jede Person in einem Frame, berechnet auf Basis dieser Punkte eine Bounding-Box und kann Größe und Form der Box anpassen. Die resultierenden Bounding-Boxen werden so formatiert, dass sie mit anderen Nodes im SDPose-Workflow kompatibel sind, z. B. mit dem SDPoseKeypointExtractor.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `keypoints` | Die Pose-Keypoint-Daten, die Informationen über erkannte Personen und deren Körper-/Gesichts-Landmarks pro Frame enthalten. | POSE_KEYPOINT | Ja | - |
| `scale` | Multiplikator für die Bounding-Box-Fläche um jedes erkannte Gesicht. Ein größerer Wert erzeugt eine größere Box. (Standard: 1.5) | FLOAT | Nein | 1.0 - 10.0 |
| `force_square` | Die kürzere BBox-Achse erweitern, sodass der Zuschneidebereich immer quadratisch ist. (Standard: True) | BOOLEAN | Nein | - |

**Hinweis:** Der Eingang `keypoints` muss im spezifischen Format vorliegen, das von Nodes wie SDPoseKeypointExtractor erzeugt wird, und `canvas_height`, `canvas_width` sowie `people`-Daten mit `face_keypoints_2d` für jede Person enthalten.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `bboxes` | Eine Liste von Gesichts-Bounding-Boxen für jedes Frame. Jede Bounding-Box wird durch ihre oberen linken Koordinaten (`x`, `y`), `width` und `height` definiert. Diese Ausgabe ist mit dem `bboxes`-Eingang des SDPoseKeypointExtractor-Nodes kompatibel. | BOUNDINGBOX |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseFaceBBoxes/de.md)

---
**Source fingerprint (SHA-256):** `dc68640f46afcba4c10a907fd9467671d508cd5bac7670b35a038d159f9d8f50`
