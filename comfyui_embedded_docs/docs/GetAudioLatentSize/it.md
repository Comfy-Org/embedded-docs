# Get Audio Latent Size

Legge un latente audio e restituisce la sua lunghezza, il numero di canali audio e la dimensione del batch, in modo che tali valori possano essere riutilizzati senza decodificare l'audio. Usalo per dimensionare le maschere di rumore o per far corrispondere le lunghezze di audio e video prima del campionamento. I valori misurati vengono anche stampati sul nodo stesso.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `latent` | Il latente audio o audio/video da esaminare. Quando il latente contiene più flussi, viene misurato il flusso audio. | LATENT | Sì | - |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `length` | La lunghezza del latente audio, in celle del latente anziché in campioni audio. | INT |
| `audio_channels` | Il numero di canali audio. I latenti privi di una dimensione per i canali audio riportano un canale. | INT |
| `batch_size` | Il numero di latenti nel batch. | INT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetAudioLatentSize/it.md)

---
**Source fingerprint (SHA-256):** `82bac0636a070d14a8845c3f4a5e73359c1d943ce223be3b93212ef25d44b1a8`
