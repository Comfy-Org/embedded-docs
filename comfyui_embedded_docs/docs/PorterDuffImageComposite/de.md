# PorterDuffImageComposite

Der Node `PorterDuffImageComposite` ist für die Durchführung von Bild-Compositing unter Verwendung der Porter-Duff-Compositing-Operatoren konzipiert. Er ermöglicht die Kombination von Quell- und Zielbildern gemäß verschiedenen Mischmodi, wodurch komplexe visuelle Effekte durch Manipulation der Bildtransparenz und kreatives Überlagern von Bildern erzeugt werden können.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `source` | Der Tensor des Quellbilds, das über das Zielbild gelegt werden soll. Er spielt eine entscheidende Rolle für das endgültige visuelle Ergebnis basierend auf dem ausgewählten Compositing-Modus. | `IMAGE` |
| `source_alpha` | Der Alphakanal des Quellbilds, der die Transparenz jedes Pixels im Quellbild angibt. Er beeinflusst, wie das Quellbild mit dem Zielbild vermischt wird. | `MASK` |
| `destination` | Der Tensor des Zielbilds, das als Hintergrund dient, über den das Quellbild gelegt wird. Er trägt basierend auf dem Mischmodus zum endgültigen zusammengesetzten Bild bei. | `IMAGE` |
| `destination_alpha` | Der Alphakanal des Zielbilds, der die Transparenz der Pixel des Zielbilds definiert. Er beeinflusst die Vermischung von Quell- und Zielbild. | `MASK` |
| `mode` | Der anzuwendende Porter-Duff-Compositing-Modus, der bestimmt, wie Quell- und Zielbild miteinander vermischt werden. Jeder Modus erzeugt unterschiedliche visuelle Effekte. | COMBO[STRING] |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das zusammengesetzte Bild, das sich aus der Anwendung des angegebenen Porter-Duff-Modus ergibt. | `IMAGE` |
| `mask` | Der Alphakanal des zusammengesetzten Bilds, der die Transparenz jedes Pixels angibt. | `MASK` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PorterDuffImageComposite/de.md)
