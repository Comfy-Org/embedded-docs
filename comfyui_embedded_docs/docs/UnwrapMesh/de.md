# UnwrapMesh

Erzeugt einen UV-Atlas für ein 3D-Mesh. Die Mesh-Oberfläche wird in Charts aufgeteilt, jedes Chart wird in zwei Dimensionen abgeflacht, und die abgeflachten Charts werden in einen UV-Atlas im Bereich [0,1] gepackt. Vertices an Chart-Nähten werden dupliziert (eine Kopie pro Chart, gleiche Position, eigene UV), sodass das Ausgabe-Mesh mehr Vertices als das Eingabe-Mesh enthalten kann und die Anzahl der Ausgabe-Faces von der Eingabe abweichen kann.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `mesh` | Das Eingabe-Mesh, das entfaltet werden soll. Akzeptiert ein einzelnes Mesh oder einen Batch von Meshes; Batches werden Element für Element verarbeitet. | MESH | Yes | — |
| `segmenter` | Zu verwendender Charting-Algorithmus. `pec`: schnelles Charting auf der GPU mittels parallelem Edge-Collapse. `adaptive`: CPU, langsamer. (Standard: "pec") | COMBO | Yes | "pec"<br>"adaptive" |
| `resolution` | Ziel-Atlasauflösung für die automatische Skalierung der Texeldichte (0 = an Inhalt anpassen). (Standard: 1024) | INT | Yes | 0 bis 8192 (Schritt 256) |
| `padding` | Texel-Abstand zwischen Charts. (Standard: 1) | INT | Yes | 0 bis 16 |
| `weld_distance` | Radius zum Zusammenführen zusammenfallender Vertices als Bruchteil der Mesh-Ausdehnung (0 = auto). Erhöhen Sie ihn auf ~0.001, wenn Sie Charts pro Dreieck erhalten (nicht verschweißte Eingabe). (Standard: 0.0) | FLOAT | Yes | 0.0 bis 1.0 (Schritt 0.0001) |

Hinweis: Wenn das Eingabe-Mesh nicht verschweißte Vertices enthält, kann der Node warnen, dass die Face-Adjazenz niedrig ist, und UV-Charts pro Face erzeugen; ein Erhöhen von `weld_distance` führt zusammenfallende Vertices vor dem Entfalten zusammen. Degenerierte Faces (Faces, die denselben Vertex-Index wiederverwenden) werden während der Verarbeitung verworfen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `mesh` | Das Eingabe-Mesh mit einem generierten UV-Atlas im Bereich [0,1]. Naht-Vertices werden dupliziert, sodass die Vertex-Anzahl der Ausgabe die der Eingabe überschreiten kann. Vertex-Farben und Textur des Eingabe-Meshs bleiben erhalten. | MESH |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UnwrapMesh/de.md)

---
**Source fingerprint (SHA-256):** `fcab6f0b621693d862ee74b5ec498498d2f1f247a66f478704377598a6b39388`
