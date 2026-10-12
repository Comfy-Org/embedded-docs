# EmptyChromaRadianceLatentImage

Der Node EmptyChromaRadianceLatentImage erzeugt ein leeres latentes Bild mit den von Ihnen angegebenen Abmessungen, zur Verwendung in Chroma-Radiance-Workflows. Er erzeugt einen Tensor, der mit Nullen gefüllt ist und als Ausgangspunkt für Operationen im latenten Raum dient, sodass Sie die Breite, Höhe und Batch-Größe des leeren latenten Bildes definieren können.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `width` | Die Breite des latenten Bildes in Pixeln (Standard: 1024) | INT | Ja | 16 bis MAX_RESOLUTION |
| `height` | Die Höhe des latenten Bildes in Pixeln (Standard: 1024) | INT | Ja | 16 bis MAX_RESOLUTION |
| `batch_size` | Die Anzahl der latenten Bilder, die in einem Batch generiert werden (Standard: 1) | INT | Ja | 1 bis 4096 |

Hinweis: `width` und `height` sind mit einer Schrittweite von 16 definiert, daher werden die Werte in Vielfachen von 16 angepasst.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `samples` | Der generierte leere latente Bild-Tensor, gefüllt mit Nullen, mit der Form batch_size x 3 x height x width | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyChromaRadianceLatentImage/de.md)

---
**Source fingerprint (SHA-256):** `870cc89fb021c258c214db153cda0a32a63da1b6bf92f09cbd3b8498c363096b`
