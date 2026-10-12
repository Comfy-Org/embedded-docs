# Gesichtslandmarken erkennen (MediaPipe)

## Überblick

Erkennt Gesichter in einem Bild und identifiziert 468 Gesichts-Landmarken (Schlüsselpunkte) pro Gesicht mithilfe der Modelle BlazeFace und FaceMesh von MediaPipe. Außerdem berechnet er ARKit-52-Blendshape-Koeffizienten für die Analyse des Gesichtsausdrucks. Der Node kann mehrere Bilder in einem Batch verarbeiten und gibt sowohl die Landmarken-Daten als auch Begrenzungsrahmen für jedes erkannte Gesicht aus.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `face_detection_model` | Das MediaPipe-Gesichtsdetektionsmodell, das für die Landmarkenerkennung verwendet werden soll. | FACE_DETECTION_MODEL | Ja |  |
| `image` | Das Eingabebild oder der Batch von Bildern, in dem Gesichter erkannt werden sollen. | IMAGE | Ja |  |
| `detector_variant` | Erkennungsbereich des Gesichtsdetektors. `"short"` ist auf Nahaufnahmen von Gesichtern abgestimmt (im Umkreis von ca. 2 m von der Kamera); `"full"` deckt weiter entfernte/kleinere Gesichter ab (bis zu ca. 5 m), ist aber langsamer. `"both"` führt beide Detektoren aus und behält denjenigen, der pro Frame mehr Gesichter gefunden hat (ca. doppelte Erkennungskosten). Standard: `"short"`. | COMBO | Ja | `"short"`<br>`"full"`<br>`"both"` |
| `num_faces` | Maximale Anzahl der pro Frame zurückzugebenden Gesichter. 0 bedeutet keine Obergrenze (alle erkannten zurückgeben). Standard: 1. | INT | Ja | 0 bis 16 |
| `min_confidence` | BlazeFace-Score-Schwelle. Niedrigere Werte helfen, kleine oder verdeckte Gesichter zu erfassen. Standard: 0.5. | FLOAT | Nein | 0.00 bis 1.00 |
| `missing_frame_fallback` | Verhalten pro Frame, wenn die Erkennung in einem Batch fehlschlägt. `"empty"` lässt das Frame ohne Gesicht. `"previous"` kopiert die letzte erfolgreiche Erkennung. `"interpolate"` interpoliert Landmarken/BBox/Blendshapes zwischen den umgebenden erfolgreichen Frames. Multi-Gesicht: paart Gesichter über Frames hinweg mithilfe eines gierigen BBox-Zentrum-NN. Standard: `"empty"`. | COMBO | Nein | `"empty"`<br>`"previous"`<br>`"interpolate"` |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `face_landmarks` | Eine strukturierte Ausgabe mit den Gesichtserkennungsergebnissen pro Frame, einschließlich 468 Gesichts-Landmarken, ARKit-52-Blendshape-Koeffizienten, Transformationsmatrizen und Verbindungssets für die Mesh-Visualisierung. | FACE_LANDMARKS |
| `bboxes` | Eine Liste von Begrenzungsrahmen für jedes erkannte Gesicht mit Koordinaten (x, y, width, height), Label "face" und Konfidenzwert. Eine Liste pro Eingabe-Frame. | BOUNDING_BOX |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MediaPipeFaceLandmarker/de.md)

---
**Source fingerprint (SHA-256):** `f60ed6201288a59d65d62cc98c12f227a353870c36decea8da81a063cfdf2bba`
