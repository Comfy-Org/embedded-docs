# LatentAdd

Der LatentAdd-Node dient der Addition zweier latenter Repräsentationen. Er ermöglicht die Kombination von Merkmalen oder Eigenschaften, die in diesen Repräsentationen kodiert sind, durch elementweise Addition.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `samples1` | Der erste Satz latenter Samples, der addiert werden soll. Er stellt einen der Eingaben dar, deren Merkmale mit einem anderen Satz latenter Samples kombiniert werden sollen. | `LATENT` |
| `samples2` | Der zweite Satz latenter Samples, der addiert werden soll. Er dient als die andere Eingabe, deren Merkmale durch elementweise Addition mit dem ersten Satz latenter Samples kombiniert werden. | `LATENT` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `latent` | Das Ergebnis der elementweisen Addition zweier latenter Samples, das einen neuen Satz latenter Samples darstellt, der die Merkmale beider Eingaben kombiniert. | `LATENT` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentAdd/de.md)
