# DeprecatedCheckpointLoader

Il nodo CheckpointLoader è progettato per operazioni di caricamento avanzate, in particolare per caricare i checkpoint dei modelli insieme alle relative configurazioni. Facilita il recupero dei componenti del modello necessari per inizializzare ed eseguire modelli generativi, incluse configurazioni e checkpoint dalle directory specificate.

## Input

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `config_name` | Specifica il nome del file di configurazione da utilizzare. Questo è cruciale per determinare i parametri e le impostazioni del modello, influenzandone il comportamento e le prestazioni. | COMBO[STRING] |
| `ckpt_name` | Indica il nome del file di checkpoint da caricare. Questo influenza direttamente lo stato del modello inizializzato, incidendo sui suoi pesi e bias iniziali. | COMBO[STRING] |

## Output

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `model` | Rappresenta il modello principale caricato dal checkpoint, pronto per ulteriori operazioni o inferenza. | MODEL |
| `clip` | Fornisce il componente modello CLIP, se disponibile e richiesto, caricato dal checkpoint. | CLIP |
| `vae` | Fornisce il componente modello VAE, se disponibile e richiesto, caricato dal checkpoint. | VAE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DeprecatedCheckpointLoader/it.md)
