# Gesichtsausdruck zu SAM3D-Körper

Dieser Node fügt einem SAM3D-Körper Gesichtsausdrücke hinzu, indem er mit dem MediaPipe Face Landmarker Gesichter in einem Bild erkennt, jedes erkannte Gesicht einer verfolgten Person zuordnet und die 52 ARKit-Blendshapes auf die 72-Achsen-Ausdrucksparameter von MHR abbildet. Anschließend führt er das Körpermodell erneut aus, sodass die Mesh-Vertices und Keypoints der Ausgabe den neuen Ausdruck widerspiegeln.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `sam3d_body_model` | Das SAM3D-Körpermodell, das den Gesichtslandmarken-Detektor enthält, mit dem Gesichter erkannt und das Körper-Mesh neu erzeugt wird. | SAM3D_BODY_MODEL | Ja | - |
| `mhr_pose_data` | Posendaten, die pro Frame verfolgte Personen mit Bounding-Boxes, Keypoints und Ausdrucksparametern enthalten. Der Node ordnet jedes erkannte Gesicht einer Person zu und schreibt aktualisierte Ausdrucksparameter in diese Daten. | MHR_POSE_DATA | Ja | - |
| `image` | Bildframes, die zur Gesichtserkennung verwendet werden. Wenn der Bildstapel weniger Frames als die Posendaten enthält, wird der letzte Frame für die verbleibenden Frames wiederverwendet. | IMAGE | Ja | - |
| `strength` | Globaler Multiplikator für alle Blendshapes. Werte >1 verstärken. Standard: 1.0. | FLOAT | Nein | 0.0 bis 4.0 (Schritt 0.05, Standard 1.0) |
| `mouth_strength` | Multiplikator für Mund-/Kiefer-Formen. MediaPipes jawOpen erreicht bei etwa 1.0 Sättigung. Standard: 1.0. | FLOAT | Nein | 0.0 bis 4.0 (Schritt 0.05, Standard 1.0) |
| `eye_strength` | Multiplikator für Augenformen. MediaPipe überschreitet selten 0.5; 2- bis 3-fach ist oft erforderlich. Standard: 2.0. | FLOAT | Nein | 0.0 bis 4.0 (Schritt 0.05, Standard 2.0) |
| `brow_strength` | Multiplikator für Brauen-/Wangen-/Naserümpfen-Formen. MediaPipe gibt ~0.1-0.3 aus; 2- bis 3-fach. Standard: 2.0. | FLOAT | Nein | 0.0 bis 4.0 (Schritt 0.05, Standard 2.0) |
| `input_threshold` | Totzone für MediaPipes Rohausgabe (unterhalb = null, oberhalb = lineare Neuzuordnung). Standard: 0.02. | FLOAT | Nein | 0.0 bis 0.5 (Schritt 0.01, Standard 0.02) |
| `blendshape_smooth_window` | Gauß-Fenster auf MediaPipes Signal pro Frame vor der MHR-Zuordnung. MediaPipes Rohausgabe schwankt bei statischen Gesichtern um 30-70 % von Frame zu Frame. 1 = deaktiviert. Ungerade Werte verwenden. Standard: 7. | INT | Nein | 1 bis 31 (Schritt 2, Standard 7) |

Hinweis: Eine Basislinien-Subtraktion pro Clip wird nur angewendet, wenn mindestens 30 Frames im Clip erkannte Personen enthalten. Erkennungslücken von bis zu 12 Frames pro Person werden durch Interpolation gefüllt.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `mhr_pose_data` | Die aktualisierten Posendaten. Die Ausdrucksparameter jeder verfolgten Person werden durch den zugeordneten Gesichtsausdruck ersetzt, und die Mesh-Vertices und Keypoints werden entsprechend neu generiert. | MHR_POSE_DATA |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_FaceExpression/de.md)

---
**Source fingerprint (SHA-256):** `b2299e51be3556e639d5b04fcbee541ecf41e0d84c2c8a0fd4e211b2f6caba0b`
