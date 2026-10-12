# WanDancerVideo

Il nodo WanDancerVideo prepara i dati di condizionamento e un tensore latente vuoto per la generazione video con il modello WanDancer. Allega immagini iniziali opzionali, maschere, embedding CLIP vision e caratteristiche audio al condizionamento positivo e negativo, così possono guidare il video generato.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `positive` | Il condizionamento positivo per guidare la generazione video. | CONDITIONING | Sì |  |
| `negative` | Il condizionamento negativo per guidare la generazione video. | CONDITIONING | Sì |  |
| `vae` | Il VAE usato per codificare l'immagine iniziale nello spazio latente. | VAE | Sì |  |
| `width` | La larghezza del video generato in pixel (predefinito: 480). | INT | Sì | 16 a MAX_RESOLUTION (passo: 16) |
| `height` | L'altezza del video generato in pixel (predefinito: 832). | INT | Sì | 16 a MAX_RESOLUTION (passo: 16) |
| `length` | Il numero di fotogrammi nel video generato. Dovrebbe rimanere 149 per WanDancer (predefinito: 149). | INT | Sì | 1 a MAX_RESOLUTION (passo: 4) |
| `clip_vision_output` | Gli embedding CLIP vision per il primo fotogramma. | CLIP_VISION_OUTPUT | No |  |
| `clip_vision_output_ref` | Gli embedding CLIP vision per l'immagine di riferimento. | CLIP_VISION_OUTPUT | No |  |
| `start_image` | L'immagine o le immagini iniziali da codificare; può contenere un numero qualsiasi di fotogrammi. | IMAGE | No |  |
| `mask` | Maschera di condizionamento immagine per l'immagine o le immagini iniziali. Il bianco viene mantenuto, il nero viene generato. Usata per le generazioni locali. | MASK | No |  |
| `audio_encoder_output` | Un output dell'encoder audio che fornisce caratteristiche audio, frequenza dei fotogrammi e valori di scala di iniezione, che vengono allegati al condizionamento quando fornito. | AUDIO_ENCODER_OUTPUT | No |  |

### Note sul comportamento dei parametri

- `start_image` è opzionale. Quando fornito, viene ridimensionato a `width` e `height`, codificato dal `vae` e allegato sia al condizionamento positivo sia a quello negativo. Se `start_image` ha più fotogrammi di `length`, i fotogrammi in eccesso vengono scartati. Se ne ha meno, i fotogrammi mancanti vengono riempiti con valori zero.
- `mask` ha effetto solo quando viene fornito anche `start_image`. Le aree bianche vengono mantenute e le aree nere vengono generate.
- `clip_vision_output_ref` ha effetto solo quando viene fornito anche `clip_vision_output`.
- `audio_encoder_output`, quando fornito, allega embedding audio, frequenza dei fotogrammi e scala di iniezione sia al condizionamento positivo sia a quello negativo.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `positive` | Il condizionamento positivo con eventuali dati allegati di latente dell'immagine iniziale, maschera, CLIP vision o audio. | CONDITIONING |
| `negative` | Il condizionamento negativo con eventuali dati allegati di latente dell'immagine iniziale, maschera, CLIP vision o audio. | CONDITIONING |
| `latent` | Un tensore latente vuoto dimensionato per la lunghezza, l'altezza e la larghezza del video richieste. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerVideo/it.md)

---
**Source fingerprint (SHA-256):** `086a0ec361cf7f7ae7ce9505b55d31d92b025c6c7c9cde192009e6664011ad05`
