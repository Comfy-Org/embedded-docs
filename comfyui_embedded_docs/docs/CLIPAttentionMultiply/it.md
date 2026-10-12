# CLIPAttentionMultiply

Il nodo CLIPAttentionMultiply consente di regolare il meccanismo di attenzione nei modelli CLIP applicando fattori moltiplicativi a diverse componenti dei livelli di self-attention. Funziona modificando i pesi e i bias delle proiezioni query, key, value e output nel meccanismo di attenzione del modello CLIP. Questo nodo sperimentale crea una copia modificata del modello CLIP di input con i fattori di scalatura specificati applicati.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `clip` | Il modello CLIP da modificare | CLIP | Sì | - |
| `q` | Fattore moltiplicativo per i pesi e i bias della proiezione query (predefinito: 1.0) | FLOAT | Sì | 0.0 - 10.0 |
| `k` | Fattore moltiplicativo per i pesi e i bias della proiezione key (predefinito: 1.0) | FLOAT | Sì | 0.0 - 10.0 |
| `v` | Fattore moltiplicativo per i pesi e i bias della proiezione value (predefinito: 1.0) | FLOAT | Sì | 0.0 - 10.0 |
| `out` | Fattore moltiplicativo per i pesi e i bias della proiezione output (predefinito: 1.0) | FLOAT | Sì | 0.0 - 10.0 |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `CLIP` | Restituisce un modello CLIP modificato con i fattori di scalatura dell'attenzione specificati applicati | CLIP |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPAttentionMultiply/it.md)

---
**Source fingerprint (SHA-256):** `1f5c437cb4a372dfd69ad3c10e2b8cfc68821e0fe82dcf37df5e6fd64aa0b436`
