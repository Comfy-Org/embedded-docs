# WanFirstLastFrameToVideo

Il nodo WanFirstLastFrameToVideo prepara il condizionamento per la generazione video combinando un frame iniziale e un frame finale con prompt testuali. Codifica le immagini dei frame nello spazio latente, crea una maschera che indica al modello video quali frame sono già noti e collega le feature di visione CLIP quando vengono fornite. Il nodo restituisce il condizionamento positivo e negativo aggiornati, più un latente vuoto che definisce le dimensioni e la lunghezza del video da generare.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `positive` | Condizionamento testuale positivo utilizzato per guidare la generazione video. | CONDITIONING | Sì | - |
| `negative` | Condizionamento testuale negativo utilizzato per guidare la generazione video. | CONDITIONING | Sì | - |
| `vae` | Modello VAE utilizzato per codificare le immagini dei frame combinate nello spazio latente. | VAE | Sì | - |
| `width` | Larghezza del video generato in pixel (predefinito: 832, passo: 16). | INT | Sì | 16 to MAX_RESOLUTION |
| `height` | Altezza del video generato in pixel (predefinito: 480, passo: 16). | INT | Sì | 16 to MAX_RESOLUTION |
| `length` | Numero di frame nella sequenza video (predefinito: 81, passo: 4). | INT | Sì | 1 to MAX_RESOLUTION |
| `batch_size` | Numero di video da generare contemporaneamente (predefinito: 1). | INT | Sì | 1 to 4096 |
| `clip_vision_start_image` | Feature di visione CLIP estratte dall'immagine iniziale. Se vengono forniti sia l'input di visione CLIP iniziale che quello finale, le loro feature vengono combinate. | CLIP_VISION_OUTPUT | No | - |
| `clip_vision_end_image` | Feature di visione CLIP estratte dall'immagine finale. Se vengono forniti sia l'input di visione CLIP iniziale che quello finale, le loro feature vengono combinate. | CLIP_VISION_OUTPUT | No | - |
| `start_image` | Immagine del frame iniziale per la sequenza video. I suoi primi `length` frame vengono utilizzati e ridimensionati a `width` × `height`. | IMAGE | No | - |
| `end_image` | Immagine del frame finale per la sequenza video. I suoi ultimi `length` frame vengono utilizzati e ridimensionati a `width` × `height`. | IMAGE | No | - |

**Nota:** Quando viene fornito almeno uno tra `start_image` o `end_image`, il nodo costruisce una sequenza di frame combinata in cui i frame iniziale e finale vengono inseriti e i frame rimanenti utilizzano un segnaposto grigio neutro (0.5). Una maschera contrassegna le regioni riempite come note e le regioni segnaposto come sconosciute, consentendo al modello video di generare i frame intermedi. Quando viene fornita un'immagine iniziale, la regione nota si estende anche a 3 frame extra oltre l'immagine. La stessa immagine frame codificata e la maschera vengono collegate sia al condizionamento `positive` che a quello `negative`. Se vengono forniti entrambi gli input di visione CLIP, i loro stati nascosti vengono concatenati; se ne viene fornito solo uno, viene utilizzato da solo. La lunghezza del video latente è derivata da `length` dopo la compressione temporale: `((length - 1) // 4) + 1`.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `positive` | Condizionamento positivo con l'immagine frame codificata, la maschera e (se fornite) le feature di visione CLIP allegate. | CONDITIONING |
| `negative` | Condizionamento negativo con l'immagine frame codificata, la maschera e (se fornite) le feature di visione CLIP allegate. | CONDITIONING |
| `latent` | Tensore latente vuoto (tutti zeri) con forma corrispondente alla dimensione del batch, alla lunghezza del video e alla risoluzione specificate. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFirstLastFrameToVideo/it.md)

---
**Source fingerprint (SHA-256):** `0072e441cb80334c3c961d1bbf2d081c78bc38ed1eacca840c577a2d01b36f05`
