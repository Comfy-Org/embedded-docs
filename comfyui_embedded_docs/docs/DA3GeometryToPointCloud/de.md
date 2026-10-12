# DA3GeometryToPointCloud

Konvertiert eine Tiefenkarte aus einem DA3_GEOMETRY-Objekt in eine 3D-Punktwolke. Es wendet eine Filterung basierend auf Konfidenz- und Himmelsmasken an und transformiert die Punkte in ein gemeinsames Weltkoordinatensystem, das für Multi-View-Szenen geeignet ist.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `da3_geometry` | Das DA3_GEOMETRY-Objekt, das Tiefendaten und optionale Bild-, Konfidenz- und Himmelskarten enthält | DA3_GEOMETRY | Ja | - |
| `batch_index` | Welches Bild aus einem Batch konvertiert werden soll (Standard: 0) | INT | Ja | 0 bis 4096 |
| `confidence_threshold` | Schließt Pixel aus, deren pro Bild normalisierte Konfidenz unter diesem Wert liegt (0 = alle behalten). Wird verwendet, wenn die Geometrie eine Konfidenzkarte enthält (Small/Base-Modelle). (Standard: 0.1) | FLOAT | Ja | 0.0 bis 1.0 |
| `use_sky_mask` | Schließt Pixel mit Himmel-Wahrscheinlichkeit aus (Himmel >= 0.5). Wird verwendet, wenn die Geometrie eine Himmelskarte enthält (Mono/Metric-Modelle). (Standard: True) | BOOLEAN | Ja | True or False |
| `downsample` | Jeden N-ten Pixel nehmen (1 = volle Auflösung). Höhere Werte ergeben weniger Punkte und eine schnellere Verarbeitung. (Standard: 1) | INT | Ja | 1 bis 16 |

**Hinweise:**
- `batch_index` muss kleiner als die Batch-Größe der Eingabegeometrie sein; andernfalls löst der Node einen Fehler aus.
- Wenn die Filterung alle Pixel entfernt, löst der Node einen Fehler aus. Ein Verringern von `confidence_threshold` oder Deaktivieren von `use_sky_mask` kann dies verhindern.
- `confidence_threshold` wird nur angewendet, wenn die Geometrie eine Konfidenzkarte enthält (Small/Base-Modelle).
- `use_sky_mask` wird nur angewendet, wenn die Geometrie eine Himmelskarte enthält (Mono/Metric-Modelle).
- Wenn `downsample` größer als 1 ist, werden die Kamera-Intrinsics entsprechend skaliert, damit die projizierten Punkte korrekt bleiben.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `point_cloud` | Eine Punktwolke, die gefilterte 3D-Punkte, optionale Farben und optionale Konfidenzwerte enthält | DA3_POINT_CLOUD |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DA3GeometryToPointCloud/de.md)

---
**Source fingerprint (SHA-256):** `3cf5bdbb8afdfcfc02f9832a8cbc5a3df49da755dea6df01792aa6ef9e5d7287`
