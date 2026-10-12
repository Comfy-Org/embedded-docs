# Tripo: Importa Modello

Questo nodo importa un modello 3D esterno in Tripo, in modo che i nodi di post-elaborazione di Tripo, come Texture, Rig e Convert, possano utilizzarlo. Il nodo carica il file su Tripo e restituisce un ID attività che identifica il modello importato per l'uso da parte di tali nodi. Si consiglia GLB perché le texture vengono preservate solo quando sono incorporate nel file, e la texturizzazione di un modello importato richiede un prompt di texture. Questo nodo è gratuito.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model_3d` | Modello 3D da importare (GLB / FBX / OBJ / STL, fino a 150 MB). I file OBJ e STL non contengono texture incorporate. | FILE3D | Sì | GLB<br>FBX<br>OBJ<br>STL<br>Any 3D format |

**Nota:** Sono supportati solo i formati GLB, FBX, OBJ e STL. GLTF (.gltf) non può essere importato perché fa riferimento a file esterni; esportare invece un GLB in file singolo. Il file del modello deve essere di 150 MB o inferiore. Si consiglia GLB perché le texture vengono mantenute all'importazione solo quando sono incorporate nel file. I file OBJ e STL non contengono texture incorporate. La texturizzazione di un modello importato richiede un prompt di texture.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `model task_id` | Un ID attività che identifica il modello importato, da utilizzare con i nodi di post-elaborazione di Tripo | MODEL_TASK_ID |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImportModelNode/it.md)

---
**Source fingerprint (SHA-256):** `bf91e964c5705f7377868dd06bbf5d57b41cc3607fc377cd45886d3d6c5ceddc`
