# p-h3-image Conditioning

Questo nodo trasforma un prompt in condizionamento e in un latent vuoto per una singola immagine statica con p-h3-image. Senza immagini funziona come testo-immagine; con immagini collegate, `image_1` è l'immagine da modificare e gli altri slot fungono da riferimenti, a cui il prompt fa riferimento come `<Picture 1>`, `<Picture 2>` e così via. Il sampler richiede un modello patchato dal nodo MiniMax H3 sigma shift con entrambi i valori di shift impostati a 1.0.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `clip` | Il modello CLIP p-h3-image usato per tokenizzare il prompt, incluse eventuali immagini di riferimento, e per codificare il condizionamento. | CLIP | Sì | - |
| `prompt` | Cosa generare, o come modificare `image_1`. Con immagini collegate, a una breve istruzione viene anteposto `Edit <Picture 1>. `. Un'istruzione che inizia già con `Edit <Picture` o un edit brief prodotto da un prompt upsampler viene usata esattamente così com'è. | STRING | Sì | - |
| `width` | Larghezza di output in pixel. 0 usa la larghezza di `image_1` dopo il ridimensionamento, oppure 2912 quando nessuna immagine è collegata (predefinito: 0). | INT | Sì | 0 a MAX_RESOLUTION |
| `height` | Altezza di output in pixel. 0 usa l'altezza di `image_1` dopo il ridimensionamento, oppure 2912 quando nessuna immagine è collegata (predefinito: 0). | INT | Sì | 0 a MAX_RESOLUTION |
| `vae` | VAE di p-h3-image. Con esso le immagini vengono anche ancorate come latenti di riferimento; senza, condizionano solo il codificatore di testo. | VAE | No | - |
| `images` | Gruppo espandibile di fino a 9 immagini, da `image_1` a `image_9`. `image_1` è l'immagine da modificare, gli slot rimanenti sono riferimenti. | AUTOGROW | No | 0 a 9 immagini |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `positive` | Condizionamento per il sampler p-h3-image. Quando sono collegate immagini, trasporta anche i latent di riferimento impacchettati. | CONDITIONING |
| `latent` | Latent vuoto per un singolo frame statico, inclusi i due latent audio che il modello si aspetta. | LATENT |

**Nota:** Con immagini collegate e senza `vae`, le immagini influenzano comunque il prompt tramite il codificatore di testo, ma non vengono ancorate come latenti di riferimento.

**Nota:** Il condizionamento copre un singolo frame. Per video o audio, usare invece i nodi video MiniMax H3.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PH3ImageConditioning/it.md)

---
**Source fingerprint (SHA-256):** `19db44388a093dd9a90e9d2911741c732cef3e9e39664ad29dee125765f5f887`
