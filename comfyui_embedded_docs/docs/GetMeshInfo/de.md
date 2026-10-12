# GetMeshInfo

Get Mesh Info gibt die Anzahl der Vertices und Faces in einem Mesh sowie die enthaltenen Attribute an (wie UVs, Vertexfarben, Normalen und Texturen). Der Bericht wird auf dem Node angezeigt und als Textausgabe zurückgegeben, während das Mesh selbst unverändert weitergegeben wird.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `mesh` | Das zu untersuchende Mesh. Der Node zählt seine Vertices und Faces, erkennt, welche Attribute vorhanden sind, und gibt das Mesh unverändert weiter. | MESH | Ja | — |

Hinweis: Wenn die Eingabe mehrere Meshes enthält (ein Batch), zeigt der Bericht die Gesamtanzahlen der Vertices und Faces für den gesamten Batch sowie eine Aufschlüsselung pro Mesh an. Bei Zero-Padding-Batches werden die pro Element in den Mesh-Daten gespeicherten Zählungen verwendet.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `mesh` | Das ursprüngliche Mesh, unverändert weitergegeben. | MESH |
| `info` | Ein mehrzeiliger Textbericht mit Vertex-Anzahl, Face-Anzahl und erkannten Attributen (uvs, vertex_colors, normals, tangents, texture, metallic_roughness, normal_map). Texturähnliche Attribute werden mit ihren Abmessungen Höhe × Breite angezeigt. Große Anzahlen werden mit Tausendertrennzeichen formatiert, zum Beispiel „1,234,567 (1.23M)“ oder „12,345 (12.3K)“. Derselbe Text wird auf dem Node angezeigt. | STRING |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetMeshInfo/de.md)

---
**Source fingerprint (SHA-256):** `cd168a5e69131a4a37f1f47014af2bc2ac2c8aa69e146cf33c2072480b35ebb2`
