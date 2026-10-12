# Ritaglia Immagine (DEPRECATO)

Il nodo `ImageCrop` è progettato per ritagliare le immagini a una larghezza e un'altezza specificate, partendo da una determinata coordinata x e y. Questa funzionalità è essenziale per concentrarsi su regioni specifiche di un'immagine o per adattare le dimensioni dell'immagine a determinati requisiti.

## Input

| Campo | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | L'immagine di input da ritagliare. Questo parametro è cruciale poiché definisce l'immagine sorgente da cui verrà estratta una regione in base alle dimensioni e alle coordinate specificate. | `IMAGE` |
| `width` | Specifica la larghezza dell'immagine ritagliata. Questo parametro determina quanto sarà larga l'immagine ritagliata risultante. | `INT` |
| `height` | Specifica l'altezza dell'immagine ritagliata. Questo parametro determina l'altezza dell'immagine ritagliata risultante. | `INT` |
| `x` | La coordinata x dell'angolo in alto a sinistra dell'area di ritaglio. Questo parametro imposta il punto di partenza per la dimensione della larghezza del ritaglio. | `INT` |
| `y` | La coordinata y dell'angolo in alto a sinistra dell'area di ritaglio. Questo parametro imposta il punto di partenza per la dimensione dell'altezza del ritaglio. | `INT` |

## Output

| Campo | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | L'immagine ritagliata come risultato dell'operazione di ritaglio. Questo output è significativo per ulteriori elaborazioni o analisi della regione dell'immagine specificata. | `IMAGE` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCrop/it.md)
