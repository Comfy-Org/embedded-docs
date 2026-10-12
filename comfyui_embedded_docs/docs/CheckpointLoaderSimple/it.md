# Carica Checkpoint

Carica un file checkpoint di modello diffusion e lo suddivide in tre componenti principali: il modello principale usato per il denoising dei latenti, l'encoder di testo CLIP e l'encoder/decoder di immagini VAE. Il nodo rileva automaticamente tutti i file di modello nella cartella `ComfyUI/models/checkpoints` e in eventuali percorsi aggiuntivi configurati nel file `extra_model_paths.yaml`.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `ckpt_name` | Il nome del checkpoint (modello) da caricare. Seleziona il nome del file del modello checkpoint, che determina il modello AI usato per la successiva generazione di immagini. | COMBO | Sì | Tutti i file di modello trovati nella cartella dei checkpoint |

**Nota:** Se vengono aggiunti nuovi file di modello mentre ComfyUI è in esecuzione, è necessario aggiornare il browser (Ctrl+R) per visualizzare i nuovi file nell'elenco a discesa.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `MODEL` | Il modello usato per il denoising dei latenti. Questo è il modello di diffusione principale usato per la generazione di immagini. | MODEL |
| `CLIP` | Il modello CLIP usato per codificare i prompt testuali, convertendo le descrizioni testuali in informazioni che l'IA può comprendere. | CLIP |
| `VAE` | Il modello VAE usato per codificare e decodificare immagini da e verso lo spazio latente. | VAE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoaderSimple/it.md)

---
**Source fingerprint (SHA-256):** `db99a8ba83a586491463df0d4e99ba5f77d4511c6d8337a721d76edd3450f310`
