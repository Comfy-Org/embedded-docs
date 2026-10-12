# Ribatch Latent

Il nodo RebatchLatents è progettato per riorganizzare un batch di rappresentazioni latenti in una nuova configurazione di batch, in base a una dimensione del batch specificata. Assicura che i campioni latenti siano raggruppati in modo appropriato, gestendo variazioni nelle dimensioni e nelle grandezze, per facilitare ulteriori elaborazioni o l'inferenza del modello.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `latents` | Il parametro `latents` rappresenta le rappresentazioni latenti di input da riorganizzare in batch. È fondamentale per determinare la struttura e il contenuto del batch di output. | `LATENT` |
| `batch_size` | Il parametro `batch_size` specifica il numero desiderato di campioni per batch nell'output. Influisce direttamente sul raggruppamento e sulla suddivisione dei latenti di input in nuovi batch. | `INT` |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `latent` | L'output è un batch riorganizzato di rappresentazioni latenti, adattato in base alla dimensione del batch specificata. Facilita ulteriori elaborazioni o analisi. | `LATENT` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RebatchLatents/it.md)
