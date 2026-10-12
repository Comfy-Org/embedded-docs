# Leeres Hunyuan Bild-Latent

Der Node EmptyHunyuanImageLatent erzeugt einen leeren, vollständig mit Nullen gefüllten Latent-Raum für Hunyuan-Bildgenerierungsmodelle. Er erstellt ein leeres Ausgangs-Latent mit der angegebenen Breite, Höhe und Batch-Größe, das anschließend an nachgelagerte Nodes im Workflow weitergegeben werden kann. Der Latent-Tensor enthält 64 Kanäle, und jede räumliche Dimension entspricht der jeweiligen Pixel-Dimension geteilt durch 32.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `width` | Die Breite des erzeugten Latent-Bildes in Pixeln (Standard: 2048, Schrittweite: 32) | INT | Ja | 64 bis MAX_RESOLUTION |
| `height` | Die Höhe des erzeugten Latent-Bildes in Pixeln (Standard: 2048, Schrittweite: 32) | INT | Ja | 64 bis MAX_RESOLUTION |
| `batch_size` | Die Anzahl der in einem Batch zu erzeugenden Latent-Stichproben (Standard: 1) | INT | Ja | 1 bis 4096 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `LATENT` | Ein leerer Latent-Tensor mit 64 Kanälen und Dimensionen von Höhe ÷ 32 mal Breite ÷ 32, bereit für die Hunyuan-Bildverarbeitung | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanImageLatent/de.md)

---
**Source fingerprint (SHA-256):** `31fc10d43c224810709870cf40256b6fccd4743445ea9d98d148d443bc591d7a`
