# DualClipLoader

Il nodo DualCLIPLoader è progettato per caricare due modelli CLIP contemporaneamente, facilitando operazioni che richiedono l'integrazione o il confronto delle caratteristiche di entrambi i modelli.

Questo nodo rileva i modelli situati nella cartella `ComfyUI/models/text_encoders`.

## Input

| Parametro | Descrizione | Tipo di dato Comfy |
| --- | --- | --- |
| `clip_name1` | Specifica il nome del primo modello CLIP da caricare. Questo parametro è cruciale per identificare e recuperare il modello corretto da un elenco predefinito di modelli CLIP disponibili. | COMBO[STRING] |
| `clip_name2` | Specifica il nome del secondo modello CLIP da caricare. Questo parametro consente di caricare un secondo modello CLIP distinto per un'analisi comparativa o integrativa insieme al primo modello. | COMBO[STRING] |
| `type` | Scegli tra "sdxl", "sd3", "flux" per adattarsi a modelli diversi. | `option` |

* L'ordine di caricamento non influisce sul risultato di output

## Output

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `clip` | L'output è un modello CLIP combinato che integra le caratteristiche o le funzionalità dei due modelli CLIP specificati. | CLIP |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualCLIPLoader/it.md)
