# MiniMax H3 Image Conditioning

Trasforma un prompt in condizionamento e in un latent vuoto per un'immagine statica con MiniMax H3 Image. Senza immagini esegue text to image; con immagini collegate le modifica, e il prompt vi fa riferimento come `<Picture 1>`, `<Picture 2>` e così via.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `clip` | Il modello CLIP di MiniMax H3 Image, che tokenizza il prompt con eventuali immagini di riferimento e codifica il condizionamento. | CLIP | Sì | - |
| `vae` | Il VAE di MiniMax H3 Image. Con esso le immagini vengono anche ancorate come latent di riferimento; senza di esso condizionano solo il text encoder. | VAE | No | - |
| `prompt` | Cosa generare o come modificare le immagini di riferimento. | STRING | Sì | Testo multiriga |
| `width` | Larghezza di output in pixel. 0 usa la larghezza di `image_1` dopo il suo ridimensionamento di riferimento, oppure 2048 senza immagini. Predefinito: 0. | INT | Sì | 0 a MAX_RESOLUTION (passo 32) |
| `height` | Altezza di output in pixel. 0 usa l'altezza di `image_1` dopo il suo ridimensionamento di riferimento, oppure 2048 senza immagini. Predefinito: 0. | INT | Sì | 0 a MAX_RESOLUTION (passo 32) |
| `images` | Gruppo espandibile di immagini di riferimento, da `image_1` in su; `image_1` è l'immagine da modificare. Il prompt vi fa riferimento come `<Picture n>`. | AUTOGROW | No | 0 a 100 immagini |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `positive` | Condizionamento per il sampler di MiniMax H3 Image, con i latent di riferimento allegati quando le immagini sono collegate. | CONDITIONING |
| `latent` | Latent vuoto per un'immagine, 24 canali a un sedicesimo della dimensione di output. | LATENT |

Nota: il modello è ottimizzato per un'area di 2048x2048 pixel, quindi lascia `width` e `height` a 0 a meno che non sia necessaria una tela diversa.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ImageConditioning/it.md)

---
**Source fingerprint (SHA-256):** `b0927bbc44ac82e8a23b1edb5470c0cc8945844c326a352d75495ed801d11b1d`
