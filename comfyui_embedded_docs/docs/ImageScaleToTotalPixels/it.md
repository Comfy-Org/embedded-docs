# Scala Immagine al Numero Totale di Pixel

Il nodo ImageScaleToTotalPixels è progettato per ridimensionare le immagini a un numero totale di pixel specificato mantenendo il rapporto d'aspetto. Fornisce vari metodi per eseguire l'upscaling dell'immagine al fine di raggiungere il numero di pixel desiderato.

## Input

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | L'immagine di input da ridimensionare al numero totale di pixel specificato. | `IMAGE` |
| `upscale_method` | Il metodo utilizzato per l'upscaling dell'immagine. Influisce sulla qualità e sulle caratteristiche dell'immagine ingrandita. | COMBO[STRING] |
| `megapixels` | La dimensione target dell'immagine in megapixel. Determina il numero totale di pixel nell'immagine ingrandita. | `FLOAT` |

## Output

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | L'immagine ingrandita con il numero totale di pixel specificato, mantenendo il rapporto d'aspetto originale. | `IMAGE` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleToTotalPixels/it.md)
