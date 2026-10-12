# ComfySwitchNode

Il nodo If/Else Switch seleziona tra due possibili input in base a una condizione booleana. Quando `switch` è abilitato (true), passa l'input `on_true` all'output; quando è disabilitato (false), passa `on_false`. Gli input sono lazy, quindi viene valutato solo il ramo selezionato e l'altro input non deve essere connesso.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `switch` | Una condizione booleana che determina quale input viene passato all'output. Quando è abilitata (true), viene selezionato l'input `on_true`. Quando è disabilitata (false), viene selezionato l'input `on_false`. | BOOLEAN | Sì |  |
| `on_false` | I dati da passare all'output quando `switch` è disabilitato (false). Questo input viene richiesto solo quando `switch` è false. | MATCH_TYPE | No |  |
| `on_true` | I dati da passare all'output quando `switch` è abilitato (true). Questo input viene richiesto solo quando `switch` è true. | MATCH_TYPE | No |  |

**Nota sui requisiti degli input:** Gli input `on_false` e `on_true` vengono richiesti in modo condizionale. Il nodo richiede `on_true` solo quando `switch` è true, e richiede `on_false` solo quando `switch` è false. Entrambi gli input devono essere dello stesso tipo di dato, e tale tipo deve corrispondere al tipo di dato dell'output. Se l'input selezionato non è connesso, il nodo non restituisce alcun valore.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `output` | I dati selezionati: il valore di `on_true` quando `switch` è true, oppure il valore di `on_false` quando `switch` è false. | MATCH_TYPE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySwitchNode/it.md)

---
**Source fingerprint (SHA-256):** `42c442efeda0197d950702c52647233dee1a30216fb07e1ce4bc844784a6c5f2`
