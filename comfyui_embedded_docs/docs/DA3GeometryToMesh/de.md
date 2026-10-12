# DA3-Geometrie in Mesh konvertieren

Dieser Node wandelt ein DA3_GEOMETRY-Paket in ein 3D-Mesh um, indem er die Tiefenkarte rückprojiziert und die resultierende Punktwolke trianguliert. Er verarbeitet ein einzelnes Bild aus einem Batch und erzeugt ein texturiertes oder untexturiertes Mesh, das für 3D-Rendering geeignet ist.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `da3_geometry` | Das DA3_GEOMETRY-Paket mit Tiefenkarte, optionaler Konfidenzkarte, optionaler Sky-Map und Quellbild | DA3_GEOMETRY | Ja | - |
| `batch_index` | Welches Bild eines Batches konvertiert werden soll. Die Vertex-Anzahl pro Bild unterscheidet sich, daher können Batches nicht gestapelt werden (Standard: 0). Muss kleiner als die Batch-Größe der eingegebenen Geometrie sein, andernfalls wird ein Fehler ausgelöst | INT | Ja | 0 to 4096 |
| `decimation` | Vertex-Stride. 1 = volle Auflösung, 2 = halbe Auflösung usw. (Standard: 1) | INT | Ja | 1 to 8 |
| `discontinuity_threshold` | Verwirft Dreiecke, deren 3x3-Tiefenspanne diesen Bruchteil überschreitet. 0 = aus (Standard: 0.04) | FLOAT | Ja | 0.0 to 1.0 |
| `confidence_threshold` | Schließt Pixel aus, deren pro Bild normalisierte Konfidenz unter diesem Wert liegt. 0 = alle behalten, 1 = nur das einzelne Pixel mit der höchsten Konfidenz behalten. Wird verwendet, wenn die Geometrie eine Konfidenzkarte besitzt (Small/Base-Modelle) (Standard: 0.1) | FLOAT | Ja | 0.0 to 1.0 |
| `use_sky_mask` | Schließt Pixel mit Sky-Wahrscheinlichkeit (Sky >= 0.5) vom Mesh aus. Wird verwendet, wenn die Geometrie eine Sky-Map besitzt (Mono/Metric-Modelle) (Standard: True) | BOOLEAN | Ja | True or False |
| `texture` | Verwendet das Quellbild als Basisfarbtextur (Standard: True) | BOOLEAN | Ja | True or False |

Pixel mit nicht-finiten, null- oder negativen Tiefenwerten werden immer vom Mesh ausgeschlossen. Wenn das resultierende Mesh leer ist, wird ein Fehler ausgelöst; die Fehlermeldung schlägt vor, `discontinuity_threshold` zu erhöhen, `confidence_threshold` zu senken oder `use_sky_mask` zu deaktivieren.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `MESH` | Ein trianguliertes 3D-Mesh mit Eckpunkten, Flächen, UV-Koordinaten und optionaler Textur | MESH |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DA3GeometryToMesh/de.md)

---
**Source fingerprint (SHA-256):** `1d311223a8d131030bcd4930d21852a21ac9dd5758e7f8b8d20b1cf68698893b`
