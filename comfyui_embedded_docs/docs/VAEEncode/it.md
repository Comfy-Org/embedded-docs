# VaeEncode

Questo nodo è progettato per codificare le immagini in una rappresentazione nello spazio latente utilizzando un modello VAE specificato. Astrae la complessità del processo di codifica, offrendo un modo semplice per trasformare le immagini nelle loro rappresentazioni latenti.

## Input

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `pixels` | Il parametro 'pixels' rappresenta i dati dell'immagine da codificare nello spazio latente. Svolge un ruolo cruciale nel determinare la rappresentazione latente di output, fungendo da input diretto per il processo di codifica. | `IMAGE` |
| `vae` | Il parametro 'vae' specifica il modello VAE (autoencoder variazionale) da utilizzare per codificare i dati dell'immagine nello spazio latente. È essenziale per definire il meccanismo di codifica e le caratteristiche della rappresentazione latente generata. | VAE |

## Output

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `latent` | L'output è una rappresentazione nello spazio latente dell'immagine di input, che racchiude le sue caratteristiche essenziali in forma compressa. | `LATENT` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncode/it.md)
