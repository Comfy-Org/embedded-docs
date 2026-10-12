# LatentFlip

Der LatentFlip-Node dient dazu, latente Repräsentationen durch vertikales oder horizontales Spiegeln zu manipulieren. Diese Operation ermöglicht die Transformation des latenten Raums und kann möglicherweise neue Variationen oder Perspektiven innerhalb der Daten aufdecken.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `samples` | Der Parameter `samples` repräsentiert die latenten Repräsentationen, die gespiegelt werden sollen. Die Spiegelungsoperation verändert diese Repräsentationen abhängig vom Parameter `flip_method` entweder vertikal oder horizontal und transformiert somit die Daten im latenten Raum. | `LATENT` |
| `flip_method` | Der Parameter `flip_method` gibt die Achse an, entlang derer die latenten Samples gespiegelt werden. Er kann entweder 'x-axis: vertically' oder 'y-axis: horizontally' sein, wodurch die Richtung der Spiegelung und damit die Art der auf die latenten Repräsentationen angewendeten Transformation bestimmt wird. | COMBO[STRING] |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `latent` | Die Ausgabe ist eine modifizierte Version der latenten Eingaberepräsentationen, die gemäß der angegebenen Methode gespiegelt wurden. Diese Transformation kann neue Variationen innerhalb des latenten Raums einführen. | `LATENT` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentFlip/de.md)
