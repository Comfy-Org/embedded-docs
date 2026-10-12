# LoopResult

LoopResult è un nodo di output riservato agli sviluppatori che segna il punto di chiusura di un blocco loop. Raccoglie i valori che gli vengono passati in ordine (denominati `output0`, `output1`, e così via) e rilascia il blocco di esecuzione esterno identificato da un ID di chiusura. Poiché il fingerprinting degli input restituisce sempre NaN, il nodo viene considerato sempre modificato e viene rieseguito a ogni esecuzione.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `close_id` | Identificatore del blocco loop da chiudere; viene utilizzato solo il primo valore della lista | STRING | Sì | - |
| `output0`, `output1`, ... | Valori raccolti dal blocco loop. Il nodo accetta qualsiasi input aggiuntivo e li raccoglie in ordine sequenziale partendo da `output0`, fermandosi al primo indice mancante | Qualsiasi tipo | No | - |

Nota: questo nodo accetta tutti gli input (`accept_all_inputs`). Qualsiasi input oltre `close_id` viene trattato come un valore di loop raccolto e deve essere denominato `output0`, `output1`, `output2`, ecc., senza salti, affinché venga incluso nel risultato.

## Output

Questo nodo non restituisce alcun output. Rilascia solo il blocco di esecuzione esterno associato a `close_id`.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoopResult/it.md)

---
**Source fingerprint (SHA-256):** `637f8a39b0e99e8d4453cfc482463bd14d909b710264021ac2c27fdcd68b6063`
