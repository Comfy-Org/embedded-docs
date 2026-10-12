# SavePointCloud

Il nodo Save Point Cloud salva un file di nuvola di punti 3D nella directory di output e, facoltativamente, fornisce dati di anteprima per il visualizzatore 3D. Gestisce la denominazione e il salvataggio dei file, passando anche le informazioni su camera e modello per scopi di visualizzazione.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model_3d` | File di nuvola di punti (.ply) | FILE3D_POINT_CLOUD_ANY o FILE3D_PLY | Sì | - |
| `filename_prefix` | Prefisso per il nome del file salvato (predefinito: "3d/ComfyUI") | STRING | Sì | - |
| `viewport_state` | Stato corrente del viewport contenente informazioni su camera e modello | LOAD3D | Sì | - |
| `model_3d_info` | Informazioni aggiuntive sul modello per il visualizzatore 3D | LOAD3D_MODEL_INFO | No | - |
| `camera_info` | Informazioni sulla camera per il visualizzatore 3D | LOAD3D_CAMERA | No | - |
| `width` | Larghezza della visualizzazione di anteprima in pixel (predefinito: 1024) | INT | Sì | 1 a 4096 |
| `height` | Altezza della visualizzazione di anteprima in pixel (predefinito: 1024) | INT | Sì | 1 a 4096 |

Il file salvato viene scritto nella directory di output usando `filename_prefix` con un contatore a 5 cifre aggiunto (ad esempio, `3d/ComfyUI_00001.ply`). Quando l'input facoltativo `camera_info` non è connesso, le informazioni sulla camera vengono prese da `viewport_state`; analogamente, quando `model_3d_info` non è connesso, le informazioni sul modello vengono prese da `viewport_state` (o una lista vuota se non ne è disponibile alcuna).

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `model_3d` | Il file di nuvola di punti salvato | FILE3D_POINT_CLOUD_ANY |
| `model_3d_info` | Informazioni sul modello per il visualizzatore 3D | LOAD3D_MODEL_INFO |
| `camera_info` | Informazioni sulla camera per il visualizzatore 3D | LOAD3D_CAMERA |
| `width` | Larghezza della visualizzazione di anteprima | INT |
| `height` | Altezza della visualizzazione di anteprima | INT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SavePointCloud/it.md)

---
**Source fingerprint (SHA-256):** `ce8f005c431843a57d87a4aff2eed7a1604ebdf360f83b3aaaadc3ed364d218a`
