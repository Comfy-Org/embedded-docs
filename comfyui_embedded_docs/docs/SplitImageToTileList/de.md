# SplitImageToTileList

Der Node „Split Image into List of Tiles“ unterteilt ein einzelnes Eingabebild in eine Reihe kleinerer, überlappender rechteckiger Bereiche, sogenannte Kacheln. Er erzeugt eine Batch-Liste dieser Kacheln, die von anderen Nodes einzeln verarbeitet werden können. Die Größe jeder Kachel und der Überlappungsgrad zwischen ihnen können angegeben werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image` | Das Eingabebild, das in Kacheln aufgeteilt werden soll. | IMAGE | Ja | - |
| `tile_width` | Die Breite jeder Ausgabekachel in Pixeln (Standard: 1024). | INT | Ja | 64 bis 1048576 |
| `tile_height` | Die Höhe jeder Ausgabekachel in Pixeln (Standard: 1024). | INT | Ja | 64 bis 1048576 |
| `overlap` | Die Anzahl der Pixel, um die sich benachbarte Kacheln überlappen (Standard: 128). | INT | Ja | 0 bis 4096 |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Eine Batch-Liste, die alle einzelnen Bildkacheln enthält. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitImageToTileList/de.md)

---
**Source fingerprint (SHA-256):** `4a04e7042446c2368091ffd051c781f9f0ec8496ab681ee9e0741bb269bb54af`
