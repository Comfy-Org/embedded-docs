# SAM3DBody_Predict

SAM3D Body Prediction führt eine 3D-Körper- und Handposenschätzung an Eingabebildern durch und erkennt dabei eine oder mehrere Personen pro Frame. Tracking-Daten oder Bounding-Boxes können zur Verbesserung der Erkennung bereitgestellt werden; wenn keines von beiden angegeben wird, fällt der Node auf die Einzelpersonenerkennung im Vollbild zurück.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `sam3d_body_model` | Das SAM3D-Körpermodell, das für die Vorhersage verwendet werden soll. | SAM3D_BODY_MODEL | Ja | — |
| `image` | Bild oder Stapel von Bildern, auf denen die Körpervorhersage ausgeführt werden soll. | IMAGE | Ja | — |
| `track_data` | Tracking-Daten aus SAM3 Video Track, erforderlich für die Erkennung mehrerer Personen. | SAM3_TRACK_DATA | Nein | — |
| `bboxes` | Bounding-Boxes pro Frame, die für eine bessere Erkennung verwendet werden. Können als Alternative zu Tracking-Daten verwendet werden. | BBOX | Nein | — |
| `run_hand_refinement` | Verbessert die Handpose auf Kosten zusätzlicher Inferenzzeit und Speichernutzung. Standard: true. | BOOLEAN | Nein | true<br>false |
| `fov` | Vertikales FoV in Grad. Beeinflusst die vorhergesagte Tiefe und den absoluten Maßstab. 0 = Rückfall auf ~53° (16:9). Standard: 0.0. | FLOAT | Nein | 0.0 oder größer |
| `batch_size` | Maximale Anzahl an Personenausschnitten, die als Stapel verarbeitet werden. Größere Werte nutzen mehr VRAM für eine schnellere Inferenz. Standard: 64. | INT | Nein | 1 bis 512 |

Hinweis: Wenn `track_data` bereitgestellt wird, hat es Vorrang vor `bboxes`. Wenn weder `track_data` noch `bboxes` bereitgestellt werden, fällt der Node auf die Einzelpersonenerkennung im Vollbild zurück. Bounding-Boxes können für einen einzelnen Frame (angewendet auf jeden Frame) oder pro Frame bereitgestellt werden.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `mhr_pose_data` | Datenbündel für Körperpose, das Pose-Erkennungsergebnisse pro Frame, Gesichtsgeometrie, die Größe des Eingabebilds, kanonische Vertexfarben und eine Hand-Vertexmaske enthält. | MHR_POSE_DATA |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_Predict/de.md)

---
**Source fingerprint (SHA-256):** `f1039349cd2809423053bffde1c7d119c7c42f217327d23c608b1224d183770e`
