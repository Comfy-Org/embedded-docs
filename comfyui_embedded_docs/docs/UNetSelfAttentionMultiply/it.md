# UNetSelfAttentionMultiply

Il nodo UNetSelfAttentionMultiply applica fattori di moltiplicazione ai componenti query, key, value e output del meccanismo di auto-attenzione in un modello UNet. Consente di scalare diverse parti del calcolo dell'attenzione per sperimentare come i pesi di attenzione influenzano il comportamento del modello.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello UNet da modificare con fattori di scala dell'attenzione | MODEL | Sì | - |
| `q` | Fattore di moltiplicazione per il componente query (predefinito: 1.0) | FLOAT | No | 0.0 - 10.0 |
| `k` | Fattore di moltiplicazione per il componente key (predefinito: 1.0) | FLOAT | No | 0.0 - 10.0 |
| `v` | Fattore di moltiplicazione per il componente value (predefinito: 1.0) | FLOAT | No | 0.0 - 10.0 |
| `out` | Fattore di moltiplicazione per il componente di output (predefinito: 1.0) | FLOAT | No | 0.0 - 10.0 |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `MODEL` | Il modello UNet modificato con i componenti di attenzione scalati | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetSelfAttentionMultiply/it.md)

---
**Source fingerprint (SHA-256):** `7a6039eb2faae56437a5eb6fe01be6d38e53c0632175a3405a1e24a476d4da82`
