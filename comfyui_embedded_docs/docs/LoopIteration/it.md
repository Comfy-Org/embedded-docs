# LoopIteration

Questo nodo fornisce metadati di iterazione per workflow in stile loop. Riceve input basati su liste e passa attraverso il primo elemento di ciascuna lista, così un loop può tenere traccia dell'indice corrente, se si tratta del primo o dell'ultimo passaggio, dell'elemento corrente della lista e di qualsiasi valore di iterazione in corso. Il comportamento della cache è controllato dal flag `reuse_cache`. Questo nodo è contrassegnato come solo per sviluppatori.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `iteration_index` | L'indice dell'iterazione corrente, fornito come lista. Il primo elemento viene passato all'output. | INT | Sì | - |
| `is_first` | Indica se l'iterazione corrente è la prima, fornito come lista. Il primo elemento viene passato all'output. | BOOLEAN | Sì | - |
| `is_last` | Indica se l'iterazione corrente è l'ultima, fornito come lista. Il primo elemento viene passato all'output. | BOOLEAN | Sì | - |
| `list_item` | L'elemento prelevato dalla lista per questa iterazione. Opzionale; quando fornito, il primo elemento viene passato all'output, altrimenti viene restituito None. | ANY | No | - |
| `current_iteration_value` | Il valore trasportato dall'iterazione corrente. Opzionale; quando fornito, l'intero valore viene passato all'output, altrimenti viene restituito None. | ANY | No | - |
| `reuse_cache` | Controlla se il risultato può essere riutilizzato dalla cache. Quando è abilitato, il nodo mantiene un fingerprint stabile in modo che i risultati in cache possano essere riutilizzati. Quando è disabilitato, viene prodotto un fingerprint non corrispondente in modo che il nodo venga eseguito di nuovo a ogni iterazione. | BOOLEAN | Sì | - |

Nota: questo nodo è abilitato per input di tipo lista, il che significa che ogni input deve arrivare come lista e il nodo restituisce solo il primo elemento di ciascuna lista (tranne `current_iteration_value`, che viene passato come lista). Accetta inoltre input aggiuntivi oltre a quelli elencati qui.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `iteration_index` | L'indice dell'iterazione corrente. | INT |
| `is_first` | Indica se l'iterazione corrente è la prima. | BOOLEAN |
| `is_last` | Indica se l'iterazione corrente è l'ultima. | BOOLEAN |
| `list_item` | L'elemento prelevato dalla lista per questa iterazione, oppure None quando non è stato fornito alcun elemento. | ANY |
| `current_iteration_value` | Il valore trasportato dall'iterazione corrente, oppure None quando non è stato fornito alcun valore. Questo output viene restituito come lista. | ANY |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoopIteration/it.md)

---
**Source fingerprint (SHA-256):** `c7072f22bd382f567792d2ea7a30312c64d33c213551f8983c25cd7b95adc4fb`
