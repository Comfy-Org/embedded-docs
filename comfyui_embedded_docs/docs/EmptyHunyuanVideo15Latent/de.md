# EmptyHunyuanVideo15Latent

Dieser Node erstellt einen leeren latenten Tensor, der speziell für die Verwendung mit dem HunyuanVideo 1.5-Modell formatiert ist. Er erzeugt einen leeren Ausgangspunkt für die Videogenerierung, indem er einen Tensor aus Nullen mit der richtigen Kanalanzahl und den räumlichen Dimensionen für den latenten Raum des Modells zuweist.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `width` | Die Breite des Videobilds in Pixeln. | INT | Ja | - |
| `height` | Die Höhe des Videobilds in Pixeln. | INT | Ja | - |
| `length` | Die Anzahl der Frames in der Videosequenz. | INT | Ja | - |
| `batch_size` | Die Anzahl der Videobeispiele, die in einem Batch generiert werden sollen (Standard: 1). | INT | Nein | - |

**Hinweis:** Die räumlichen Dimensionen des erzeugten latenten Tensors werden berechnet, indem die Eingaben `width` und `height` durch 16 geteilt werden (dieser Node verwendet einen räumlichen Skalierungsfaktor von 16 statt 8). Die zeitliche Dimension (Frames) wird als `((length - 1) // 4) + 1` berechnet. Diese Berechnungen verwenden die Ganzzahldivision, daher sollten `width` und `height` Vielfache von 16 sein, um Abschneidungen zu vermeiden.

## Ausgaben

| Ausgabename | Beschreibung | Datentyp |
| --- | --- | --- |
| `samples` | Ein leerer latenter Tensor mit Dimensionen, die für das HunyuanVideo 1.5-Modell geeignet sind. Der Tensor hat die Form `[batch_size, 32, ((length - 1) // 4) + 1, height // 16, width // 16]`. Die Ausgabe enthält außerdem einen `downscale_ratio_spacial`-Wert von 16. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanVideo15Latent/de.md)

---
**Source fingerprint (SHA-256):** `ce7ec75e8433c778d175a3e2ea260a4397aa5507428908b9a32f50fbe9e184c6`
