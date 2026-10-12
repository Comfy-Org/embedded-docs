# ComfySoftSwitchNode

Il nodo Soft Switch seleziona tra due possibili valori di input in base a una condizione booleana. Restituisce il valore dall'input `on_true` quando `switch` è true, e il valore dall'input `on_false` quando `switch` è false. Questo nodo è progettato per essere lazy, ovvero valuta solo l'input effettivamente necessario in base allo stato dello switch.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Range |
| --- | --- | --- | --- | --- |
| `switch` | La condizione booleana che determina quale input passare. Quando è true, viene selezionato l'input `on_true`. Quando è false, viene selezionato l'input `on_false`. | BOOLEAN | Sì | True or False |
| `on_false` | Il valore da restituire quando la condizione `switch` è false. Questo input è opzionale, ma almeno uno tra `on_false` e `on_true` deve essere collegato. | MATCH_TYPE | No | Stesso tipo di dati di `on_true` |
| `on_true` | Il valore da restituire quando la condizione `switch` è true. Questo input è opzionale, ma almeno uno tra `on_false` e `on_true` deve essere collegato. | MATCH_TYPE | No | Stesso tipo di dati di `on_false` |

**Nota:** Gli input `on_false` e `on_true` devono essere dello stesso tipo di dati, come definito dal template interno del nodo. Almeno uno di questi due input deve essere collegato, altrimenti il nodo restituisce il messaggio di validazione "At least one of on_false or on_true must be connected to Switch node". Poiché il nodo è lazy, quando è collegato un solo input, il nodo restituisce sempre il valore di quell'input indipendentemente dallo stato di `switch`.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `output` | Il valore selezionato. Corrisponde al tipo di dati dell'input collegato `on_false` o `on_true`. Quando entrambi gli input sono collegati, restituisce `on_true` se `switch` è true, e `on_false` se `switch` è false. | MATCH_TYPE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfySoftSwitchNode/it.md)

---
**Source fingerprint (SHA-256):** `7bf4bed69d8fd8c360e971ab8068382cd8ebaa02004d5df44312977a7309ae00`
