# QuadrupleClipLoader

Il Quadruple CLIP Loader, QuadrupleCLIPLoader, è uno dei nodi core di ComfyUI, introdotto inizialmente per supportare il modello HiDream I1. Se questo nodo non è presente, prova ad aggiornare ComfyUI all'ultima versione per garantirne il supporto.

Richiede 4 modelli CLIP, corrispondenti ai parametri `clip_name1`, `clip_name2`, `clip_name3` e `clip_name4`, e fornirà un output di modello CLIP per i nodi successivi.

Questo nodo rileva i modelli situati nella cartella `ComfyUI/models/text_encoders` e legge anche i modelli dai percorsi aggiuntivi configurati nel file extra_model_paths.yaml.
A volte, dopo aver aggiunto dei modelli, potrebbe essere necessario **ricaricare l'interfaccia di ComfyUI** per consentirle di leggere i file dei modelli nella cartella corrispondente.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuadrupleClipLoader/it.md)
