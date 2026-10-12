# Mesh-Normalen glätten

Berechnen Sie glatte Normalen pro Vertex für ein Mesh und hängen Sie diese an. Meshes ohne Normalen werden von glTF-Viewern flach (pro Fläche) schattiert; dieser Node sorgt dafür, dass sie glatt schattiert werden. Bei einem Knickwinkel unter 180 werden Kanten, die schärfer als der Schwellenwert sind, hart gehalten, indem Vertices entlang dieser geteilt werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `mesh` | Das zu verarbeitende Eingabe-Mesh. | MESH | Ja | - |
| `crease_angle` | Kanten, deren Diederwinkel diesen Wert (Grad) überschreitet, bleiben hart (Vertices werden geteilt). 180 = vollständig glatt; niedrigere Werte erhalten scharfe Kanten (z. B. ~30-60 für Hard-Surface). Standard: 180.0. | FLOAT | Ja | 0.0 bis 180.0 (Schrittweite 1.0) |

Wenn `crease_angle` 180 oder höher ist, bleibt die Mesh-Topologie unverändert. Wenn der Wert unter 180 gesetzt wird, werden Vertices entlang harter Kanten geteilt, was die Vertex-Anzahl erhöhen kann. Wenn Vertices geteilt werden, werden Daten pro Vertex (Farben, UVs und Tangenten) dupliziert, um dem neuen Vertex-Layout zu entsprechen, und das resultierende Mesh wird als Batch variabler Größe neu aufgebaut.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `mesh` | Das Eingabe-Mesh mit angehängten glatten Normalendaten oder mit geteilten Vertices und Normalen, wenn ein Knickwinkel festgelegt ist. | MESH |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshSmoothNormals/de.md)

---
**Source fingerprint (SHA-256):** `bbe9c0fba68369d8e9d3fb68e635869233804f3aac458e7c217d94977e77b9be`
