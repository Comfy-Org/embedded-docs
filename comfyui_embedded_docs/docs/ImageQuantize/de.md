# ImageQuantize

Der Node ImageQuantize dient dazu, die Anzahl der Farben in einem Bild auf einen angegebenen Wert zu reduzieren, wobei optional Dithering-Techniken angewendet werden, um die visuelle Qualität zu erhalten. Dieser Prozess ist nützlich, um palettenbasierte Bilder zu erstellen oder die Farbkomplexität für bestimmte Anwendungen zu verringern.

## Eingaben

| Feld | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Der Eingabe-Bildtensor, der quantisiert werden soll. Er beeinflusst die Ausführung des Nodes, da er die primären Daten darstellt, auf denen die Farbreduktion durchgeführt wird. | `IMAGE` |
| `colors` | Gibt die Anzahl der Farben an, auf die das Bild reduziert werden soll. Beeinflusst direkt den Quantisierungsprozess, indem die Größe der Farbpalette bestimmt wird. | `INT` |
| `dither` | Bestimmt die Dithering-Technik, die während der Quantisierung angewendet werden soll, und beeinflusst die visuelle Qualität und das Erscheinungsbild des Ausgabebilds. | COMBO[STRING] |

## Ausgaben

| Feld | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Die quantisierte Version des Eingabebilds mit reduzierter Farbkomplexität und optional gedithert, um die visuelle Qualität zu erhalten. | `IMAGE` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageQuantize/de.md)
