# Leeres Cosmos Latent-Video

EmptyCosmosLatentVideo erstellt einen leeren latenten Video-Tensor mit den angegebenen Dimensionen. Er generiert eine mit Nullen gefüllte latente Repräsentation, die als Ausgangspunkt für Videogenerierungs-Workflows verwendet werden kann, mit konfigurierbaren Parametern für Breite, Höhe, Länge und Batch-Größe.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `width` | Die Breite des latenten Videos in Pixeln (Standard: 1280, in 16er-Schritten) | INT | Ja | 16 bis MAX_RESOLUTION |
| `height` | Die Höhe des latenten Videos in Pixeln (Standard: 704, in 16er-Schritten) | INT | Ja | 16 bis MAX_RESOLUTION |
| `length` | Die Anzahl der Frames im latenten Video (Standard: 121, in 8er-Schritten) | INT | Ja | 1 bis MAX_RESOLUTION |
| `batch_size` | Die Anzahl der latenten Videos, die in einem Batch generiert werden (Standard: 1) | INT | Nein | 1 bis 4096 |

Hinweis: Der latente Tensor wird sowohl in der Höhe als auch in der Breite räumlich um den Faktor 8 heruntergesampelt und enthält 16 Kanäle. Die Anzahl der latenten zeitlichen Frames wird als `((length - 1) // 8) + 1` berechnet.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `samples` | Der generierte leere latente Video-Tensor mit Nullwerten | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyCosmosLatentVideo/de.md)

---
**Source fingerprint (SHA-256):** `7ee194324b02367ed853f6d36bc51742081bac6a9469c4a619586e0560a1b33b`
