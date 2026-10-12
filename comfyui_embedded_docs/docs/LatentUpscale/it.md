# Ingrandisci Latent

Il nodo LatentUpscale è progettato per ingrandire le rappresentazioni latenti delle immagini. Consente di regolare le dimensioni dell'immagine di output e il metodo di ingrandimento, offrendo flessibilità nel migliorare la risoluzione delle immagini latenti.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `samples` | La rappresentazione latente di un'immagine da ingrandire. Questo parametro è cruciale per determinare il punto di partenza del processo di ingrandimento. | `LATENT` |
| `upscale_method` | Specifica il metodo utilizzato per ingrandire l'immagine latente. Metodi diversi possono influire sulla qualità e sulle caratteristiche dell'immagine ingrandita. | COMBO[STRING] |
| `width` | La larghezza desiderata dell'immagine ingrandita. Se impostata a 0, verrà calcolata in base all'altezza per mantenere le proporzioni. | `INT` |
| `height` | L'altezza desiderata dell'immagine ingrandita. Se impostata a 0, verrà calcolata in base alla larghezza per mantenere le proporzioni. | `INT` |
| `crop` | Determina come ritagliare l'immagine ingrandita, influenzando l'aspetto finale e le dimensioni dell'output. | COMBO[STRING] |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `latent` | La rappresentazione latente ingrandita dell'immagine, pronta per ulteriori elaborazioni o per la generazione. | `LATENT` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscale/it.md)
