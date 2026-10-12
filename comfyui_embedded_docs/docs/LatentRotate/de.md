# latent drehen

Der LatentRotate-Node dient dazu, latente Repräsentationen von Bildern um bestimmte Winkel zu drehen. Er abstrahiert die Komplexität der Manipulation des latenten Raums, um Rotationseffekte zu erzielen, und ermöglicht es Anwendern, Bilder im latenten Raum eines generativen Modells auf einfache Weise zu transformieren.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `samples` | Der Parameter `samples` repräsentiert die latenten Repräsentationen der zu drehenden Bilder. Er ist entscheidend für die Bestimmung des Ausgangspunkts der Drehoperation. | `LATENT` |
| `rotation` | Der Parameter `rotation` gibt den Winkel an, um den die latenten Bilder gedreht werden sollen. Er beeinflusst direkt die Ausrichtung der resultierenden Bilder. | COMBO[STRING] |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `latent` | Die Ausgabe ist eine modifizierte Version der latenten Eingaberepräsentationen, gedreht um den angegebenen Winkel. | `LATENT` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentRotate/de.md)
