# WanTrackToVideo

Il nodo WanTrackToVideo converte i dati di tracciamento del movimento in sequenze video elaborando i punti traccia e generando i fotogrammi video corrispondenti. Riceve in input le coordinate di tracciamento e produce conditioning video e rappresentazioni latenti che possono essere utilizzati per la generazione video. Quando non vengono fornite tracce, passa alla conversione standard da immagine a video.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `positive` | Conditioning positivo per la generazione video | CONDITIONING | Sì | - |
| `negative` | Conditioning negativo per la generazione video | CONDITIONING | Sì | - |
| `vae` | Modello VAE per codifica e decodifica | VAE | Sì | - |
| `tracks` | Dati di tracciamento in formato JSON come stringa multilinea (predefinito: "[]"). Ogni traccia viene estesa con padding o troncata a una lunghezza fissa di 121 punti. | STRING | Sì | - |
| `width` | Larghezza del video di output in pixel (predefinito: 832, passo: 16) | INT | Sì | 16 a MAX_RESOLUTION |
| `height` | Altezza del video di output in pixel (predefinito: 480, passo: 16) | INT | Sì | 16 a MAX_RESOLUTION |
| `length` | Numero di fotogrammi nel video di output (predefinito: 81, passo: 4) | INT | Sì | 1 a MAX_RESOLUTION |
| `batch_size` | Numero di video da generare simultaneamente (predefinito: 1) | INT | Sì | 1 a 4096 |
| `temperature` | Parametro di temperatura per il motion patching (predefinito: 220.0, passo: 0.1). Impostazione avanzata. | FLOAT | Sì | 1.0 a 1000.0 |
| `topk` | Valore top-k per il motion patching (predefinito: 2). Impostazione avanzata. | INT | Sì | 1 a 10 |
| `start_image` | Immagine iniziale per la generazione video | IMAGE | No | - |
| `clip_vision_output` | Output di visione CLIP per conditioning aggiuntivo | CLIP_VISION_OUTPUT | No | - |

**Nota:** Quando `tracks` contiene dati di tracciamento validi, il nodo elabora le tracce di movimento per generare il video. Quando `tracks` è vuoto, passa alla modalità standard da immagine a video. Se viene fornito `start_image`, inizializza il primo fotogramma della sequenza video e il risultato del motion patching viene aggiunto sia al conditioning positivo sia a quello negativo. Se viene fornito `clip_vision_output`, viene aggiunto anch'esso sia al conditioning positivo sia a quello negativo.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `positive` | Conditioning positivo con informazioni sulle tracce di movimento applicate | CONDITIONING |
| `negative` | Conditioning negativo con informazioni sulle tracce di movimento applicate | CONDITIONING |
| `latent` | Rappresentazione latente del video generato | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTrackToVideo/it.md)

---
**Source fingerprint (SHA-256):** `e67fe326dd7e5ae63ddc35946d8144138d04d9523ec1ad2e08ea6bc1dc9325da`
