# VaeEncode

Dieser Node ist dafür ausgelegt, Bilder mithilfe eines angegebenen VAE-Modells in eine Latent-Raum-Darstellung zu kodieren. Er abstrahiert die Komplexität des Kodierungsprozesses und bietet einen unkomplizierten Weg, Bilder in ihre Latent-Repräsentationen umzuwandeln.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `pixels` | Der Parameter `pixels` repräsentiert die Bilddaten, die in den Latent-Raum kodiert werden sollen. Er spielt eine entscheidende Rolle bei der Bestimmung der ausgegebenen Latent-Repräsentation, indem er als direkte Eingabe für den Kodierungsprozess dient. | `IMAGE` |
| `vae` | Der Parameter `vae` gibt das Variational-Autoencoder-Modell an, das zur Kodierung der Bilddaten in den Latent-Raum verwendet werden soll. Er ist wesentlich für die Definition des Kodierungsmechanismus und der Eigenschaften der erzeugten Latent-Repräsentation. | VAE |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `latent` | Die Ausgabe ist eine Latent-Raum-Darstellung des Eingabebildes, die dessen wesentliche Merkmale in komprimierter Form zusammenfasst. | `LATENT` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeEncode/de.md)
