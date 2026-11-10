# Bake Texture From Views

Projiziert gerenderte Bilder zurück auf das UV-Layout des Meshes. Rendern Sie das Mesh mit Render Mesh, bearbeiten oder regenerieren Sie die Bilder und backen Sie sie anschließend mit demselben Mesh und denselben Kameras. Texel, die keine Ansicht abdeckt, behalten die eigene Textur oder Vertexfarben des Meshes.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `mesh` | Das UV-entfaltete Mesh, das gerendert wurde. | MESH | Ja | - |
| `images` | Ein Bild pro Kamera, in Kamera-Reihenfolge (Batch Images). Beliebige Auflösung mit dem Seitenverhältnis des Renders; eine höhere Auflösung ergibt ein schärferes Bake. | IMAGE | Ja | - |
| `camera_info` | Die Kameras, mit denen die Bilder gerendert wurden, wie mit Render Mesh verbunden. Rigs mit Batch Cameras zusammenführen. Keine: automatisch gerahmte Frontansicht von Render Mesh. | LOAD3D_CAMERA | Nein | - |
| `resolution` | Quadratische Texturauflösung. 0 behält die aktuelle Texturgröße des Meshes bei bzw. 2048, wenn es keine hat; andernfalls wird die aktuelle Textur darauf neu abgetastet. Standard: 0. | INT | Nein | 0 bis 8192 (Schritt: 64) |
| `blend_exponent` | Ansichten werden mit cos(Blickwinkel)^Exponent gewichtet. Höher bevorzugt die frontalste Ansicht (schärfer, härtere Nähte); niedriger mittelt mehr Ansichten (weicher). Standard: 4.0. | FLOAT | Nein | 0.0 bis 32.0 (Schritt: 0.5) |
| `fill_unseen` | Texel, die keine Ansicht sieht, erhalten eine Farbe, die aus der gesehenen Oberfläche fortgeschrieben wird, anstelle der eigenen Textur oder Vertexfarben des Meshes. Verwenden, wenn die Ansichten die gesamte Textur ersetzen. Standard: false. | BOOLEAN | Nein | true<br>false |
| `mask` | Bearbeitete Bereiche pro Ansicht; nur maskierte Pixel werden projiziert. Eine einzelne Maske gilt für jede Ansicht. | MASK | Nein | - |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `base_color` | Die gebackene Textur, für Apply Texture to Mesh. | IMAGE |
| `confidence` | Pro Texel, wie frontal die beste Ansicht ihn gesehen hat; 0 bedeutet ungesehen. | MASK |

Hinweis: Renders, die mit einer Viewer-Modelltransformation erstellt wurden, stimmen nicht mit dem Bake überein, und nur das erste Mesh eines Batches wird verwendet.

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeTextureFromViews/de.md)

---
**Source fingerprint (SHA-256):** `e5f2456977693dc09e69ce4d846f2ab775f2520115623d9f63a76807d6c9f797`
