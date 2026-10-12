# VAEEncodeAudio

Der Node VAE Encode Audio wandelt Audiodaten mithilfe eines Variational Autoencoder (VAE) in eine latente Repräsentation um. Er verarbeitet das eingehende Audio durch den VAE, um komprimierte latente Samples zu erzeugen, die für weitere Aufgaben zur Audioerzeugung oder -manipulation verwendet werden können. Wenn die Abtastrate des Audios von der erwarteten Abtastrate des VAE abweicht, wird das Audio vor der Kodierung automatisch neu abgetastet.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `audio` | Die zu kodierenden Audiodaten, die Wellenform- und Abtastrateninformationen enthalten | AUDIO | Ja | - |
| `vae` | Das Variational-Autoencoder-Modell, das verwendet wird, um das Audio in den latenten Raum zu kodieren | VAE | Ja | - |

**Hinweis:** Die Audioeingabe wird automatisch neu abgetastet, um der erwarteten Abtastrate des VAE zu entsprechen (Standard: 44100 Hz), wenn die ursprüngliche Abtastrate von diesem Wert abweicht. Wenn die Audioeingabe None ist (zum Beispiel, wenn das Quellvideo keine Audiospur enthält), löst der Node einen Fehler aus.

## Ausgaben

| Ausgabenname | Beschreibung | Datentyp |
| --- | --- | --- |
| `LATENT` | Die kodierte Audiodarstellung im latenten Raum, die komprimierte Samples enthält | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeAudio/de.md)

---
**Source fingerprint (SHA-256):** `224563af40a377a37209b26ec8becf035560da273b18293634f684e18c5e63ed`
