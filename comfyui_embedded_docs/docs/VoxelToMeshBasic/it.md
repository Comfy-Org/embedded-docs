# VoxelToMeshBasic

Il nodo VoxelToMeshBasic converte i dati voxel 3D in geometria mesh. Elabora i volumi voxel applicando un valore di soglia per determinare quali parti del volume diventano superfici solide nella mesh risultante. Il nodo restituisce una struttura mesh completa con vertici e facce utilizzabile per il rendering e la modellazione 3D.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `voxel` | I dati voxel 3D da convertire in una mesh | VOXEL | Sì | - |
| `threshold` | Il valore di soglia utilizzato per determinare quali voxel diventano parte della superficie della mesh (predefinito: 0.6) | FLOAT | Sì | da -1.0 a 1.0 |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `MESH` | La mesh 3D generata contenente vertici e facce | MESH |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VoxelToMeshBasic/it.md)

---
**Source fingerprint (SHA-256):** `95d729463e9d32fb0b8a82a397c6ed7fccaf190ec8a183d71a99fef170747fd1`
