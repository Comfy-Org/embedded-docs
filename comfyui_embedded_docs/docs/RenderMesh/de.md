# Mesh rendern

Dieser Node rendert ein 3D-Mesh durch Ray-Casting einer einzelnen Ansicht in ein 2D-Bild. Er kann das texturierte Mesh, Vertex-Farben, eine einfarbig schattierte Oberfläche, Oberflächennormalen oder Tiefe ausgeben. Die Kamera und die optionale Modelltransformation können aus einem Load3D-/Preview3D-Viewer stammen; wenn keine Kamera verbunden ist, wird automatisch eine Standard-Frontansicht eingepasst.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `mesh` | Das zu rendernde 3D-Mesh. | MESH | Ja | — |
| `mode` | Was gerendert werden soll. auto: Textur, falls vorhanden, sonst Vertex-Farben, sonst schattierte Clay-Darstellung. (Standard: "auto") | COMBO | Ja | `"auto"`<br>`"texture"`<br>`"vertex colors"`<br>`"solid"`<br>`"normal"`<br>`"depth"` |
| `width` | Breite des gerenderten Bildes in Pixeln. (Standard: 1024) | INT | Ja | 64 bis 4096 (Schrittweite 8) |
| `height` | Höhe des gerenderten Bildes in Pixeln. (Standard: 1024) | INT | Ja | 64 bis 4096 (Schrittweite 8) |
| `background` | Hintergrundfarbe für Pixel, die das Mesh nicht abdeckt. (Standard: "#000000") | COLOR | Ja | — |
| `model_3d_info` | Modelltransformation aus demselben Load3D-/Preview3D-Viewer. Verbinden Sie sie mit `camera_info`, um den Bildausschnitt des Viewers zu übernehmen. | LOAD3D_MODEL_INFO | Nein | — |
| `camera_info` | Kamera aus einem Load3D-/Preview3D-Viewer oder einem Create Camera Info-Node. Wenn keine verbunden ist, wird automatisch eine Standard-Frontansicht eingepasst. | LOAD3D_CAMERA | Nein | — |

Hinweis: Nur das erste Element eines gebatchten Meshes wird gerendert – wenn der Mesh-Batch mehr als ein Element enthält, protokolliert der Node eine Warnung und verwendet das erste. Der Modus `texture` erfordert, dass das Mesh sowohl eine Textur als auch UVs besitzt, und der Modus `vertex colors` erfordert Vertex-Farben; falls die Daten für den ausgewählten Modus nicht verfügbar sind, fällt der Node auf die einfarbig schattierte Darstellung zurück. Der Modus `normal` verwendet die glatten Vertex-Normalen des Meshes, falls vorhanden, andernfalls die Flächennormale. Im Modus `depth` erscheinen nähere Oberflächen heller (nah = weiß) und nicht vom Mesh bedeckte Pixel bleiben schwarz. Die Anschlüsse `model_3d_info` und `camera_info` sind dafür gedacht, gemeinsam aus demselben Load3D-/Preview3D-Viewer verbunden zu werden, damit das Rendering dem Bildausschnitt des Viewers entspricht.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|--------------|--------------|----------|
| `image` | Das gerenderte Bild des Meshes. | IMAGE |
| `mask` | Eine Maske, die 1.0 dort ist, wo das Mesh gerendert wurde, und 0.0 andernfalls. | MASK |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenderMesh/de.md)

---
**Source fingerprint (SHA-256):** `d23e85a904520eb2dfed899eb3e6a9cf45c980df00c034503687ac4eccc66ac4`
