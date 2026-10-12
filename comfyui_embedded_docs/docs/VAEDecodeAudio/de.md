# VAE-Audio dekodieren

Dieser Node wandelt eine latente Audiodarstellung mithilfe eines Variational Autoencoder (VAE) wieder in eine abspielbare Audiowellenform um. Er nimmt die kodierten Samples, dekodiert sie durch das ausgewählte VAE und normalisiert anschließend die resultierende Wellenform, damit der Gesamtlautstärkepegel konsistent bleibt. Das Ausgangsaudio verwendet die Audio-Abtastrate des VAE (standardmäßig 44100 Hz) oder die in den Eingabe-Samples gespeicherte Abtastrate, sofern eine vorhanden ist.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
|-----------|-------------|-----------|----------|-------|
| `samples` | Die kodierten Audio-Samples im latenten Raum, die wieder in eine Audiowellenform dekodiert werden. Wenn die Samples eine eigene Abtastrate mitführen, wird dieser Wert für die Ausgabe verwendet. | LATENT | Ja | - |
| `vae` | Das Variational Autoencoder-Modell, das zum Dekodieren der latenten Samples in Audio verwendet wird. Seine Audio-Ausgangs-Abtastrate (standardmäßig 44100 Hz) bestimmt die Abtastrate der resultierenden Wellenform, wenn die Eingabe-Samples keine angeben. | VAE | Ja | - |

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
|-------------|-------------|-----------|
| `AUDIO` | Die dekodierte Audiowellenform mit normalisierter Lautstärke, zurückgegeben zusammen mit ihrer Abtastrate (die Abtastrate aus den Eingabe-`samples`, falls vorhanden, andernfalls die Audio-Abtastrate des VAE, standardmäßig 44100 Hz). | AUDIO |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudio/de.md)

---
**Source fingerprint (SHA-256):** `2a3f5c912d1d84eea7768979f6b8f0eaa9fe89041f3a3352434f38abd3c09fea`
