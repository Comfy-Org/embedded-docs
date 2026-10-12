# Tripo: Segmenta modello

Questo nodo suddivide un modello 3D in singole parti. Invia il modello al servizio di segmentazione Tripo, attende il completamento dell'operazione e restituisce il modello segmentato in formato GLB insieme a un elenco dei nomi delle parti separato da virgole. Questi nomi delle parti alimentano i passaggi successivi, come Tripo: Complete Mesh Parts, Tripo: Retopology e Tripo: Convert model.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model_task_id` | L'ID del task del modello 3D da segmentare in parti. | MODEL_TASK_ID | Sì | N/A |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `model_file` | Nome del file di output del modello GLB segmentato, nella forma `<task_id>.glb`. Mantenuto solo per compatibilità con le versioni precedenti. | STRING |
| `segment task_id` | L'ID del task del processo di segmentazione che ha prodotto il risultato. | SEGMENT_TASK_ID |
| `GLB` | Il modello 3D segmentato, come file GLB. | GLB |
| `part_names` | Nomi delle parti separati da virgole. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSegmentNode/it.md)

---
**Source fingerprint (SHA-256):** `3218f87bfdc347d58b639cbe57b01cf7625c95c753bf381e35b4a28376eeb0e8`
