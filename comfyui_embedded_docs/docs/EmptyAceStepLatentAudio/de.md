# EmptyAceStepLatentAudio

Der Node Empty Ace Step 1.0 Latent Audio erzeugt leere latente Audio-Samples für eine gewählte Dauer. Er füllt einen Batch stiller (ausschließlich aus Nullen bestehender) latenter Audiodaten, wobei die Länge anhand der Eingabe `seconds` unter Verwendung von Audioverarbeitungsparametern berechnet wird. Dies wird typischerweise verwendet, um Audio-Workflows zu initialisieren, die eine latente Repräsentation als Ausgangspunkt benötigen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `seconds` | Die Dauer des Audios in Sekunden (Standard: 120.0, Schritt: 0.1) | FLOAT | Ja | 1.0 - 1000.0 |
| `batch_size` | Die Anzahl der latenten Bilder im Batch (Standard: 1) | INT | Ja | 1 - 4096 |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Gibt leere latente Audio-Samples zurück, die mit Nullen gefüllt sind. Die Ausgabe enthält einen `samples`-Tensor und ein `type`-Feld, das auf "audio" gesetzt ist. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStepLatentAudio/de.md)

---
**Source fingerprint (SHA-256):** `8268eb582a28c7acc495c52831cc6edd8f8fdd1b294857451ce94abc37ca0d14`
