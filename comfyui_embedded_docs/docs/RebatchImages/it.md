# RebatchImages

Il nodo RebatchImages è progettato per riorganizzare un batch di immagini in una nuova configurazione di batch, regolando la dimensione del batch come specificato. Questo processo è essenziale per gestire e ottimizzare l'elaborazione dei dati immagine nelle operazioni in batch, garantendo che le immagini siano raggruppate in base alla dimensione del batch desiderata per una gestione efficiente.

## Input

| Campo | Descrizione | Tipo di dato |
| --- | --- | --- |
| `images` | Un elenco di immagini da riorganizzare in batch. Questo parametro è cruciale per determinare i dati di input che saranno sottoposti al processo di riorganizzazione in batch. | `IMAGE` |
| `batch_size` | Specifica la dimensione desiderata dei batch di output. Questo parametro influenza direttamente il modo in cui le immagini di input vengono raggruppate ed elaborate, incidendo sulla struttura dell'output. | `INT` |

## Output

| Campo | Descrizione | Tipo di dato |
| --- | --- | --- |
| `image` | L'output consiste in un elenco di batch di immagini, riorganizzati in base alla dimensione del batch specificata. Ciò consente un'elaborazione flessibile ed efficiente dei dati immagine nelle operazioni in batch. | `IMAGE` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RebatchImages/it.md)
