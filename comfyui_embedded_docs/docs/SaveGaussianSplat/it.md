# Salva Splat

Questo nodo salva un file Gaussian splat 3D nella directory di output. Gestisce il processo di salvataggio del file e fornisce dati di anteprima per il viewport 3D.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model_3d` | Un file Gaussian splat 3D. | FILE3D | Sì | SplatAny<br>PLY<br>SPLAT<br>SPZ<br>KSPLAT |
| `filename_prefix` | Il prefisso per il nome file salvato (predefinito: "3d/ComfyUI"). | STRING | Sì | Qualsiasi prefisso di nome file valido |
| `viewport_state` | Lo stato attuale del viewport contenente informazioni sulla camera e sul modello. | LOAD3D | Sì | - |
| `model_3d_info` | Informazioni aggiuntive sul modello 3D per il viewport. | LOAD3DMODELINFO | No | - |
| `camera_info` | Informazioni sulla camera per l'anteprima del viewport. | LOAD3DCAMERA | No | - |
| `width` | La larghezza dell'anteprima (predefinita: 1024). | INT | Sì | Da 1 a 4096 |
| `height` | L'altezza dell'anteprima (predefinita: 1024). | INT | Sì | Da 1 a 4096 |

Nota: se `camera_info` o `model_3d_info` non vengono forniti, il nodo usa i valori corrispondenti da `viewport_state` quando disponibili.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `model_3d` | Il file Gaussian splat 3D che è stato salvato nella directory di output. | FILE3D |
| `model_3d_info` | Informazioni sul modello 3D per il viewport. | LOAD3DMODELINFO |
| `camera_info` | Informazioni sulla camera per l'anteprima del viewport. | LOAD3DCAMERA |
| `width` | La larghezza dell'anteprima. | INT |
| `height` | L'altezza dell'anteprima. | INT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveGaussianSplat/it.md)

---
**Source fingerprint (SHA-256):** `f2d6b98d2ce1fe11df8ba440b7f46a21e2308966c15daa5ca0bdca7dab1726cc`
