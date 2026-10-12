# HitPawVideoEnhance

Il nodo HitPaw Video Enhance utilizza un'API esterna per migliorare la qualità dei video. Aumenta la risoluzione dei video a bassa risoluzione, rimuove artefatti visivi e riduce il rumore. Il costo di elaborazione viene calcolato per ogni secondo del video di input.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello AI da utilizzare per il miglioramento del video. Selezionando un modello viene visualizzato un parametro `resolution` annidato. I modelli disponibili e le relative risoluzioni supportate variano. | DYNAMIC_COMBO | Sì | `"Portrait Restore Model (1x)"`<br>`"Portrait Restore Model (2x)"`<br>`"General Restore Model (1x)"`<br>`"General Restore Model (2x)"`<br>`"General Restore Model (4x)"`<br>`"Ultra HD Model (2x)"`<br>`"Generative Model (1x)"` |
| `video` | Il file video di input da migliorare. | VIDEO | Sì | N/A |

### Input di Portrait Restore, General Restore e Ultra HD Model

Queste opzioni di risoluzione sono condivise da Portrait Restore Model (1x), Portrait Restore Model (2x), General Restore Model (1x), General Restore Model (2x), General Restore Model (4x) e Ultra HD Model (2x).

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model.resolution` | La risoluzione di destinazione per il video migliorato. Selezionando `"original"` viene mantenuta la risoluzione del video di input. | COMBO | Sì | `"original"`<br>`"720p"`<br>`"1080p"`<br>`"2K/QHD"`<br>`"4K/UHD"`<br>`"8K"` |

### Input di Generative Model (1x)

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model.resolution` | La risoluzione di destinazione per il video migliorato. Selezionando `"original"` viene mantenuta la risoluzione del video di input. L'opzione `"8K"` non è disponibile per questo modello. | COMBO | Sì | `"original"`<br>`"720p"`<br>`"1080p"`<br>`"2K/QHD"`<br>`"4K/UHD"` |

**Note:**

* Il `video` di input deve avere una durata compresa tra 0,5 secondi e 60 minuti (3600 secondi).
* La `resolution` selezionata deve essere almeno pari alle dimensioni del video di input. Per i video quadrati, deve essere almeno pari alla larghezza e all'altezza del video. Per i video non quadrati, deve essere almeno pari alla dimensione più corta del video. Se la risoluzione di destinazione è inferiore, viene generato un errore. Selezionando `"original"` viene mantenuta la risoluzione del video di input.
* Quando viene selezionata una risoluzione diversa da `"original"`, i video non quadrati vengono ridimensionati in modo che la loro dimensione più corta corrisponda alla risoluzione selezionata, preservando le proporzioni. I video quadrati vengono ridimensionati in modo che entrambe le dimensioni corrispondano alla dimensione target quadrata della risoluzione selezionata (ad esempio, `"4K/UHD"` produce 2048×2048).

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `video` | Il file video migliorato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HitPawVideoEnhance/it.md)

---
**Source fingerprint (SHA-256):** `42803c7137d62dbce5021cd2bd9b9fba1a89c80e7b3f237f8a0eb03858c49967`
