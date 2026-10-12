# PrimitiveBoundingBox

Der Node PrimitiveBoundingBox erstellt einen einfachen rechteckigen Bereich, der durch seine Position und Größe definiert ist. Er verwendet X- und Y-Koordinaten für die obere linke Ecke sowie Werte für Breite und Höhe und gibt eine Bounding-Box-Datenstruktur aus, die von anderen Nodes in einem Workflow verwendet werden kann.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `x` | Die X-Koordinate für die obere linke Ecke der Bounding-Box (Standard: 0). | INT | Ja | 0 bis 16384 |
| `y` | Die Y-Koordinate für die obere linke Ecke der Bounding-Box (Standard: 0). | INT | Ja | 0 bis 16384 |
| `width` | Die Breite der Bounding-Box (Standard: 512). | INT | Ja | 1 bis 16384 |
| `height` | Die Höhe der Bounding-Box (Standard: 512). | INT | Ja | 1 bis 16384 |

Hinweis: Alle Maximalwerte folgen der MAX_RESOLUTION-Konstante von ComfyUI, welche die größte Bildabmessung definiert, die der Node akzeptiert.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `bounding_box` | Eine Datenstruktur, die die Eigenschaften `x`, `y`, `width` und `height` des definierten Rechtecks enthält. | BOUNDING_BOX |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveBoundingBox/de.md)

---
**Source fingerprint (SHA-256):** `dc50286b09b8aaf7ff21eb699b9a04317f099b3deedb6cb7d4a1ec7668edeb97`
