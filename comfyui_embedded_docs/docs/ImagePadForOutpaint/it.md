# ImagePadForOutpaint

Questo nodo è progettato per preparare le immagini al processo di outpainting aggiungendo padding attorno a esse. Regola le dimensioni dell'immagine per garantirne la compatibilità con gli algoritmi di outpainting, facilitando la generazione di aree estese oltre i confini originali.

## Input

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | L'input `image` è l'immagine principale da preparare per l'outpainting, che funge da base per le operazioni di padding. | `IMAGE` |
| `left` | Specifica la quantità di padding da aggiungere sul lato sinistro dell'immagine, influenzando l'area espansa per l'outpainting. | `INT` |
| `top` | Determina la quantità di padding da aggiungere sulla parte superiore dell'immagine, influenzando l'espansione verticale per l'outpainting. | `INT` |
| `right` | Definisce la quantità di padding da aggiungere sul lato destro dell'immagine, incidendo sull'espansione orizzontale per l'outpainting. | `INT` |
| `bottom` | Indica la quantità di padding da aggiungere sulla parte inferiore dell'immagine, contribuendo all'espansione verticale per l'outpainting. | `INT` |
| `feathering` | Controlla la morbidezza della transizione tra l'immagine originale e il padding aggiunto, migliorando l'integrazione visiva per l'outpainting. | `INT` |

## Output

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | L'output `image` rappresenta l'immagine con padding, pronta per il processo di outpainting. | `IMAGE` |
| `mask` | L'output `mask` indica le aree dell'immagine originale e il padding aggiunto, utile per guidare gli algoritmi di outpainting. | `MASK` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImagePadForOutpaint/it.md)
