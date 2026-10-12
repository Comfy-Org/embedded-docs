# ImageCompositeMasked

Il nodo `ImageCompositeMasked` è progettato per la composizione di immagini, consentendo la sovrapposizione di un'immagine sorgente su un'immagine di destinazione a coordinate specificate, con ridimensionamento e mascheramento opzionali.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `destination` | L'immagine di destinazione sulla quale verrà composta l'immagine sorgente. Funge da sfondo per l'operazione di composizione. | `IMAGE` |
| `source` | L'immagine sorgente da comporre sull'immagine di destinazione. Questa immagine può facoltativamente essere ridimensionata per adattarsi alle dimensioni dell'immagine di destinazione. | `IMAGE` |
| `x` | La coordinata x nell'immagine di destinazione in cui verrà posizionato l'angolo superiore sinistro dell'immagine sorgente. | `INT` |
| `y` | La coordinata y nell'immagine di destinazione in cui verrà posizionato l'angolo superiore sinistro dell'immagine sorgente. | `INT` |
| `resize_source` | Un flag booleano che indica se l'immagine sorgente deve essere ridimensionata per corrispondere alle dimensioni dell'immagine di destinazione. | `BOOLEAN` |
| `mask` | Una maschera opzionale che specifica quali parti dell'immagine sorgente devono essere composte sull'immagine di destinazione. Ciò consente operazioni di composizione più complesse, come la miscelazione o le sovrapposizioni parziali. | `MASK` |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `image` | L'immagine risultante dopo l'operazione di composizione, che combina elementi di entrambe le immagini. | `IMAGE` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompositeMasked/it.md)
