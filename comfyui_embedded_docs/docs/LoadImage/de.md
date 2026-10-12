# Bild laden

Der LoadImage-Node dient zum Laden und Vorverarbeiten von Bildern von einem angegebenen Pfad. Er verarbeitet Bildformate mit mehreren Frames, wendet erforderliche Transformationen wie Drehung basierend auf EXIF-Daten an, normalisiert Pixelwerte und erzeugt optional eine Maske für Bilder mit einem Alphakanal. Dieser Node ist unerlässlich, um Bilder für die weitere Verarbeitung oder Analyse innerhalb einer Pipeline vorzubereiten.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Der Parameter `image` gibt die Kennung des zu ladenden und zu verarbeitenden Bildes an. Er ist entscheidend, um den Pfad zur Bilddatei zu bestimmen und anschließend das Bild zum Transformieren und Normalisieren zu laden. | COMBO[STRING] |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `image` | Das verarbeitete Bild mit normalisierten Pixelwerten und bei Bedarf angewendeten Transformationen. Es ist bereit für die weitere Verarbeitung oder Analyse. | `IMAGE` |
| `mask` | Eine optionale Ausgabe, die eine Maske für das Bild bereitstellt; nützlich in Szenarien, in denen das Bild einen Alphakanal für Transparenz enthält. | `MASK` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImage/de.md)
