# LTXVLatentUpsampler

Il nodo LTXVLatentUpsampler aumenta di un fattore due la risoluzione spaziale di una rappresentazione latente video. Utilizza un modello di upscaling dedicato per elaborare i dati latenti, che vengono prima denormalizzati e poi rinormalizzati usando le statistiche dei canali del VAE fornito. Questo nodo è progettato per flussi di lavoro video all'interno dello spazio latente.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `samples` | La rappresentazione latente in ingresso del video da sottoporre a upscaling. | LATENT | Sì |  |
| `upscale_model` | Il modello caricato utilizzato per eseguire l'upscaling 2x sui dati latenti. | LATENT_UPSCALE_MODEL | Sì |  |
| `vae` | Il modello VAE utilizzato per denormalizzare i latenti in ingresso prima dell'upscaling e per normalizzare i latenti in uscita successivamente. | VAE | Sì |  |

Nota: questo nodo è contrassegnato come sperimentale in ComfyUI.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `LATENT` | La rappresentazione latente sottoposta a upscaling, con dimensioni spaziali raddoppiate rispetto all'input. Il latente di output ha la stessa dimensione del batch, lo stesso numero di canali e la stessa lunghezza temporale dell'input. La `noise_mask` dell'input, se presente, viene rimossa dall'output. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVLatentUpsampler/it.md)

---
**Source fingerprint (SHA-256):** `7d7f0b733cb3758e9ec985cac30134d719b130b5b86c35bfdd14576a5b4575db`
