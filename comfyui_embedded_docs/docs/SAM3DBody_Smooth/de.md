# SAM3D-Körperposendaten glätten

Smooth SAM3D Body Pose Data reduziert Frame-zu-Frame-Jitter in einer Sequenz von 3D-Körperposen durch zeitliche Mittelung der Bewegung. Kamera- und Erscheinungsdaten werden vollständig geglättet, während die Mesh-Geometrie weniger geglättet wird, wenn sich das Subjekt schnell dreht, damit schnelle Drehungen nicht abgeflacht werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `mhr_pose_data` | Die zu glättende MHR-Pose-Daten-Sequenz, die Modellparameter, Formparameter, Ausdrucksparameter, das MHR70-Keypoint-Layout und zugehörige Mesh-Daten enthält. | MHR_POSE_DATA | Ja | — |
| `strength` | Glättungsstärke. 0 = ungeglättet, 1 = geglättet. (Standard: 1.0) | FLOAT | Ja | 0.0 to 1.0 (step 0.05) |
| `method` | gaussian: symmetrischer gewichteter Mittelwert, bester Allzweck-Glätter.<br>savgol: gleitende Polynom-Anpassung, bewahrt scharfe Spitzen. (Standard: "savgol") | COMBO | Ja | "gaussian"<br>"savgol" |
| `window` | Zeitliches Fenster in Frames (ungerade Werte). (Standard: 7) | INT | Ja | 1 to 51 (odd values, step 2) |
| `rotation_threshold_degrees` | Deaktiviert die Glättung für diese Root-Rotationsrate (Grad/Frame), um schnelle Drehungen zu erhalten. 30° passt für die meisten Inhalte; niedrige Werte können die Glättung bei gewöhnlichem Jitter deaktivieren und beeinträchtigen die Qualität stillschweigend. 0 = deaktivieren. (Standard: 30.0) | FLOAT | Ja | 0.0 to 90.0 (step 1.0) |

Hinweis: Wenn `strength` 0.0 oder niedriger ist oder `window` 1 oder niedriger ist, gibt der Node die Eingabedaten unverändert zurück. Die Eingabe muss mindestens 2 Frames und Keypoint-Daten enthalten; andernfalls gibt der Node die Eingabedaten unverändert zurück. Wenn `rotation_threshold_degrees` 0.0 ist, wird die rotationsbasierte Rücknahme der Glättung deaktiviert.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `mhr_pose_data` | Die geglättete MHR-Pose-Daten-Sequenz mit reduziertem Frame-zu-Frame-Jitter. | MHR_POSE_DATA |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_Smooth/de.md)

---
**Source fingerprint (SHA-256):** `a80a1c121f1d2bc49e9112576775588d5deab4690c4cd6ec9c1f98de78457b30`
