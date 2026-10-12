# DA3Inference

Questo nodo esegue il modello Depth Anything 3 su un'immagine per stimare informazioni di profondità e geometria. In modalità multiview, più immagini vengono elaborate insieme come viste separate della stessa scena per produrre mappe di profondità e pose della camera geometricamente coerenti.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `da3_model` | Il modello Depth Anything 3 da usare per l'inferenza | DA3_MODEL | Sì | - |
| `image` | Immagine o immagini di input da elaborare | IMAGE | Sì | - |
| `resolution` | Risoluzione alla quale viene eseguito il modello (lato più lungo, multiplo di 14). Valori più bassi sono più veloci e usano meno VRAM. Valori più alti producono più dettaglio. L'output viene riportato alla dimensione originale tramite upsampling (predefinito: 504) | INT | Sì | 140 a 2520 (passo: 14) |
| `resize_method` | upper_bound_resize: ridimensiona in modo che il lato più lungo sia uguale alla risoluzione (limita la memoria, predefinito). lower_bound_resize: ridimensiona in modo che il lato più corto sia uguale alla risoluzione (preserva più dettagli su immagini alte/larghe, usa più memoria) | COMBO | Sì | `"upper_bound_resize"`<br>`"lower_bound_resize"` |
| `mode` | mono: elaborazione di immagini a vista singola (funziona con qualsiasi variante del modello). multiview: tutte le immagini vengono elaborate insieme per coerenza geometrica e stima della posa della camera (solo per i modelli Small e Base) | COMBO | Sì | `"mono"`<br>`"multiview"` |
| `ref_view_strategy` | Quale vista funge da ancoraggio geometrico in modalità multiview. saddle_balanced: la vista più media rispetto a tutte le altre (scelta generale migliore). saddle_sim_range: la vista più visivamente distinta dalle altre. first / middle: selezioni posizionali fisse (predefinito: saddle_balanced) | COMBO | No (condizionale) | `"saddle_balanced"`<br>`"saddle_sim_range"`<br>`"first"`<br>`"middle"` |
| `pose_method` | Come viene stimato il campo visivo della camera (solo per i modelli Small e Base). cam_dec: appreso dalle caratteristiche dell'immagine. ray_pose: derivato geometricamente dall'output dei raggi 3D del modello. Influisce sulla correttezza prospettica dell'output 3D (predefinito: cam_dec) | COMBO | No (condizionale) | `"cam_dec"`<br>`"ray_pose"` |

**Note sui vincoli dei parametri:**
- I parametri `ref_view_strategy` e `pose_method` sono disponibili solo quando `mode` è impostato su `"multiview"`.
- La modalità multiview richiede una variante del modello Small o Base. I modelli con altri tipi di head (come Metric o Mono) non supportano l'attenzione cross-view o la stima della posa della camera.
- Quando `pose_method` è impostato su `"cam_dec"`, il modello deve avere un decoder della camera. Se impostato su `"ray_pose"`, il modello deve avere una head DualDPT.
- Se il `pose_method` selezionato non è compatibile con il modello caricato, verrà generato un errore.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `da3_geometry` | Dizionario di tensori non normalizzati. Contiene sempre le chiavi: depth, image, mode. Le chiavi opzionali includono: sky (per i modelli Mono/Metric), confidence (per i modelli Small/Base), extrinsics e intrinsics (per la modalità multiview) | DA3_GEOMETRY |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DA3Inference/it.md)

---
**Source fingerprint (SHA-256):** `e91dd47e6a01719cdd6b6ce8a9bcc45933cac72c5e147ac42906d2f83ab7c250`
