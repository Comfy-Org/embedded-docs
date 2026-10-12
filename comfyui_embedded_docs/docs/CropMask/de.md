# CropMask

Der CropMask-Node dient zum Zuschneiden eines angegebenen Bereichs aus einer gegebenen Maske. Er ermöglicht es Benutzern, den gewünschten Bereich durch Angabe von Koordinaten und Abmessungen zu definieren und so einen Teil der Maske für die weitere Verarbeitung oder Analyse zu extrahieren.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `mask` | Die Maskeingabe stellt das zuzuschneidende Maskenbild dar. Sie ist erforderlich, um den zu extrahierenden Bereich anhand der angegebenen Koordinaten und Abmessungen festzulegen. | MASK |
| `x` | Die x-Koordinate gibt den Startpunkt auf der horizontalen Achse an, an dem das Zuschneiden beginnen soll. | INT |
| `y` | Die y-Koordinate bestimmt den Startpunkt auf der vertikalen Achse für den Zuschneidevorgang. | INT |
| `width` | Die Breite definiert die horizontale Ausdehnung des Zuschneidebereichs ab dem Startpunkt. | INT |
| `height` | Die Höhe gibt die vertikale Ausdehnung des Zuschneidebereichs ab dem Startpunkt an. | INT |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `mask` | Die Ausgabe ist eine zugeschnittene Maske, also ein Teil der ursprünglichen Maske, der durch die angegebenen Koordinaten und Abmessungen definiert ist. | MASK |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CropMask/de.md)
