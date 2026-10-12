# WeldVertices

Weld Vertices führt das Zusammenführen von zusammenfallenden Vertices in einem 3D-Mesh durch, sodass Flächen, die zuvor separate Eckpunkte hatten, anschließend dieselben Vertices gemeinsam nutzen. Es gruppiert nahe gelegene Vertices mithilfe von Gitterquantisierung mit einer Toleranz basierend auf der Bounding Box des Meshes und mittelt die Vertexfarben für jede zusammengeführte Gruppe. Das ist nützlich, wenn ein Mesh unverschweißt ankommt, d. h. jede Fläche hat ihre eigenen Vertices und keine gemeinsamen Kanten, und kann als Vorverarbeitungsschritt vor topologiebewussten Operationen wie FillHoles oder DecimateMesh dienen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|--------|
| `mesh` | Das eingegebene 3D-Mesh, dessen zusammenfallende Vertices zusammengeführt werden. | MESH | Ja | - |
| `epsilon_rel` | Schweißtoleranz (Anteil der Bounding-Box-Diagonale). 1e-5 für Float-Deduplizierung; 1e-3 für sichtbar nahe, aber verschiedene Vertices. Standard: 1e-5. | FLOAT | Ja | 0.0 to unlimited (step 1e-6) |
| `epsilon_abs` | Absolute Schweißtoleranz (überschreibt epsilon_rel, wenn > 0). Standard: 0.0. | FLOAT | Ja | 0.0 to unlimited (step 1e-6) |

Hinweis: Wenn `epsilon_abs` größer als 0 ist, hat es Vorrang vor `epsilon_rel`, und die relative Toleranz wird ignoriert. Wenn `epsilon_abs` 0 ist, wird die relative Toleranz `epsilon_rel` verwendet und in eine absolute Distanz umgerechnet, indem sie mit der Diagonale der Bounding Box des Meshes multipliziert wird.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `mesh` | Das verschweißte Mesh mit zusammengeführten Vertices, aktualisierten Flächenindizes und gemittelten Vertexfarben (falls das Eingabe-Mesh Farben hatte). | MESH |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WeldVertices/de.md)

---
**Source fingerprint (SHA-256):** `f8779e764b344de651b8459f6e4c28773509d9596a98fd164dc7044278856435`
