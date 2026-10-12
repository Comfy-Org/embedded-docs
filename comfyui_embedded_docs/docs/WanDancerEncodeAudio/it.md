# WanDancerEncodeAudio

Questo nodo analizza una clip audio e la trasforma in un insieme di feature che possono guidare un modello di generazione video. Stima tempo e battiti, estrae feature come spettrogramma Mel, MFCC, chroma e onset, quindi le assembla insieme a un frame rate calcolato per la sincronizzazione.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `audio` | L'input audio da analizzare e codificare. Se l'audio ha più canali, i canali vengono mediati in mono prima dell'estrazione delle feature. | AUDIO | Sì | - |
| `video_frames` | Il numero di fotogrammi nel video di destinazione. Utilizzato per calcolare il frame rate per la sincronizzazione (predefinito: 149). | INT | Sì | Min: 1, Max: 16384 (MAX_RESOLUTION), Passo: 4 |
| `audio_inject_scale` | La scala per le feature audio quando vengono iniettate nel modello video (predefinito: 1.0). | FLOAT | Sì | Min: 0.0, Max: 10.0, Passo: 0.01 |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `audio_encoder_output` | Un dizionario contenente le feature audio elaborate, il frame rate calcolato (fps) e la scala di iniezione audio. Questo output viene utilizzato per condizionare il modello di generazione video. | AUDIO_ENCODER_OUTPUT |
| `fps_string` | Una stringa di testo che descrive il frame rate calcolato (fps) in base alla durata dell'audio e al numero di fotogrammi video. Questa stringa è pensata per essere utilizzata nel prompt del modello video. È formattata in cinese per corrispondere alla pipeline di riferimento. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerEncodeAudio/it.md)

---
**Source fingerprint (SHA-256):** `ce27a3bdea2d9e3cf8875c24236a2a0a1429e9bc13a58581e372fb669d2c0018`
