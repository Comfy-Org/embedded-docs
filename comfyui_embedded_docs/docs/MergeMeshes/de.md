# Meshes zusammenführen

MergeMeshes kombiniert mehrere Mesh-Eingaben zu einem einzigen Mesh, indem deren Vertices, Faces, UV-Koordinaten und Vertexfarben gestapelt und die Face-Indizes versetzt werden, sodass alle Teile korrekt zu einem durchgehenden Mesh verbunden werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|--------------|----------|--------------|---------|
| `meshes` | Erweiterbarer Slot: Verbinden Sie 2 bis 50 Mesh-Objekte (benannt `mesh_1`, `mesh_2`, ..., `mesh_50`). Alle verbundenen Meshes werden zu einem Ausgabe-Mesh zusammengeführt. | MESH | Ja | 2 bis 50 Meshes |

**Hinweis:** Mindestens ein Mesh muss bereitgestellt werden; andernfalls gibt der Node einen Fehler aus. Es wird nur das erste Mesh-Element aus dem Batch jedes Eingabe-Meshes verwendet. Eingabe-Meshes werden vor dem Zusammenführen auf die CPU verschoben. Wenn ein Eingabe-Mesh UV-Daten besitzt, enthält die Ausgabe UVs, und Meshes ohne UVs erhalten mit Null aufgefüllte UV-Werte. Wenn ein Eingabe-Mesh Vertexfarben besitzt, enthält die Ausgabe Vertexfarben; Meshes ohne Farben erhalten weiße Farben (Wert 1), und Farbkanäle werden auf die größte Kanalanzahl aufgefüllt, die unter den Eingaben gefunden wurde. Nur die Textur der ersten Eingabe, die eine bereitstellt, wird beibehalten; zusätzliche Texturen werden verworfen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|--------------|----------|
| `mesh` | Das zusammengeführte Mesh, das alle Eingabe-Vertices, Faces, UVs und Farben in einem einzigen Mesh vereint. | MESH |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeMeshes/de.md)

---
**Source fingerprint (SHA-256):** `0ce49b522f6348d524df20d6c27eb8bd9575c4a781790f6f8e3ac4f3ee255d38`
