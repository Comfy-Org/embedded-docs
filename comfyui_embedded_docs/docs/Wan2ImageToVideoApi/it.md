# Wan2ImageToVideoApi

Il nodo Wan 2.7 Image to Video genera un video partendo da un'immagine del primo frame. Puoi facoltativamente fornire un'immagine dell'ultimo frame per creare una transizione tra le due, oppure fornire un file audio per guidare il movimento e la temporizzazione del video. Il nodo usa un modello AI per animare la scena in base alla tua descrizione testuale.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello AI da usare per la generazione del video. | DYNAMIC_COMBO | Sì | `"wan2.7-i2v"` |
| `first_frame` | Immagine del primo frame. Il rapporto d'aspetto dell'output viene derivato da questa immagine. | IMAGE | Sì | - |
| `last_frame` | Immagine dell'ultimo frame. Il modello genera un video con transizione dal primo all'ultimo frame. | IMAGE | No | - |
| `audio` | Audio per guidare la generazione del video (ad es. sincronizzazione labiale, movimento sincronizzato al ritmo). Durata: 2s-30s. Se non fornito, il modello genera automaticamente musica di sottofondo o effetti sonori corrispondenti. | AUDIO | No | - |
| `seed` | Seed da usare per la generazione (predefinito: 0). | INT | Sì | 0 a 2147483647 |
| `prompt_extend` | Se migliorare il prompt con l'assistenza AI (predefinito: True). Questa è un'impostazione avanzata. | BOOLEAN | Sì | True<br>False |
| `watermark` | Se aggiungere una filigrana generata dall'IA al risultato (predefinito: False). Questa è un'impostazione avanzata. | BOOLEAN | Sì | True<br>False |

### Input di wan2.7-i2v

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt che descrive gli elementi e le caratteristiche visive. Supporta l'inglese e il cinese. (predefinito: vuoto) | STRING | Sì | - |
| `negative_prompt` | Prompt negativo che descrive cosa evitare. (predefinito: vuoto) | STRING | Sì | - |
| `resolution` | La risoluzione del video di output. | COMBO | Sì | `"720P"`<br>`"1080P"` |
| `duration` | La durata del video generato in secondi (predefinito: 5). | INT | Sì | 2 a 15 |

**Nota:** L'input `audio` ha un vincolo di durata. Se fornito, il file audio deve durare tra 2 e 30 secondi.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `output` | Il file video generato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ImageToVideoApi/it.md)

---
**Source fingerprint (SHA-256):** `81b0dc9500ff00e1428422d3d9c8df8f790c1d9dec547dcba0d1aa239f8a8beb`
