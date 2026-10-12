# LoadMediaPipeFaceLandmarker

Dieser Node lädt ein MediaPipe Face Landmarker v2-Modell, das Gesichter und Gesichtsmerkmale (wie Augen, Nase und Mund) in Bildern erkennt. Das geladene Modell bündelt zwei Erkennungsvarianten (Nahbereich und Vollbereich) zusammen mit gemeinsam genutzten Mesh-Daten, Blendshapes und kanonischer Geometrie, die für die Gesichtsanalyse verwendet werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `model_name` | Gesichtserkennungsmodell aus models/detection/. | COMBO | Ja | Liste der verfügbaren Modelldateinamen, die im Verzeichnis `models/detection/` gefunden werden |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `FACE_DETECTION_MODEL` | Ein geladenes FaceLandmarker-Modellobjekt, das beide Erkennungsvarianten (short/full), Verbindungssätze für die Gesichtstopologie, kanonische Daten und Modell-Patcher für die GPU-Verwaltung enthält. | FACE_DETECTION_MODEL |

**Hinweis:** Die Ausgabe ist ein komplexes Objekt, das von anderen Nodes für Aufgaben zur Gesichtserkennung und Landmark-Extraktion verwendet werden kann. Es enthält zwei Erkennungsvarianten: „short“ für die Nahbereichserkennung und „full“ für die Vollbereichserkennung.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMediaPipeFaceLandmarker/de.md)

---
**Source fingerprint (SHA-256):** `33dda845b572ccffc1bd4b64fb9c338ce4313783b092fe311d89741a211f18c9`
