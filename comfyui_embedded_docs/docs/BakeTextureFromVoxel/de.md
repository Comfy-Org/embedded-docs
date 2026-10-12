# Textur aus Voxel backen

Dieser Node backt PBR-Texturen auf ein 3D-Mesh unter Verwendung des vorhandenen UV-Layouts des Meshes. Er rastert das Mesh im UV-Raum und tastet an jedem Texel Farb- und Materialattribute aus einem dünnbesetzten Voxelvolumen ab, wobei er ein Basisfarbbild sowie Metallic- und Roughness-Maps ausgibt. Er entpackt das Mesh nicht, daher muss ein UV-Unwrap-Node vorgeschaltet sein; die resultierenden Bilder sind dafür gedacht, in ApplyTextureToMesh mit demselben Mesh kombiniert zu werden, um als GLB gespeichert zu werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `mesh` | Das 3D-Mesh, auf das Texturen gebacken werden sollen. Muss bereits ein UV-Layout besitzen; ein UV-Unwrap-Node muss vorgeschaltet sein. | MESH | Ja | |
| `voxel_colors` | Dünnbesetztes Voxelvolumen mit Farben pro Voxel und optionalen PBR-Attributen (Metallic- und Roughness-Kanäle). | VOXEL | Ja | |
| `texture_size` | Quadratische UV-Atlas-Auflösung (Anzeigename: "resolution", Standard: 2048). | INT | Ja | 64 bis 8192 |
| `reference_mesh` | Optionales dichtes Mesh vor der Dezimierung; projiziert jedes Texel vor der Abtastung auf seine tatsächliche Oberfläche zurück, wodurch facettiertes Baking auf groben Meshes vermieden wird. | MESH | Nein | |

Hinweise:

- Das Eingabe-Mesh muss UVs besitzen. Wenn keine UVs vorhanden sind, löst der Node einen Fehler aus. UVs müssen 1:1 zu den Vertices sein (ein UV pro Vertex).
- Wenn das Mesh und die Voxelkoordinaten eine Batch-Dimension enthalten, wird jedes Batch-Element separat gebacken. Wenn ein Batch-Element keine Voxel oder keine Flächen enthält, wird es übersprungen und für es wird eine schwarze Textur ausgegeben.
- Wenn `reference_mesh` für einen Batch bereitgestellt wird, wird es anhand des Batch-Index zugeordnet, es sei denn, es enthält nur ein einzelnes Mesh; in diesem Fall wird dieses Mesh für alle Elemente verwendet.
- Texel, die von keinem UV-Dreieck abgedeckt werden, werden vom nächstgelegenen abgedeckten Texel gefüllt, damit Texturnähte nicht Schwarz hineinziehen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `base_color` | RGB-Basisfarb-Texturmap. Werte sind Float im Bereich 0–1. | IMAGE |
| `metallic` | Graustufen-Metallic-Map (Float, 0–1). Schwarz, wenn die Voxelfarben keinen Metallic-Kanal enthalten. | IMAGE |
| `roughness` | Graustufen-Roughness-Map (Float, 0–1). Schwarz, wenn die Voxelfarben keinen Roughness-Kanal enthalten. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeTextureFromVoxel/de.md)

---
**Source fingerprint (SHA-256):** `080dcb670620f1cb97523d04fc45293e03d139e513845d0fa7b1c4d2f8bdf32d`
