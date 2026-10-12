# ControlnetLoader

Questo nodo rileva i modelli presenti nella cartella `ComfyUI/models/controlnet` e legge anche i modelli da percorsi aggiuntivi configurati nel file extra_model_paths.yaml. A volte potrebbe essere necessario **aggiornare l'interfaccia di ComfyUI** per consentire la lettura dei file dei modelli dalla cartella corrispondente.

Il nodo ControlNetLoader è progettato per caricare un modello ControlNet da un percorso specificato. Svolge un ruolo cruciale nell'inizializzazione dei modelli ControlNet, essenziali per applicare meccanismi di controllo sui contenuti generati o per modificare contenuti esistenti in base ai segnali di controllo.

## Input

| Campo | Descrizione | Comfy dtype |
| --- | --- | --- |
| `control_net_name` | Specifica il nome del modello ControlNet da caricare, utilizzato per individuare il file del modello all'interno di una struttura di directory predefinita. | `COMBO[STRING]` |

## Output

| Campo | Descrizione | Comfy dtype |
| --- | --- | --- |
| `control_net` | Restituisce il modello ControlNet caricato, pronto per l'uso nel controllo o nella modifica dei processi di generazione dei contenuti. | `CONTROL_NET` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlnetLoader/it.md)
