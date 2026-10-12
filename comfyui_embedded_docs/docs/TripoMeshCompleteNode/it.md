# TripoMeshCompleteNode

Completa le parti di un modello 3D segmentato e ripara le regioni mancanti o danneggiate della mesh. Prende il task ID di un risultato di segmentazione mesh Tripo, richiede a Tripo il job di completamento e attende che termini. Puoi facoltativamente limitare il lavoro a nomi di parti specifici. Il modello completato viene restituito come file GLB.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `segment_task_id` | Task ID di un'attività di segmentazione mesh Tripo. Le parti del modello segmentato da questa attività vengono completate. Collega l'output SEGMENT_TASK_ID di un precedente nodo di segmentazione mesh Tripo. | SEGMENT_TASK_ID | Sì | Un singolo task ID |
| `part_names` | Nomi delle parti separati da virgole da completare. Se vuoto, completa ogni parte. Predefinito: stringa vuota. Gli spazi extra attorno ai nomi vengono rimossi e i nomi duplicati vengono ignorati. | STRING | No | Testo libero o vuoto |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `model_file` | Nome file del modello completato. Questo output esiste solo per compatibilità con le versioni precedenti. | STRING |
| `model task_id` | Task ID dell'attività di completamento mesh Tripo completata. Può essere usato come input da altri nodi Tripo che si aspettano un task ID del modello. | MODEL_TASK_ID |
| `GLB` | Il modello 3D completato con le parti riparate, scaricato come file GLB. | GLB |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoMeshCompleteNode/it.md)

---
**Source fingerprint (SHA-256):** `c5709231fa2e33e6f3c9b25669acca1d4ae9adb882b90210d703aeddc0d11ecc`
