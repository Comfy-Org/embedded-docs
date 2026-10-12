# EmptyAceStep1.5LatentAudio

Der Node Empty Ace Step 1.5 Latent Audio erstellt einen leeren (stillen) Audio-Latent-Tensor für Workflows zur Audiogenerierung. Er erstellt einen Latent-Tensor mit 64 Kanälen, dessen zeitliche Länge aus der angeforderten Dauer berechnet wird, und kennzeichnet ihn als Audiodaten zur Verwendung durch nachgelagerte Audio-Nodes.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `seconds` | Die Dauer des zu generierenden Audios in Sekunden (Standard: 120.0). Die Latent-Länge wird als `seconds * 48000 / 1920` berechnet und auf die nächste ganze Zahl gerundet. | FLOAT | Ja | 1.0 - 1000.0 (step: 0.01) |
| `batch_size` | Die Anzahl der Latent-Bilder im Batch (Standard: 1). | INT | Ja | 1 - 4096 |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `LATENT` | Ein leerer Latent-Tensor, der stilles Audio repräsentiert. Der Tensor hat die Form [batch_size, 64, length], wobei length von `seconds` abgeleitet wird. Die Ausgabe enthält außerdem einen Typbezeichner "audio" und einen `downscale_ratio_temporal`-Wert von 1764, der für die zeitliche Herunterskalierung in der Audioverarbeitung verwendet wird. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStep1.5LatentAudio/de.md)

---
**Source fingerprint (SHA-256):** `bb7120c91ce5d779147cb8553d6f96fa160d87468d4d87550fb6dd4ec89b1557`
