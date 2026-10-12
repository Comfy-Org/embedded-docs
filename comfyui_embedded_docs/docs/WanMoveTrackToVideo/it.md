# WanMoveTrackToVideo

Il nodo WanMoveTrackToVideo prepara i dati di condizionamento e dello spazio latente per la generazione video, incorporando informazioni opzionali di tracciamento del movimento. Codifica una sequenza di immagini iniziale in una rappresentazione latente e può fondere dati posizionali provenienti dalle tracce degli oggetti per guidare il movimento nel video generato. Il nodo restituisce i condizionamenti positivo e negativo modificati insieme a un tensore latente vuoto pronto per un modello video.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `positive` | L'input di condizionamento positivo da modificare. | CONDITIONING | Sì | - |
| `negative` | L'input di condizionamento negativo da modificare. | CONDITIONING | Sì | - |
| `vae` | Il modello VAE usato per codificare l'immagine iniziale nello spazio latente. | VAE | Sì | - |
| `tracks` | Dati opzionali di tracciamento del movimento contenenti i percorsi degli oggetti. Usa `track_path` e, opzionalmente, `track_visibility`; se `track_visibility` è assente, tutte le tracce vengono considerate visibili. | TRACKS | No | - |
| `strength` | Intensità del condizionamento tramite tracce. (predefinito: 1.0) | FLOAT | Sì | 0.0 - 100.0 |
| `width` | La larghezza del video di output. Deve essere divisibile per 16. (predefinito: 832) | INT | Sì | 16 - MAX_RESOLUTION |
| `height` | L'altezza del video di output. Deve essere divisibile per 16. (predefinito: 480) | INT | Sì | 16 - MAX_RESOLUTION |
| `length` | Il numero di fotogrammi nella sequenza video, in incrementi di 4. (predefinito: 81) | INT | Sì | 1 - MAX_RESOLUTION |
| `batch_size` | La dimensione del batch per l'output latente. (predefinito: 1) | INT | Sì | 1 - 4096 |
| `start_image` | L'immagine o la sequenza di immagini iniziale da codificare. | IMAGE | Sì | - |
| `clip_vision_output` | Output opzionale del modello CLIP vision da aggiungere al condizionamento. | CLIP_VISION_OUTPUT | No | - |

**Nota:** Il parametro `strength` ha effetto solo quando vengono forniti `tracks` e `strength` è maggiore di 0.0; il condizionamento tramite tracce viene applicato solo quando è fornito anche `start_image`. Se `tracks` non vengono forniti o `strength` è 0.0, la fusione delle tracce viene saltata. Quando la fusione delle tracce è attiva, il condizionamento positivo riceve l'immagine latente con tracce fuse, mentre il condizionamento negativo riceve l'immagine latente non modificata. Se `start_image` non viene fornito, non viene creato alcun condizionamento di immagine latente e maschera; i condizionamenti positivo e negativo vengono passati invariati (tranne il fatto che `clip_vision_output` viene comunque aggiunto se fornito) e il nodo restituisce un latente vuoto.

**Nota:** Quando viene fornito `start_image`, la sequenza di immagini viene ridimensionata alla `width` e `height` di destinazione e troncata ai primi `length` fotogrammi. Se la sequenza è più corta di `length`, i fotogrammi rimanenti vengono riempiti con fotogrammi grigio neutro (valore 0.5) prima della codifica VAE. Il condizionamento risultante include un `concat_mask` con valore 0 nelle posizioni temporali corrispondenti ai fotogrammi dell'immagine iniziale e 1 altrove.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `positive` | Il condizionamento positivo modificato, che può contenere `concat_latent_image`, `concat_mask` e `clip_vision_output`. | CONDITIONING |
| `negative` | Il condizionamento negativo modificato, che può contenere `concat_latent_image`, `concat_mask` e `clip_vision_output`. | CONDITIONING |
| `latent` | Un tensore latente vuoto con forma `[batch_size, 16, ((length - 1) // 4) + 1, height // 8, width // 8]`, determinato dagli input `batch_size`, `length`, `height` e `width`. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTrackToVideo/it.md)

---
**Source fingerprint (SHA-256):** `b02a1a359d349a0136d84ed77a510c46cb2c8b565650ed54d5fca6c87cd0ab1f`
