# MeshyTextureMultiViewNode

Questo nodo applica texture a un modello 3D creato in precedenza usando da 1 a 4 viste di riferimento dello stesso oggetto. Fornisci l'ID attività del modello originale e le immagini di riferimento; il nodo le invia al servizio Meshy, attende il completamento del processo e restituisce il modello con texture come file GLB e FBX.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Il modello AI usato per il processo di texturing. Attualmente è disponibile solo "meshy-7". | COMBO | Sì | `"meshy-7"` |
| `meshy_task_id` | L'ID attività del modello 3D creato in precedenza a cui applicare le texture. | MESHY_TASK_ID | Sì | — |
| `multiview_images` | Viste di riferimento dello stesso oggetto. La prima immagine è la vista primaria (frontale); l'ordine delle viste rimanenti non ha importanza. Slot espandibile: collega da 1 a 4 immagini (`image_1` a `image_4`). | IMAGE | Sì | Da 1 a 4 immagini |
| `enable_original_uv` | Usa gli UV originali del modello invece di generare nuovi UV. Quando è abilitato, Meshy preserva le texture esistenti dal modello caricato. Se il modello non ha UV originali, la qualità dell'output potrebbe non essere altrettanto buona. (predefinito: True; opzione avanzata) | BOOLEAN | No | True / False |
| `pbr` | Abilita la generazione di texture PBR (rendering basato sulla fisica). (predefinito: False; opzione avanzata) | BOOLEAN | No | True / False |
| `texture_resolution` | Risoluzione della texture di colore di base. Risoluzioni più elevate catturano più dettagli della superficie. | COMBO | Sì | `"2k"`<br>`"4k"`<br>`"8k"` |

**Nota:** `multiview_images` deve contenere tra 1 e 4 immagini. Il nodo lo convalida in fase di esecuzione e genera un errore se il conteggio è al di fuori di questo intervallo. Se un'immagine collegata contiene un batch di più immagini, ogni immagine del batch concorre al limite. La prima immagine viene usata come vista primaria (frontale); l'ordine delle immagini rimanenti non ha importanza.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `model_file` | Nome del file del modello. Questo output è mantenuto solo per retrocompatibilità. | STRING |
| `meshy_task_id` | ID attività del processo di texturing. | MESHY_TASK_ID |
| `GLB` | Il modello 3D con texture scaricato in formato GLB. | FILE3DGLB |
| `FBX` | Il modello 3D con texture scaricato in formato FBX. | FILE3DFBX |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextureMultiViewNode/it.md)

---
**Source fingerprint (SHA-256):** `3a08d003683a182121471a064833c09b932c7c84c20fd5cb5ac0285e135b2b7e`
