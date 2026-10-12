# Wan2ReferenceVideoApi

Questo nodo genera un video con una persona o un oggetto basandosi sui materiali di riferimento forniti. Utilizza il modello Wan 2.7 per creare video da un prompt testuale, supportando performance con singolo personaggio e interazioni multi-personaggio. È necessario fornire almeno un video o un'immagine di riferimento affinché la generazione funzioni.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello specifico da utilizzare per la generazione video. | DYNAMIC_COMBO | Sì | "wan2.7-r2v" |
| `seed` | Seme da utilizzare per la generazione, che aiuta a controllare la casualità dell'output (predefinito: 0). | INT | Sì | 0 a 2147483647 |
| `watermark` | Indica se aggiungere una filigrana generata dall'IA al risultato (predefinito: False). Questa è un'impostazione avanzata. | BOOLEAN | Sì | True<br>False |

### Input di wan2.7-r2v

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt che descrive il video. Utilizza identificatori come 'character1' e 'character2' per riferirti ai personaggi di riferimento. Deve contenere almeno un personaggio. | STRING | Sì | - |
| `negative_prompt` | Prompt negativo che descrive cosa evitare (predefinito: vuoto). | STRING | No | - |
| `resolution` | La risoluzione del video di output. | COMBO | Sì | "720P"<br>"1080P" |
| `ratio` | Le proporzioni del video di output. | COMBO | Sì | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |
| `duration` | La durata del video generato in secondi (predefinito: 5). | INT | Sì | 2 a 10 |

### Input di riferimento

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `reference_videos` | Slot espandibile: collega fino a 3 video di riferimento (slot da `video1` a `video3`). È richiesto almeno un video o un'immagine di riferimento in totale. | VIDEO | No | 0 a 3 elementi |
| `reference_images` | Slot espandibile: collega fino a 5 immagini di riferimento (slot da `image1` a `image5`). È richiesto almeno un video o un'immagine di riferimento in totale. | IMAGE | No | 0 a 5 elementi |

**Vincoli importanti:**

* È necessario fornire almeno un video o un'immagine di riferimento negli input `reference_videos` o `reference_images`. Altrimenti il nodo genera un errore.
* Il numero totale combinato di video e immagini di riferimento non può superare 5.
* L'input `prompt` deve contenere almeno un personaggio.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `output` | Il file video generato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ReferenceVideoApi/it.md)

---
**Source fingerprint (SHA-256):** `52ac550522bf3fe8f57444ce8586fe83be470b893ff8c01292743553cfbd623d`
