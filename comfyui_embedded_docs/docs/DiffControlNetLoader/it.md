# DiffControlnetLoader

Questo nodo rileva i modelli presenti nella cartella `ComfyUI/models/controlnet` e legge anche i modelli dai percorsi aggiuntivi configurati nel file extra_model_paths.yaml. In alcuni casi, potrebbe essere necessario **aggiornare l'interfaccia di ComfyUI** per consentire la lettura dei file dei modelli dalla cartella corrispondente.

Il nodo DiffControlNetLoader è progettato per caricare ControlNet differenziali, modelli specializzati che possono modificare il comportamento di un altro modello in base alle specifiche della ControlNet. Questo nodo consente la regolazione dinamica del comportamento dei modelli applicando ControlNet differenziali, facilitando la creazione di output personalizzati del modello.

## Input

| Campo | Descrizione | Tipo di dato Comfy |
| --- | --- | --- |
| `model` | Il modello di base a cui verrà applicato il ControlNet differenziale, consentendo la personalizzazione del comportamento del modello. | `MODEL` |
| `control_net_name` | Identifica il ControlNet differenziale specifico da caricare e applicare al modello di base per modificarne il comportamento. | `COMBO[STRING]` |

## Output

| Campo | Descrizione | Tipo di dato Comfy |
| --- | --- | --- |
| `control_net` | Un ControlNet differenziale che è stato caricato ed è pronto per essere applicato a un modello di base per modificarne il comportamento. | `CONTROL_NET` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DiffControlNetLoader/it.md)
