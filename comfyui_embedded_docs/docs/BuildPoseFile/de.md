# BuildPoseFile

Dieser Node erstellt aus Pose-Daten eine speicherfertige 3D-Animationsdatei. Sie können eine animierte GLB in mehreren visuellen Stilen exportieren – ein vollständiges Körper-Mesh, eine Vorschau nur mit Gelenken, ein OpenPose-Skelett oder ein SCAIL-Kapsel-Rig – oder stattdessen einen BVH-Motion-Capture-Clip speichern. Die Ausgabe wird an einen dateispeichernden Node wie Save 3D Model angeschlossen, um die Datei auf die Festplatte zu schreiben.

## Eingaben

### Gemeinsame Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `pose_data` | 3D-Pose-Daten. Akzeptiert MHR-Pose-Daten (Modell-/Form-/Ausdrucksparameter, MHR70-Keypoints, kanonische Farben, Hand-Vertex-Maske) oder Kimodo-Pose-Daten (externes Y-up-Rig mit pro Frame vorhergesagten Vertizes und Kamera). | MHR_POSE_DATA / KIMODO_POSE_DATA | Ja | — |
| `format` | Ausgabeformat; beide werden an Save 3D Model übergeben, um auf die Festplatte geschrieben zu werden. 'glb' = animierte GLB (Mesh / Bones / OpenPose / SCAIL). 'bvh' = BVH-Mocap-Clip (ein Skelett; benötigt das Modell). (Standard: glb) | DYNAMIC_COMBO | Ja | "glb"<br>"bvh" |
| `sam3d_body_model` | Optionales SAM3D-Körpermodell. Erforderlich für die Formate 'bvh', 'body_mesh' und 'bones_only', es sei denn, die Pose-Daten enthalten eine Skelett-Überschreibung. | SAM3D_BODY_MODEL | Nein | — |
| `fps` | Animations-Framerate. (Standard: 24.0) | FLOAT | Ja | 1.0-240.0 |
| `camera_translation` | pred_cam_t in die Root-Translation einbacken: 'off' = Bind-Position; 'centered' = Delta von Frame 0; 'absolute' = roh (Z ist die Kameratiefe – üblicherweise mehrere Meter entfernt). (Standard: off) | COMBO | Ja | "off"<br>"centered"<br>"absolute" |
| `track_index` | Track-Auswahl: -1 = alle Tracks; ≥0 = einzelner Track. (Standard: -1) | INT | Ja | -1 bis 15 |

### GLB-Eingaben

Diese Eingaben erscheinen, wenn `format` auf "glb" gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `mesh_style` | Visueller Stil der GLB: 'body_mesh' = echte Armature (127 Knochen, Skinning, TRS-Keyframes, 72 Gesichts-Morphs; benötigt Modell). 'bones_only' = knochenförmige Primitive an jedem Gelenk (Vorschau-Armature). 'openpose' = OpenPose-18-3D-Skelett aus Keypoints. 'scail' = SCAIL-3D-Kapsel-Rig (offene Zylinder, deren offene Enden von Gelenkkugeln bündig verschlossen werden). (Standard: body_mesh) | DYNAMIC_COMBO | Ja | "body_mesh"<br>"bones_only"<br>"openpose"<br>"scail" |
| `bone_smooth_window` | Gaußsches Glättungsfenster für Rotation-Keyframes pro Knochen / Keypoint-Tracks. 0 = aus. 7-15 beruhigt Drehungen/Zittern, wo vorgeschaltetes Smooth Spitzen verpasst. (Standard: 0) | INT | Ja | 0-51, Schritt 2 |

#### Body-Mesh-Eingaben

Erscheinen, wenn `mesh_style` auf "body_mesh" gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `bone_vis` | Form der Knochenvisualisierung, starr an jedes Gelenk geskinnt. 'off' = keine Knochenvisualisierung; 'octahedrons' = direktionale Knochen im Blender-Stil. (Standard: off) | DYNAMIC_COMBO | Ja | "off"<br>"octahedrons" |
| `bone_vis_radius_m` | Erscheint, wenn `bone_vis` = "octahedrons". Radius in m (Kugelradius / halbe Oktaederbreite). (Standard: 0.02) | FLOAT | Ja | 0.005-0.5 |
| `bone_vis_color` | Erscheint, wenn `bone_vis` = "octahedrons". Vertex-Farben pro Knochen (unlit Material). 'white' = keine, 'rainbow_y' = Farbverlauf von Kopf bis Fuß. (Standard: rainbow_y) | COMBO | Ja | "white"<br>"rainbow_y" |
| `shader` | Vertex-Farben passend zu den Shadern des Render-Nodes backen (COLOR_0 + KHR_materials_unlit). 'default' = keine Farben. (Standard: default) | DYNAMIC_COMBO | Ja | "default"<br>"rainbow"<br>"rainbow_face_normal"<br>"rainbow_face_semantic" |
| `rainbow_tilt_z` | Erscheint, wenn `shader` eine Rainbow-Variante ist. Dreht die Achse des Rainbow-Verlaufs um Z (vorwärts). Unterscheidet links/rechts. (Standard: -35.0) | FLOAT | Ja | -90.0 bis 90.0 |
| `rainbow_tilt_x` | Erscheint, wenn `shader` eine Rainbow-Variante ist. Dreht die Achse des Rainbow-Verlaufs um X (rechts). Unterscheidet vorne/hinten. (Standard: 0.0) | FLOAT | Ja | -90.0 bis 90.0 |
| `person_palette_falloff` | Erscheint, wenn `shader` eine Rainbow-Variante ist. Entsättigung pro Person: Jeder Track erhält einen Pastell-Mix aus (1 - falloff^k). (Standard: 0.6) | FLOAT | Ja | 0.1-1.0 |

#### Bones-Only-Eingaben

Erscheinen, wenn `mesh_style` auf "bones_only" gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `bone_vis` | Form der Knochenvisualisierung, starr an jedes Gelenk geskinnt. 'octahedrons' = direktionale Knochen im Blender-Stil (Gelenk → primäres Kind). | DYNAMIC_COMBO | Ja | "octahedrons" |
| `bone_vis_radius_m` | Radius in m (Kugelradius / halbe Oktaederbreite). (Standard: 0.02) | FLOAT | Ja | 0.005-0.5 |
| `bone_vis_color` | Vertex-Farben pro Knochen (unlit Material). 'white' = keine, 'rainbow_y' = Farbverlauf von Kopf bis Fuß. (Standard: rainbow_y) | COMBO | Ja | "white"<br>"rainbow_y" |

#### OpenPose-Eingaben

Erscheinen, wenn `mesh_style` auf "openpose" gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `marker_radius_m` | Kugelradius in m. (Standard: 0.010) | FLOAT | Ja | 0.005-0.1 |
| `stick_radius_m` | Halbe Gliedmaßenbreite in m. Automatisch auf bone_length x 0.1 begrenzt. (Standard: 0.008) | FLOAT | Ja | 0.002-0.05 |
| `include_hands` | 21+21 OpenPose-Hände anhängen (Handgelenk + 5 Finger x 4 Gelenke, Basis→Spitze) aus pred_keypoints_3d. (Standard: False) | BOOLEAN | Ja | True / False |
| `hand_marker_radius_m` | Kugelradius der Hand in m. (Standard: 0.005) | FLOAT | Ja | 0.001-0.1 |
| `hand_stick_radius_m` | Halbe Gliedmaßenbreite der Hand in m. (Standard: 0.003) | FLOAT | Ja | 0.001-0.05 |
| `face_style` | Gesichtskontur-Landmarks, die aus pred_vertices an festen Vertex-IDs des Kopf-Meshes abgetastet werden (benötigt canonical_colors in pose_data). 'full' = alle ~30 Punkte; 'eyes_mouth' = nur Augen + äußere Lippen. (Standard: disabled) | COMBO | Ja | "disabled"<br>"full"<br>"eyes_mouth" |
| `face_marker_radius_m` | Radius der Gesichtspunkte. 0 = auto = 0.3 x marker_radius_m. (Standard: 0.0) | FLOAT | Ja | 0.0-0.05 |

#### SCAIL-Eingaben

Erscheinen, wenn `mesh_style` auf "scail" gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `stick_radius_m` | Zylinderradius in m. Knochen sind offene Zylinder mit konstantem Radius; Gelenkkugeln (automatisch passend dimensioniert) verschließen die offenen Enden. SCAIL-Referenz = 0.0215 m. (Standard: 0.022) | FLOAT | Ja | 0.002-0.1 |
| `marker_radius_m` | Radius der Gelenkkugel. 0 = auto = stick_radius_m (bündiger Abschluss). (Standard: 0.0) | FLOAT | Ja | 0.0-0.1 |
| `material_roughness` | PBR-Rauheit. SCAIL-Referenz = 0.3. 1 = matt; 0 = Chrom. (Standard: 0.3) | FLOAT | Ja | 0.0-1.0 |
| `include_hands` | 21+21 Hand-Keypoints + Kapsel-Sticks pro Track anhängen. (Standard: False) | BOOLEAN | Ja | True / False |
| `hand_marker_radius_m` | Kugelradius der Hand in m. (Standard: 0.005) | FLOAT | Ja | 0.001-0.05 |
| `hand_stick_radius_m` | Zylinderradius der Hand in m. (Standard: 0.003) | FLOAT | Ja | 0.001-0.05 |
| `face_style` | Gesichtskontur-Landmarks, die aus pred_vertices abgetastet werden (benötigt canonical_colors in pose_data). 'full' = alle ~30 Punkte; 'eyes_mouth' = nur Augen + äußere Lippen. (Standard: disabled) | COMBO | Ja | "disabled"<br>"full"<br>"eyes_mouth" |

### BVH-Eingaben

Erscheinen, wenn `format` auf "bvh" gesetzt ist.

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `units` | BVH-OFFSET/Positionseinheiten. 'cm' ist der Mocap-Standard. (Standard: cm) | COMBO | Ja | "cm"<br>"m" |

**Hinweise:**

- Das `bvh`-Format sowie die Mesh-Stile `body_mesh` und `bones_only` erfordern den Eingang `sam3d_body_model`, es sei denn, die `pose_data` selbst enthält eine Skelett-Überschreibung (ein `_skeleton_override`-Dict, beispielsweise von einem KimodoSample-Node). Der Node löst einen Fehler aus, wenn keines von beiden verfügbar ist. Die Stile `openpose` und `scail` sind rig-unabhängig und arbeiten direkt mit Keypoints ohne das Körpermodell.
- Im `bvh`-Format enthält die Ausgabe ein einzelnes Skelett. Wenn `track_index` -1 ist (alle Tracks), wird der erste Track verwendet.
- Die Optionen `full` und `eyes_mouth` für `face_style` erfordern `canonical_colors` in den Pose-Daten; diese sind vorhanden, wenn die Pose-Daten zusammen mit dem Körpermodell aus der MHR-Pipeline stammen.
- `bone_smooth_window` wird in Schritten von 2 zwischen 0 und 51 erhöht.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model_3d` | Die generierte Animationsdatei: eine animierte GLB oder ein BVH-Mocap-Clip, bereit, mit einem Node wie Save 3D Model auf die Festplatte gespeichert zu werden. | 3D_FILE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BuildPoseFile/de.md)

---
**Source fingerprint (SHA-256):** `f3672f0749c4f9affcc92da98198c5b142f6fcd9f5e317ab43dd7e53533c0fa3`
