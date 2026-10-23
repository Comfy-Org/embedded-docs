# VaeDecode

Der Node VAEDecode dient zum Dekodieren latenter Repräsentationen in Bilder unter Verwendung eines angegebenen Variational Autoencoders (VAE). Er erfüllt den Zweck, Bilder aus komprimierten Datenrepräsentationen zu erzeugen, und ermöglicht die Rekonstruktion von Bildern aus ihren Kodierungen im latenten Raum.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `samples` | Der Parameter `samples` repräsentiert die latenten Repräsentationen, die in Bilder dekodiert werden sollen. Er ist entscheidend für den Dekodierungsprozess, da er die komprimierten Daten bereitstellt, aus denen die Bilder rekonstruiert werden. | `LATENT` |
| `vae` | Der Parameter `vae` gibt das Variational-Autoencoder-Modell an, das zur Dekodierung der latenten Repräsentationen in Bilder verwendet werden soll. Er ist wesentlich für die Bestimmung des Dekodierungsmechanismus und der Qualität der rekonstruierten Bilder. | VAE |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Die Ausgabe ist ein Bild, das aus der bereitgestellten latenten Repräsentation unter Verwendung des angegebenen VAE-Modells rekonstruiert wurde. | `IMAGE` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecode/de.md)
