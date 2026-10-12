# DeprecatedDiffusersLoader

Il nodo DiffusersLoader è progettato per caricare modelli dalla libreria diffusers, gestendo specificamente il caricamento di modelli UNet, CLIP e VAE in base ai percorsi dei modelli forniti. Facilita l'integrazione di questi modelli nel framework ComfyUI, abilitando funzionalità avanzate come la generazione testo-immagine, la manipolazione delle immagini e altro ancora.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model_path` | Specifica il percorso del modello da caricare. Questo percorso è cruciale poiché determina quale modello verrà utilizzato per le operazioni successive, influenzando l'output e le capacità del nodo. | COMBO[STRING] |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il modello UNet caricato, che fa parte della tupla di output. Questo modello è essenziale per le attività di sintesi e manipolazione delle immagini all'interno del framework ComfyUI. | MODEL |
| `clip` | Il modello CLIP caricato, incluso nella tupla di output se richiesto. Questo modello abilita capacità avanzate di comprensione e manipolazione di testo e immagini. | CLIP |
| `vae` | Il modello VAE caricato, incluso nella tupla di output se richiesto. Questo modello è cruciale per le attività che comportano la manipolazione dello spazio latente e la generazione di immagini. | VAE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DeprecatedDiffusersLoader/it.md)
