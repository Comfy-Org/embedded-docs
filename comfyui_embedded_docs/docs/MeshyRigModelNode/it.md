# MeshyRigModelNode

Il nodo Meshy: Rig Model prende un modello 3D da una precedente attività Meshy e crea automaticamente uno scheletro per esso, producendo un personaggio riggato che può essere posizionato e animato. Il nodo restituisce il modello riggato sia nel formato file GLB sia nel formato FBX.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `meshy_task_id` | L'ID univoco dell'attività di una precedente operazione Meshy (ad es. text-to-3D o image-to-3D) che ha generato il modello da riggare. | MESHY_TASK_ID | Sì | N/A |
| `height_meters` | L'altezza approssimativa del modello del personaggio in metri. Questo aiuta nella precisione di scalatura e rigging (predefinito: 1.7). | FLOAT | Sì | 0.1 to 15.0 |
| `texture_image` | L'immagine di texture base color con UV unwrap del modello. | IMAGE | No | N/A |

**Nota:** Il processo di rigging automatico al momento non è adatto a mesh non texturizzate, asset non umanoidi o asset umanoidi con struttura degli arti e del corpo non chiara.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `model_file` | Un output legacy mantenuto solo per retrocompatibilità, contenente il nome file del modello GLB. | STRING |
| `rig_task_id` | L'ID univoco dell'attività per questa operazione di rigging, che può essere utilizzato per fare riferimento al risultato nei nodi Meshy successivi. | MESHY_RIGGED_TASK_ID |
| `GLB` | Il modello 3D del personaggio con rig salvato nel formato file GLB. | FILE3DGLB |
| `FBX` | Il modello 3D del personaggio con rig salvato nel formato file FBX. | FILE3DFBX |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyRigModelNode/it.md)

---
**Source fingerprint (SHA-256):** `6ae79359fa54f36dd2491a952fe54fa56866038758e8cd475a2d2f8e9e47e3b3`
