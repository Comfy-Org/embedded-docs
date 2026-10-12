# Meshy: Anima Modello

Questo nodo applica una specifica azione di animazione a un personaggio 3D precedentemente riggato utilizzando il servizio Meshy. Riceve un ID attività da una precedente operazione di rigging e un ID azione per selezionare l'animazione desiderata dalla libreria, quindi restituisce il modello animato nei formati di file GLB e FBX.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `rig_task_id` | L'ID attività univoco di una precedente operazione di rigging di un personaggio Meshy completata. | MESHY_RIGGED_TASK_ID | Sì | N/A |
| `action_id` | Il numero ID dell'azione di animazione da applicare. Visita https://docs.meshy.ai/en/api/animation-library per un elenco dei valori disponibili. (predefinito: 0) | INT | Sì | 0 to 696 |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-----------|-----------|
| `model_file` | Un identificatore stringa per il modello animato. Questo output è fornito solo per compatibilità con le versioni precedenti. | STRING |
| `GLB` | Il file del modello 3D animato in formato GLB. | FILE3DGLB |
| `FBX` | Il file del modello 3D animato in formato FBX. | FILE3DFBX |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyAnimateModelNode/it.md)

---
**Source fingerprint (SHA-256):** `760e94d3a92910051d9b473545191842dc9672e6c4a59c3d1cd9cfdc5eb2589d`
