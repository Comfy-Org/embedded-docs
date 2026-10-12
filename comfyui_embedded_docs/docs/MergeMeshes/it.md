# MergeMeshes

MergeMeshes combina più mesh di input in un'unica mesh impilando i loro vertici, facce, coordinate UV e colori dei vertici, e applicando un offset agli indici delle facce in modo che tutte le parti si uniscano correttamente in un'unica mesh continua.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `meshes` | Slot espandibile: collega da 2 a 50 oggetti mesh (denominati `mesh_1`, `mesh_2`, ..., `mesh_50`). Tutte le mesh collegate vengono unite in un'unica mesh di output. | MESH | Sì | Da 2 a 50 mesh |

**Nota:** È necessario fornire almeno una mesh; in caso contrario il nodo genera un errore. Viene utilizzato solo il primo elemento mesh del batch di ogni mesh di input. Le mesh di input vengono spostate sulla CPU prima dell'unione. Se una qualsiasi mesh di input ha dati UV, l'output include gli UV e le mesh prive di UV ricevono valori UV riempiti con zeri. Se una qualsiasi mesh di input ha colori dei vertici, l'output include i colori dei vertici; le mesh prive di colori ricevono colori bianchi (valore 1) e i canali di colore vengono estesi al maggior numero di canali riscontrato tra gli input. Viene mantenuta solo la texture del primo input che ne fornisce una; le texture aggiuntive vengono scartate.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `mesh` | La mesh unita contenente tutti i vertici, le facce, gli UV e i colori di input combinati in un'unica mesh. | MESH |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MergeMeshes/it.md)

---
**Source fingerprint (SHA-256):** `0ce49b522f6348d524df20d6c27eb8bd9575c4a781790f6f8e3ac4f3ee255d38`
