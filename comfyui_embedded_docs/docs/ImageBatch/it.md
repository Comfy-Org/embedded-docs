# Batch Immagini (DEPRECATO)

Il nodo `ImageBatch` è progettato per combinare due immagini in un unico batch. Se le dimensioni delle immagini non corrispondono, ridimensiona automaticamente la seconda immagine per adattarla alle dimensioni della prima prima di combinarle.

## Input
| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `image1` | La prima immagine da combinare nel batch. Funge da riferimento per le dimensioni a cui la seconda immagine verrà adattata, se necessario. | `IMAGE` |
| `image2` | La seconda immagine da combinare nel batch. Viene ridimensionata automaticamente per corrispondere alle dimensioni della prima immagine, se diverse. | `IMAGE` |

## Output
| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `image` | Il batch combinato di immagini, con la seconda immagine ridimensionata per corrispondere alle dimensioni della prima, se necessario. | `IMAGE` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageBatch/it.md)
