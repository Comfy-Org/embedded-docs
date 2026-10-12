# AudioEncoderEncode

Der Node AudioEncoderEncode konvertiert Audio mithilfe eines Audio-Encoder-Modells in eine codierte Darstellung. Er nimmt einen Audio-Encoder und eine Audioeingabe entgegen, extrahiert dann die Wellenform und die Abtastrate aus dem Audio und übergibt sie an den Encoder, um eine codierte Ausgabe zu erzeugen.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `audio_encoder` | Das Audio-Encoder-Modell, das zur Verarbeitung der Audioeingabe verwendet wird | AUDIO_ENCODER | Ja | - |
| `audio` | Die Audiodaten, die Informationen zu Wellenform und Abtastrate enthalten | AUDIO | Ja | - |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `output` | Die codierte Audiodarstellung, die vom Audio-Encoder erzeugt wird | AUDIO_ENCODER_OUTPUT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderEncode/de.md)

---
**Source fingerprint (SHA-256):** `85f77152ccc1e3f4687e2b655283e69e03d90b862d6a676dcb89ea973dd70a63`
