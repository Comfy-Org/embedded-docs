# Ingrandisci Immagine di

Il nodo ImageScaleBy è progettato per ingrandire le immagini di un fattore di scala specificato utilizzando vari metodi di interpolazione. Consente di regolare le dimensioni dell'immagine in modo flessibile, soddisfacendo diverse esigenze di ingrandimento.

## Input

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | L'immagine di input da ingrandire. Questo parametro è cruciale poiché fornisce l'immagine di base che sarà sottoposta al processo di ingrandimento. | `IMAGE` |
| `upscale_method` | Specifica il metodo di interpolazione da utilizzare per l'ingrandimento. La scelta del metodo può influire sulla qualità e sulle caratteristiche dell'immagine ingrandita. | COMBO[STRING] |
| `scale_by` | Il fattore di ingrandimento dell'immagine. Determina l'aumento di dimensione dell'immagine di output rispetto all'immagine di input. | `FLOAT` |

## Output

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | L'immagine ingrandita, che è più grande dell'immagine di input in base al fattore di scala e al metodo di interpolazione specificati. | `IMAGE` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleBy/it.md)
