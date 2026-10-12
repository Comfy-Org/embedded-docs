# ImageOnlyCheckpointSave

Questo nodo salva un file di checkpoint che raggruppa un modello insieme al suo encoder visivo CLIP e al VAE. Il file viene scritto in formato safetensors nella directory di output, usando il prefisso del nome file fornito, così i componenti relativi alle immagini di un modello possono essere archiviati come un singolo checkpoint.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello da salvare nel checkpoint | MODEL | Sì | - |
| `clip_vision` | L'encoder visivo CLIP da salvare nel checkpoint | CLIP_VISION | Sì | - |
| `vae` | Il VAE (autoencoder variazionale) da salvare nel checkpoint | VAE | Sì | - |
| `filename_prefix` | Il prefisso per il nome file di output (predefinito: "checkpoints/ComfyUI") | STRING | Sì | - |
| `prompt` | Parametro nascosto che riceve i dati del prompt del workflow | PROMPT | No | - |
| `extra_pnginfo` | Parametro nascosto che riceve metadati PNG aggiuntivi | EXTRA_PNGINFO | No | - |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| - | Questo nodo non restituisce alcun output | - |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointSave/it.md)

---
**Source fingerprint (SHA-256):** `8ff4b3a78d8da523eaa5f784f847e954ba73b4d6037e748dcce592b447fcdee9`
