# VaeDecode

Il nodo VAEDecode è progettato per decodificare rappresentazioni latenti in immagini utilizzando un Autoencoder Variazionale (VAE) specificato. Ha lo scopo di generare immagini da rappresentazioni di dati compressi, facilitando la ricostruzione delle immagini dalle loro codifiche nello spazio latente.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `samples` | Il parametro `samples` rappresenta le rappresentazioni latenti da decodificare in immagini. È cruciale per il processo di decodifica poiché fornisce i dati compressi dai quali vengono ricostruite le immagini. | `LATENT` |
| `vae` | Il parametro `vae` specifica il modello Autoencoder Variazionale (VAE) da utilizzare per decodificare le rappresentazioni latenti in immagini. È essenziale per determinare il meccanismo di decodifica e la qualità delle immagini ricostruite. | VAE |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `image` | L'output è un'immagine ricostruita dalla rappresentazione latente fornita utilizzando il modello VAE specificato. | `IMAGE` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecode/it.md)
