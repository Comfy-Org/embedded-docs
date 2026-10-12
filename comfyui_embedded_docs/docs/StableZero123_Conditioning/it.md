# StableZero123_Conditioning

Il nodo StableZero123_Conditioning elabora un'immagine di input e angoli di camera per generare dati di condizionamento e rappresentazioni latenti per la generazione di modelli 3D. Utilizza un modello CLIP vision per codificare le caratteristiche dell'immagine, le combina con informazioni di embedding della camera basate sugli angoli di elevazione e azimut, e produce condizionamento positivo e negativo insieme a una rappresentazione latente per le attività di generazione 3D a valle.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `clip_vision` | Il modello CLIP vision utilizzato per codificare le caratteristiche dell'immagine | CLIP_VISION | Sì | - |
| `init_image` | L'immagine di input da elaborare e codificare | IMAGE | Sì | - |
| `vae` | Il modello VAE utilizzato per codificare i pixel nello spazio latente | VAE | Sì | - |
| `width` | Larghezza di output per la rappresentazione latente (predefinito: 256, passo: 8) | INT | Sì | 16 a MAX_RESOLUTION |
| `height` | Altezza di output per la rappresentazione latente (predefinito: 256, passo: 8) | INT | Sì | 16 a MAX_RESOLUTION |
| `batch_size` | Numero di campioni da generare nel batch (predefinito: 1) | INT | Sì | 1 a 4096 |
| `elevation` | Angolo di elevazione della camera in gradi (predefinito: 0.0, passo: 0.1) | FLOAT | Sì | -180.0 a 180.0 |
| `azimuth` | Angolo di azimut della camera in gradi (predefinito: 0.0, passo: 0.1) | FLOAT | Sì | -180.0 a 180.0 |

**Nota:** I parametri `width` e `height` usano un passo di 8, quindi i valori vengono impostati con incrementi di 8. Il nodo li divide per 8 per determinare le dimensioni della rappresentazione latente. L'immagine viene ridimensionata alla `width` e `height` indicate usando un upscaling bilineare con ritaglio centrale prima della codifica VAE.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `positive` | Dati di condizionamento positivo che combinano le caratteristiche dell'immagine e gli embedding della camera, includendo l'immagine di input codificata dal VAE come latente da concatenare | CONDITIONING |
| `negative` | Dati di condizionamento negativo con caratteristiche inizializzate a zero e un latente inizializzato a zero | CONDITIONING |
| `latent` | Rappresentazione latente inizializzata a zero con dimensioni [batch_size, 4, height//8, width//8] | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableZero123_Conditioning/it.md)

---
**Source fingerprint (SHA-256):** `a694610c9f22fe0dab3ae02f4aabb33e3de8e5031c82dff5e8ba232c098f4a1d`
