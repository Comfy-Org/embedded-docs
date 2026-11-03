# p-h3-image Conditioning

Questo nodo trasforma un prompt in condizionamento e in un latent vuoto per una singola immagine statica con p-h3-image. Senza immagini funziona come testo-immagine; con immagini collegate, `image_1` è l'immagine da modificare e gli altri slot fungono da riferimenti, a cui il prompt fa riferimento come `<Picture 1>`, `<Picture 2>` e così via. Il sampler richiede un modello patchato dal nodo MiniMax H3 sigma shift con entrambi i valori di shift impostati a 1.0.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `clip` | Il modello CLIP p-h3-image usato per tokenizzare il prompt, incluse eventuali immagini di riferimento, e per codificare il condizionamento. | CLIP | Sì | - |
| `prompt` | Cosa generare, o come modificare `image_1`. Con immagini collegate, a una breve istruzione viene anteposto `Edit <Picture 1>. `. Un'istruzione che inizia già con `Edit <Picture` o un edit brief prodotto da un prompt upsampler viene usata esattamente così com'è. | STRING | Sì | - |
| `width` | Larghezza di output in pixel. 0 usa la larghezza di `image_1` dopo il ridimensionamento, oppure 2912 quando nessuna immagine è collegata (predefinito: 0). | INT | Sì | 0 a MAX_RESOLUTION |
| `height` | Altezza di output in pixel. 0 usa l'altezza di `image_1` dopo il ridimensionamento, oppure 2912 quando nessuna immagine è collegata (predefinito: 0). | INT | Sì | 0 a MAX_RESOLUTION |
| `vae` | Il VAE p-h3-image. Necessario non appena viene collegato uno slot immagine, perché i latent di riferimento vengono codificati con esso. | VAE | No | - |
| `images` | Gruppo espandibile di fino a 9 immagini, da `image_1` a `image_9`. `image_1` è l'immagine da modificare, gli slot rimanenti sono riferimenti. | AUTOGROW | No | 0 a 9 immagini |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `positive` | Condizionamento per il sampler p-h3-image. Quando sono collegate immagini, trasporta anche i latent di riferimento impacchettati. | CONDITIONING |
| `latent` | Latent vuoto per un singolo frame statico, inclusi i due latent audio che il modello si aspetta. | LATENT |

**Nota:** Le immagini richiedono l'input `vae`. Eseguire il nodo con un'immagine collegata e senza VAE genera un errore.

**Nota:** Il condizionamento copre un singolo frame. Per video o audio, usare invece i nodi video MiniMax H3.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PH3ImageConditioning/it.md)

---
**Source fingerprint (SHA-256):** `f1f5e5b2d3ff9bc2f3b81f3d0dd722e725c7930c6f95bf44ad83bc64357d2fb7`
