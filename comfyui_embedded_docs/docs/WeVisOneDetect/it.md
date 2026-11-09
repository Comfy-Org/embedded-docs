# WeVisOne-VL Detect

WeVisOne-VL Detect individua gli oggetti in un'immagine a partire da un prompt testuale e restituisce box, alpha matte, punti o la risposta del modello stesso, a seconda dell'attività scelta. Copre il rilevamento e la segmentazione a vocabolario aperto, le espressioni referenziali, il pointing, il conteggio e l'OCR grounding, ed esegue un prompt per ogni immagine del batch.

## Ingressi

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `clip` | L'encoder di testo WeVisOne-VL che carica il checkpoint. | CLIP | Sì | - |
| `image` | L'immagine o il batch di immagini in cui cercare. | IMAGE | Sì | - |
| `task` | Cosa deve restituire il nodo. La segmentazione restituisce box più alpha matte; detection, referring, ocr e ocr_grounding restituiscono box; point e count_point restituiscono punti; count_box esegue il conteggio con i box; visual_prompt trova oggetti simili ai box di riferimento in `bboxes`; freeform invia la query invariata e restituisce solo testo (predefinito: "segmentation"). | COMBO | Sì | `"segmentation"`<br>`"detection"`<br>`"referring"`<br>`"point"`<br>`"count_box"`<br>`"count_point"`<br>`"ocr"`<br>`"ocr_grounding"`<br>`"visual_prompt"`<br>`"freeform"` |
| `query` | Cosa trovare, in linguaggio naturale (ad esempio "la tazza rossa"). `detection` e `point` leggono un'etichetta per riga, `count_box` e `count_point` contano il soggetto indicato, `ocr_grounding` cerca questo testo esatto, `visual_prompt` usa invece `bboxes`, e `freeform` lo invia come prompt completo. `ocr` lo ignora. | STRING | Sì | - |
| `bboxes` | Box di riferimento che `visual_prompt` usa come esempi dell'oggetto da trovare. | BOUNDING_BOX | No | - |
| `individual_masks` | Restituisce una matte per box, nell'ordine di `bboxes` e fotogramma per fotogramma, invece di una matte combinata per fotogramma (predefinito: false). | BOOLEAN | No | true<br>false |
| `max_length` | Numero massimo di token che il modello può generare per la sua risposta (predefinito: 4096). | INT | Sì | 1 a 32768 |

**Nota:** Le matte vengono riempite solo quando il modello risponde con riferimenti agli oggetti, che è ciò che richiedono le attività di segmentazione e visual prompt. Le altre attività restituiscono box, punti o testo con una matte vuota.

## Uscite

| Nome dell'output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `masks` | Alpha matte degli oggetti corrispondenti, una per fotogramma per impostazione predefinita oppure una per box con `individual_masks`. | MASK |
| `bboxes` | Box trovati in ciascuna immagine, memorizzati come `x`, `y`, `width`, `height` e `label`. | BOUNDING_BOX |
| `points` | Punti come JSON in pixel, con forma `[{"x", "y", "label", "frame"}]`, riempiti dalle attività `point` e `count_point`. | STRING |
| `text` | La risposta grezza del modello, una riga per immagine. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WeVisOneDetect/it.md)

---
**Source fingerprint (SHA-256):** `0cef1dfcab790e145ace51401a84cdc10282835330cda5a3770f5b20a32d475e`
