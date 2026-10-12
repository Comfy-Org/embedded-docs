# WanVaceToVideo

Il nodo WanVaceToVideo prepara i dati di condizionamento video per i modelli di generazione video controllati da VACE. Combina il condizionamento positivo e negativo con un video di controllo opzionale, maschere di controllo e un'immagine di riferimento, li codifica tramite un VAE e restituisce il condizionamento aggiornato, un tensore latente vuoto e un valore di taglio.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `positive` | Input di condizionamento positivo per guidare la generazione | CONDITIONING | Sì | - |
| `negative` | Input di condizionamento negativo per guidare la generazione | CONDITIONING | Sì | - |
| `vae` | Modello VAE utilizzato per codificare immagini e fotogrammi video | VAE | Sì | - |
| `width` | Larghezza del video di output in pixel (predefinito: 832, passo: 16) | INT | Sì | da 16 a MAX_RESOLUTION |
| `height` | Altezza del video di output in pixel (predefinito: 480, passo: 16) | INT | Sì | da 16 a MAX_RESOLUTION |
| `length` | Numero di fotogrammi nel video (predefinito: 81, passo: 4) | INT | Sì | da 1 a MAX_RESOLUTION |
| `batch_size` | Numero di video da generare simultaneamente (predefinito: 1) | INT | Sì | da 1 a 4096 |
| `strength` | Intensità del condizionamento per il controllo VACE (predefinito: 1.0, passo: 0.01). Questa non è un'intensità LoRA. I pesi LoRA vengono applicati tramite nodi LoRA separati. | FLOAT | Sì | da 0.0 a 1000.0 |
| `control_video` | Video di input opzionale utilizzato per il condizionamento di controllo. Se non fornito, viene creato automaticamente un video grigio neutro. | IMAGE | No | - |
| `control_masks` | Maschere opzionali che determinano quali parti del video di controllo sono attive. Se non fornite, viene utilizzata una maschera completamente bianca. | MASK | No | - |
| `reference_image` | Immagine di riferimento opzionale per un condizionamento aggiuntivo. Quando fornita, viene codificata e anteposta alla sequenza latente. Viene utilizzata solo la prima immagine. | IMAGE | No | - |

**Nota:** Quando viene fornito `control_video`, viene troncato a `length` fotogrammi e ingrandito alle dimensioni specificate di `width` e `height`; se contiene meno fotogrammi di `length`, i fotogrammi mancanti vengono riempiti con grigio neutro (valore 0.5). Quando non viene fornito, viene creato automaticamente un video grigio neutro di `length` fotogrammi. Le `control_masks` vengono ingrandite alle dimensioni specificate di `width` e `height`, troncate a `length` fotogrammi e riempite con valore 1.0 se più corte. La maschera separa il video di controllo in parti inattive e reattive, ciascuna codificata dal VAE e concatenata lungo la dimensione dei canali; la maschera viene anche sottocampionata alla risoluzione latente. Quando viene fornita `reference_image`, la sua prima immagine viene codificata dal VAE e anteposta alla sequenza latente, e `trim_latent` riporta il numero di fotogrammi latenti aggiunti. Il numero di fotogrammi latenti è calcolato come `((length - 1) // 4) + 1`, e le dimensioni spaziali latenti sono `height / 8` e `width / 8`.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `positive` | Condizionamento positivo con dati di controllo video (vace_frames, vace_mask, vace_strength) applicati | CONDITIONING |
| `negative` | Condizionamento negativo con dati di controllo video (vace_frames, vace_mask, vace_strength) applicati | CONDITIONING |
| `latent` | Tensore latente vuoto pronto per la generazione video con forma [batch_size, 16, latent_length, height/8, width/8] | LATENT |
| `trim_latent` | Numero di fotogrammi latenti da tagliare quando viene utilizzata un'immagine di riferimento; 0 se non viene fornita alcuna immagine di riferimento | INT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanVaceToVideo/it.md)

---
**Source fingerprint (SHA-256):** `2039b7509ce5b731e9e41d9cd2dad022d4c5004751f571a4cf88c1ba0cae405b`
