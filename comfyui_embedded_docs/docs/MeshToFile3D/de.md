# MeshToFile3D

Dieser Node serialisiert ein Mesh in ein GLB-Dateiobjekt, das an Save 3D- oder Preview 3D-Nodes übergeben werden kann. Es führt alle Mesh-Daten mit, einschließlich UVs, Farben, Normalen, Textur, Normal-/Occlusion-/Emissive-Maps und Materialeinstellungen. Es wird nur das erste Element eines Batches mit mehreren Elementen verwendet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `mesh` | Das Mesh, das in eine GLB-Datei konvertiert werden soll, einschließlich UVs, Farben, Normalen, Textur, Normal-/Occlusion-/Emissive-Maps und Material. Es wird nur ein Element pro Batch unterstützt; wenn ein Batch mehrere Elemente enthält, wird das erste verwendet. | MESH | Ja | Einzelnes Mesh |

Hinweis: Der Node unterstützt nur ein Element pro Batch. Wenn das eingegebene Mesh mehr als ein Element in seinem Batch enthält, wird eine Warnung protokolliert und das erste Element verwendet. Das Mesh muss mindestens einen Vertex und eine Fläche enthalten; ein leeres Mesh führt zu einem Fehler.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `model_3d` | Ein GLB-(glTF-Binary-)Dateiobjekt, das das serialisierte Mesh enthält und bereit ist, von anderen 3D-Nodes gespeichert oder in der Vorschau angezeigt zu werden. | FILE3D |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshToFile3D/de.md)

---
**Source fingerprint (SHA-256):** `f004c2907c0df2e0127e49b4767d1624bf89c72665fc7028347a0b8a63a5772e`
