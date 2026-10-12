# CreateBoundingBoxes

Dieser Node stellt eine Canvas-Oberfläche zum Zeichnen von Bounding-Boxen um Objekte oder Textbereiche in einem Bild bereit. Er gibt die Koordinaten der Bounding-Boxen im Pixelraum, strukturierte Elementdaten, die mit der Ideogram-Prompt-Formatierung kompatibel sind, und ein Vorschaubild aus, das die gezeichneten Boxen mit Beschriftungen und Farbpaletten zeigt.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `background` | Optionales Bild, das als Hintergrund in der Canvas und der Vorschau verwendet wird. | IMAGE | Nein | - |
| `bboxes` | Bounding-Boxen, Elemente oder ein JSON-String zum Initialisieren der Canvas. Ein neuer vorgelagerter Wert initialisiert die Canvas; auf der Canvas vorgenommene Änderungen haben Vorrang und bleiben erhalten, bis sich der vorgelagerte Wert erneut ändert. | BOUNDING_BOX, ARRAY, STRING | Nein | - |
| `width` | Breite der Canvas und des Pixelrasters für die Bounding-Boxen (Standard: 1024). | INT | Ja | 64 bis 16384 (Schritt: 16) |
| `height` | Höhe der Canvas und des Pixelrasters für die Bounding-Boxen (Standard: 1024). | INT | Ja | 64 bis 16384 (Schritt: 16) |
| `editor_state` | Bounding-Boxen zeichnen und für jede Box Typ, Text, Beschreibung und Farbpalette festlegen. Zuerst mit dem Hintergrund-Element beginnen, zuletzt mit dem Vordergrund-Element. | BOUNDING_BOXES | Ja | - |
| `last_incoming` | Interner, von der Canvas verwalteter Zustand: der vorgelagerte `bboxes`-Wert, der sie zuletzt initialisiert hat. Leer lassen, um die Canvas beim nächsten Lauf aus der Eingabe `bboxes` erneut zu initialisieren. | BOUNDING_BOXES | Nein | - |

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `preview` | Ein RGB-Bild, das die Canvas mit allen gerenderten Bounding-Boxen zeigt, einschließlich Beschriftungen, Farbfeldern der Farbpalette und beschreibendem Text. | IMAGE |
| `bboxes` | Eine Liste von Bounding-Boxen in Pixelkoordinaten, wobei jede Box Werte für x, y, width und height enthält. | BOUNDING_BOX |
| `elements` | Ein strukturiertes Array von Elementobjekten, die jeweils Typ, Bounding-Box-Koordinaten (normalisiert 0-1000), Text (für den Elementtyp Text), Beschreibung und Farbpalette enthalten. | ARRAY |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateBoundingBoxes/de.md)

---
**Source fingerprint (SHA-256):** `dc5545dffefdccf14f3919ff4d9966dbfd1a497dcd64e1863556d5728659ee94`
