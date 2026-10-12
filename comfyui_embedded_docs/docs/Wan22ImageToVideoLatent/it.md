# Wan22ImageToVideoLatent

Wan22ImageToVideoLatent crea rappresentazioni latenti video a partire da immagini. Genera uno spazio latente video vuoto con larghezza, altezza, lunghezza in frame e dimensione del batch specificate, e può facoltativamente codificare una sequenza di immagini iniziale nei frame iniziali. Quando viene fornita un'immagine iniziale, il nodo la codifica nello spazio latente e crea una maschera di rumore corrispondente che indica quali regioni devono essere sottoposte a denoising durante la generazione.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `vae` | Il modello VAE utilizzato per codificare l'immagine iniziale nello spazio latente | VAE | Sì | - |
| `width` | La larghezza del video di output in pixel (predefinito: 1280, passo: 32) | INT | Sì | 32 a MAX_RESOLUTION |
| `height` | L'altezza del video di output in pixel (predefinito: 704, passo: 32) | INT | Sì | 32 a MAX_RESOLUTION |
| `length` | Il numero di frame nella sequenza video (predefinito: 49, passo: 4) | INT | Sì | 1 a MAX_RESOLUTION |
| `batch_size` | Il numero di latenti video da generare (predefinito: 1) | INT | Sì | 1 a 4096 |
| `start_image` | Sequenza di immagini iniziale opzionale da codificare nei frame iniziali del latente video (usa i primi `length` frame) | IMAGE | No | - |

**Nota:** Quando viene fornito `start_image`, la sequenza di immagini viene ridimensionata alle dimensioni `width` e `height` di destinazione, codificata con il VAE e inserita nei primi frame del latente. La maschera di rumore per quei frame è impostata su 0 (preservati), mentre i frame rimanenti hanno un valore di maschera pari a 1 (da sottoporre a denoising). Il latente ha sempre 48 canali, dimensioni spaziali di `height / 16` per `width / 16` e una dimensione temporale di `((length - 1) // 4) + 1`. `width` e `height` devono essere divisibili per 16 (imposto dal passo di 32), e `length` aumenta la dimensione temporale a passi di 4.

Quando `start_image` non viene fornito, viene restituito un latente completamente vuoto senza maschera di rumore, e l'input `batch_size` non viene applicato a quel latente vuoto.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `samples` | La rappresentazione latente video generata, ripetuta per ogni elemento del batch | LATENT |
| `noise_mask` | La maschera di rumore che indica quali regioni devono essere sottoposte a denoising (valore 1) e quali mantengono l'immagine iniziale codificata (valore 0) | LATENT |

Entrambi i campi vengono restituiti insieme all'interno di un singolo output LATENT.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22ImageToVideoLatent/it.md)

---
**Source fingerprint (SHA-256):** `3d05980641eeef2e86df7a845aa8b2bd703882db98fe71adef2746ab34a9d717`
