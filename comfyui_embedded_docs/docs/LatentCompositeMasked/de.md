# Maskierte Latent-Komposition

Der Node LatentCompositeMasked ist dafür ausgelegt, zwei latente Repräsentationen an angegebenen Koordinaten miteinander zu kombinieren, optional unter Verwendung einer Maske für ein kontrollierteres Zusammensetzen. Dieser Node ermöglicht die Erstellung komplexer latenter Bilder, indem Teile eines Bildes über ein anderes gelegt werden, wobei die Quellbildgröße für eine perfekte Passform angepasst werden kann.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `destination` | Die latente Repräsentation, auf die eine weitere latente Repräsentation gesetzt wird. Dient als Basisebene für die Zusammensetzungsoperation. | `LATENT` |
| `source` | Die latente Repräsentation, die auf das Ziel gesetzt werden soll. Diese Quell-Ebene kann gemäß den angegebenen Parametern skaliert und positioniert werden. | `LATENT` |
| `x` | Die x-Koordinate in der latenten Ziel-Repräsentation, an der die Quelle platziert wird. Ermöglicht eine präzise Positionierung der Quell-Ebene. | `INT` |
| `y` | Die y-Koordinate in der latenten Ziel-Repräsentation, an der die Quelle platziert wird, wodurch eine präzise Positionierung der Überlagerung ermöglicht wird. | `INT` |
| `resize_source` | Ein boolesches Flag, das angibt, ob die latente Quell-Repräsentation vor dem Zusammensetzen an die Abmessungen des Ziels angepasst werden soll. | `BOOLEAN` |
| `mask` | Eine optionale Maske, die verwendet werden kann, um die Überblendung der Quelle auf das Ziel zu steuern. Die Maske legt fest, welche Teile der Quelle in der finalen Zusammensetzung sichtbar sind. | `MASK` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `latent` | Die resultierende latente Repräsentation nach dem Zusammensetzen der Quelle auf das Ziel, möglicherweise unter Verwendung einer Maske für eine selektive Überblendung. | `LATENT` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCompositeMasked/de.md)
