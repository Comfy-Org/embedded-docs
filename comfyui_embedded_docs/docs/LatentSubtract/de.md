# LatentSubtract

Der LatentSubtract-Node dient dazu, eine latente Repräsentation von einer anderen zu subtrahieren. Diese Operation kann verwendet werden, um die Eigenschaften der Ausgaben generativer Modelle zu manipulieren oder zu verändern, indem Merkmale oder Attribute, die in einem latenten Raum repräsentiert sind, effektiv aus einem anderen entfernt werden.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `samples1` | Der erste Satz latenter Samples, von dem subtrahiert wird. Er dient als Basis für die Subtraktionsoperation. | `LATENT` |
| `samples2` | Der zweite Satz latenter Samples, der vom ersten Satz subtrahiert wird. Diese Operation kann die Ausgabe des resultierenden generativen Modells verändern, indem Attribute oder Merkmale entfernt werden. | `LATENT` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `latent` | Das Ergebnis der Subtraktion des zweiten Satzes latenter Samples vom ersten. Diese modifizierte latente Repräsentation kann für weitere generative Aufgaben verwendet werden. | `LATENT` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentSubtract/de.md)
