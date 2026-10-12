# ImageSharpen

Il nodo ImageSharpen migliora la nitidezza di un'immagine accentuandone i bordi e i dettagli. Applica all'immagine un filtro di nitidezza, regolabile in intensità e raggio, rendendo così l'immagine più definita e nitida.

## Input

| Campo | Descrizione | Tipo di dato |
| --- | --- | --- |
| `image` | L'immagine di input da nitidizzare. Questo parametro è cruciale poiché determina l'immagine di base su cui verrà applicato l'effetto di nitidezza. | `IMAGE` |
| `sharpen_radius` | Definisce il raggio dell'effetto di nitidezza. Un raggio maggiore significa che verranno interessati più pixel attorno ai bordi, producendo un effetto di nitidezza più marcato. | `INT` |
| `sigma` | Controlla la diffusione dell'effetto di nitidezza. Un valore sigma più alto produce una transizione più morbida ai bordi, mentre un sigma più basso rende la nitidezza più localizzata. | `FLOAT` |
| `alpha` | Regola l'intensità dell'effetto di nitidezza. Valori alpha più alti producono un effetto di nitidezza più forte. | `FLOAT` |

## Output

| Campo | Descrizione | Tipo di dato |
| --- | --- | --- |
| `image` | L'immagine nitidizzata, con bordi e dettagli migliorati, pronta per ulteriori elaborazioni o visualizzazione. | `IMAGE` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageSharpen/it.md)
