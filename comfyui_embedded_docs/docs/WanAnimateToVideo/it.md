# WanAnimateToVideo

WanAnimateToVideo prepara dati di condizionamento e un latente iniziale per generare video animati con Wan, usando input come un'immagine di riferimento, posa, volto, sfondo e movimento opzionale da un chunk precedente. Supporta inoltre la generazione di video più lunghi a chunk leggendo e aggiornando un valore `video_frame_offset`. Questo nodo è contrassegnato come sperimentale.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `positive` | Condizionamento positivo per guidare la generazione verso il contenuto desiderato. | CONDITIONING | Sì | - |
| `negative` | Condizionamento negativo per allontanare la generazione da contenuti indesiderati. | CONDITIONING | Sì | - |
| `vae` | Modello VAE utilizzato per codificare input immagine e video nello spazio latente. | VAE | Sì | - |
| `width` | Larghezza del video generato in pixel (predefinito: 832, passo: 16). | INT | Sì | 16 a MAX_RESOLUTION |
| `height` | Altezza del video generato in pixel (predefinito: 480, passo: 16). | INT | Sì | 16 a MAX_RESOLUTION |
| `length` | Numero di frame da generare (predefinito: 77, passo: 4). | INT | Sì | 1 a MAX_RESOLUTION |
| `batch_size` | Numero di video da generare in un batch (predefinito: 1). | INT | Sì | 1 a 4096 |
| `clip_vision_output` | Output opzionale di CLIP vision aggiunto sia al condizionamento positivo sia a quello negativo. | CLIP_VISION_OUTPUT | No | - |
| `reference_image` | Immagine di riferimento utilizzata come punto di partenza per l'aspetto del video generato. Se non fornita, viene usata un'immagine nera. | IMAGE | No | - |
| `face_video` | Input video che fornisce indicazioni sull'espressione facciale. Viene ridimensionato a 512x512 e scalato internamente nell'intervallo da -1.0 a 1.0. | IMAGE | No | - |
| `pose_video` | Input video che fornisce indicazioni su posa e movimento. | IMAGE | No | - |
| `continue_motion_max_frames` | Numero massimo di frame trasferiti da una sequenza di movimento precedente (predefinito: 5, passo: 4). | INT | Sì | 1 a MAX_RESOLUTION |
| `background_video` | Video di sfondo usato per riempire le parti non occupate dal personaggio nei frame. | IMAGE | No | - |
| `character_mask` | Maschera che definisce le regioni del personaggio, usata per separare il personaggio dallo sfondo. | MASK | No | - |
| `continue_motion` | Frame di movimento precedenti da cui continuare, mantenendo la coerenza temporale con i chunk generati in precedenza. | IMAGE | No | - |
| `video_frame_offset` | Quantità di frame da avanzare in tutti i video di input. Usata per generare video più lunghi a chunk. Collegare all'output `video_frame_offset` del nodo precedente per estendere un video. (predefinito: 0, passo: 1) | INT | Sì | 0 a MAX_RESOLUTION |

**Vincoli dei parametri:**

- Quando viene fornito `continue_motion`, vengono usati solo i suoi ultimi `continue_motion_max_frames` frame.
- I video di input (`face_video`, `pose_video`, `background_video`, `character_mask`) vengono spostati di `video_frame_offset` prima dell'uso. Se l'offset è maggiore o uguale al numero di frame dell'input, quell'input viene ignorato, tranne nel caso di una `character_mask` con un solo frame.
- Se `character_mask` ha un solo frame, quel frame viene ripetuto per ogni frame dell'output.
- Quando `pose_video` è più corto di `length`, il suo ultimo frame viene ripetuto per riempire i frame rimanenti; la lunghezza dell'output non viene modificata.
- Se viene fornito `clip_vision_output`, viene aggiunto sia al condizionamento positivo sia a quello negativo.
- Se `reference_image` non viene fornito, viene usata come riferimento predefinito un'immagine nera (tutti valori zero).
- Se `continue_motion` non viene fornito, i frame di movimento iniziali vengono riempiti con frame grigi costanti (intensità 0.5).
- Quando viene usato `continue_motion`, `video_frame_offset` viene ridotto del numero di frame trasferiti prima di calcolare l'offset del chunk successivo, così i frame sovrapposti non vengono elaborati due volte.
- `background_video` riempie i frame di movimento dopo la porzione di movimento di riferimento; non sostituisce l'immagine di riferimento né i frame `continue_motion` trasferiti.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `positive` | Condizionamento positivo modificato con contesto video aggiuntivo, inclusi output di CLIP vision, latente del video di posa, pixel del video del volto, immagine latente concatenata e maschera concatenata. | CONDITIONING |
| `negative` | Condizionamento negativo modificato con contesto video aggiuntivo, inclusi output di CLIP vision, latente del video di posa, pixel del volto vuoti, immagine latente concatenata e maschera concatenata. | CONDITIONING |
| `latent` | Tensore latente iniziale (campioni tutti zero) per il video generato, con forma `[batch_size, 16, latent_length + trim_latent, latent_height, latent_width]`. | LATENT |
| `trim_latent` | Numero di frame latenti da tagliare dall'inizio del latente, corrispondenti ai frame dell'immagine di riferimento. | INT |
| `trim_image` | Numero di frame immagine da tagliare dall'inizio, corrispondenti ai frame di movimento di riferimento. | INT |
| `video_frame_offset` | Offset dei frame aggiornato da usare per il chunk successivo, basato sull'offset di input e sul numero di frame elaborati. | INT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanAnimateToVideo/it.md)

---
**Source fingerprint (SHA-256):** `a95bae4c7ae4ddc8a95bc9dafa2ca920b1d2166802615189537dce16949bfc03`
