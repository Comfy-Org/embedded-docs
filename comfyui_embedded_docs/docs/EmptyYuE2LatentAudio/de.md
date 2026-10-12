# Leeres YuE2-Latent-Audio

Dieser Node erstellt ein leeres Audio-Latent für YuE2, dimensioniert auf eine gewählte Dauer und Batch-Anzahl. Er erzeugt stille Platzhalter-Audiodaten, die spätere Nodes während der Audiogenerierung füllen können.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `seconds` | Länge des zu erstellenden Audio-Latents in Sekunden (Standard: 120.0). Die Anzahl der Latent-Frames wird aus diesem Wert berechnet, mit mindestens 1 Frame. | FLOAT | Ja | 0.04 bis 1000.0 (Schrittweite 0.04) |
| `batch_size` | Anzahl der Audio-Latents, die in einem Batch erstellt werden (Standard: 1). | INT | Ja | 1 bis 4096 |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `LATENT` | Ein leeres Audio-Latent, das einen Tensor aus Nullen enthält, dimensioniert durch `batch_size` und die aus `seconds` abgeleitete Frame-Anzahl. Es ist als Audio-Typ mit einem zeitlichen Downscale-Verhältnis von 1920 gekennzeichnet. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyYuE2LatentAudio/de.md)

---
**Source fingerprint (SHA-256):** `3397e3feb534c87d9790bbfe36e8e641476d9b6aa00d75a4e6d0c32f4a948563`
