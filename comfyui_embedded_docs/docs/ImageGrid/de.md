# ImageGrid

Der Image-Grid-Node kombiniert mehrere Bilder zu einem einzelnen, organisierten Raster oder einer Collage. Er nimmt eine Liste von Bildern entgegen und ordnet sie in einer festgelegten Anzahl von Spalten an, wobei er jedes Bild auf eine definierte Zellgröße skaliert und optional Abstand zwischen ihnen hinzufügt. Das Ergebnis ist ein einzelnes neues Bild, das alle Eingabebilder in einem Rasterlayout enthält.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `images` | Eine Liste von Bildern, die im Raster angeordnet werden. Der Node benötigt mindestens ein Bild, um zu funktionieren. | IMAGE | Ja | - |
| `columns` | Die Anzahl der Spalten im Raster (Standard: 4). | INT | Nein | 1 - 20 |
| `cell_width` | Die Breite jeder Zelle im Raster in Pixeln (Standard: 256). | INT | Nein | 32 - 2048 |
| `cell_height` | Die Höhe jeder Zelle im Raster in Pixeln (Standard: 256). | INT | Nein | 32 - 2048 |
| `padding` | Der Abstand in Pixeln, der zwischen den Bildern im Raster eingefügt wird (Standard: 4). | INT | Nein | 0 - 50 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das einzelne Ausgabebild, das alle Eingabebilder in einem Raster angeordnet enthält. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageGrid/de.md)

---
**Source fingerprint (SHA-256):** `87bc0af8af33a0fd703f13fec782075502c9562847fa3887a2273afa5b28c47e`
