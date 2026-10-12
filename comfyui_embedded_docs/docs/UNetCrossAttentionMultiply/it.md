# UNetCrossAttentionMultiply

Il nodo UNetCrossAttentionMultiply applica fattori di moltiplicazione al meccanismo di cross-attention in un modello UNet. Consente di scalare le componenti query, key, value e output dei livelli di cross-attention per sperimentare comportamenti ed effetti di attenzione diversi.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello UNet da modificare con fattori di scala dell'attenzione | MODEL | Sì | - |
| `q` | Fattore di scala per le componenti query nella cross-attention (predefinito: 1.0) | FLOAT | No | 0.0 - 10.0 |
| `k` | Fattore di scala per le componenti key nella cross-attention (predefinito: 1.0) | FLOAT | No | 0.0 - 10.0 |
| `v` | Fattore di scala per le componenti value nella cross-attention (predefinito: 1.0) | FLOAT | No | 0.0 - 10.0 |
| `out` | Fattore di scala per le componenti output nella cross-attention (predefinito: 1.0) | FLOAT | No | 0.0 - 10.0 |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il modello UNet modificato con componenti di cross-attention scalate | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetCrossAttentionMultiply/it.md)

---
**Source fingerprint (SHA-256):** `f55a6809be88bfb32fa2c70fabd0e5bb7360be78670c9473d4a79517b811454e`
