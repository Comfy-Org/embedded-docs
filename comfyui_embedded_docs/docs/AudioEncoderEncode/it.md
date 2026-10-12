# AudioEncoderEncode

Il nodo AudioEncoderEncode converte l'audio in una rappresentazione codificata utilizzando un modello di codificatore audio. Prende un codificatore audio e un input audio, quindi estrae la forma d'onda e la frequenza di campionamento dall'audio e le passa al codificatore per produrre un output codificato.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `audio_encoder` | Il modello di codificatore audio utilizzato per elaborare l'input audio | AUDIO_ENCODER | Sì | - |
| `audio` | I dati audio contenenti le informazioni sulla forma d'onda e sulla frequenza di campionamento | AUDIO | Sì | - |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `output` | La rappresentazione audio codificata prodotta dal codificatore audio | AUDIO_ENCODER_OUTPUT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderEncode/it.md)

---
**Source fingerprint (SHA-256):** `85f77152ccc1e3f4687e2b655283e69e03d90b862d6a676dcb89ea973dd70a63`
