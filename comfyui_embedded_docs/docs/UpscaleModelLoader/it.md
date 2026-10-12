# UpscaleModelLoader

Questo nodo rileva i modelli situati nella cartella `ComfyUI/models/upscale_models` e legge anche i modelli da percorsi aggiuntivi configurati nel file extra_model_paths.yaml. A volte, potrebbe essere necessario **aggiornare l'interfaccia di ComfyUI** per consentirle di leggere i file dei modelli dalla cartella corrispondente.

Il nodo UpscaleModelLoader è progettato per caricare modelli di upscale da una directory specificata. Facilita il recupero e la preparazione dei modelli di upscale per le attività di upscaling delle immagini, garantendo che i modelli siano caricati e configurati correttamente per la valutazione.

## Input

| Campo | Descrizione | Tipo di dato Comfy |
| --- | --- | --- |
| `model_name` | Specifica il nome del modello di upscale da caricare, identificando e recuperando il file del modello corretto dalla directory dei modelli di upscale. | `COMBO[STRING]` |

## Output

| Campo | Descrizione | Tipo di dato Comfy |
| --- | --- | --- |
| `upscale_model` | Restituisce il modello di upscale caricato e preparato, pronto per l'uso in attività di upscaling delle immagini. | `UPSCALE_MODEL` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UpscaleModelLoader/it.md)
