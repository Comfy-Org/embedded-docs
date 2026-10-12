# VaeEncodeForInpaint

Questo nodo è progettato per codificare immagini in una rappresentazione latente adatta ad attività di inpainting, incorporando passaggi aggiuntivi di pre-elaborazione per regolare l'immagine di input e la maschera al fine di ottenere una codifica ottimale da parte del modello VAE.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `pixels` | L'immagine di input da codificare. Questa immagine viene sottoposta a pre-elaborazione e ridimensionamento per corrispondere alle dimensioni di input previste dal modello VAE prima della codifica. | `IMAGE` |
| `vae` | Il modello VAE utilizzato per codificare l'immagine nella sua rappresentazione latente. Svolge un ruolo cruciale nel processo di trasformazione, determinando la qualità e le caratteristiche dello spazio latente di output. | VAE |
| `mask` | Una maschera che indica le regioni dell'immagine di input da sottoporre a inpainting. Viene utilizzata per modificare l'immagine prima della codifica, assicurando che il VAE si concentri sulle aree rilevanti. | `MASK` |
| `grow_mask_by` | Specifica di quanto espandere la maschera di inpainting per garantire transizioni senza interruzioni nello spazio latente. Un valore maggiore aumenta l'area interessata dall'inpainting. | `INT` |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `latent` | L'output include la rappresentazione latente codificata dell'immagine e una maschera di rumore, entrambe cruciali per le successive attività di inpainting. | `LATENT` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeEncodeForInpaint/it.md)
