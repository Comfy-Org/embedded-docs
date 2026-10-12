# Wan 2.7 Da Testo a Video

Questo nodo genera un video da una descrizione testuale utilizzando il modello Wan 2.7. Invia il tuo prompt all'API di generazione video Wan, attende il completamento dell'attività e restituisce il video risultante. Puoi facoltativamente collegare una clip audio per influenzare il movimento e la temporizzazione del video; se non viene fornito alcun audio, il modello genera automaticamente un audio corrispondente.

## Input

### Input comuni

Questi input sono sempre disponibili al livello superiore del nodo.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello specifico da utilizzare per la generazione video. | DYNAMIC_COMBO | Sì | `"wan2.7-t2v"` |
| `audio` | Audio per guidare la generazione video (ad es. sincronizzazione labiale, movimento a tempo). Durata: 3s-30s. Se non fornito, il modello genera automaticamente musica di sottofondo o effetti sonori corrispondenti. | AUDIO | No | - |
| `seed` | Seme da utilizzare per la generazione (predefinito: 0). | INT | Sì | 0 to 2147483647 |
| `prompt_extend` | Indica se migliorare il prompt con l'assistenza AI (predefinito: True). | BOOLEAN | Sì | True<br>False |
| `watermark` | Indica se aggiungere una filigrana generata dall'AI al risultato (predefinito: False). | BOOLEAN | Sì | True<br>False |

### Input di wan2.7-t2v

Queste impostazioni compaiono quando è selezionato il modello `wan2.7-t2v`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt che descrive gli elementi e le caratteristiche visive. Supporta inglese e cinese. | STRING | Sì | - |
| `negative_prompt` | Prompt negativo che descrive cosa evitare. Il valore predefinito è una stringa vuota. | STRING | No | - |
| `resolution` | La risoluzione del video di output (predefinito: "720P"). | COMBO | Sì | `"720P"`<br>`"1080P"` |
| `ratio` | Le proporzioni del video di output. | COMBO | Sì | `"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | La durata del video in secondi (predefinito: 5). | INT | Sì | 2 to 15 |

**Nota:** L'input `prompt` non deve essere vuoto. L'input `audio` è facoltativo; se fornito, il nodo accetta audio tra 1,5 e 60 secondi, anche se il tooltip consiglia 3s-30s. Se non viene fornito alcun audio, il modello genera automaticamente un audio corrispondente. Quando `negative_prompt` viene lasciato vuoto, non viene inviato all'API. `prompt_extend` e `watermark` sono opzioni avanzate.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `output` | Il file video generato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2TextToVideoApi/it.md)

---
**Source fingerprint (SHA-256):** `2b35fb3e897f8c5fb9786576f4e314cb6709527a3cdc4f2eb9f0600d09076835`
