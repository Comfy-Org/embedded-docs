# Meshy: Texture Model

Il nodo Meshy: Texture Model applica texture generate dall'IA a un modello 3D esistente. Utilizza un ID attività da una precedente attività di generazione o conversione 3D di Meshy e guida il processo di texturizzazione con un prompt di stile testuale o un'immagine di riferimento. Il nodo restituisce il modello texturizzato nei formati di file GLB e FBX.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | La versione del modello IA da usare per la texturizzazione. | COMBO | Sì | `"meshy-7"`<br>`"meshy-6"`<br>`"latest"` |
| `meshy_task_id` | L'identificatore univoco (ID attività) di una precedente attività di generazione o conversione 3D di Meshy. Fornisce il modello 3D di base da texturizzare. | MESHY_TASK_ID | Sì | - |
| `enable_original_uv` | Usa l'UV originale del modello invece di generare nuovi UV. Quando è abilitata (predefinito: `True`), Meshy conserva le texture esistenti dal modello caricato. Se il modello non ha un UV originale, la qualità dell'output potrebbe non essere altrettanto buona. Questa è un'opzione avanzata. | BOOLEAN | Sì | true / false |
| `pbr` | Abilita l'output del materiale PBR (Physically Based Rendering) per il modello texturizzato (predefinito: `False`). Questa è un'opzione avanzata. | BOOLEAN | Sì | true / false |
| `text_style_prompt` | Descrivi lo stile di texture desiderato per l'oggetto usando il testo (predefinito: stringa vuota). Massimo 600 caratteri. Non può essere usato contemporaneamente a `image_style`. | STRING | Sì | - |
| `image_style` | Un'immagine 2D per guidare il processo di texturizzazione. Non può essere usata contemporaneamente a `text_style_prompt`. | IMAGE | No | - |
| `texture_resolution` | Risoluzione della texture del colore di base. Risoluzioni più alte catturano più dettagli della superficie. | COMBO | Sì | `"2k"`<br>`"4k"`<br>`"8k"` |

**Vincoli dei parametri:**

* Devi fornire un `text_style_prompt` oppure un `image_style`, ma non puoi fornire entrambi contemporaneamente.
* Il `text_style_prompt` è limitato a un massimo di 600 caratteri.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model_file` | Il nome del file del modello GLB generato. Questo output è fornito solo per compatibilità con le versioni precedenti. | STRING |
| `meshy_task_id` | L'identificatore univoco dell'attività per questa operazione di texturizzazione, che può essere usato per fare riferimento al risultato. | MESHY_TASK_ID |
| `GLB` | Il modello 3D texturizzato salvato nel formato di file GLB. | FILE3DGLB |
| `FBX` | Il modello 3D texturizzato salvato nel formato di file FBX. | FILE3DFBX |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextureNode/it.md)

---
**Source fingerprint (SHA-256):** `30d51f6efe3602f27d99706840c974baf2c4397a4f9a191f3478e7eff372e319`
