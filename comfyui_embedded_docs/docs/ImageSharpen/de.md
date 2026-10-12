# Bild schärfen

Der ImageSharpen-Node verbessert die Klarheit eines Bildes, indem er dessen Kanten und Details betont. Er wendet einen Schärfungsfilter auf das Bild an, dessen Intensität und Radius angepasst werden können, wodurch das Bild definierter und schärfer erscheint.

## Eingaben

| Feld | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das zu schärfende Eingabebild. Dieser Parameter ist entscheidend, da er das Basisbild bestimmt, auf das der Schärfungseffekt angewendet wird. | `IMAGE` |
| `sharpen_radius` | Definiert den Radius des Schärfungseffekts. Ein größerer Radius bedeutet, dass mehr Pixel um die Kante herum beeinflusst werden, was zu einem ausgeprägteren Schärfungseffekt führt. | `INT` |
| `sigma` | Steuert die Ausbreitung des Schärfungseffekts. Ein höherer Sigma-Wert führt zu einem weicheren Übergang an den Kanten, während ein niedrigerer Sigma-Wert die Schärfung lokaler macht. | `FLOAT` |
| `alpha` | Passt die Intensität des Schärfungseffekts an. Höhere Alpha-Werte führen zu einem stärkeren Schärfungseffekt. | `FLOAT` |

## Ausgaben

| Feld | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das geschärfte Bild mit verbesserten Kanten und Details, bereit für die weitere Verarbeitung oder Anzeige. | `IMAGE` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageSharpen/de.md)
