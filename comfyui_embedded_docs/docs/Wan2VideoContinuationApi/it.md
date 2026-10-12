# Wan 2.7 Continuazione Video

Il nodo Wan 2.7 Video Continuation genera un nuovo segmento video che continua dalla fine di una clip video di input. Utilizza il modello Wan 2.7 per sintetizzare la continuazione basandosi su un prompt testuale e può facoltativamente guidare il finale verso un fotogramma target specifico.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello di generazione video da utilizzare. L'opzione selezionata determina quali impostazioni aggiuntive appaiono di seguito. | DYNAMIC_COMBO | Sì | `"wan2.7-i2v"` |
| `first_clip` | Video di input da cui continuare. Durata: 2s-10s. Le proporzioni dell'output sono derivate da questo video. | VIDEO | Sì | 2s a 10s |
| `last_frame` | Immagine dell'ultimo fotogramma. La continuazione si avvicinerà progressivamente a questo fotogramma. | IMAGE | No | - |
| `seed` | Seed da utilizzare per la generazione. (predefinito: 0) | INT | Sì | 0 a 2147483647 |
| `prompt_extend` | Se migliorare il prompt con l'assistenza AI. (predefinito: True) | BOOLEAN | Sì | - |
| `watermark` | Se aggiungere una filigrana generata dall'AI al risultato. (predefinito: False) | BOOLEAN | Sì | - |

### Input di wan2.7-i2v

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt che descrive gli elementi e le caratteristiche visive. Supporta inglese e cinese. (predefinito: stringa vuota) | STRING | Sì | - |
| `negative_prompt` | Prompt negativo che descrive cosa evitare. (predefinito: stringa vuota) | STRING | Sì | - |
| `resolution` | La risoluzione di output per il video generato. | COMBO | Sì | `"720P"`<br>`"1080P"` |
| `duration` | Durata totale dell'output in secondi. Il modello genera la continuazione per riempire il tempo rimanente dopo la clip di input. (predefinito: 5) | INT | Sì | 2 a 15 |

**Nota:** Il video di input `first_clip` deve avere una durata compresa tra 2 e 10 secondi.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `output` | La continuazione video generata. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2VideoContinuationApi/it.md)

---
**Source fingerprint (SHA-256):** `591e551676969bc1fedb5f820f6866512c132bb98ee8ef1766d1e0b389e2dc11`
