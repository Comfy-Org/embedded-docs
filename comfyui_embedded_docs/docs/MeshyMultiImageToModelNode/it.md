# MeshyMultiImageToModelNode

Questo nodo utilizza l'API Meshy per generare un modello 3D da più immagini di input. Carica le immagini fornite, invia un'attività di elaborazione e restituisce i file del modello 3D risultante (GLB e FBX) insieme all'ID attività per riferimento.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Richiesto | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Specifica la versione del modello AI da utilizzare. | COMBO | Sì | `"meshy-7.1"`<br>`"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `should_remesh` | Determina se la mesh generata viene elaborata. Se impostato su `"false"`, il nodo restituisce una mesh triangolare non elaborata. Se impostato su `"true"`, vengono mostrate le impostazioni di remesh sottostanti. | DYNAMIC_COMBO | Sì | `"true"`<br>`"false"` |
| `symmetry_mode` | Controlla se la simmetria viene applicata al modello generato. | COMBO | Sì | `"auto"`<br>`"on"`<br>`"off"` |
| `should_texture` | Determina se vengono generate le texture. Impostandolo su `"false"`, la fase di texture viene saltata e viene restituita una mesh senza texture. Se impostato su `"true"`, vengono mostrate le impostazioni texture sottostanti. | DYNAMIC_COMBO | Sì | `"true"`<br>`"false"` |
| `pose_mode` | Specifica la modalità di posa per il modello generato. | COMBO | Sì | `""` (vuoto)<br>`"A-pose"`<br>`"T-pose"` |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. (predefinito: 0) | INT | Sì | 0 a 2147483647 |
| `ultra_mode` | Esegue un passaggio di raffinamento aggiuntivo a 2048³ per una geometria di maggiore fedeltà con dettagli superficiali più fini. Richiede il modello `"meshy-7.1"`, `"meshy-7"` o `"latest"` (predefinito: `False`). | BOOLEAN | No | `True`<br>`False` |

### Impostazioni remesh (visibili quando `should_remesh` è `"true"`)

| Parametro | Descrizione | Tipo di dato | Richiesto | Intervallo |
| --- | --- | --- | --- | --- |
| `topology` | Il tipo di poligono target per l'output rimagliato. | COMBO | No | `"triangle"`<br>`"quad"` |
| `target_polycount` | Il numero target di poligoni per il modello rimagliato (predefinito: 300000). | INT | No | 100 a 300000 |

### Impostazioni texture (visibili quando `should_texture` è `"true"`)

| Parametro | Descrizione | Tipo di dato | Richiesto | Intervallo |
| --- | --- | --- | --- | --- |
| `enable_pbr` | Genera mappe PBR (metallico, rugosità, normale) oltre al colore di base. (predefinito: False) | BOOLEAN | No | True / False |
| `texture_prompt` | Fornisce un prompt testuale per guidare il processo di texturing. Massimo 600 caratteri. Non può essere utilizzato contemporaneamente a `texture_image`. (predefinito: vuoto) | STRING | No | Fino a 600 caratteri |
| `texture_image` | È possibile utilizzare solo uno tra `texture_image` o `texture_prompt` contemporaneamente. | IMAGE | No | - |
| `texture_resolution` | Risoluzione della texture del colore di base. Risoluzioni più elevate catturano più dettagli superficiali. | COMBO | No | `"2k"`<br>`"4k"`<br>`"8k"` |

### Input immagini

| Parametro | Descrizione | Tipo di dato | Richiesto | Intervallo |
| --- | --- | --- | --- | --- |
| `images` | Slot espandibile: collega da 2 a 4 immagini di input (`image_1`, `image_2`, `image_3`, `image_4`). Queste immagini vengono utilizzate per generare il modello 3D. | IMAGE | Sì | Da 2 a 4 immagini |

**Note**

* Devi fornire tra 2 e 4 immagini per l'input `images`.
* I parametri `topology` e `target_polycount` sono attivi solo quando `should_remesh` è impostato su `"true"`.
* I parametri `enable_pbr`, `texture_prompt`, `texture_image` e `texture_resolution` sono attivi solo quando `should_texture` è impostato su `"true"`.
* `texture_prompt` e `texture_image` sono mutuamente esclusivi; non puoi utilizzarli entrambi contemporaneamente. `texture_prompt` è limitato a 600 caratteri.
* Il valore `seed` non rende i risultati deterministici; modificarlo fa semplicemente rieseguire al nodo l'attività di generazione.
* `ultra_mode` richiede il modello `"meshy-7.1"`, `"meshy-7"` o `"latest"`; qualsiasi altro modello genera un errore.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model_file` | Il nome file del modello GLB generato. Questo output è fornito solo per compatibilità all'indietro. | STRING |
| `meshy_task_id` | L'identificatore univoco dell'attività API Meshy. | MESHY_TASK_ID |
| `GLB` | Il modello 3D generato in formato GLB. | FILE3DGLB |
| `FBX` | Il modello 3D generato in formato FBX. | FILE3DFBX |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyMultiImageToModelNode/it.md)

---
**Source fingerprint (SHA-256):** `9475279c0990fc069b4fef2bf0e2e20218ca1a9591a261ce6d33a2b651782ddb`
