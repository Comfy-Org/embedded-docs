# CosmosImageToVideoLatent

Il nodo CosmosImageToVideoLatent crea una rappresentazione latente video dalle immagini di input. Costruisce un latent video vuoto con la larghezza, l'altezza e il numero di fotogrammi richiesti, poi codifica opzionalmente un'immagine iniziale nei fotogrammi iniziali e/o un'immagine finale nei fotogrammi finali. Quando vengono fornite immagini, genera anche una maschera di rumore in modo che i fotogrammi codificati rimangano fissi durante la generazione.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `vae` | Il modello VAE usato per codificare le immagini nello spazio latente video. | VAE | Sì | - |
| `width` | La larghezza del video di output in pixel (predefinito: 1280). | INT | Sì | 16 to MAX_RESOLUTION (step: 16) |
| `height` | L'altezza del video di output in pixel (predefinito: 704). | INT | Sì | 16 to MAX_RESOLUTION (step: 16) |
| `length` | Il numero totale di fotogrammi nel video (predefinito: 121). | INT | Sì | 1 to MAX_RESOLUTION (step: 8) |
| `batch_size` | Il numero di latent video da generare (predefinito: 1). | INT | Sì | 1 to 4096 |
| `start_image` | Immagine o sequenza di immagini opzionale da codificare all'inizio del video. | IMAGE | No | - |
| `end_image` | Immagine o sequenza di immagini opzionale da codificare alla fine del video. | IMAGE | No | - |

**Nota:**
- Quando non viene fornito né `start_image` né `end_image`, il nodo restituisce un latent vuoto senza maschera di rumore.
- Quando viene fornito `start_image`, viene codificato nei primi fotogrammi del latent e tali fotogrammi sono contrassegnati con valore della maschera di rumore 0 (preservati). Quando viene fornito `end_image`, viene codificato negli ultimi fotogrammi e tali fotogrammi sono contrassegnati con valore della maschera di rumore 0. I fotogrammi rimanenti mantengono un valore della maschera pari a 1.
- Il latent ha 16 canali e le sue dimensioni spaziali sono `height / 8` per `width / 8`. Il numero di fotogrammi latenti è `((length - 1) // 8) + 1`.
- `batch_size` ripete il latent e, quando presente, la maschera di rumore.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `latent` | Il latent video generato contenente le immagini iniziale e/o finale opzionalmente codificate e, quando vengono fornite immagini, una maschera di rumore corrispondente con valore 0 sui fotogrammi preservati. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CosmosImageToVideoLatent/it.md)

---
**Source fingerprint (SHA-256):** `0b06ccfcb14c27c81eeebbbff519da1e187970d4cfc19c8796fc3da20688245c`
