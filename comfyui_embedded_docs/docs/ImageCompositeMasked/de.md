# ImageCompositeMasked

Der `ImageCompositeMasked`-Node ist für das Compositing von Bildern konzipiert. Er ermöglicht das Überlagern eines Quellbilds auf ein Zielbild an angegebenen Koordinaten, mit optionaler Größenänderung und Maskierung.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `destination` | Das Zielbild, auf das das Quellbild composited wird. Es dient als Hintergrund für die Compositing-Operation. | `IMAGE` |
| `source` | Das Quellbild, das auf das Zielbild composited wird. Dieses Bild kann optional an die Abmessungen des Zielbilds angepasst werden. | `IMAGE` |
| `x` | Die x-Koordinate im Zielbild, an der die obere linke Ecke des Quellbilds platziert wird. | `INT` |
| `y` | Die y-Koordinate im Zielbild, an der die obere linke Ecke des Quellbilds platziert wird. | `INT` |
| `resize_source` | Ein boolesches Flag, das angibt, ob das Quellbild an die Abmessungen des Zielbilds angepasst werden soll. | `BOOLEAN` |
| `mask` | Eine optionale Maske, die angibt, welche Teile des Quellbilds auf das Zielbild composited werden sollen. Dies ermöglicht komplexere Compositing-Operationen wie Überblendungen oder teilweise Überlagerungen. | `MASK` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das resultierende Bild nach der Compositing-Operation, das Elemente aus beiden Bildern kombiniert. | `IMAGE` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompositeMasked/de.md)
