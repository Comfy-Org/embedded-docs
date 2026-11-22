# SVD_img2vid_Conditioning

Il nodo SVD_img2vid_Conditioning prepara i dati di condizionamento per la generazione video utilizzando Stable Video Diffusion. Riceve un'immagine iniziale e la elabora tramite gli encoder CLIP vision e VAE per creare coppie di condizionamenti positivi e negativi, insieme a uno spazio latente vuoto per la generazione video. Questo nodo imposta i parametri necessari per controllare movimento, frame rate e livelli di augmentation nel video generato.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `clip_vision` | Modello CLIP vision per codificare l'immagine di input | CLIP_VISION | Sì | - |
| `immagine iniziale` | Immagine iniziale da usare come punto di partenza per la generazione video | IMAGE | Sì | - |
| `vae` | Modello VAE per codificare l'immagine nello spazio latente | VAE | Sì | - |
| `larghezza` | Larghezza del video di output (predefinito: 1024, step: 8) | INT | Sì | 16 a MAX_RESOLUTION |
| `altezza` | Altezza del video di output (predefinito: 576, step: 8) | INT | Sì | 16 a MAX_RESOLUTION |
| `fotogrammi video` | Numero di fotogrammi da generare nel video (predefinito: 14) | INT | Sì | 1 a 4096 |
| `ID motion bucket` | Controlla la quantità di movimento nel video generato (predefinito: 127) | INT | Sì | 1 a 1023 |
| `fps` | Fotogrammi al secondo per il video generato (predefinito: 6) | INT | Sì | 1 a 1024 |
| `livello di aumentazione` | Livello di augmentation del rumore da applicare all'immagine di input (predefinito: 0.0, step: 0.01) | FLOAT | Sì | 0.0 a 10.0 |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `positive` | Dati di condizionamento positivi contenenti embedding dell'immagine e parametri video | CONDITIONING |
| `negative` | Dati di condizionamento negativi con embedding azzerati e parametri video | CONDITIONING |
| `latent` | Tensore di spazio latente vuoto pronto per la generazione video | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SVD_img2vid_Conditioning/it.md)

---
**Source fingerprint (SHA-256):** `33b295b6f2e459852aaa95d9dca26c724aa2e9ad0f884a1c7760766530a00a09`
