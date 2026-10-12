# WanInfiniteTalkToVideo

WanInfiniteTalkToVideo genera sequenze video dall'input audio. Utilizza un modello di diffusione video, condizionato dalle caratteristiche audio estratte da uno o due parlanti, per produrre una rappresentazione latente di un video di un volto parlante. Il nodo può generare una nuova sequenza o estendere una sequenza esistente usando i frame precedenti come contesto di movimento.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `mode` | La modalità di input audio. `single_speaker` usa un solo input audio. `two_speakers` abilita l'input audio aggiuntivo e le maschere elencate nella sezione Input per due parlanti. | DYNAMIC_COMBO | Sì | `"single_speaker"`<br>`"two_speakers"` |
| `model` | Il modello di diffusione video di base. | MODEL | Sì | - |
| `model_patch` | La patch del modello contenente i livelli di proiezione audio. | MODEL_PATCH | Sì | - |
| `positive` | Il condizionamento positivo per guidare la generazione. | CONDITIONING | Sì | - |
| `negative` | Il condizionamento negativo per guidare la generazione. | CONDITIONING | Sì | - |
| `vae` | Il VAE utilizzato per codificare le immagini da e verso lo spazio latente. | VAE | Sì | - |
| `width` | La larghezza del video di output in pixel. Deve essere divisibile per 16. (predefinito: 832) | INT | Sì | 16 - MAX_RESOLUTION (passo 16) |
| `height` | L'altezza del video di output in pixel. Deve essere divisibile per 16. (predefinito: 480) | INT | Sì | 16 - MAX_RESOLUTION (passo 16) |
| `length` | Il numero di frame da generare. (predefinito: 81) | INT | Sì | 1 - MAX_RESOLUTION (passo 4) |
| `clip_vision_output` | Output CLIP vision opzionale per condizionamento aggiuntivo. | CLIP_VISION_OUTPUT | No | - |
| `start_image` | Immagine iniziale opzionale per inizializzare la sequenza video. | IMAGE | No | - |
| `audio_encoder_output_1` | L'output principale dell'encoder audio contenente le caratteristiche per il primo parlante. | AUDIO_ENCODER_OUTPUT | Sì | - |
| `motion_frame_count` | Numero di frame precedenti da usare come contesto di movimento. (predefinito: 9; parametro avanzato) | INT | Sì | 1 - 33 (passo 1) |
| `audio_scale` | Un fattore di scala applicato al condizionamento audio. (predefinito: 1.0) | FLOAT | Sì | -10.0 - 10.0 (passo 0.01) |
| `previous_frames` | Frame video precedenti opzionali da cui estendere la sequenza. Gli ultimi `motion_frame_count` frame vengono usati come contesto di movimento. | IMAGE | No | - |

### Input per due parlanti

Gli input in questa sezione vengono mostrati quando `mode` è impostato su `"two_speakers"`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `audio_encoder_output_2` | Il secondo output dell'encoder audio contenente le caratteristiche per il secondo parlante. | AUDIO_ENCODER_OUTPUT | No | - |
| `mask_1` | Maschera per il primo parlante, obbligatoria se si usano due input audio. | MASK | No | - |
| `mask_2` | Maschera per il secondo parlante, obbligatoria se si usano due input audio. | MASK | No | - |

**Vincoli sui parametri:**

- Quando `mode` è impostato su `"two_speakers"`, `audio_encoder_output_2`, `mask_1` e `mask_2` sono obbligatori per la configurazione con secondo parlante.
- Se viene fornito `audio_encoder_output_2`, devono essere forniti anche sia `mask_1` sia `mask_2`.
- Se vengono forniti sia `mask_1` sia `mask_2`, deve essere fornito anche `audio_encoder_output_2`.
- Se viene fornito `previous_frames`, deve contenere almeno tanti frame quanti ne specifica `motion_frame_count`.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `model` | Il modello con patch a cui è applicato il condizionamento audio. | MODEL |
| `positive` | Il condizionamento positivo, potenzialmente modificato con contesto aggiuntivo come un'immagine iniziale o un output CLIP vision. | CONDITIONING |
| `negative` | Il condizionamento negativo, potenzialmente modificato con contesto aggiuntivo. | CONDITIONING |
| `latent` | La sequenza video generata nello spazio latente. | LATENT |
| `trim_image` | Il numero di frame dall'inizio del contesto di movimento che devono essere tagliati quando si estende una sequenza. È uguale a `motion_frame_count` quando viene fornito `previous_frames`, altrimenti 0. | INT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanInfiniteTalkToVideo/it.md)

---
**Source fingerprint (SHA-256):** `b7359490c1de86d9c82122bc227295b3b7f8a3493f629365ae0f22f9f34d9a66`
