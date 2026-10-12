# UnclipCheckpointLoader

Questo nodo rileva i modelli presenti nella cartella `ComfyUI/models/checkpoints` e legge anche i modelli da percorsi aggiuntivi configurati nel file extra_model_paths.yaml. A volte potrebbe essere necessario **aggiornare l'interfaccia di ComfyUI** per consentirle di leggere i file dei modelli dalla cartella corrispondente.

Il nodo unCLIPCheckpointLoader è progettato per caricare checkpoint specificamente pensati per i modelli unCLIP. Facilita il recupero e l'inizializzazione di modelli, moduli CLIP vision e VAE da un checkpoint specificato, semplificando il processo di configurazione per ulteriori operazioni o analisi.

## Input

| Campo | Descrizione | Comfy dtype |
| --- | --- | --- |
| `ckpt_name` | Specifica il nome del checkpoint da caricare, identificando e recuperando il file checkpoint corretto da una directory predefinita, determinando l'inizializzazione di modelli e configurazioni. | `COMBO[STRING]` |

## Output

| Campo | Descrizione | Comfy dtype | Python dtype |
| --- | --- | --- | --- |
| `model` | Rappresenta il modello principale caricato dal checkpoint. | `MODEL` | `torch.nn.Module` |
| `clip` | Rappresenta il modulo CLIP caricato dal checkpoint, se disponibile. | `CLIP` | `torch.nn.Module` |
| `vae` | Rappresenta il modulo VAE caricato dal checkpoint, se disponibile. | `VAE` | `torch.nn.Module` |
| `clip_vision` | Rappresenta il modulo CLIP vision caricato dal checkpoint, se disponibile. | `CLIP_VISION` | `torch.nn.Module` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UnclipCheckpointLoader/it.md)
