# HunyuanVideo15ImageToVideo

Il nodo HunyuanVideo15ImageToVideo prepara i dati di condizionamento e dello spazio latente per la generazione video basata sul modello HunyuanVideo 1.5. Crea una rappresentazione latente iniziale per una sequenza video e può opzionalmente integrare un'immagine iniziale o un output di visione CLIP per guidare il processo di generazione.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `positive` | I prompt di condizionamento positivi che descrivono ciò che il video dovrebbe contenere. | CONDITIONING | Sì | - |
| `negative` | I prompt di condizionamento negativi che descrivono ciò che il video dovrebbe evitare. | CONDITIONING | Sì | - |
| `vae` | Il modello VAE (Autoencoder Variazionale) utilizzato per codificare l'immagine iniziale nello spazio latente. | VAE | Sì | - |
| `width` | La larghezza dei fotogrammi del video di output in pixel. Deve essere divisibile per 16. (predefinito: 848) | INT | Sì | 16 to MAX_RESOLUTION, step: 16 |
| `height` | L'altezza dei fotogrammi del video di output in pixel. Deve essere divisibile per 16. (predefinito: 480) | INT | Sì | 16 to MAX_RESOLUTION, step: 16 |
| `length` | Il numero totale di fotogrammi nella sequenza video. I valori aumentano a passi di 4 partendo da 1 (1, 5, 9, 13, ...). (predefinito: 33) | INT | Sì | 1 to MAX_RESOLUTION, step: 4 |
| `batch_size` | Il numero di sequenze video da generare in un singolo batch. (predefinito: 1) | INT | Sì | 1 to 4096 |
| `start_image` | Un'immagine iniziale opzionale per inizializzare la generazione del video. Se fornita, viene codificata e usata per condizionare i primi fotogrammi. Vengono usati solo i primi `length` fotogrammi dell'immagine. | IMAGE | No | - |
| `clip_vision_output` | Embedding di visione CLIP opzionali per fornire un condizionamento visivo aggiuntivo alla generazione. | CLIP_VISION_OUTPUT | No | - |

**Nota:** Quando viene fornita una `start_image`, viene automaticamente ridimensionata per corrispondere a `width` e `height` specificati usando l'interpolazione bilineare. Vengono usati i primi `length` fotogrammi del batch di immagini, e vengono codificati solo i primi 3 canali di colore di ciascun fotogramma. L'immagine codificata viene quindi aggiunta sia al condizionamento `positive` sia a quello `negative` come `concat_latent_image` con una corrispondente `concat_mask`. La maschera è impostata a 0.0 per i fotogrammi coperti dall'immagine iniziale e a 1.0 per i fotogrammi rimanenti. Quando viene fornito un `clip_vision_output`, viene anch'esso aggiunto sia al condizionamento `positive` sia a quello `negative`.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `positive` | Il condizionamento positivo modificato, che ora può includere l'immagine iniziale codificata o l'output di visione CLIP. | CONDITIONING |
| `negative` | Il condizionamento negativo modificato, che ora può includere l'immagine iniziale codificata o l'output di visione CLIP. | CONDITIONING |
| `latent` | Un tensore latente vuoto con dimensioni configurate per la dimensione del batch, la lunghezza del video, la larghezza e l'altezza specificate. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15ImageToVideo/it.md)

---
**Source fingerprint (SHA-256):** `dbedf7f378ae9613c8f47fe9876a4576c815055b4cdb6bf687b7575fcd7ea80a`
