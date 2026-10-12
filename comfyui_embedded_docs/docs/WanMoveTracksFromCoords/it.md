# WanMoveTracksFromCoords

Il nodo WanMoveTracksFromCoords crea tracce di movimento da una stringa di coordinate in formato JSON. Converte i dati delle coordinate in un formato di traccia che può essere utilizzato da altri nodi di elaborazione video e può facoltativamente applicare una maschera per controllare la visibilità delle tracce nel tempo.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `track_coords` | Una stringa in formato JSON contenente i dati delle coordinate per le tracce. Il valore predefinito è una lista vuota (`"[]"`). Questo input è forzato, quindi deve essere collegato nell'interfaccia utente. | STRING | No | N/A |
| `track_mask` | Una maschera opzionale. Quando fornita, il nodo la utilizza per determinare la visibilità delle tracce per frame: le tracce sono visibili nei frame in cui la maschera contiene almeno un pixel diverso da zero. Quando non viene fornita, tutte le tracce sono visibili in tutti i frame. | MASK | No | N/A |

**Nota:** L'input `track_coords` richiede una struttura JSON specifica. Deve essere una lista di tracce, dove ogni traccia è una lista di frame e ogni frame è un oggetto con coordinate `x` e `y`. Il numero di frame deve essere coerente tra tutte le tracce e deve essere fornita almeno una traccia.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `tracks` | I dati delle tracce generati, contenenti le coordinate del percorso e le informazioni di visibilità per ciascuna traccia. | TRACKS |
| `track_length` | Il numero totale di frame nelle tracce generate. | INT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanMoveTracksFromCoords/it.md)

---
**Source fingerprint (SHA-256):** `125187c96332fa81f0a30bcc4c927f405b56b578638ea565642a2b88dff808b7`
