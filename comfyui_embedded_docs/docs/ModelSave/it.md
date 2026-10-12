# ModelSave

Il nodo ModelSave salva un MODEL nell'archiviazione del computer come file di checkpoint `.safetensors`. Scrive il file nella directory di output di ComfyUI usando il prefisso del nome file fornito e incorpora le informazioni del prompt del workflow e i metadati del modello nel file salvato, quando disponibili.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello da salvare su disco | MODEL | Sì | - |
| `filename_prefix` | Il prefisso del nome file e del percorso per il file del modello salvato (predefinito: "diffusion_models/ComfyUI") | STRING | Sì | - |
| `prompt` | Informazioni del prompt del workflow (fornite automaticamente) | PROMPT | No | - |
| `extra_pnginfo` | Metadati aggiuntivi del workflow (forniti automaticamente) | EXTRA_PNGINFO | No | - |

Nota: il nome file salvato è composto dal valore di `filename_prefix` seguito da un contatore a cinque cifre (ad esempio, `diffusion_models/ComfyUI_00001_.safetensors`). Se esiste già un file con lo stesso prefisso, il contatore viene incrementato in modo che il nuovo file riceva un nome univoco. Quando disponibili, il prompt del workflow, i metadati aggiuntivi e le informazioni sull'architettura del modello (ad esempio Stable Diffusion XL, SDXL Refiner, Stable Video Diffusion o Stable Diffusion 3) vengono incorporati nel file salvato. Se il salvataggio dei metadati è disabilitato tramite le impostazioni della riga di comando di ComfyUI, il prompt e i metadati aggiuntivi non vengono scritti nel file.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| *Nessuno* | Questo nodo non restituisce alcun valore di output | - |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSave/it.md)

---
**Source fingerprint (SHA-256):** `943e60f2c596d9cbcaabe95029fd9d443df5b61c6137736a8b1b81ab78f200ea`
