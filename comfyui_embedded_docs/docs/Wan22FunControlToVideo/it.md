# Wan22FunControlToVideo

Il nodo Wan22FunControlToVideo prepara i dati di condizionamento e un tensore latente vuoto per la generazione video con il modello video Wan. Codifica immagini di riferimento e video di controllo opzionali nello spazio latente, li collega al condizionamento positivo e negativo e crea un tensore latente riempito di zeri con le dimensioni spaziali e temporali corrette per il video richiesto.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `positive` | Input di condizionamento positivo per guidare la generazione video | CONDITIONING | Sì | - |
| `negative` | Input di condizionamento negativo per guidare la generazione video | CONDITIONING | Sì | - |
| `vae` | Modello VAE usato per codificare le immagini nello spazio latente | VAE | Sì | - |
| `width` | Larghezza del video di output in pixel (predefinito: 832, passo: 16) | INT | Sì | da 16 a MAX_RESOLUTION |
| `height` | Altezza del video di output in pixel (predefinito: 480, passo: 16) | INT | Sì | da 16 a MAX_RESOLUTION |
| `length` | Numero di frame nella sequenza video (predefinito: 81, passo: 4) | INT | Sì | da 1 a MAX_RESOLUTION |
| `batch_size` | Numero di sequenze video da generare (predefinito: 1) | INT | Sì | da 1 a 4096 |
| `ref_image` | Immagine di riferimento opzionale che fornisce una guida visiva per la generazione | IMAGE | No | - |
| `control_video` | Video di controllo opzionale che guida il processo di generazione | IMAGE | No | - |

**Nota:** Il parametro `length` viene elaborato a passi di 4 frame e il nodo applica automaticamente la scalatura temporale durante la costruzione dello spazio latente. Quando viene fornito `ref_image`, solo il suo primo frame viene codificato (ridimensionato a `width` x `height`) e collegato al condizionamento come latenti di riferimento. Quando viene fornito `control_video`, questo viene tagliato a `length` frame, ridimensionato, codificato e inserito nel latente concatenato usato dal condizionamento. Il latente concatenato viene duplicato lungo la dimensione dei canali e la sua disposizione dei canali dipende dal numero di canali latenti del VAE (48 canali utilizza il formato Wan 2.2, altrimenti il formato Wan 2.1). Il parametro `start_image` è referenziato nella logica di esecuzione ma non è esposto nello schema degli input del nodo, quindi non può essere impostato dall'interfaccia del nodo.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `positive` | Condizionamento positivo con dati latenti specifici per il video aggiunti, inclusi il latente concatenato, la maschera e i latenti di riferimento opzionali | CONDITIONING |
| `negative` | Condizionamento negativo con dati latenti specifici per il video aggiunti, inclusi il latente concatenato, la maschera e i latenti di riferimento opzionali | CONDITIONING |
| `latent` | Tensore latente vuoto preparato per la generazione video, dimensionato in base alla dimensione del batch, ai canali latenti, alla lunghezza, all'altezza e alla larghezza | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan22FunControlToVideo/it.md)

---
**Source fingerprint (SHA-256):** `731b848f15c13ddc662f19230acb55d195f934bad7d9ae516a288e0ed8f8d899`
