# WanSoundImageToVideoExtend

Il nodo WanSoundImageToVideoExtend estende un latent video esistente generando frame aggiuntivi, opzionalmente guidato da audio, un'immagine di riferimento e un video di controllo. Prende un latent video iniziale e produce una sequenza video più lunga, usando il condizionamento e i segnali audio forniti per influenzare il nuovo contenuto.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `positive` | Prompt di condizionamento positivi che guidano ciò che il video dovrebbe includere | CONDITIONING | Sì | - |
| `negative` | Prompt di condizionamento negativi che specificano ciò che il video dovrebbe evitare | CONDITIONING | Sì | - |
| `vae` | Autoencoder variazionale utilizzato per codificare l'immagine di riferimento e il video di controllo nello spazio latente | VAE | Sì | - |
| `length` | Numero totale di frame da generare per la sequenza video (predefinito: 77, passo: 4) | INT | Sì | 1 to MAX_RESOLUTION |
| `video_latent` | Latent video iniziale che funge da punto di partenza per l'estensione. La larghezza, l'altezza, la dimensione del batch e l'offset dei frame dell'output derivano da questo latent. I suoi ultimi 19 frame vengono usati come condizionamento del movimento di riferimento. | LATENT | Sì | - |
| `audio_encoder_output` | Embedding audio opzionali che possono influenzare la generazione video in base alle caratteristiche del suono. Quando forniti, l'audio viene interpolato e convertito in un bucket di embedding audio che viene aggiunto al condizionamento. | AUDIOENCODEROUTPUT | No | - |
| `ref_image` | Immagine di riferimento opzionale che fornisce una guida visiva per la generazione video. L'immagine viene sottoposta a upscaling per corrispondere alle dimensioni target e codificata in un latent, che viene poi aggiunto sia al condizionamento positivo sia a quello negativo. Viene utilizzata solo la prima immagine del batch. | IMAGE | No | - |
| `control_video` | Video di controllo opzionale che guida il movimento e la struttura del video generato. Il video viene sottoposto a upscaling, codificato e aggiunto sia al condizionamento positivo sia a quello negativo. Il video di controllo viene troncato alla `length` specificata. | IMAGE | No | - |

Nota: il latent di output viene inizializzato a zeri con le dimensioni target. Il `video_latent` di input non viene copiato in questo output; i suoi ultimi 19 frame vengono invece usati come movimento di riferimento.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `positive` | Condizionamento positivo elaborato con contesto video applicato, inclusi embedding audio, latent di riferimento, movimento di riferimento e video di controllo, se forniti | CONDITIONING |
| `negative` | Condizionamento negativo elaborato con contesto video applicato, inclusi embedding audio (azzerati), latent di riferimento, movimento di riferimento e video di controllo, se forniti | CONDITIONING |
| `latent` | Rappresentazione latent video della sequenza estesa, inizializzata a zeri con dimensioni derivate dal `video_latent` di input e dalla `length` target | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideoExtend/it.md)

---
**Source fingerprint (SHA-256):** `32b58aaba566f346a0388ba804fc92e7ad426bf2e9e7039e5fdb0bf6a746e972`
