# CropByBBoxes

Der Node CropByBBoxes extrahiert und skaliert bestimmte rechteckige Bereiche aus einem Eingabe-Bildstapel. Er verwendet die bereitgestellten Bounding-Box-Koordinaten, um den Bereich zu definieren, der aus jedem Bild zugeschnitten werden soll. Die zugeschnittenen Bereiche werden anschließend auf eine angegebene Ausgabegröße skaliert, wobei die Option besteht, den Ausschnitt entweder zu strecken oder ihn mit Padding zu versehen, um sein ursprüngliches Seitenverhältnis beizubehalten.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `image` | Der Eingabe-Bildstapel, aus dem zugeschnitten werden soll. | IMAGE | Ja | - |
| `bboxes` | Die Liste der Bounding-Boxen, die die zuzuschneidenden Bereiche definieren. Dieser Eingang ist obligatorisch, d. h. er muss verbunden werden. | BOUNDINGBOX | Ja | - |
| `output_width` | Die Breite, auf die jeder Ausschnitt skaliert wird (Standard: 512). | INT | Nein | 64 - 4096 |
| `output_height` | Die Höhe, auf die jeder Ausschnitt skaliert wird (Standard: 512). | INT | Nein | 64 - 4096 |
| `padding` | Zusätzliches Padding in Pixeln, das vor dem Zuschneiden auf jeder Seite der Bounding-Box hinzugefügt wird (Standard: 0). | INT | Nein | 0 - 1024 |
| `keep_aspect` | Ob der Ausschnitt gestreckt werden soll, um in die Ausgabegröße zu passen, oder ob er mit schwarzen Pixeln aufgefüllt werden soll, um sein Seitenverhältnis beizubehalten (Standard: "stretch"). | COMBO | Nein | `"stretch"`<br>`"pad"` |

**Hinweis:** Der Node verarbeitet jeweils ein Einzelbild. Wenn für ein einzelnes Einzelbild mehrere Bounding-Boxen bereitgestellt werden, berechnet er einen einzelnen Zuschneidebereich, der die Vereinigung (das kleinste Rechteck, das alle Boxen enthält) aller bereitgestellten Boxen ist. Wenn ein berechneter Zuschneidebereich ungültig ist (z. B. Breite oder Höhe von null), erstellt der Node einen Fallback-Zuschnitt von der oberen Mitte des Bildes.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Alle zugeschnittenen und skalierten Bereiche, zu einem einzelnen Bildstapel gestapelt. | IMAGE |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CropByBBoxes/de.md)

---
**Source fingerprint (SHA-256):** `7524d629e61f5af2475f819bc9431d4f4173feb5ad59f9bcf81d822330fb3e22`
