# CLIPAdd

Il nodo CLIPAdd combina due modelli CLIP unendo le rispettive key patch. Crea una copia del primo modello CLIP e poi aggiunge la maggior parte delle key patch del secondo modello, escludendo gli ID di posizione e i parametri di scala logit. Ciò consente di fondere le caratteristiche di modelli CLIP diversi preservando la struttura del primo modello.

## Input

| Parametro | Descrizione | Tipo di dato | Tipo di input | Predefinito | Intervallo |
| --- | --- | --- | --- | --- | --- |
| `clip1` | Il modello CLIP principale che verrà utilizzato come base per l'unione | CLIP | Obbligatorio | - | - |
| `clip2` | Il modello CLIP secondario che fornisce patch aggiuntive da aggiungere | CLIP | Obbligatorio | - | - |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `CLIP` | Restituisce un modello CLIP unito che combina le caratteristiche di entrambi i modelli di input | CLIP |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPAdd/it.md)

---
**Source fingerprint (SHA-256):** `935d450d25d90dc623e3f2b39b251359a9066c9e1fdd2a70384982fb26a21864`
