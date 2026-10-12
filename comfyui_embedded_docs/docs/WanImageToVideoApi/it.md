# Wan Image to Video

Il nodo Wan Image to Video genera un video a partire da una singola immagine di input e da un prompt testuale. Utilizza l'immagine fornita come primo fotogramma e crea una sequenza video basata sulla descrizione, con opzioni per risoluzione, durata, audio e altre impostazioni avanzate.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Modello da utilizzare (predefinito: "wan2.6-i2v") | COMBO | Sì | "wan2.5-i2v-preview"<br>"wan2.6-i2v" |
| `image` | Immagine di input che funge da primo fotogramma per la generazione del video. È richiesta una sola immagine. | IMAGE | Sì | - |
| `prompt` | Prompt che descrive gli elementi e le caratteristiche visive. Supporta l'inglese e il cinese (predefinito: vuoto). | STRING | Sì | - |
| `negative_prompt` | Prompt negativo che descrive cosa evitare (predefinito: vuoto). | STRING | No | - |
| `resolution` | Qualità della risoluzione video (predefinito: "720P"). Il modello Wan 2.6 non supporta 480P. | COMBO | No | "480P"<br>"720P"<br>"1080P" |
| `duration` | Durata del video generato in secondi. Una durata di 15 secondi è supportata solo dal modello Wan 2.6 (predefinito: 5). | INT | No | 5-15 (passo: 5) |
| `audio` | L'audio deve contenere una voce chiara e forte, senza rumori estranei o musica di sottofondo. Se fornito, la durata dell'audio deve essere compresa tra 3,0 e 29,0 secondi. | AUDIO | No | - |
| `seed` | Seed da utilizzare per la generazione (predefinito: 0). | INT | No | 0-2147483647 |
| `generate_audio` | Se non viene fornito alcun input audio, genera automaticamente l'audio (predefinito: False). | BOOLEAN | No | - |
| `prompt_extend` | Indica se migliorare il prompt con l'assistenza dell'IA (predefinito: True). | BOOLEAN | No | - |
| `watermark` | Indica se aggiungere una filigrana generata dall'IA al risultato (predefinito: False). | BOOLEAN | No | - |
| `shot_type` | Specifica il tipo di inquadratura per il video generato, ovvero se il video è un'unica ripresa continua o più riprese con tagli. Questo parametro ha effetto solo quando prompt_extend è True (predefinito: "single"). | COMBO | No | "single"<br>"multi" |

**Vincoli:**

- Per la generazione del video è richiesta una sola immagine di input.
- Il modello Wan 2.6 (`wan2.6-i2v`) non supporta la risoluzione 480P.
- Una durata di 15 secondi è supportata solo dal modello Wan 2.6 (`wan2.6-i2v`).
- Quando viene fornito un audio, la sua durata deve essere compresa tra 3,0 e 29,0 secondi.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `output` | Video generato in base all'immagine di input e al prompt. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideoApi/it.md)

---
**Source fingerprint (SHA-256):** `dabcbfa3118669d9ff5b40b79ef643ffcf7ac5e510e61d6ad859d80360061673`
