# WanSoundImageToVideo

Il nodo WanSoundImageToVideo prepara il condizionamento e un tensore latente video vuoto per la generazione sound-to-video di Wan. Può opzionalmente incorporare una codifica audio, un'immagine di riferimento, un video di controllo e un riferimento di movimento per guidare il video generato.

## Input
| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `positive` | Prompt di condizionamento positivi che guidano il contenuto che deve apparire nel video generato | CONDITIONING | Sì | - |
| `negative` | Prompt di condizionamento negativi che specificano il contenuto da evitare nel video generato | CONDITIONING | Sì | - |
| `vae` | Modello VAE utilizzato per codificare immagini di riferimento, riferimenti di movimento e fotogrammi del video di controllo in rappresentazioni latenti | VAE | Sì | - |
| `width` | Larghezza del video di output in pixel (predefinito: 832, passo: 16) | INT | Sì | 16 a MAX_RESOLUTION |
| `height` | Altezza del video di output in pixel (predefinito: 480, passo: 16) | INT | Sì | 16 a MAX_RESOLUTION |
| `length` | Numero di fotogrammi nel video generato (predefinito: 77, passo: 4) | INT | Sì | 1 a MAX_RESOLUTION |
| `batch_size` | Numero di video da generare simultaneamente (predefinito: 1) | INT | Sì | 1 a 4096 |
| `audio_encoder_output` | Codifica audio opzionale che può influenzare la generazione del video in base alle caratteristiche del suono. Quando fornita, le caratteristiche audio vengono interpolate e utilizzate per condizionare la generazione del video. | AUDIO_ENCODER_OUTPUT | No | - |
| `ref_image` | Immagine di riferimento opzionale che fornisce una guida visiva per il contenuto del video. L'immagine viene ingrandita per corrispondere alla larghezza e all'altezza specificate, quindi codificata in una rappresentazione latente. Viene utilizzata come riferimento solo la prima immagine dell'input. | IMAGE | No | - |
| `control_video` | Video di controllo opzionale che guida il movimento e la struttura del video generato. Il video viene ingrandito e codificato, quindi utilizzato per condizionare l'output. Vengono utilizzati solo i primi `length` fotogrammi. | IMAGE | No | - |
| `ref_motion` | Riferimento di movimento opzionale che fornisce una guida per i pattern di movimento nel video. Se l'input ha più di 73 fotogrammi, vengono utilizzati solo gli ultimi 73. Se vengono forniti meno di 73 fotogrammi, la sequenza viene riempita con fotogrammi neutri. | IMAGE | No | - |

Nota: tutti gli input opzionali possono essere usati indipendentemente o insieme. Il nodo modifica il condizionamento `positive` e `negative` fornito in base a quali input opzionali sono collegati.

## Output
| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `positive` | Condizionamento positivo elaborato che è stato modificato per la generazione video, includendo embedding audio, latenti di riferimento, riferimenti di movimento e condizionamento del video di controllo quando vengono forniti i corrispondenti input opzionali | CONDITIONING |
| `negative` | Condizionamento negativo elaborato che è stato modificato per la generazione video, includendo embedding audio (impostati a zero), latenti di riferimento, riferimenti di movimento e condizionamento del video di controllo quando vengono forniti i corrispondenti input opzionali | CONDITIONING |
| `latent` | Tensore latente video vuoto utilizzato come punto di partenza per la generazione. Il tensore latente ha forma `[batch_size, 16, latent_t, height/8, width/8]`, dove `latent_t` è calcolato come `((length - 1) // 4) + 1`. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideo/it.md)

---
**Source fingerprint (SHA-256):** `b1148cd00d8999dd6842e3c2fb13655fda8f20d5befed975a6d1652688b2807c`
