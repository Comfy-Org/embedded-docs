# PiDConditioning

Associa un latent e un valore degrade_sigma a un CONDITIONING, così può essere utilizzato per la decodifica PiD o l'upscaling. Questo consente di controllare quanto il latent viene degradato prima di essere elaborato.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `positive` | I dati di conditioning a cui associare il latent e il valore degrade sigma. | CONDITIONING | Sì | - |
| `latent` | Il latent (da VAEEncode o da un KSampler) da associare al conditioning. | LATENT | Sì | - |
| `latent_format` | Il formato del latent. I latent Flux1 (16 canali) e Flux2 (128 canali) vengono rilevati automaticamente dalla dimensione dei canali con "flux". Per SD3 (16 canali), SDXL (4 canali) o QwenImage (16 canali), selezionare manualmente (predefinito: "flux"). | COMBO | Sì | `"flux"`<br>`"sd3"`<br>`"sdxl"`<br>`"qwenimage"` |
| `degrade_sigma` | La quantità di degradazione da applicare. 0 indica un latent pulito. Aumentare questo valore per eseguire il denoising di output latent corrotti (predefinito: 0.0). | FLOAT | Sì | 0.0 to 1.0 (step: 0.01) |

Nota: quando `latent_format` è impostato su `"flux"`, il nodo rileva automaticamente il tipo di latent dalla dimensione dei canali: 128 canali vengono trattati come latent Flux2, mentre 16 canali vengono trattati come latent Flux1.

Nota: un valore `latent_format` non supportato genera un errore, ma tutte le opzioni disponibili sono gestite dal nodo.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `CONDITIONING` | I dati di conditioning originali con il latent e il valore degrade sigma associati. | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PiDConditioning/it.md)

---
**Source fingerprint (SHA-256):** `24f613b33e7872cb35f458aa5794a3cc4d37ceaecd43725039edef75f4a512bc`
