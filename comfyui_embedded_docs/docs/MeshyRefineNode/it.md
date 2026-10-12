# MeshyRefineNode

Il nodo Meshy: Refine Draft Model prende un modello 3D draft da un task Meshy precedente e lo migliora, aggiungendo facoltativamente texture tramite un prompt testuale o un'immagine di riferimento. Invia il job di rifinitura all'API Meshy e restituisce il modello finito come file GLB e FBX una volta completato il task.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Il modello AI utilizzato per rifinire il modello draft. | COMBO | Sì | `"meshy-7.1"`<br>`"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `meshy_task_id` | L'ID task univoco del modello draft che vuoi rifinire. | MESHY_TASK_ID | Sì | - |
| `enable_pbr` | Genera mappe PBR (metallic, roughness, normal) oltre al colore di base. Nota: deve essere impostato su false quando si usa lo stile Sculpture, poiché lo stile Sculpture genera il proprio insieme di mappe PBR. (predefinito: False) | BOOLEAN | Sì | - |
| `texture_prompt` | Fornisci un prompt testuale per guidare il processo di texturing. Massimo 600 caratteri. Non può essere usato contemporaneamente a `texture_image`. (predefinito: stringa vuota) | STRING | Sì | Massimo 600 caratteri |
| `texture_image` | Solo uno tra `texture_image` e `texture_prompt` può essere usato contemporaneamente. | IMAGE | No | - |
| `texture_resolution` | Risoluzione della texture del colore di base. Risoluzioni più alte catturano più dettagli della superficie. | COMBO | Sì | `"2k"`<br>`"4k"`<br>`"8k"` |

**Nota:** Gli input `texture_prompt` e `texture_image` si escludono a vicenda. Non è possibile fornire sia un prompt testuale sia un'immagine per il texturing nella stessa operazione.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `model_file` | Il nome file del modello GLB generato. (Solo per compatibilità con le versioni precedenti) | STRING |
| `meshy_task_id` | L'ID task univoco per il job di rifinitura inviato. | MESHY_TASK_ID |
| `GLB` | Il modello 3D rifinito finale in formato GLB. | FILE3DGLB |
| `FBX` | Il modello 3D rifinito finale in formato FBX. | FILE3DFBX |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyRefineNode/it.md)

---
**Source fingerprint (SHA-256):** `d9aac584e6abf9688c97bf01ea515bca13844d08c93923a672fb2853266926c8`
