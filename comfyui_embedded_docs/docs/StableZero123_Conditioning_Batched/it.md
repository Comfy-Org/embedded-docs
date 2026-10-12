# StableZero123_Conditioning_Batched

Il nodo StableZero123_Conditioning_Batched prepara i dati di condizionamento per generare un modello 3D da una singola immagine di input. Codifica l'immagine con un modello CLIP vision e un VAE, combina le caratteristiche visive con gli embedding della camera costruiti dagli angoli di elevazione e azimut, e produce condizionamento positivo e negativo più un tensore latente per un batch di campioni. Quando `batch_size` è maggiore di 1, gli angoli di elevazione e azimut vengono aumentati dei rispettivi valori di incremento per batch per ogni elemento del batch.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `clip_vision` | Il modello CLIP vision utilizzato per codificare l'immagine di input | CLIP_VISION | Sì | - |
| `init_image` | L'immagine di input iniziale da elaborare e codificare | IMAGE | Sì | - |
| `vae` | Il modello VAE utilizzato per codificare i pixel dell'immagine nello spazio latente | VAE | Sì | - |
| `width` | La larghezza di output per l'immagine elaborata (predefinito: 256) | INT | Sì | 16 a MAX_RESOLUTION (passo di 8) |
| `height` | L'altezza di output per l'immagine elaborata (predefinito: 256) | INT | Sì | 16 a MAX_RESOLUTION (passo di 8) |
| `batch_size` | Il numero di campioni di condizionamento da generare nel batch (predefinito: 1) | INT | Sì | 1 a 4096 |
| `elevation` | L'angolo di elevazione iniziale della camera in gradi (predefinito: 0.0) | FLOAT | Sì | -180.0 a 180.0 (passo di 0.1) |
| `azimuth` | L'angolo di azimut iniziale della camera in gradi (predefinito: 0.0) | FLOAT | Sì | -180.0 a 180.0 (passo di 0.1) |
| `elevation_batch_increment` | La quantità di cui incrementare l'elevazione per ogni elemento del batch (predefinito: 0.0). Contrassegnato come input avanzato. | FLOAT | Sì | -180.0 a 180.0 (passo di 0.1) |
| `azimuth_batch_increment` | La quantità di cui incrementare l'azimut per ogni elemento del batch (predefinito: 0.0). Contrassegnato come input avanzato. | FLOAT | Sì | -180.0 a 180.0 (passo di 0.1) |

**Nota:** I valori di `width` e `height` devono essere multipli di 8, poiché il nodo divide internamente queste dimensioni per 8 quando costruisce il tensore latente.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `positive` | I dati di condizionamento positivi contenenti gli embedding dell'immagine e gli embedding della camera per ogni elemento del batch | CONDITIONING |
| `negative` | I dati di condizionamento negativi con embedding inizializzati a zero | CONDITIONING |
| `latent` | Un tensore latente inizializzato a zero con dimensioni batch_size x 4 x height/8 x width/8, insieme alle informazioni di indicizzazione del batch | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning_Batched/it.md)

---
**Source fingerprint (SHA-256):** `94fc53dace8f294a746c47f8aa0da145f3e7beeb77a95912a38f0037ac094292`
