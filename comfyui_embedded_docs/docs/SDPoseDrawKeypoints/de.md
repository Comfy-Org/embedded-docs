# SDPoseDrawKeypoints

Der Node SDPoseDrawKeypoints nimmt Pose-Schätzungsdaten (Keypoints) entgegen und zeichnet sie als visuelles Skelett auf eine leere Zeichenfläche. Er ermöglicht es Ihnen, verschiedene Teile der Pose selektiv zu zeichnen, wie Körper, Kopf, Hände, Gesicht und Füße, mit anpassbaren Linienbreiten und Punktgrößen. Das resultierende Bild kann zur Visualisierung oder als Eingabe für andere Nodes verwendet werden, die ein Pose-Bild erfordern.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `keypoints` | Die zu zeichnenden Pose-Keypoint-Daten. Diese Daten stammen typischerweise von einem Pose-Erkennungs-Node und können ein oder mehrere Frames enthalten. | POSE_KEYPOINT | Ja | - |
| `draw_body` | Steuert, ob das Hauptkörperskelett gezeichnet wird (Standard: True). | BOOLEAN | Nein | - |
| `draw_hands` | Steuert, ob die Hand-Keypoints gezeichnet werden (Standard: True). | BOOLEAN | Nein | - |
| `draw_face` | Steuert, ob die Gesichts-Keypoints gezeichnet werden (Standard: True). | BOOLEAN | Nein | - |
| `draw_feet` | Steuert, ob die Fuß-Keypoints gezeichnet werden (Standard: False). | BOOLEAN | Nein | - |
| `stick_width` | Die Breite der Linien, die zum Zeichnen des Körper- und Kopfskeletts verwendet werden (Standard: 4). | INT | Nein | 1 bis 10 |
| `face_point_size` | Die Größe der Punkte, die zum Zeichnen der Gesichts-Keypoints verwendet werden (Standard: 3). | INT | Nein | 1 bis 10 |
| `score_threshold` | Der minimale Konfidenzwert, den ein Keypoint haben muss, um gezeichnet zu werden. Keypoints mit Werten unterhalb dieses Schwellenwerts werden ignoriert (Standard: 0.3). | FLOAT | Nein | 0.0 bis 1.0 |
| `draw_head` | Steuert, ob die Kopf-Keypoints (Nase, Augen, Ohren) gezeichnet werden (Standard: True). | BOOLEAN | Nein | - |

**Hinweis:** Wenn die Eingabe `keypoints` leer oder `None` ist, gibt der Node ein leeres 64x64-Bild aus.

**Hinweis:** `draw_body` und `draw_head` funktionieren unabhängig voneinander. Wenn `draw_head` deaktiviert ist, werden die Kopf-Keypoints nicht gezeichnet, selbst wenn `draw_body` aktiviert ist. Wenn `draw_body` deaktiviert ist, aber `draw_head` aktiviert ist, werden nur die Kopf-Keypoints und der Nackenpunkt gezeichnet. Wenn beide deaktiviert sind, werden keine Körper- oder Kopf-Keypoints gezeichnet.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Ein Bild mit den gezeichneten Pose-Keypoints. Die Bildabmessungen entsprechen der `canvas_height` und `canvas_width`, die in den Eingabe-Keypoint-Daten angegeben sind. Wenn die Eingabe mehrere Frames enthält, wird ein Batch von Bildern zurückgegeben. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseDrawKeypoints/de.md)

---
**Source fingerprint (SHA-256):** `2b2b9530b55c56e278666bd5d139bb6a1bb503b75b948a89266b9982b5a295e4`
