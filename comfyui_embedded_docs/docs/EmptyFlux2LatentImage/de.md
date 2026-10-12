# EmptyFlux2LatentImage

Der Node Empty Flux 2 Latent erstellt eine leere latente Repräsentation, die mit Nullen gefüllt ist. Er wird als Ausgangspunkt für den Denoising-Prozess des Flux-Modells verwendet. Die latenten Dimensionen werden aus den Eingabeparametern `width` und `height` übernommen, jeweils geteilt durch 16.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `width` | Die Breite des finalen Bildes, das generiert werden soll. Die latente Breite entspricht diesem Wert geteilt durch 16. Der Standardwert ist 1024. | INT | Ja | 16 bis 16384 |
| `height` | Die Höhe des finalen Bildes, das generiert werden soll. Die latente Höhe entspricht diesem Wert geteilt durch 16. Der Standardwert ist 1024. | INT | Ja | 16 bis 16384 |
| `batch_size` | Die Anzahl der latenten Samples, die in einem einzelnen Batch generiert werden sollen. Der Standardwert ist 1. | INT | Nein | 1 bis 4096 |

**Hinweis:** Die Eingaben `width` und `height` verwenden eine Schrittweite von 16, daher müssen sie durch 16 teilbar sein. Das liegt daran, dass der Node sie durch diesen Faktor teilt, um die latenten Dimensionen zu erstellen.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `samples` | Ein latenter Tensor, der mit Nullen gefüllt ist. Die Form ist `[batch_size, 128, height // 16, width // 16]`. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyFlux2LatentImage/de.md)

---
**Source fingerprint (SHA-256):** `f8356568f0ab521a3f246d1f672492e74f9a2f449694961b913bd14a5f0f3878`
