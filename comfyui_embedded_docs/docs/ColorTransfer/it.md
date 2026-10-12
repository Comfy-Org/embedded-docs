# ColorTransfer

Il nodo ColorTransfer regola la palette di colori di un'immagine di destinazione per farla corrispondere ai colori di un'immagine di riferimento. Utilizza diversi algoritmi matematici per analizzare e trasferire le caratteristiche cromatiche, come luminosità, contrasto e distribuzione della tonalità, dal riferimento all'immagine di destinazione. Questo è utile per creare coerenza visiva tra più immagini o per applicare una specifica gradazione cromatica.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `image_target` | Immagine/i a cui applicare la trasformazione del colore. | IMAGE | Sì | - |
| `image_ref` | Immagine/i di riferimento a cui far corrispondere i colori. | IMAGE | Sì | - |
| `method` | L'algoritmo di trasferimento del colore da utilizzare. | COMBO | Sì | `"reinhard_lab"`<br>`"mkl_lab"`<br>`"histogram"` |
| `source_stats` | Determina come vengono calcolate le statistiche cromatiche dalle immagini di origine (destinazione). | DYNAMICCOMBO | Sì | `"per_frame"`<br>`"uniform"`<br>`"target_frame"` |
| `strength` | L'intensità dell'effetto di trasferimento del colore. Un valore di 1.0 applica la trasformazione completa, mentre 0.0 restituisce l'immagine originale. Valore predefinito: 1.0 | FLOAT | Sì | 0.0 to 10.0 |

**Dettagli dei parametri:**
*   **Opzioni di `source_stats`:**
    *   **`per_frame`**: Ogni fotogramma di un batch viene associato individualmente a `image_ref`.
    *   **`uniform`**: Le statistiche cromatiche vengono aggregate su tutti i fotogrammi di origine per creare un'unica base di riferimento, che viene poi associata a `image_ref`.
    *   **`target_frame`**: Utilizza un fotogramma scelto dal batch di destinazione come base per calcolare la trasformazione verso `image_ref`. Questa trasformazione viene quindi applicata uniformemente a tutti i fotogrammi, preservando le differenze cromatiche relative tra essi. Quando questa opzione è selezionata, diventa disponibile un parametro aggiuntivo `target_index`.
*   **`target_index`** (compare quando `source_stats` è `"target_frame"`): L'indice del fotogramma (a partire da 0) utilizzato come base di origine per calcolare la trasformazione. Valore predefinito: 0. Deve essere compreso tra 0 e 10000.

**Vincoli:**
*   Se `strength` è impostato a 0.0 oppure `image_ref` è `None`, il nodo restituisce l'`image_target` originale senza elaborazione.
*   Quando `source_stats` è impostato a `"target_frame"`, `target_index` deve essere un indice valido all'interno del batch di `image_target`. Se supera il numero di fotogrammi, viene utilizzato l'ultimo fotogramma.
*   Per il metodo `histogram` con `source_stats` impostato a `"per_frame"`, se la dimensione del batch di `image_ref` è maggiore di 1, ogni fotogramma di destinazione viene associato al fotogramma di riferimento corrispondente per indice. Se il batch di riferimento ha un solo fotogramma, viene utilizzato per tutti i fotogrammi di destinazione.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | L'immagine o le immagini risultanti dopo l'applicazione del trasferimento del colore. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ColorTransfer/it.md)

---
**Source fingerprint (SHA-256):** `f844af34ac6129c7751953c48e2d12aa0d2c556937e610f649f3eb2725955711`
