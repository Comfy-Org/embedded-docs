# CLIPMergeAdd

Il nodo CLIPMergeAdd combina due modelli CLIP aggiungendo patch dal secondo modello al primo. Crea una copia del primo modello CLIP e incorpora selettivamente patch chiave dal secondo modello, escludendo gli ID di posizione e i parametri di scala logit. Ciò consente di unire i componenti dei modelli CLIP preservando la struttura del modello di base.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `clip1` | Il modello CLIP di base che verrà clonato e utilizzato come fondamento per l'unione | CLIP | Sì | - |
| `clip2` | Il modello CLIP secondario che fornisce le patch chiave da aggiungere al modello di base | CLIP | Sì | - |

Le chiavi che terminano con `.position_ids` o `.logit_scale` in `clip2` vengono ignorate, quindi quei parametri mantengono i valori da `clip1`.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `CLIP` | Un modello CLIP unito contenente la struttura del modello di base con le patch aggiunte dal modello secondario | CLIP |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeAdd/it.md)

---
**Source fingerprint (SHA-256):** `e6271ea9139598eb580f79ce63ff5d92307d7ed93f57cdc666c5e022b671a0dd`
