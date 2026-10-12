# EmptyTrellis2LatentStructure

Dieser Node erstellt eine leere latente Struktur für das Trellis2-Modell, bei der alle Werte auf null gesetzt sind. Er erzeugt einen leeren 3D-Latent-Tensor mit 32 Kanälen bei einer Auflösung von 16×16×16, dimensioniert für die angegebene Anzahl von Elementen im Batch.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `batch_size` | Die Anzahl der latenten Bilder im Batch (Standard: 1). | INT | Ja | 1 bis 4096 |

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `LATENT` | Eine leere Trellis2-Latent-Struktur. Die Samples sind ein mit Nullen gefüllter Tensor mit der Form (batch_size, 32, 16, 16, 16), und der Latent-Typ ist auf "trellis2" gesetzt. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyTrellis2LatentStructure/de.md)

---
**Source fingerprint (SHA-256):** `a551f0e05e58b025df03a3babee36f57fd900b5e02926fbdbd67a512ebead078`
