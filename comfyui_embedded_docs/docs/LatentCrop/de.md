# latent zuschneiden

Der LatentCrop-Node ist dafür ausgelegt, Zuschneideoperationen an latenten Repräsentationen von Bildern durchzuführen. Er ermöglicht die Angabe der Zuschneideabmessungen und -position, wodurch gezielte Änderungen des latenten Raums möglich sind.

## Eingaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `samples` | Der Parameter `samples` repräsentiert die latenten Repräsentationen, die zugeschnitten werden sollen. Er ist entscheidend für die Definition der Daten, auf denen die Zuschneideoperation ausgeführt wird. | `LATENT` |
| `width` | Gibt die Breite des Zuschneidebereichs an. Sie beeinflusst direkt die Abmessungen der ausgegebenen latenten Repräsentation. | `INT` |
| `height` | Gibt die Höhe des Zuschneidebereichs an und beeinflusst die Größe der resultierenden zugeschnittenen latenten Repräsentation. | `INT` |
| `x` | Bestimmt die Anfangs-x-Koordinate des Zuschneidebereichs und beeinflusst die Position des Zuschnitts innerhalb der ursprünglichen latenten Repräsentation. | `INT` |
| `y` | Bestimmt die Anfangs-y-Koordinate des Zuschneidebereichs und legt die Position des Zuschnitts innerhalb der ursprünglichen latenten Repräsentation fest. | `INT` |

## Ausgaben

| Parameter | Beschreibung | Datentyp |
| --- | --- | --- |
| `latent` | Die Ausgabe ist eine modifizierte latente Repräsentation, auf die der angegebene Zuschnitt angewendet wurde. | `LATENT` |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCrop/de.md)
