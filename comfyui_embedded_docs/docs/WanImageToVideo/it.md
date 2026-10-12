# WanImageToVideo

Il nodo WanImageToVideo prepara le rappresentazioni di condizionamento e latenti per la generazione video. Crea uno spazio latente vuoto per il video e può opzionalmente incorporare un'immagine iniziale e l'output di CLIP vision per guidare la generazione. Sia gli input di condizionamento positivo sia quello negativo vengono aggiornati con l'immagine e i dati di visione forniti.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `positive` | Input di condizionamento positivo usato per guidare la generazione | CONDITIONING | Sì | - |
| `negative` | Input di condizionamento negativo usato per guidare la generazione | CONDITIONING | Sì | - |
| `vae` | Modello VAE usato per codificare le immagini nello spazio latente | VAE | Sì | - |
| `width` | Larghezza del video generato (predefinito: 832, passo: 16) | INT | Sì | da 16 a MAX_RESOLUTION |
| `height` | Altezza del video generato (predefinito: 480, passo: 16) | INT | Sì | da 16 a MAX_RESOLUTION |
| `length` | Numero di frame nel video (predefinito: 81, passo: 4) | INT | Sì | da 1 a MAX_RESOLUTION |
| `batch_size` | Numero di video da generare in un batch (predefinito: 1) | INT | Sì | da 1 a 4096 |
| `clip_vision_output` | Output opzionale di CLIP vision aggiunto come condizionamento extra sia all'input positivo sia a quello negativo | CLIP_VISION_OUTPUT | No | - |
| `start_image` | Immagine iniziale opzionale usata per inizializzare il video. Quando fornita, viene ridimensionata alla `width` e alla `height` specificate e posizionata all'inizio della sequenza di frame; eventuali frame oltre `length` vengono ignorati. I frame rimanenti vengono riempiti con valori di grigio neutro (0,5) a meno che non venga fornita `ref_pad_image`. | IMAGE | No | - |
| `ref_pad_image` | Immagine di riferimento opzionale il cui primo frame sostituisce il riempimento grigio neutro della sequenza di frame. Viene ridimensionata alla `width` e alla `height` specificate, e viene usata solo la prima immagine del batch. Ha effetto solo quando è fornita anche `start_image`. | IMAGE | No | - |

**Nota:** Quando viene fornita `start_image`, la sequenza di frame viene codificata con il VAE e viene applicata una maschera al condizionamento. La maschera è impostata a 0 per i frame coperti dall'immagine iniziale e a 1 per i frame rimanenti, così la generazione continua dall'immagine fornita. Durante la codifica vengono usati solo i primi tre canali di colore (RGB) dell'immagine. Sia il condizionamento positivo sia quello negativo ricevono la stessa immagine latente concatenata, la maschera e (se fornito) l'output di CLIP vision. Quando `ref_pad_image` viene fornita insieme a `start_image`, il suo primo frame viene ridimensionato a `width` e `height` e scritto nei canali RGB dei frame di riempimento prima che l'immagine iniziale venga posizionata sopra, così il riempimento trasporta l'immagine di riferimento invece del grigio uniforme. Questo è un riempimento anti-drift in stile SVI, usato da modelli come ID-V2V.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `positive` | Condizionamento positivo, aggiornato con l'immagine e i dati di visione | CONDITIONING |
| `negative` | Condizionamento negativo, aggiornato con l'immagine e i dati di visione | CONDITIONING |
| `latent` | Tensore latente vuoto pronto per la generazione video, con forma [batch_size, 16, ((length-1)//4)+1, height//8, width//8] | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideo/it.md)

---
**Source fingerprint (SHA-256):** `3000c1c816d2c123fc5bc46ea1f193c52c0f81a2f8c4a9110d8a4fa909185aea`
