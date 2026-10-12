# ByteDance Seedance 2.5 Draft in Video finale

Questo nodo esegue il rendering del video finale a 1080p di una bozza Seedance 2.5. Una bozza è un'anteprima veloce a 480p: in un nodo video Seedance 2.5 (text to video, first-last-frame to video o reference to video), imposta `model` su `Seedance 2.5 Draft`, eseguilo e collega qui il suo output `draft_task_id`. Il risultato finale mantiene la scena e il movimento della bozza e riutilizza il prompt, i riferimenti, la durata, le proporzioni e l'impostazione audio che hanno prodotto la bozza.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `draft_task_id` | L'output `draft_task_id` di un nodo Seedance 2.5 eseguito con il modello Seedance 2.5 Draft, oppure un ID attività di bozza incollato. Quando riesegui il nodo produttore, imposta il suo controllo del seed su fixed; in caso contrario, l'esecuzione successiva genera una nuova bozza invece di riutilizzare quella revisionata. | STRING | Sì | - |
| `watermark` | Indica se aggiungere una filigrana al video. Il valore predefinito è False. Questa è un'impostazione avanzata. | BOOLEAN | No | True / False |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `video` | Il video finale a 1080p renderizzato, scaricato dal provider una volta completata l'attività di rendering. | VIDEO |

**Nota:** Una bozza può essere renderizzata per 7 giorni dopo la sua creazione. L'ID attività della bozza identifica la bozza da solo, quindi non è necessario passare di nuovo il prompt, i riferimenti, la durata, le proporzioni e l'impostazione audio.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2DraftToFinalVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `c9a607826915f09ec199748964010a00a239b5efab3647a3b97fdceee6b04cde`
