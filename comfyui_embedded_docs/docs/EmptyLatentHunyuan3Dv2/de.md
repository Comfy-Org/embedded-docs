# Leeres Hunyuan 3D v2 Latent

Dieser Node erstellt einen Batch leerer (ausschließlich aus Nullen bestehender) Latent-Samples, die für Hunyuan3Dv2-3D-Generierungsmodelle formatiert sind. Er erzeugt den korrekt geformten Latent-Tensor, der als Ausgangspunkt für 3D-Generierungsworkflows dient, wobei das Latent mit dem Typ „hunyuan3dv2“ gekennzeichnet ist.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `resolution` | Die Auflösungsdimension des zu erzeugenden latenten Raums (Standard: 3072) | INT | Ja | 1 - 8192 |
| `batch_size` | Die Anzahl der latenten Bilder im Batch (Standard: 1) | INT | Ja | 1 - 4096 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `LATENT` | Ein leerer Latent-Tensor der Form [batch_size, 64, resolution], der mit Nullen gefüllte Samples enthält und mit dem Typ „hunyuan3dv2“ gekennzeichnet ist | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentHunyuan3Dv2/de.md)

---
**Source fingerprint (SHA-256):** `e9061301341ab84290cd2b16d5307636310a0772562cf485e3444876e4786ddd`
