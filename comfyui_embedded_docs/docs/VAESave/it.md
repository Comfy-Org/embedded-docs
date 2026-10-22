# VaeSave

Il nodo VAESave è progettato per salvare i modelli VAE insieme ai relativi metadati, inclusi prompt e informazioni PNG aggiuntive, in una directory di output specificata. Incapsula la funzionalità di serializzare lo stato del modello e le informazioni associate in un file, facilitando la conservazione e la condivisione dei modelli addestrati.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `vae` | Il modello VAE da salvare. Questo parametro è cruciale poiché rappresenta il modello il cui stato deve essere serializzato e memorizzato. | VAE |
| `filename_prefix` | Un prefisso per il nome del file con cui verranno salvati il modello e i suoi metadati. Ciò consente una memorizzazione organizzata e un facile recupero dei modelli. | STRING |

## Output

Il nodo non ha tipi di output.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAESave/it.md)
