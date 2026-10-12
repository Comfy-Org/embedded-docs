# GetItemFromList

Questo nodo restituisce un singolo elemento da un elenco, selezionato in base alla sua posizione. Fornisci l'elenco e il numero di indice dell'elemento desiderato, e il nodo restituisce quell'elemento. È utile per scegliere un elemento specifico da un gruppo di valori, ad esempio una particolare immagine da un batch.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `list` | L'elenco di valori da cui selezionare. Poiché questo nodo è contrassegnato come avente un input di tipo lista, il valore connesso viene gestito come un gruppo di elementi. | Qualsiasi tipo | Sì | Qualsiasi elenco di valori |
| `index` | La posizione dell'elemento da restituire. Il valore inizia da 0, quindi `0` restituisce il primo elemento, `1` restituisce il secondo elemento e così via (predefinito: 0). | INT | Sì | Qualsiasi indice intero |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `OUTPUT` | Il singolo elemento situato in corrispondenza dell'`index` specificato all'interno della `list` fornita. | Qualsiasi tipo |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetItemFromList/it.md)

---
**Source fingerprint (SHA-256):** `11c1c90fed0e29f1110b4c1dda64d60797aff38d7f3af69f76b74e94fe94e976`
