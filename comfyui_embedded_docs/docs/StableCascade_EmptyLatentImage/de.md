# StableCascade_EmptyLatentImage

Der Node StableCascade_EmptyLatentImage erzeugt leere latente Tensoren für Stable-Cascade-Modelle. Er generiert zwei separate latente Repräsentationen – eine für Stufe C und eine für Stufe B – deren Dimensionen aus der Eingabeauflösung und den Kompressionseinstellungen berechnet werden. Dieser Node bietet einen Ausgangspunkt für die Stable-Cascade-Generierungspipeline.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `width` | Die Breite des Ausgabebilds in Pixeln (Standard: 1024, Schrittweite: 8) | INT | Ja | 256 bis MAX_RESOLUTION |
| `height` | Die Höhe des Ausgabebilds in Pixeln (Standard: 1024, Schrittweite: 8) | INT | Ja | 256 bis MAX_RESOLUTION |
| `compression` | Der Kompressionsfaktor, der die latenten Dimensionen für Stufe C bestimmt (Standard: 42, Schrittweite: 1). Dies ist ein erweiterter Parameter. | INT | Ja | 4 bis 128 |
| `batch_size` | Die Anzahl der latenten Samples, die in einem Batch generiert werden (Standard: 1) | INT | Ja | 1 bis 4096 |

Hinweis: Der Wert `compression` steuert die latente Größe von Stufe C: Höhe und Breite ergeben sich aus den Eingaben `height` und `width`, geteilt durch `compression`. Das Latent von Stufe B verwendet immer eine feste Kompression von 4.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
| --- | --- | --- |
| `stage_c` | Der latente Tensor von Stufe C mit Dimensionen [batch_size, 16, height//compression, width//compression] | LATENT |
| `stage_b` | Der latente Tensor von Stufe B mit Dimensionen [batch_size, 4, height//4, width//4] | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_EmptyLatentImage/de.md)

---
**Source fingerprint (SHA-256):** `f336f87d0ec14b3716efda2cfaa194b1f80707d64821bb56ade7d88d9bd5b53f`
