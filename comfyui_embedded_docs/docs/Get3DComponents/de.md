# Get3DComponents

Get3DComponents parst eine 3D-Modelldatei (GLB, GLTF, OBJ oder STL) in ein editierbares Mesh, das von Mesh-Verarbeitungs-Nodes wie Decimate, Remesh, UV Unwrap und Bake verwendet werden kann. Alle Szenen-Nodes und Primitive werden unter Anwendung ihrer Transformationen zu einem einzigen Mesh zusammengeführt; Texturen und Materialeinstellungen stammen vom ersten Material. Es ist das Gegenstück zum Node MeshToFile3D.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `model_3d` | 3D-Modelldatei von Load 3D oder einem anderen 3D-Node. FBX/USDZ werden nicht unterstützt – zuerst in GLB konvertieren. | File3DGLB<br>File3DGLTF<br>File3DOBJ<br>File3DSTL<br>File3DAny | Ja | GLB<br>GLTF<br>OBJ<br>STL |

Hinweis: FBX- und USDZ-Dateien werden nicht unterstützt und verursachen einen Fehler; konvertieren Sie sie zuerst in GLB oder GLTF. Wenn das Dateiformat nicht als GLB, GLTF, OBJ oder STL erkannt werden kann, löst der Node einen Fehler aus und listet die unterstützten Formate auf. Wenn die glTF-Szene keine Dreiecksgeometrie enthält oder die Datei Flächenindizes enthält, die außerhalb der Vertexliste liegen (ein Hinweis auf eine beschädigte Datei), löst der Node einen Fehler aus. Wenn die 3D-Datei mehrere Materialien enthält, werden nur die Texturen und Materialfaktoren des ersten Materials beibehalten (eine Warnung wird protokolliert). Alle Szenenprimitive werden unter Anwendung ihrer Transformationen zu einem einzigen Mesh zusammengeführt. Dieser Node ist experimentell.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `mesh` | Editierbares Mesh mit Vertices, Faces, UVs, Vertexfarben, Normalen und Tangenten sowie Materialinformationen aus der Datei (Textur, Metallic-Roughness, Normal Map, Emissionsfarbe, Unlit-Flag, Occlusion-in-Metallic-Roughness-Flag und Materialdaten). | MESH |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Get3DComponents/de.md)

---
**Source fingerprint (SHA-256):** `f2cdc9767a50503988484f09d2b3d110caf086b8cd84f65034a4a1e17a94405e`
