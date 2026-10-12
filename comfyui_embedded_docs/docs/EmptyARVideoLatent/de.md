# EmptyARVideoLatent

Der Node EmptyARVideoLatent erstellt eine leere Latent-Repräsentation für die Videogenerierung. Er erzeugt einen Tensor aus Nullen mit der angeforderten Breite, Höhe, Frame-Anzahl und Batch-Größe, der dann verwendet werden kann, um einen Videogenerierungsprozess zu initialisieren.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `width` | Die Breite der Videoframes in Pixeln (Standard: 832) | INT | Ja | 16 bis 8192 (Schritt: 16) |
| `height` | Die Höhe der Videoframes in Pixeln (Standard: 480) | INT | Ja | 16 bis 8192 (Schritt: 16) |
| `length` | Die Anzahl der Frames im Video (Standard: 81) | INT | Ja | 1 bis 1024 (Schritt: 4) |
| `batch_size` | Die Anzahl der Videos, die in einem einzelnen Batch generiert werden sollen (Standard: 1) | INT | Ja | 1 bis 64 |

Hinweis: Die interne Latent-Größe wird aus diesen Eingaben abgeleitet. `width` und `height` werden durch 8 geteilt, und die Anzahl der Latent-Zeitschritte wird als `((length - 1) // 4) + 1` berechnet.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `LATENT` | Ein mit Nullen gefüllter Latent-Tensor, der einen leeren Video-Latent-Raum mit den angegebenen Dimensionen, der Länge und der Batch-Größe repräsentiert. Die Tensorform ist [batch_size, 16, lat_t, height/8, width/8], wobei lat_t = ((length - 1) // 4) + 1 die Anzahl der Latent-Zeitschritte ist, die aus der angeforderten Länge abgeleitet wird. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyARVideoLatent/de.md)

---
**Source fingerprint (SHA-256):** `02ed3c96d94f2a3df9fb5315a5312e5280b9bee280369eb1218ba10bc122e609`
