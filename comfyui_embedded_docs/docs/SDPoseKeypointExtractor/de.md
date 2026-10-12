# SDPoseKeypointExtractor

Der SDPoseKeypointExtractor-Node erkennt menschliche Pose-Keypoints aus Eingabebildern mithilfe des SDPose-Modells. Er kann vollständige Bilder oder bestimmte, durch Begrenzungsrahmen definierte Regionen verarbeiten und gibt die erkannten Keypoints im OpenPose-Format aus, das die Koordinaten für jede Person und einen Konfidenzwert für jeden Keypoint enthält.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `model` | Das SDPose-Modell, das für die Keypoint-Erkennung verwendet wird. Muss ein Modell mit einem `heatmap_head`-Attribut sein, insbesondere aus dem SDPose-Repository. | MODEL | Ja | - |
| `vae` | Das VAE-Modell, das verwendet wird, um die Eingabebilder zur Verarbeitung in den latenten Raum zu kodieren. | VAE | Ja | - |
| `image` | Das Eingabebild oder der Batch von Bildern, aus dem bzw. denen Pose-Keypoints extrahiert werden sollen. | IMAGE | Ja | - |
| `batch_size` | Die Anzahl der Bilder, die im Vollbildmodus (d. h., wenn `bboxes` nicht angegeben ist) gleichzeitig verarbeitet werden. Dies kann die Verarbeitung beschleunigen. (Standard: 16) | INT | Nein | 1 bis 10000 |
| `bboxes` | Optionale Begrenzungsrahmen für genauere Erkennungen. Erforderlich für die Mehrpersonenerkennung. Wenn angegeben, extrahiert der Node Keypoints aus jeder angegebenen Region. | BOUNDINGBOX | Nein | - |

**Parameterbeschränkungen:**
*   Der `model`-Eingang muss ein spezifisches SDPose-Modell sein. Wenn das bereitgestellte Modell kein `heatmap_head`-Attribut aufweist, löst der Node einen Fehler aus.
*   Der Node arbeitet abhängig vom `bboxes`-Eingang in zwei unterschiedlichen Modi:
    1.  **Begrenzungsrahmen-Modus:** Wenn `bboxes` angegeben ist, verarbeitet er jede angegebene Region einzeln. Dies ist erforderlich, um mehrere Personen in einem einzelnen Bild zu erkennen.
    2.  **Vollbildmodus:** Wenn `bboxes` nicht angegeben ist, verarbeitet er das gesamte Bild als Batch. Der Parameter `batch_size` gilt nur in diesem Modus.
*   Wenn `bboxes` angegeben ist, muss es eine Liste von Begrenzungsrahmen sein. Wenn weniger Begrenzungsrahmenlisten als Bilder vorhanden sind, wird die letzte Liste für die verbleibenden Bilder wiederverwendet.
*   Begrenzungsrahmen mit einer Breite oder Höhe von null (z. B. `x2 <= x1` oder `y2 <= y1`) werden übersprungen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `keypoints` | Keypoints im OpenPose-Frame-Format (canvas_width, canvas_height, people). Die Ausgabe enthält die erkannten Personen, jeweils mit einem Array von Keypoint-Koordinaten (x, y) und ihren entsprechenden Konfidenzwerten. | POSE_KEYPOINT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SDPoseKeypointExtractor/de.md)

---
**Source fingerprint (SHA-256):** `5e199e9d08a46d934c6d1f4b1a411f0ca95eb5e7f85ec39f59a058c9be598e9f`
