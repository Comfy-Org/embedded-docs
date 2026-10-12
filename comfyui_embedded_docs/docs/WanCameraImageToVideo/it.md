# WanCameraImageToVideo

Il nodo WanCameraImageToVideo prepara i dati di condizionamento e latent per la generazione video controllata dalla camera a partire da immagini. Accetta prompt di condizionamento positivi e negativi, insieme a input opzionali come un'immagine iniziale, l'output di CLIP vision e le condizioni della camera, e restituisce il condizionamento aggiornato più un tensore latent vuoto pronto per essere riempito da un modello video.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `positive` | Prompt di condizionamento positivi per la generazione video | CONDITIONING | Sì | - |
| `negative` | Prompt di condizionamento negativi da evitare nella generazione video | CONDITIONING | Sì | - |
| `vae` | Modello VAE per codificare immagini nello spazio latente | VAE | Sì | - |
| `width` | Larghezza del video di output in pixel (predefinito: 832, passo: 16) | INT | Sì | da 16 a MAX_RESOLUTION |
| `height` | Altezza del video di output in pixel (predefinito: 480, passo: 16) | INT | Sì | da 16 a MAX_RESOLUTION |
| `length` | Numero di frame nella sequenza video (predefinito: 81, passo: 4) | INT | Sì | da 1 a MAX_RESOLUTION |
| `batch_size` | Numero di video da generare simultaneamente (predefinito: 1) | INT | Sì | da 1 a 4096 |
| `clip_vision_output` | Output CLIP vision opzionale per condizionamento aggiuntivo | CLIP_VISION_OUTPUT | No | - |
| `start_image` | Immagine iniziale opzionale per inizializzare la sequenza video. Se fornita, vengono usati solo i primi `length` frame e l'immagine viene ridimensionata per corrispondere a `width` e `height` specificati. I primi frame della sequenza vengono codificati nel latent e viene applicata una maschera per fondere i frame iniziali con il contenuto generato. | IMAGE | No | - |
| `camera_conditions` | Condizioni di embedding della camera opzionali per la generazione video. Se fornite, queste condizioni vengono applicate sia al condizionamento positivo sia a quello negativo. | WAN_CAMERA_EMBEDDING | No | - |

**Nota:** Quando viene fornito `start_image`, il nodo imposta i valori `concat_latent_image` e `concat_mask` sia sul condizionamento `positive` sia su quello `negative`. I parametri `camera_conditions` e `clip_vision_output` sono opzionali, ma se forniti modificano il condizionamento sia per i prompt positivi sia per quelli negativi.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `positive` | Condizionamento positivo modificato con condizioni della camera, output CLIP vision e/o dati dell'immagine iniziale applicati | CONDITIONING |
| `negative` | Condizionamento negativo modificato con condizioni della camera, output CLIP vision e/o dati dell'immagine iniziale applicati | CONDITIONING |
| `latent` | Rappresentazione latent video vuota per l'uso con modelli video. Il tensore latent ha dimensioni [batch_size, 16, frames, height/8, width/8], dove frames è calcolato come ((length - 1) // 4) + 1. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanCameraImageToVideo/it.md)

---
**Source fingerprint (SHA-256):** `467a82be0dfd6ac1c3b2dd2a6cb02e0d0749de4536a7fbdb000456b817b20ebb`
