# LTXV Audio VAE kodieren

Der LTXV Audio VAE Encode-Node nimmt eine Audioeingabe entgegen und komprimiert sie mithilfe eines angegebenen Audio-VAE-Modells in eine kleinere latente Repräsentation. Dieser Prozess ist essenziell für die Generierung oder Manipulation von Audio in einem Latent-Space-Workflow, da er Rohaudiodaten in ein Format umwandelt, das andere Nodes in der Pipeline verstehen und verarbeiten können.

## Eingaben

| Parameter | Beschreibung | Datentyp | Erforderlich | Bereich |
| --- | --- | --- | --- | --- |
| `audio` | Das zu kodierende Audio. | AUDIO | Ja | - |
| `audio_vae` | Das Audio-VAE-Modell, das für die Kodierung verwendet wird. | VAE | Ja | - |

## Ausgaben

| Ausgabenamen | Beschreibung | Datentyp |
| --- | --- | --- |
| `Audio Latent` | Die komprimierte latente Repräsentation des Eingabeaudios. Die Ausgabe enthält die latenten Samples, die Abtastrate des VAE-Modells und eine Typkennung. | LATENT |

> Diese Dokumentation wurde von KI generiert. Wenn Sie Fehler finden oder Verbesserungsvorschläge haben, tragen Sie gerne dazu bei! [Auf GitHub bearbeiten](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAEEncode/de.md)

---
**Source fingerprint (SHA-256):** `68f70e0f8048cd9ba723f52eefc93cc33564eb3e68c0cb9b677964dc99aecb97`
