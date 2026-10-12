# CosmosPredict2ImageToVideoLatent

Crea latent video per il flusso di lavoro image-to-video di Cosmos Predict2. Il nodo può produrre un latent video vuoto di una determinata dimensione e lunghezza, oppure inserire immagini iniziali e/o finali codificate nella sequenza, in modo che quei fotogrammi vengano mantenuti durante la generazione. Qualsiasi immagine fornita viene ridimensionata alla `width` e `height` richieste e codificata con il VAE fornito prima di essere posizionata all'inizio e/o alla fine della sequenza latente.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `vae` | Il modello VAE utilizzato per codificare le immagini iniziali e finali nello spazio latente | VAE | Sì | - |
| `width` | Larghezza del video di output in pixel (predefinito: 848, deve essere un multiplo di 16) | INT | Sì | 16 a MAX_RESOLUTION |
| `height` | Altezza del video di output in pixel (predefinito: 480, deve essere un multiplo di 16) | INT | Sì | 16 a MAX_RESOLUTION |
| `length` | Numero di fotogrammi nella sequenza video (predefinito: 93) | INT | Sì | 1 a MAX_RESOLUTION |
| `batch_size` | Numero di sequenze video da generare (predefinito: 1) | INT | Sì | 1 a 4096 |
| `start_image` | Immagine iniziale opzionale per la sequenza video | IMAGE | No | - |
| `end_image` | Immagine finale opzionale per la sequenza video | IMAGE | No | - |

**Nota:** Quando non viene fornita né `start_image` né `end_image`, il nodo restituisce semplicemente un latent vuoto della dimensione e lunghezza richieste. Quando viene fornita una o entrambe le immagini, vengono ridimensionate a `width` e `height`, codificate con il `vae` e posizionate all'inizio e/o alla fine della sequenza latente. Le regioni corrispondenti sono contrassegnate nella maschera del rumore in modo che vengano preservate durante la generazione. I latent codificati vengono convertiti con il formato latent di Wan 2.1, e il latent e la maschera risultanti vengono ripetuti `batch_size` volte.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `LATENT` | Il latent video generato contenente `samples` (la sequenza latente video) e, quando almeno uno tra `start_image` o `end_image` è fornito, una `noise_mask` che contrassegna i fotogrammi che dovrebbero essere preservati durante la generazione | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosPredict2ImageToVideoLatent/it.md)

---
**Source fingerprint (SHA-256):** `842bd2b8cda438e7b938439d4eba280478939e3302dc1846d52595d40082ff05`
