# Ruota Latent

Il nodo LatentRotate è progettato per ruotare le rappresentazioni latenti delle immagini di angoli specificati. Astrae la complessità della manipolazione dello spazio latente per ottenere effetti di rotazione, consentendo agli utenti di trasformare facilmente le immagini nello spazio latente di un modello generativo.

## Input

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `samples` | Il parametro `samples` rappresenta le rappresentazioni latenti delle immagini da ruotare. È cruciale per determinare il punto di partenza dell'operazione di rotazione. | `LATENT` |
| `rotation` | Il parametro `rotation` specifica l'angolo di cui le immagini latenti devono essere ruotate. Influisce direttamente sull'orientamento delle immagini risultanti. | COMBO[STRING] |

## Output

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `latent` | L'output è una versione modificata delle rappresentazioni latenti in input, ruotata dell'angolo specificato. | `LATENT` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentRotate/it.md)
