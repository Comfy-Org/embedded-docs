# EmptyLTXVLatentVideo

Der Node EmptyLTXVLatentVideo erstellt einen leeren (mit Nullen gefüllten) latenten Video-Tensor unter Verwendung der von Ihnen angegebenen Werte für Breite, Höhe, Länge und Batch-Größe. Er bietet einen leeren Ausgangspunkt für LTXV-Videogenerierungs-Workflows, wobei die latenten Dimensionen im Verhältnis zur angeforderten Videogröße automatisch komprimiert werden.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `width` | Die Breite des latenten Video-Tensors (Standard: 768, Schritt: 32) | INT | Ja | 64 bis MAX_RESOLUTION |
| `height` | Die Höhe des latenten Video-Tensors (Standard: 512, Schritt: 32) | INT | Ja | 64 bis MAX_RESOLUTION |
| `length` | Die Anzahl der Frames im latenten Video (Standard: 97, Schritt: 8) | INT | Ja | 1 bis MAX_RESOLUTION |
| `batch_size` | Die Anzahl der latenten Videos, die in einem Batch generiert werden (Standard: 1) | INT | Ja | 1 bis 4096 |

Hinweis: Das latente Video ist im Vergleich zu den angeforderten Dimensionen komprimiert: Die räumlichen Dimensionen (Breite und Höhe) werden durch 32 geteilt, und die Frame-Anzahl (Länge) wird durch 8 geteilt und auf die nächste ganze Zahl aufgerundet. Die Schrittwerte für Breite, Höhe und Länge helfen dabei, diese Divisionen gleichmäßig zu halten.

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
| --- | --- | --- |
| `samples` | Der generierte leere latente Tensor mit Nullwerten in den angegebenen Dimensionen, zusammen mit einem räumlichen Downscale-Verhältnis von 32 | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLTXVLatentVideo/de.md)

---
**Source fingerprint (SHA-256):** `0b1e57baf9730d852b03b6bccbb8a033e2be9b9cd2420a0aa3638c31f6d3cd26`
