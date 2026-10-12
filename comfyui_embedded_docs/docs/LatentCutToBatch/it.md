# LatentCutToBatch

Il nodo LatentCutToBatch suddivide una rappresentazione latente lungo una dimensione scelta (tempo, larghezza o altezza) in sezioni di dimensione specificata e impila tali sezioni in un nuovo batch. Ogni sezione diventa un elemento separato nel batch, così parti diverse di un campione latente possono essere elaborate indipendentemente.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `samples` | La rappresentazione latente da suddividere e raggruppare in batch. | LATENT | Sì | - |
| `dim` | La dimensione lungo la quale tagliare i campioni latenti. `"t"` si riferisce alla dimensione temporale (fotogrammi), `"x"` alla larghezza e `"y"` all'altezza. | COMBO | Sì | `"t"`<br>`"x"`<br>`"y"` |
| `slice_size` | La dimensione di ciascuna sezione da tagliare dalla dimensione specificata. Se la lunghezza della dimensione specificata non è perfettamente divisibile per questo valore, il resto viene scartato. (predefinito: 1) | INT | Sì | da 1 a 16384 (risoluzione massima) |

Nota: l'opzione `"t"` ha effetto solo quando il latente include una dimensione temporale. Se la dimensione scelta corrisponde alla posizione del batch o dei canali, oppure non esiste (ad esempio, selezionando `"t"` su un latente senza fotogrammi), il nodo restituisce l'input invariato. Se `slice_size` è maggiore della lunghezza della dimensione selezionata, l'intera dimensione viene usata come un'unica sezione. Quando la lunghezza della dimensione non è divisibile esattamente per `slice_size`, la parte restante alla fine viene scartata. La dimensione del batch in output è pari alla dimensione del batch in input moltiplicata per il numero di sezioni, mentre la dimensione tagliata stessa viene ridotta a `slice_size`.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `samples` | Il batch latente risultante, contenente i campioni suddivisi in sezioni e impilati. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentCutToBatch/it.md)

---
**Source fingerprint (SHA-256):** `873c9bc8391971887f1ab636c086cab86f5504a9c653bc80b54120ee53980bdf`
