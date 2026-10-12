# Bild für Outpainting auffüllen

Dieser Node ist dafür konzipiert, Bilder für den Outpainting-Prozess vorzubereiten, indem er Padding um sie herum hinzufügt. Er passt die Bildabmessungen an, um die Kompatibilität mit Outpainting-Algorithmen sicherzustellen, und erleichtert so die Generierung erweiterter Bildbereiche über die ursprünglichen Grenzen hinaus.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Die Eingabe `image` ist das primäre Bild, das für Outpainting vorbereitet wird, und dient als Basis für die Padding-Operationen. | `IMAGE` |
| `left` | Gibt an, wie viel Padding links am Bild hinzugefügt werden soll, wodurch der erweiterte Bereich für Outpainting beeinflusst wird. | `INT` |
| `top` | Bestimmt die Menge an Padding, die oben am Bild hinzugefügt werden soll, und beeinflusst die vertikale Erweiterung für Outpainting. | `INT` |
| `right` | Definiert die Menge an Padding, die rechts am Bild hinzugefügt werden soll, und wirkt sich auf die horizontale Erweiterung für Outpainting aus. | `INT` |
| `bottom` | Gibt die Menge an Padding an, die unten am Bild hinzugefügt werden soll, und trägt zur vertikalen Erweiterung für Outpainting bei. | `INT` |
| `feathering` | Steuert die Weichheit des Übergangs zwischen dem Originalbild und dem hinzugefügten Padding, wodurch die visuelle Integration für Outpainting verbessert wird. | `INT` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Die Ausgabe `image` stellt das aufgefüllte Bild dar, bereit für den Outpainting-Prozess. | `IMAGE` |
| `mask` | Die Ausgabe `mask` gibt die Bereiche des Originalbilds und des hinzugefügten Paddings an, was nützlich ist, um die Outpainting-Algorithmen zu steuern. | `MASK` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImagePadForOutpaint/de.md)
