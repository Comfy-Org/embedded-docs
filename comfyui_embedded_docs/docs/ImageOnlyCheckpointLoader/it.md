# ImageOnlyCheckpointLoader

Questo nodo rileva i modelli situati nella cartella `ComfyUI/models/checkpoints` e legge anche i modelli da percorsi aggiuntivi configurati nel file extra_model_paths.yaml. A volte potrebbe essere necessario **aggiornare l'interfaccia di ComfyUI** per consentirle di leggere i file dei modelli dalla cartella corrispondente.

Questo nodo è specializzato nel caricamento di checkpoint specificamente per modelli basati su immagini all'interno di flussi di lavoro di generazione video. Recupera e configura in modo efficiente i componenti necessari da un determinato checkpoint, concentrandosi sugli aspetti del modello relativi alle immagini.

## Input

| Campo | Descrizione | Tipo di dato |
| --- | --- | --- |
| `ckpt_name` | Specifica il nome del checkpoint da caricare, fondamentale per identificare e recuperare il file di checkpoint corretto da un elenco predefinito. | COMBO[STRING] |

## Output

| Campo | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Restituisce il modello principale caricato dal checkpoint, configurato per l'elaborazione delle immagini in contesti di generazione video. | MODEL |
| `clip_vision` | Fornisce il componente CLIP vision dal checkpoint, adattato alla comprensione delle immagini e all'estrazione di feature. | `CLIP_VISION` |
| `vae` | Fornisce il componente Variational Autoencoder (VAE), essenziale per le attività di manipolazione e generazione delle immagini. | VAE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageOnlyCheckpointLoader/it.md)
