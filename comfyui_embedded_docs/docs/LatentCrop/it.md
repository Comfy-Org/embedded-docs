# Ritaglia Latent

Il nodo LatentCrop è progettato per eseguire operazioni di ritaglio sulle rappresentazioni latenti delle immagini. Consente di specificare le dimensioni e la posizione del ritaglio, permettendo modifiche mirate dello spazio latente.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `samples` | Il parametro `samples` rappresenta le rappresentazioni latenti da ritagliare. È cruciale per definire i dati sui quali verrà eseguita l'operazione di ritaglio. | `LATENT` |
| `width` | Specifica la larghezza dell'area di ritaglio. Influisce direttamente sulle dimensioni della rappresentazione latente di output. | `INT` |
| `height` | Specifica l'altezza dell'area di ritaglio, influenzando la dimensione della rappresentazione latente ritagliata risultante. | `INT` |
| `x` | Determina la coordinata x iniziale dell'area di ritaglio, influenzando la posizione del ritaglio all'interno della rappresentazione latente originale. | `INT` |
| `y` | Determina la coordinata y iniziale dell'area di ritaglio, impostando la posizione del ritaglio all'interno della rappresentazione latente originale. | `INT` |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `latent` | L'output è una rappresentazione latente modificata con il ritaglio specificato applicato. | `LATENT` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCrop/it.md)
