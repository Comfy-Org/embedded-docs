# ComfyOrNode

Il nodo Or esegue un'operazione logica OR su un insieme di valori di input. Restituisce `true` se uno qualsiasi dei valori forniti è considerato vero (truthy) secondo le regole standard di veridicità di Python.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `values` | Una raccolta espandibile di valori da valutare per veridicità. Ogni slot di input aggiunto è denominato `value_1`, `value_2` e così via. Il nodo restituisce `true` se uno qualsiasi di questi valori è considerato vero (truthy). | ANY | Sì | 1 o più valori |

**Nota:** Il nodo accetta un minimo di 1 valore di input. Puoi aggiungere altri input secondo necessità utilizzando la funzionalità di espansione automatica.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `BOOLEAN` | Restituisce `true` se uno qualsiasi dei valori di input è considerato vero (truthy); restituisce `false` se tutti i valori di input sono considerati falsi (falsy). | BOOLEAN |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyOrNode/it.md)

---
**Source fingerprint (SHA-256):** `f673aa2b0d754f55c51ba9c9ceea7d9de9a21d2e7308bd1281b4d4461243e4ad`
