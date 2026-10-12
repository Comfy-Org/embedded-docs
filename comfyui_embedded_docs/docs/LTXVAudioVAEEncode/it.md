# LTXVAudioVAEEncode

Il nodo LTXV Audio VAE Encode prende in input un audio e lo comprime in una rappresentazione latente più piccola usando uno specifico modello Audio VAE. Questo processo è essenziale per generare o manipolare audio all'interno di un flusso di lavoro con spazio latente, poiché converte i dati audio grezzi in un formato che gli altri nodi della pipeline possono comprendere ed elaborare.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `audio` | L'audio da codificare. | AUDIO | Sì | - |
| `audio_vae` | Il modello Audio VAE da usare per la codifica. | VAE | Sì | - |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `Audio Latent` | La rappresentazione latente compressa dell'audio in input. L'output include i campioni latenti, la frequenza di campionamento del modello VAE e un identificatore di tipo. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAEEncode/it.md)

---
**Source fingerprint (SHA-256):** `68f70e0f8048cd9ba723f52eefc93cc33564eb3e68c0cb9b677964dc99aecb97`
