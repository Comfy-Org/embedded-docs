# KlingStartEndFrameNode

Questo nodo crea una sequenza video che esegue la transizione tra le immagini iniziale e finale fornite. Genera tutti i frame intermedi per produrre una trasformazione fluida dal primo frame all’ultimo. Questo nodo chiama l’API image-to-video ma supporta solo le opzioni di input compatibili con il campo della richiesta `image_tail`.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `start_frame` | Immagine di riferimento - URL o stringa codificata Base64, non può superare 10 MB, risoluzione non inferiore a 300×300 px, rapporto d’aspetto compreso tra 1:2.5 e 2.5:1. Base64 non deve includere il prefisso data:image. | IMAGE | Sì | - |
| `end_frame` | Immagine di riferimento - Controllo del frame finale. URL o stringa codificata Base64, non può superare 10 MB, risoluzione non inferiore a 300×300 px. Base64 non deve includere il prefisso data:image. | IMAGE | Sì | - |
| `prompt` | Prompt testuale positivo. Non deve essere vuoto e non può superare 500 caratteri. | STRING | Sì | - |
| `negative_prompt` | Prompt testuale negativo. Non può superare 500 caratteri. Se lasciato vuoto, viene omesso dalla richiesta. | STRING | Sì | - |
| `cfg_scale` | Controlla la forza della guida del prompt (predefinito: 0.5). | FLOAT | Sì | 0.0-1.0 |
| `aspect_ratio` | Il rapporto d’aspetto per il video generato (predefinito: "16:9"). | COMBO | Sì | "16:9"<br>"9:16"<br>"1:1" |
| `mode` | La configurazione da utilizzare per la generazione video, secondo il formato: mode / duration / model_name. (predefinito: "pro mode / 5s duration / kling-v2-5-turbo") | COMBO | Sì | "pro mode / 5s duration / kling-v2-5-turbo"<br>"pro mode / 10s duration / kling-v2-5-turbo" |

**Vincoli sulle immagini:**

- Sia `start_frame` che `end_frame` sono obbligatori e non possono superare 10 MB di dimensione file.
- Risoluzione minima: 300×300 pixel per entrambe le immagini.
- Il rapporto d’aspetto di `start_frame` deve essere compreso tra 1:2.5 e 2.5:1.
- Le immagini codificate in Base64 non devono includere il prefisso "data:image".

**Vincoli sul prompt:**

- `prompt` non deve essere vuoto e non può superare 500 caratteri.
- `negative_prompt` non può superare 500 caratteri; se vuoto, non viene inviato con la richiesta.

**Note sulla modalità:**

- Entrambe le opzioni di `mode` utilizzano la modalità pro con il modello kling-v2-5-turbo e differiscono solo per la durata (5 secondi o 10 secondi).
- Prezzo per generazione, come mostrato nel badge del prezzo del nodo: la modalità 5s costa $0.35 USD e la modalità 10s costa $0.70 USD.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `output` | La sequenza video generata. | VIDEO |
| `video_id` | Identificatore univoco per il video generato. | STRING |
| `duration` | Durata del video generato. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingStartEndFrameNode/it.md)

---
**Source fingerprint (SHA-256):** `a27977226360a425614255f8330ce7fd8ba94b8c3020eb8fdddc01eb74f035c1`
