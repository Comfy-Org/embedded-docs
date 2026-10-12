# SeedVR2ProgressiveSampler

Campionatore sequenziale con chunking temporale per workflow nativi SeedVR2. Questo nodo elabora latent video lunghi suddividendoli in chunk temporali più piccoli, campionando ciascun chunk in sequenza e miscelando insieme i risultati. Funge da sostituto diretto del KSampler standard quando si lavora con modelli SeedVR2 su sequenze che altrimenti causerebbero errori di memoria esaurita.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello utilizzato per il denoising del latente di input | MODEL | Sì | |
| `seed` | Il seme casuale utilizzato per creare il rumore (predefinito: 0) | INT | Sì | 0 a 0xffffffffffffffff |
| `steps` | Il numero di passaggi utilizzati nel processo di denoising (predefinito: 20) | INT | Sì | 1 a 10000 |
| `cfg` | La scala Classifier-Free Guidance bilancia creatività e aderenza al prompt. Valori più alti producono immagini più fedeli al prompt, tuttavia valori troppo alti influiscono negativamente sulla qualità (predefinito: 1.0) | FLOAT | Sì | 0.0 a 100.0 |
| `sampler_name` | L'algoritmo utilizzato durante il campionamento; può influire su qualità, velocità e stile dell'output generato | COMBO | Sì | Opzioni multiple disponibili |
| `scheduler` | Lo scheduler controlla come il rumore viene gradualmente rimosso per formare l'immagine | COMBO | Sì | Opzioni multiple disponibili |
| `positive` | Il condizionamento che descrive gli attributi che desideri includere nell'immagine | CONDITIONING | Sì | |
| `negative` | Il condizionamento che descrive gli attributi che desideri escludere dall'immagine | CONDITIONING | Sì | |
| `latent` | L'immagine latente da sottoporre a denoising | LATENT | Sì | |
| `denoise` | La quantità di denoising applicata; valori più bassi manterranno la struttura dell'immagine iniziale, consentendo il campionamento image-to-image (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `frames_per_chunk` | Frame in pixel per chunk temporale. Deve essere un valore 4n+1 (1, 5, 9, 13, 17, 21, ...) per rispettare i vincoli di SeedVR2 (predefinito: 21) | INT | Sì | 1 a 16384 (passo di 4) |
| `temporal_overlap` | Frame latenti miscelati tra chunk adiacenti per nascondere la giunzione; 0 significa nessuna miscelazione (predefinito: 0) | INT | Sì | 0 a 16384 |
| `chunking_mode` | manual = usa esattamente frames_per_chunk; auto = riduci il chunk finché non entra nella VRAM (predefinito: "manual") | COMBO | Sì | "manual"<br>"auto" |

**Nota su `frames_per_chunk`:** Questo parametro deve essere un conteggio di frame in pixel pari a 4n+1 (1, 5, 9, 13, 17, 21, ...). Il nodo solleverà un errore se viene fornito un valore non valido.

**Nota su `temporal_overlap`:** Il valore di sovrapposizione viene automaticamente limitato a un massimo di uno in meno rispetto alla dimensione del chunk latente per garantire un'elaborazione valida del chunk.

**Nota su `chunking_mode`:** Quando è impostato su "auto", il nodo proverà automaticamente dimensioni di chunk più piccole se il chunk corrente causa un errore di memoria esaurita. Se tutti i tentativi falliscono, il nodo solleva un errore.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `latent` | L'output latente denoisato, concatenato da tutti i chunk temporali in un singolo tensore latente SeedVR2 ricomposto | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2ProgressiveSampler/it.md)

---
**Source fingerprint (SHA-256):** `a4574c3e619954b5569551b5b2ba112ecbff918dcebb5ba718a14e77701144a9`
