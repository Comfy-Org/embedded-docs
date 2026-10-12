# ComfyAndNode

Il nodo And esegue un'operazione logica AND su un gruppo di valori di input. Restituisce `true` solo quando ogni valore connesso è considerato veritiero secondo le regole di verità di Python, il che lo rende utile per verificare che più condizioni siano tutte soddisfatte contemporaneamente.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `values` | Un gruppo espandibile di valori da valutare. Il nodo inizia con uno slot e puoi aggiungerne altri facendo clic sul pulsante "+" del nodo. Accetta qualsiasi tipo di dato. | ANY | Sì | Minimo 1 (nessun massimo) |

**Nota:** Questo input è un gruppo di slot espandibile. Gli slot vengono aggiunti singolarmente (ad esempio `value_1`, `value_2`, e così via) e deve essere presente almeno uno slot.

**Nota:** Il nodo usa le regole di verità di Python per decidere se un valore è `true` o `false`. Ad esempio, una stringa vuota, il numero 0, una lista vuota e `None` sono tutti considerati `false`. Tutti gli altri valori sono considerati `true`.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `BOOLEAN` | Restituisce `true` se tutti i valori di input sono veritieri, altrimenti restituisce `false`. | BOOLEAN |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyAndNode/it.md)

---
**Source fingerprint (SHA-256):** `e7359c46da62f9859ea4f4a239cf20c565b5f7de22d280afc00c7ca321f1c89d`
