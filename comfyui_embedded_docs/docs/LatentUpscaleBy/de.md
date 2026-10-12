# latent skalieren um

Der Node LatentUpscaleBy ist für das Hochskalieren latenter Darstellungen von Bildern konzipiert. Er ermöglicht die Anpassung des Skalierungsfaktors und der Methode zum Hochskalieren und bietet dadurch Flexibilität bei der Verbesserung der Auflösung latenter Samples.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `samples` | Die latente Darstellung der Bilder, die hochskaliert werden sollen. Dieser Parameter ist entscheidend für die Bestimmung der Eingabedaten, die dem Hochskalierungsprozess unterzogen werden. | `LATENT` |
| `upscale_method` | Gibt die Methode an, die zum Hochskalieren der latenten Samples verwendet wird. Die Wahl der Methode kann die Qualität und die Eigenschaften der hochskalierten Ausgabe erheblich beeinflussen. | COMBO[STRING] |
| `scale_by` | Bestimmt den Faktor, um den die latenten Samples skaliert werden. Dieser Parameter beeinflusst direkt die Auflösung der Ausgabe und ermöglicht eine präzise Steuerung des Hochskalierungsprozesses. | `FLOAT` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `latent` | Die hochskalierte latente Darstellung, bereit für weitere Verarbeitungs- oder Generierungsaufgaben. Diese Ausgabe ist wesentlich für die Verbesserung der Auflösung generierter Bilder oder für nachfolgende Modelloperationen. | `LATENT` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleBy/de.md)
