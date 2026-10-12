# SAM3DBody_Render

Rendert 3D-Körperpose-Daten mit einem auswählbaren Stil in ein Bild. Der Node akzeptiert Pose-Daten vom SAM3D Body Tracker (MHR) oder von einem externen Y-up-Rig wie Kimodo und kann das Ergebnis über ein optionales Hintergrundbild (oder eine schwarze Leinwand, wenn keines bereitgestellt wird) komponieren. Verfügbare Render-Stile sind ein schattiertes 3D-Mesh, eine binäre Silhouette, 2D- und 3D-OpenPose-Skelette sowie Körperkapseln im SCAIL-Stil.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `render_style` | Render-Modus. 'mesh' = 3D-MHR-Mesh, durch die Kamera rasterisiert. 'silhouette' = binäre Maske des Meshes. 'openpose_2d' = flaches 2D-Skelett. 'openpose_3d' = OpenPose-Skelett als flach schattiertes 3D-Modell. 'scail' = SCAIL-3D-Kapseln. (Standard: "mesh") | DYNAMIC_COMBO | Ja | "mesh"<br>"silhouette"<br>"openpose_2d"<br>"openpose_3d"<br>"scail" |
| `pose_data` | MHR-Pose-Daten oder externe Y-up-Rig-Pose-Daten (KimodoSample). Alle Render-Stile funktionieren für externe Rigs, die OpenPose-Gelenkkarten in ihrem `_skeleton_override` enthalten (KimodoSample tut dies). | MHR_POSE_DATA oder KIMODO_POSE_DATA | Ja | — |
| `background` | Hintergrund pro Frame. Weggelassen = schwarze Leinwand. | IMAGE | Nein | — |
| `width` | Ausgabebreite in Pixeln. 0 = native image_size der Pose-Daten verwenden. Wenn nur einer der Werte width/height gesetzt ist, wird der andere unter Beibehaltung des ursprünglichen Seitenverhältnisses abgeleitet. (Standard: 0) | INT | Nein | 0 bis 16384, Schritt 8 |
| `height` | Ausgabehöhe in Pixeln. 0 = native image_size der Pose-Daten verwenden. Wenn nur einer der Werte width/height gesetzt ist, wird der andere unter Beibehaltung des ursprünglichen Seitenverhältnisses abgeleitet. (Standard: 0) | INT | Nein | 0 bis 16384, Schritt 8 |
| `camera_info` | Freie 6DOF-Kameraüberschreibung. Wenn verdrahtet, wird die Pose durch diese Kamera neu projiziert (Position/Ziel/Zoom/Rotation/FoV) anstelle der vorhergesagten. | LOAD_3D_CAMERA | Nein | — |

### Mesh Eingaben

Diese Parameter erscheinen, wenn `render_style` "mesh" ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `shader` | Voreingestellter Shader. 'normals' = aktuelle Oberflächennormale im Kameraraum (OpenGL-Y+-Normalmap-Konvention: +X→R, +Y→G, +Z→B). 'rainbow' = Körper-Y-Jet im RealisDance-Stil; die Varianten 'rainbow_face_*' überschreiben Gesichts-Vertices mit Normal-/pro-Region-Farben; 'depth' = lineares Graustufenbild. (Standard: "default") | DYNAMIC_COMBO | Nein | "default"<br>"normals"<br>"rainbow"<br>"rainbow_face_normal"<br>"rainbow_face_semantic"<br>"depth" |
| `rainbow_tilt_z` | Dreht die Rainbow-Jet-Achse um Z (vorwärts). Unterscheidet links/rechts. Nur verfügbar, wenn `shader` auf "rainbow", "rainbow_face_normal" oder "rainbow_face_semantic" gesetzt ist. (Standard: -35.0) | FLOAT | Nein | -90.0 bis 90.0, Schritt 0.5 |
| `rainbow_tilt_x` | Dreht die Rainbow-Jet-Achse um X (rechts). Unterscheidet vorne/hinten. Nur verfügbar, wenn `shader` auf "rainbow", "rainbow_face_normal" oder "rainbow_face_semantic" gesetzt ist. (Standard: 0.0) | FLOAT | Nein | -90.0 bis 90.0, Schritt 0.5 |
| `opacity` | Mesh-Alpha über dem Hintergrundbild oder über Schwarz, wenn keines verbunden ist. (Standard: 1.0) | FLOAT | Nein | 0.0 bis 1.0, Schritt 0.01 |
| `person_palette_falloff` | Desaturierung pro Person in Richtung Weiß: Track k erhält eine Pastellmischung von (1 - falloff^k) (SCAIL 'weichere zweite Person'). 1.0 = aus. (Standard: 0.6) | FLOAT | Nein | 0.1 bis 1.0, Schritt 0.05 |
| `region` | 'hands_only' filtert Faces über die vorberechnete `hand_vert_mask` (LBS-Gewichtungen gegen kanonische Hand-KPs) — isoliert das Hand-Mesh zum Debuggen. Fällt auf das vollständige Mesh zurück, wenn die Maske fehlt. (Standard: "full_body") | COMBO | Nein | "full_body"<br>"hands_only" |

### Silhouette Eingaben

Wenn `render_style` "silhouette" ist, rendert der Node eine binäre Maske des 3D-Meshes. Dieser Modus hat keine zusätzlichen Parameter.

### OpenPose 2D Eingaben

Diese Parameter erscheinen, wenn `render_style` "openpose_2d" ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `marker_radius_px` | Radius der Körper-Keypoint-Punkte (px). (Standard: 4) | INT | Nein | 1 bis 32, Schritt 1 |
| `stick_width_px` | Halbe Breite der Ellipse für Körpergliedmaßen (px). DWPose-Standard = 4. (Standard: 4) | INT | Nein | 1 bis 32, Schritt 1 |
| `limb_alpha` | Alpha pro Gliedmaße. DWPose-Standard = 0.6. (Standard: 0.6) | FLOAT | Nein | 0.0 bis 1.0, Schritt 0.05 |
| `face_style` | 'full' = alle Gesichts-Landmarks (sapiens-238 falls vorhanden, sonst Rig-Fallback ~30). 'eyes_mouth' = Rig-Fallback-Teilmenge (~12 Punkte: nur Augen + äußere Lippen). 'disabled' = keine Gesichtspunkte. (Standard: "disabled") | COMBO | Nein | "disabled"<br>"full"<br>"eyes_mouth" |
| `hand_style` | Zeichnet 21+21 Hand-Keypoints + Sticks. 'disabled' = keine Hände. 'dwpose' = einfarbig blaue Punkte; 'openpose' = Regenbogen-Punkte. (Standard: "disabled") | COMBO | Nein | "disabled"<br>"dwpose"<br>"openpose" |
| `person_palette_falloff` | Desaturierung pro Person: Track k mischt sich um 1 - falloff^k in Richtung Weiß. Track 0 bleibt kräftig; 1.0 deaktiviert den Falloff. (Standard: 0.6) | FLOAT | Nein | 0.1 bis 1.0, Schritt 0.05 |

### OpenPose 3D Eingaben

Diese Parameter erscheinen, wenn `render_style` "openpose_3d" ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `radius_m` | Radius der Gliedmaßenkapsel in Metern (dünn = stickartig). (Standard: 0.015) | FLOAT | Nein | 0.004 bis 0.1, Schritt 0.001 |
| `include_hands` | Zeichnet 21+21 Hand-Keypoints als 3D-Kapseln. (Standard: True) | BOOLEAN | Nein | True oder False |
| `person_palette_falloff` | Desaturierung pro Person: Track k mischt sich um 1 - falloff^k in Richtung Weiß. Track 0 bleibt kräftig; 1.0 deaktiviert den Falloff. (Standard: 0.6) | FLOAT | Nein | 0.1 bis 1.0, Schritt 0.05 |

### SCAIL Eingaben

Diese Parameter erscheinen, wenn `render_style` "scail" ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `radius_m` | Kapselradius in Metern (SCAIL-Referenz: ~0.022 m). (Standard: 0.022) | FLOAT | Nein | 0.005 bis 0.2, Schritt 0.001 |
| `hand_style` | Komponiert 2D-OpenPose-Hände über den 3D-Kapselkörper (entspricht SCAIL — keine 3D-Handkapseln). 'disabled' = keine Hände. 'dwpose' = einfarbig blaue Handpunkte; 'openpose' = Regenbogen-Punkte. Sticks bleiben in beiden Fällen pro Finger regenbogenfarben. (Standard: "dwpose") | COMBO | Nein | "disabled"<br>"dwpose"<br>"openpose" |
| `face_style` | 'full' = alle Gesichts-Landmarks (sapiens-238 falls vorhanden, sonst Rig-Fallback ~30). 'eyes_mouth' = Rig-Fallback-Teilmenge (~12 Punkte: nur Augen + äußere Lippen). 'disabled' = keine Gesichtspunkte. (Standard: "disabled") | COMBO | Nein | "disabled"<br>"full"<br>"eyes_mouth" |
| `person_palette_falloff` | Desaturierung pro Person: Track k mischt sich um 1 - falloff^k in Richtung Weiß. Track 0 bleibt kräftig; 1.0 deaktiviert den Falloff. (Standard: 0.6) | FLOAT | Nein | 0.1 bis 1.0, Schritt 0.05 |

### Hinweise

- Wenn sowohl `width` als auch `height` 0 sind, verwendet die Ausgabe die native Bildgröße der Pose-Daten. Wenn nur einer der beiden gesetzt ist, wird der andere unter Beibehaltung des ursprünglichen Seitenverhältnisses abgeleitet. Ein verbundener `background` wird auf die Render-Auflösung skaliert.
- Wenn `camera_info` verbunden ist, wird die Pose durch diese Kamera statt durch die vorhergesagte neu projiziert.
- Im Mesh-Modus sind `rainbow_tilt_z` und `rainbow_tilt_x` nur verfügbar, wenn `shader` auf "rainbow", "rainbow_face_normal" oder "rainbow_face_semantic" gesetzt ist.
- Im Mesh-Modus, wenn `region` "hands_only" ist, erfordert der Handbereichsfilter, dass die Pose-Daten eine Hand-Vertex-Maske enthalten; wenn die Maske fehlt, wird stattdessen das vollständige Mesh gerendert.
- Im SCAIL-Modus werden Hände als 2D-OpenPose-Overlays über dem 3D-Kapselkörper statt als 3D-Kapseln gezeichnet; wenn `hand_style` auf "disabled" gesetzt ist, werden sie vollständig entfernt.
- Wenn die Ausgabeauflösung von der nativen Auflösung der Pose-Daten abweicht, werden die Marker- und Stick-Größen von openpose_2d proportional skaliert.
- Wenn der Hintergrund weniger Frames als die Pose-Daten hat, wird der letzte Hintergrund-Frame für die verbleibenden Frames wiederverwendet.
- Die Ausgabe enthält einen Frame pro Eingabe-Pose-Frame. Wenn die Pose-Daten keine Frames enthalten, wird ein einzelnes schwarzes Bild zurückgegeben.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Die gerenderten Frames: die Pose-Daten, gezeichnet im ausgewählten Render-Stil, über den Hintergrund komponiert, wenn einer verbunden ist, andernfalls über Schwarz. Ein Frame pro Eingabe-Pose-Frame, zurückgegeben als einzelnes gebatchtes Bild. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_Render/de.md)

---
**Source fingerprint (SHA-256):** `96556283cf07727e6b4bb3549537bf925ed771bab8607f65c93ab54a5f0e9ba5`
