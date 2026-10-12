# Qwen Image 3 Da Testo a Immagine

Qwen Image 3 Text to Image genera una o più immagini da un prompt testuale utilizzando i modelli Qwen-Image 3.0. Si seleziona un modello e si fornisce un prompt; il nodo restituisce le immagini generate come batch.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Modello da utilizzare (predefinito: "qwen-image-3.0-pro"). Questo selettore composito fornisce anche il prompt, il prompt negativo, la larghezza e l'altezza dell'immagine. | DYNAMIC_COMBO | Sì | "qwen-image-3.0-pro"<br>"qwen-image-3.0" |
| `n` | Numero di immagini da generare, restituite come batch (predefinito: 1). | INT | No | 1 a 6 |
| `seed` | Seed da usare per la generazione (predefinito: 42). Può essere impostato per aggiornarsi automaticamente dopo ogni generazione. | INT | No | 0 a 2147483647 |
| `prompt_extend` | Indica se migliorare il prompt con l'assistenza dell'IA (predefinito: true). Opzione avanzata. | BOOLEAN | No | true<br>false |
| `watermark` | Indica se aggiungere una filigrana generata dall'IA al risultato (predefinito: false). Opzione avanzata. | BOOLEAN | No | true<br>false |

### Input di qwen-image-3.0-pro e qwen-image-3.0

Condivisi da qwen-image-3.0-pro e qwen-image-3.0.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt che descrive l'immagine. Supporta inglese e cinese. Deve contenere almeno 1 carattere. | STRING | Sì | Testo libero |
| `negative_prompt` | Prompt negativo che descrive ciò che si vuole evitare (predefinito: ""). | STRING | No | Testo libero |
| `width` | L'area totale in pixel deve essere compresa tra 512x512 e 2560x2560; qualsiasi rapporto d'aspetto all'interno di tale area è valido. (predefinito: 1024) | INT | No | 256 a 2560 (passo 16) |
| `height` | L'area totale in pixel deve essere compresa tra 512x512 e 2560x2560; qualsiasi rapporto d'aspetto all'interno di tale area è valido. (predefinito: 1024) | INT | No | 256 a 2560 (passo 16) |

Nota: l'input `model` è un selettore composito con i sottocampi `model` (ID modello), `prompt` (obbligatorio, deve contenere almeno 1 carattere), `negative_prompt` (opzionale), `width` e `height`. L'area in pixel combinata di `width` e `height` deve essere compresa tra 262.144 pixel (512x512) e 6.553.600 pixel (2560x2560), e il rapporto d'aspetto deve rimanere tra 1:8 e 8:1.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `image` | L'immagine o le immagini generate, restituite come batch. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageTextToImageApi/it.md)

---
**Source fingerprint (SHA-256):** `c58454d26360a78b795b28dd776fa8650ec0ec7b1e4a902e81b6561f292e0fa2`
