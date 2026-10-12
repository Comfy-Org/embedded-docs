# PaintMesh

PaintMesh nimmt ein 3D-Mesh und ein Voxel-Farbfeld entgegen. Es weist jedem Vertex die Farbe des nächstgelegenen Voxels im Feld zu und gibt das Mesh mit diesen angewendeten Vertexfarben zurück. Wenn das Voxelfeld leer ist, wird das Mesh mit standardmäßigen Vertexfarben von null (Schwarz) eingefärbt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `mesh` | Das einzufärbende Mesh. | MESH | Ja | N/A |
| `voxel_colors` | Voxelfeld mit Farbdaten, die zum Einfärben verwendet werden. Aus dem Feld werden nur die RGB-Kanäle der Basisfarbe verwendet. | VOXEL | Ja | N/A |

Hinweis: Wenn die Koordinaten des Voxelfelds einen Batch-Index-Kanal enthalten und das eingegebene Mesh mehrere Mesh-Elemente enthält, wendet der Node die Farben separat auf jedes Mesh-Element im Batch an. Wenn ein bestimmtes Mesh-Element keine passenden Voxel hat, erhält es standardmäßige Vertexfarben von null (Schwarz). Die abgetasteten Farben werden für das Ausgabe-Mesh von sRGB in lineares RGB konvertiert, da das Voxelfeld vollständige PBR-Daten enthalten kann, aber für die Vertexfarben nur die RGB-Basisfarbe verwendet wird.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `mesh` | Das eingefärbte Mesh mit angewendeten Vertexfarben. | MESH |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PaintMesh/de.md)

---
**Source fingerprint (SHA-256):** `55683bef55b18487ba660fe619d6ec176f786de346be12724751b71901c14116`
