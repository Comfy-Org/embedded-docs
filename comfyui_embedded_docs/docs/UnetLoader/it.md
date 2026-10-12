# UnetLoader

Il nodo UNETLoader è progettato per caricare modelli U-Net per nome, facilitando l'uso di architetture U-Net pre-addestrate all'interno del sistema.

Questo nodo rileverà i modelli situati nella cartella `ComfyUI/models/diffusion_models`.

## Input

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `unet_name` | Specifica il nome del modello U-Net da caricare. Questo nome viene utilizzato per individuare il modello all'interno di una struttura di directory predefinita, consentendo il caricamento dinamico di diversi modelli U-Net. | COMBO[STRING] |
| `weight_dtype` | 🚧  fp8_e4m3fn fp9_e5m2 | ... |

## Output

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `model` | Restituisce il modello U-Net caricato, consentendone l'utilizzo per ulteriori elaborazioni o inferenze all'interno del sistema. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UnetLoader/it.md)
