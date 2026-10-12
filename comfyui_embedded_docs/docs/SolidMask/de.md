# SolidMask

Der SolidMask-Node erzeugt eine gleichmäßige Maske mit einem angegebenen Wert über ihre gesamte Fläche. Er wurde entwickelt, um Masken mit bestimmten Abmessungen und Intensität zu erstellen, was bei verschiedenen Bildverarbeitungs- und Maskierungsaufgaben nützlich ist.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `value` | Legt den Intensitätswert der Maske fest und beeinflusst ihr Gesamtbild sowie ihren Nutzen in nachfolgenden Operationen. | FLOAT |
| `width` | Bestimmt die Breite der erzeugten Maske und beeinflusst direkt ihre Größe und ihr Seitenverhältnis. | INT |
| `height` | Legt die Höhe der erzeugten Maske fest und beeinflusst ihre Größe und ihr Seitenverhältnis. | INT |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `mask` | Gibt eine gleichmäßige Maske mit den angegebenen Abmessungen und dem angegebenen Wert aus. | MASK |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SolidMask/de.md)
