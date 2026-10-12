# QwenImageEditApi

Questo nodo utilizza i modelli Qwen-Image 3.0 per modificare o combinare fino a 3 immagini di riferimento guidate da un prompt testuale. Selezioni un modello, fornisci il prompt e le immagini di riferimento, e il nodo restituisce una o più immagini generate.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Modello da utilizzare. Questa selezione include anche il prompt testuale, fino a 3 input di immagini di riferimento e un prompt negativo opzionale. | DYNAMIC_COMBO | Sì | "qwen-image-3.0-pro"<br>"qwen-image-3.0" |
| `size` | Risoluzione di output. "match input" riutilizza le dimensioni della prima immagine di riferimento, "auto" lascia che il modello scelga una dimensione con lo stesso rapporto d'aspetto, "custom" imposta una larghezza e un'altezza esplicite. | DYNAMIC_COMBO | Sì | "match input"<br>"auto"<br>"custom" |
| `n` | Numero di immagini da generare, restituite come batch. (predefinito: 1) | INT | No | da 1 a 6 |
| `seed` | Seed da utilizzare per la generazione. (predefinito: 42) | INT | No | da 0 a 2147483647 |
| `prompt_extend` | Se migliorare il prompt con l'assistenza AI. (predefinito: True) | BOOLEAN | No | True<br>False |
| `watermark` | Se aggiungere una filigrana generata dall'AI al risultato. (predefinito: False) | BOOLEAN | No | True<br>False |

### Input di qwen-image-3.0-pro e qwen-image-3.0

Entrambi i modelli condividono gli stessi sotto-parametri.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Istruzioni di modifica. Supporta inglese e cinese e riferimenti in stile @Image1 alle immagini di input. (predefinito: "") | STRING | Sì | - |
| `negative_prompt` | Prompt negativo che descrive cosa evitare. (predefinito: "") | STRING | No | - |

### Input di riferimento

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `images` | Slot espandibile: collega da 1 a 3 immagini di riferimento (`image_1`, `image_2`, `image_3`). Fai riferimento a esse nel prompt come @Image1, @Image2, @Image3, numerate in ordine di input; un input in batch conta una volta per immagine. | IMAGE | Sì | da 1 a 3 |

### Input dimensioni personalizzate

Mostrati quando `size` è impostato su "custom".

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `width` | Larghezza di output. L'area totale in pixel deve essere compresa tra 512x512 e 2560x2560; qualsiasi rapporto d'aspetto all'interno di tale area è valido. (predefinito: 1024) | INT | Sì (quando `size` è "custom") | da 256 a 2560, passo 16 |
| `height` | Altezza di output. L'area totale in pixel deve essere compresa tra 512x512 e 2560x2560; qualsiasi rapporto d'aspetto all'interno di tale area è valido. (predefinito: 1024) | INT | Sì (quando `size` è "custom") | da 256 a 2560, passo 16 |

### Vincoli

- Il prompt testuale è obbligatorio e deve contenere almeno un carattere.
- È supportato un massimo di 3 immagini di riferimento; viene generato un errore se ne vengono fornite di più (un input in batch conta una volta per immagine).
- Quando `size` è impostato su "custom", è necessario fornire valori espliciti di larghezza e altezza che vengono convalidati: l'area totale in pixel deve essere compresa tra 262.144 (512x512) e 6.553.600 (2560x2560) pixel, e il rapporto d'aspetto deve essere compreso tra 1:8 e 8:1.
- Quando `size` è impostato su "match input", è richiesta almeno un'immagine di riferimento perché vengono utilizzate le dimensioni della prima immagine di riferimento; le dimensioni vengono ridimensionate per rientrare nell'area e nell'intervallo di rapporto d'aspetto supportati.
- Quando `size` è impostato su "auto", il modello sceglie la dimensione di output (1,9-4,2 megapixel) preservando il rapporto d'aspetto dell'input.
- I riferimenti nel prompt utilizzano @Image1, @Image2, @Image3, numerati in ordine di input; un riferimento a un indice superiore al numero di immagini collegate genera un errore. I tag vengono riconosciuti solo ai limiti di parola, quindi indirizzi come user@image1.com vengono lasciati invariati.
- Le immagini di riferimento in input vengono ridimensionate a un massimo di 2048x2048 pixel prima di essere inviate all'API. Se la codifica PNG supera il limite di dimensione dell'API, viene utilizzata invece una codifica JPEG.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `IMAGE` | L'immagine o le immagini generate restituite come batch. Vengono restituite fino a `n` immagini. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageEditApi/it.md)

---
**Source fingerprint (SHA-256):** `efa8d2b1a039a7b91789c0332b751a5f90ab8dad755ef0e25124d7d1c44d9abb`
