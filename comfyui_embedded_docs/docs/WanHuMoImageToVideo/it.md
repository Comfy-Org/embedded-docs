# WanHuMoImageToVideo

Il nodo WanHuMoImageToVideo prepara i dati di condizionamento e un video latente vuoto per la pipeline di generazione video Wan HuMo. Può associare un'immagine di riferimento e embedding audio agli input di condizionamento positivo e negativo, e crea un latente riempito di zeri dimensionato in base a `width`, `height`, `length` e `batch_size` richiesti.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `positive` | Input di condizionamento positivo che guida la generazione video verso il contenuto desiderato. | CONDITIONING | Sì | - |
| `negative` | Input di condizionamento negativo che allontana la generazione video da contenuti indesiderati. | CONDITIONING | Sì | - |
| `vae` | Modello VAE utilizzato per codificare le immagini di riferimento nello spazio latente. | VAE | Sì | - |
| `width` | Larghezza in pixel dei fotogrammi del video di output. Predefinito: 832. | INT | Sì | 16 to MAX_RESOLUTION, step 16 |
| `height` | Altezza in pixel dei fotogrammi del video di output. Predefinito: 480. | INT | Sì | 16 to MAX_RESOLUTION, step 16 |
| `length` | Numero di fotogrammi nella sequenza video generata. Predefinito: 97. | INT | Sì | 1 to MAX_RESOLUTION, step 4 |
| `batch_size` | Numero di sequenze video da generare simultaneamente. Predefinito: 1. | INT | Sì | 1 to 4096 |
| `audio_encoder_output` | Dati opzionali di codifica audio che possono influenzare la generazione video in base al contenuto audio. | AUDIOENCODEROUTPUT | No | - |
| `ref_image` | Immagine di riferimento opzionale usata per guidare lo stile e il contenuto della generazione video. Viene utilizzata solo la prima immagine del batch. | IMAGE | No | - |

**Nota:** Quando viene fornita un'immagine di riferimento, la prima immagine del batch viene ingrandita alla `width` e `height` richieste usando l'interpolazione bilineare e codificata con il VAE. Quel latente di riferimento viene associato al condizionamento positivo, mentre un latente riempito di zeri della stessa forma viene associato al condizionamento negativo. Quando viene fornito `audio_encoder_output`, gli embedding audio vengono interpolati e associati al condizionamento positivo, mentre un embedding audio riempito di zeri viene associato al condizionamento negativo. Se uno dei due input opzionali viene omesso, vengono usati tensori segnaposto riempiti di zeri: un latente di riferimento zero di forma `[batch_size, 16, 1, height // 8, width // 8]` e/o embedding audio zero di forma `[batch_size, latent_t + 1, 8, 5, 1280]`, dove `latent_t = ((length - 1) // 4) + 1`.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `positive` | Condizionamento positivo modificato con l'immagine di riferimento e/o gli embedding audio incorporati. | CONDITIONING |
| `negative` | Condizionamento negativo modificato con l'immagine di riferimento e/o gli embedding audio incorporati. | CONDITIONING |
| `latent` | Rappresentazione latente inizializzata a zero per la sequenza video, dimensionata in base a `width`, `height`, `length` e `batch_size`. Forma: `[batch_size, 16, latent_t, height // 8, width // 8]`, dove `latent_t = ((length - 1) // 4) + 1`. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanHuMoImageToVideo/it.md)

---
**Source fingerprint (SHA-256):** `db674a4a00729a8715988030083e2858f958cd21de73bbbe4ed6d76f5f539419`
