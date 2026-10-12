# WanFunInpaintToVideo

Il nodo WanFunInpaintToVideo prepara dati di condizionamento e latenti per la generazione video in stile inpainting, utilizzando un'immagine iniziale e un'immagine finale opzionali per guidare il risultato. Funziona passando il condizionamento, il VAE e i fotogrammi immagine forniti attraverso la stessa logica usata per la generazione video con primo e ultimo fotogramma, e restituisce il condizionamento aggiornato più un latente vuoto per il campionamento.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `positive` | Prompt di condizionamento positivo per la generazione video | CONDITIONING | Sì | - |
| `negative` | Prompt di condizionamento negativo da evitare nella generazione video | CONDITIONING | Sì | - |
| `vae` | Modello VAE usato per codificare e decodificare i fotogrammi video | VAE | Sì | - |
| `width` | Larghezza del video in output in pixel (predefinito: 832, passo: 16) | INT | Sì | da 16 a MAX_RESOLUTION |
| `height` | Altezza del video in output in pixel (predefinito: 480, passo: 16) | INT | Sì | da 16 a MAX_RESOLUTION |
| `length` | Numero di fotogrammi nella sequenza video (predefinito: 81, passo: 4) | INT | Sì | da 1 a MAX_RESOLUTION |
| `batch_size` | Numero di video da generare in un batch (predefinito: 1) | INT | Sì | da 1 a 4096 |
| `clip_vision_output` | Output CLIP vision opzionale usato come condizionamento per l'immagine iniziale | CLIP_VISION_OUTPUT | No | - |
| `start_image` | Immagine del fotogramma iniziale opzionale per la generazione video | IMAGE | No | - |
| `end_image` | Immagine del fotogramma finale opzionale per la generazione video | IMAGE | No | - |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `positive` | Output di condizionamento positivo elaborato | CONDITIONING |
| `negative` | Output di condizionamento negativo elaborato | CONDITIONING |
| `latent` | Rappresentazione latente del video generato | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunInpaintToVideo/it.md)

---
**Source fingerprint (SHA-256):** `70b58e961c5df12f94183245ce320197439b2505b47d0bb3ff643b25c9fe6175`
