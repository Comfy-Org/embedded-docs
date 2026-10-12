# Ripeti Batch Immagini

Il nodo RepeatImageBatch è progettato per replicare una determinata immagine un numero specificato di volte, creando un batch di immagini identiche. Questa funzionalità è utile per operazioni che richiedono più istanze della stessa immagine, come l'elaborazione in batch o il data augmentation.

## Input

| Campo | Descrizione | Tipo di dato |
| --- | --- | --- |
| `image` | Il parametro `image` rappresenta l'immagine da replicare. È cruciale per definire il contenuto che verrà duplicato nell'intero batch. | `IMAGE` |
| `amount` | Il parametro `amount` specifica il numero di volte in cui l'immagine di input deve essere replicata. Influisce direttamente sulla dimensione del batch di output, consentendo una creazione flessibile del batch. | `INT` |

## Output

| Campo | Descrizione | Tipo di dato |
| --- | --- | --- |
| `image` | L'output è un batch di immagini, ciascuna identica all'immagine di input, replicata secondo l'`amount` specificato. | `IMAGE` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RepeatImageBatch/it.md)
