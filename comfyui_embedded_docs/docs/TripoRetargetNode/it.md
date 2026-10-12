# TripoRetargetNode

Il nodo TripoRetargetNode applica un'animazione predefinita a un modello 3D riggato esistente. Prende l'ID attività di un modello precedentemente riggato, invia una richiesta di retargeting all'API Tripo e scarica il file animato risultante. Il modello animato può essere restituito in formato GLB o FBX, con geometria mesh opzionale e riproduzione in place opzionale.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `original_model_task_id` | L'ID attività del modello 3D precedentemente riggato su cui eseguire il retargeting. L'attività referenziata deve essere un'attività di rig. | RIG_TASK_ID | Sì | - |
| `animation` | L'animazione predefinita da applicare al modello riggato. Le animazioni `preset:*` funzionano con entrambi i modelli di rig. Le animazioni `preset:biped:*` sono realizzate per rig provenienti dal modello v1.0-20240301; un rig v2.5 accetta solo chop, climb, dive, fall, hurt, idle, jump, run, shoot, slash, turn e walk. | COMBO | Sì | `"preset:idle"`<br>`"preset:walk"`<br>`"preset:run"`<br>`"preset:dive"`<br>`"preset:climb"`<br>`"preset:jump"`<br>`"preset:slash"`<br>`"preset:shoot"`<br>`"preset:hurt"`<br>`"preset:fall"`<br>`"preset:turn"`<br>`"preset:quadruped:walk"`<br>`"preset:hexapod:walk"`<br>`"preset:octopod:walk"`<br>`"preset:serpentine:march"`<br>`"preset:aquatic:march"`<br>più ulteriori opzioni `"preset:biped:*"` mostrate nell'interfaccia utente |
| `out_format` | Formato del file di output; il risultato arriva sull'output corrispondente. (predefinito: glb) | COMBO | No | `"glb"`<br>`"fbx"` |
| `export_with_geometry` | Includi la mesh nell'esportazione; se disattivato, esporta solo lo scheletro animato. (predefinito: True) | BOOLEAN | No | True<br>False |
| `animate_in_place` | Riproduci l'animazione in place, senza spostamento della radice. (predefinito: False) | BOOLEAN | No | True<br>False |
| `auth_token_comfy_org` | Token di autenticazione per l'accesso all'API di Comfy.org (parametro nascosto). | AUTH_TOKEN_COMFY_ORG | No | - |
| `api_key_comfy_org` | Chiave API per l'accesso al servizio Comfy.org (parametro nascosto). | API_KEY_COMFY_ORG | No | - |
| `unique_id` | Identificatore univoco per monitorare l'operazione (parametro nascosto). | UNIQUE_ID | No | - |

Nota: Le animazioni nel gruppo `preset:*` funzionano con entrambi i modelli di rig. Le animazioni nel gruppo `preset:biped:*` sono realizzate per rig provenienti dal modello v1.0-20240301; un rig v2.5 accetta solo chop, climb, dive, fall, hurt, idle, jump, run, shoot, slash, turn e walk. Se il rig referenziato è stato creato con la specifica Mixamo e una versione del modello che inizia con `v1.0`, la chiamata di retargeting fallisce con un errore. Il formato di output richiesto deve essere GLB o FBX; se il servizio restituisce qualsiasi altro tipo di file, il nodo genera un errore.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `model_file` | Il file del modello 3D animato generato (solo per retrocompatibilità). | STRING |
| `retarget task_id` | L'ID attività per monitorare l'operazione di retargeting. | RETARGET_TASK_ID |
| `GLB` | Il modello 3D animato in formato GLB. Valorizzato quando `out_format` è glb. | FILE3DGLB |
| `FBX` | Il modello 3D animato in formato FBX. Valorizzato quando `out_format` è fbx. | FILE3DFBX |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRetargetNode/it.md)

---
**Source fingerprint (SHA-256):** `4814858b940ece13f85010ff81fcdac0258fe8550aebd914be2613e8f40c0e5a`
