# SV3D_Conditioning

SV3D_Conditioning prepara i dati di condizionamento per la generazione di video 3D utilizzando il modello SV3D. Prende un'immagine iniziale e la elabora tramite gli encoder CLIP vision e VAE per creare condizionamenti positivo e negativo, insieme a una rappresentazione latente. Il nodo genera sequenze di elevazione e azimut della camera per la generazione di video multi-frame in base al numero specificato di frame video.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `clip_vision` | Il modello CLIP vision utilizzato per codificare l'immagine di input | CLIP_VISION | Sì | - |
| `init_image` | L'immagine iniziale che funge da punto di partenza per la generazione del video 3D | IMAGE | Sì | - |
| `vae` | Il modello VAE utilizzato per codificare l'immagine nello spazio latente | VAE | Sì | - |
| `width` | La larghezza di output per i frame video generati (predefinito: 576, passo di 8) | INT | Sì | 16 a MAX_RESOLUTION |
| `height` | L'altezza di output per i frame video generati (predefinito: 576, passo di 8) | INT | Sì | 16 a MAX_RESOLUTION |
| `video_frames` | Il numero di frame da generare per la sequenza video (predefinito: 21) | INT | Sì | 1 a 4096 |
| `elevation` | L'angolo di elevazione della camera in gradi per la vista 3D (predefinito: 0.0, passo di 0.1) | FLOAT | Sì | -90.0 a 90.0 |

Nota: L'azimut della camera parte da 0 gradi e aumenta di una quantità costante a ogni frame, così che la camera completi un'orbita completa di 360 gradi attorno all'oggetto attraverso i frame generati. L'incremento per frame è calcolato come 360 diviso (`video_frames` - 1), usando un divisore minimo di 2 quando viene richiesto un solo frame. Il valore `elevation` rimane costante per ogni frame.

L'`init_image` viene ridimensionata alla `width` e `height` specificate prima della codifica VAE, e il latente restituito usa dimensioni `video_frames` x 4 x (`height` // 8) x (`width` // 8).

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `positive` | I dati di condizionamento positivo contenenti embedding dell'immagine e parametri della camera per la generazione | CONDITIONING |
| `negative` | I dati di condizionamento negativo con embedding e latenti azzerati per la generazione contrastiva | CONDITIONING |
| `latent` | Un tensore latente vuoto con dimensioni corrispondenti ai frame video e alla risoluzione specificati | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SV3D_Conditioning/it.md)

---
**Source fingerprint (SHA-256):** `e28173cfa560290e66b032687088cf0b981256ca5c21f6aa608e0fdaec886665`
