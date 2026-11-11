# ByteDance Seedance 2.5 Draft in Video finale

Questo nodo esegue il rendering del video finale di una bozza Seedance 2.5 a 1080p oppure a 4k. Una bozza è un'anteprima rapida a 480p: in un nodo video Seedance 2.5 (da testo a video, da primo-ultimo frame a video o da riferimento a video), imposta `model` su `Seedance 2.5 Draft`, eseguilo e collega qui il suo output `draft_task_id`. Il video finale mantiene la scena e il movimento della bozza e riutilizza il prompt, i riferimenti, la durata, le proporzioni e l'impostazione audio che hanno prodotto la bozza.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `draft_task_id` | L'output `draft_task_id` di un nodo Seedance 2.5 eseguito con il modello Seedance 2.5 Draft, oppure un ID attività della bozza incollato. Quando riesegui il nodo produttore, imposta il controllo del seed su fisso; altrimenti l'esecuzione successiva genera una nuova bozza invece di riutilizzare quella che hai esaminato. | STRING | Sì | - |
| `filigrana` | Indica se aggiungere una filigrana al video. Il valore predefinito è False. Questa è un'impostazione avanzata. | BOOLEAN | No | True / False |
| `resolution` | Risoluzione del video finale. Predefinito: `"1080p"`. | COMBO | No | `"1080p"`<br>`"4k"` |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `video` | Il video finale renderizzato, scaricato dal provider al completamento dell'attività di rendering. | VIDEO |

**Nota:** una bozza può essere renderizzata per 7 giorni dalla sua creazione. L'ID attività della bozza identifica la bozza di per sé, quindi non è necessario passare di nuovo prompt, riferimenti, durata, proporzioni e impostazione audio.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2DraftToFinalVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `757f1330775554d654012daa83880c3a2fbcee5b0a9efe0a2d2650f940962be6`
