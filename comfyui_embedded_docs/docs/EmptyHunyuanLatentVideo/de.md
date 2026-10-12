# Leeres Hunyuan Video 1.0 Latent

Der Node `EmptyHunyuanLatentVideo` ähnelt dem Node `EmptyLatentImage`. Man kann ihn als leere Leinwand für die Videogenerierung betrachten, wobei Breite, Höhe und Länge die Eigenschaften der Leinwand definieren und die Batch-Größe die Anzahl der zu erstellenden Leinwände bestimmt. Dieser Node erstellt leere Leinwände, die für nachfolgende Videogenerierungsaufgaben bereit sind.

## Eingaben

| Parameter | Beschreibung | Comfy-Typ |
| --- | --- | --- |
| `width` | Videobreite, Standard 848, Minimum 16, Maximum `nodes.MAX_RESOLUTION`, Schrittweite 16. | `INT` |
| `height` | Videohöhe, Standard 480, Minimum 16, Maximum `nodes.MAX_RESOLUTION`, Schrittweite 16. | `INT` |
| `length` | Videolänge, Standard 25, Minimum 1, Maximum `nodes.MAX_RESOLUTION`, Schrittweite 4. | `INT` |
| `batch_size` | Batch-Größe, Standard 1, Minimum 1, Maximum 4096. | `INT` |

## Ausgaben

| Parameter | Beschreibung | Comfy-Typ |
| --- | --- | --- |
| `samples` | Generierte latente Video-Samples, die Null-Tensoren enthalten und für Verarbeitungs- und Generierungsaufgaben bereit sind. | `LATENT` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanLatentVideo/de.md)
