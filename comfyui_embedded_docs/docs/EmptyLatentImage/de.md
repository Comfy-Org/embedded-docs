# EmptyLatentImage

Der Node `EmptyLatentImage` dient dazu, eine leere Darstellung im latenten Raum mit angegebenen Abmessungen und Batch-Größe zu erzeugen. Dieser Node bildet einen grundlegenden Schritt bei der Generierung oder Bearbeitung von Bildern im latenten Raum und bietet einen Ausgangspunkt für weitere Bildsynthese- oder Änderungsprozesse.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `width` | Gibt die Breite des zu generierenden Latent-Bildes an. Dieser Parameter beeinflusst direkt die räumlichen Abmessungen der resultierenden latenten Darstellung. | `INT` |
| `height` | Bestimmt die Höhe des zu generierenden Latent-Bildes. Dieser Parameter ist entscheidend für die Definition der räumlichen Abmessungen der Darstellung im latenten Raum. | `INT` |
| `batch_size` | Steuert die Anzahl der in einem einzelnen Batch zu generierenden latenten Bilder. Dies ermöglicht die gleichzeitige Generierung mehrerer latenter Darstellungen und erleichtert die Stapelverarbeitung. | `INT` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `latent` | Die Ausgabe ist ein Tensor, der einen Batch leerer Latent-Bilder repräsentiert und als Basis für die weitere Bildgenerierung oder -bearbeitung im latenten Raum dient. | `LATENT` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentImage/de.md)
