# Converti Mappa Punti MoGe in Mesh

Questo nodo converte una mappa di punti MoGe in una mesh 3D. Prende i dati geometrici prodotti da un nodo di stima della profondità MoGe e li triangola in una mesh con coordinate UV e una texture opzionale.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `moge_geometry` | I dati geometrici MoGe contenenti mappe di punti, profondità e, facoltativamente, l'immagine di origine. | MOGE_GEOMETRY | Sì | N/A |
| `batch_index` | Quale immagine di una geometria MoGe in batch convertire in mesh. I conteggi dei vertici variano da immagine a immagine, quindi i batch non possono essere impilati in un unico MESH (predefinito: 0). | INT | Sì | 0 a 4096 |
| `decimation` | Passo dei vertici; 1 = risoluzione completa (predefinito: 1). | INT | Sì | 1 a 8 |
| `discontinuity_threshold` | Scarta i pixel il cui intervallo di profondità 3x3 supera questa frazione. 0 = disattivato (predefinito: 0.04). | FLOAT | Sì | 0.0 a 1.0 |
| `texture` | Propaga l'immagine di origine come texture baseColor (predefinito: True). | BOOLEAN | Sì | True/False |

Nota: `batch_index` deve essere inferiore alla dimensione del batch dell'input `moge_geometry`; la selezione di un indice fuori intervallo genera un errore. L'input deve contenere un output points, altrimenti il nodo genera un errore. Se la triangolazione produce una mesh vuota, il nodo genera un errore — impostare `discontinuity_threshold` su 0 disattiva il filtro di discontinuità della profondità. La mesh di output viene convertita in coordinate glTF: i dati MoGe prospettici (X a destra, Y in basso, Z in avanti) vengono ribaltati per corrispondere a glTF (Y in alto, Z indietro), mentre i dati panoramici (geometria senza parametri intrinseci) vengono ruotati di conseguenza con winding corretto. Quando `texture` è abilitato, l'immagine di origine da `moge_geometry` viene usata come texture baseColor.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `MESH` | Una mesh 3D con vertici, facce, coordinate UV e una texture baseColor opzionale dall'immagine di origine. | MESH |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePointMapToMesh/it.md)

---
**Source fingerprint (SHA-256):** `626925866eed6805d2ce87529909fc76b9484cd2e8118fdd1669a237d44b9b0b`
