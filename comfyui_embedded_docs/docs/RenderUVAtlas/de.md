# RenderUVAtlas

Rendert das UV-Layout eines Meshes als Bild. Jede zusammenhängende UV-Region (Chart) wird mit einer jeweils eigenen Farbe gefüllt, und die Randkanten der Charts werden auf dunkelgrauem Hintergrund schwarz umrandet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `mesh` | Das 3D-Mesh, dessen UV-Layout gerendert werden soll. Das Mesh muss UV-Koordinaten besitzen; andernfalls löst der Node den Fehler „mesh has no UVs to render. Run UnwrapMesh first.“ aus. | MESH | Ja | - |
| `resolution` | Die Breite und Höhe des gerenderten quadratischen Bildes in Pixeln (Standard: 1024). | INT | Ja | 64 bis 4096 (Schrittweite 64) |

Hinweis: Wenn das Mesh eine Batch-Dimension enthält (3D-UV- oder Face-Arrays), wird nur das erste Element des Batches gerendert.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `image` | Das gerenderte UV-Atlas-Bild, zurückgegeben als Batch mit einem einzelnen Bild. Jedes UV-Chart wird eingefärbt, und die Randkanten der Charts werden schwarz umrandet. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenderUVAtlas/de.md)

---
**Source fingerprint (SHA-256):** `b462101036418350390ffed621e583c6de14d5ea34d1e427342dc44ec3fd1922`
