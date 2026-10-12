# ImageBlend

Der Node `ImageBlend` dient dazu, zwei Bilder basierend auf einem angegebenen Mischmodus und Mischfaktor miteinander zu mischen. Er unterstützt verschiedene Mischmodi wie normal, multiply, screen, overlay, soft light und difference und ermöglicht so vielseitige Bildmanipulations- und Compositing-Techniken. Dieser Node ist unerlässlich, um zusammengesetzte Bilder zu erstellen, indem die visuelle Interaktion zwischen zwei Bildebenen angepasst wird.

## Eingaben

| Feld | Beschreibung | Datentyp |
| --- | --- | --- |
| `image1` | Das erste zu mischende Bild. Es dient als Basisebene für den Mischvorgang. | `IMAGE` |
| `image2` | Das zweite zu mischende Bild. Abhängig vom Mischmodus verändert es das Erscheinungsbild des ersten Bildes. | `IMAGE` |
| `blend_factor` | Bestimmt die Gewichtung des zweiten Bildes in der Mischung. Ein höherer Mischfaktor verleiht dem zweiten Bild im resultierenden Mischergebnis mehr Gewicht. | `FLOAT` |
| `blend_mode` | Gibt die Methode zum Mischen der beiden Bilder an. Unterstützt Modi wie normal, multiply, screen, overlay, soft light und difference, die jeweils einen eigenen visuellen Effekt erzeugen. | COMBO[STRING] |

## Ausgaben

| Feld | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das resultierende Bild nach dem Mischen der beiden Eingabebilder gemäß dem angegebenen Mischmodus und Faktor. | `IMAGE` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageBlend/de.md)
