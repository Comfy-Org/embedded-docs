# UNetTemporalAttentionMultiply

Il nodo UNetTemporalAttentionMultiply applica fattori moltiplicativi a diversi tipi di meccanismi di attenzione in un modello UNet temporale. Modifica il modello regolando i pesi dei livelli di auto-attenzione e attenzione incrociata, distinguendo tra componenti strutturali e temporali. Ciò consente di ottimizzare quanto ciascun tipo di attenzione influenzi l'output del modello.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello di input da modificare con i moltiplicatori di attenzione | MODEL | Sì | - |
| `self_structural` | Moltiplicatore per le componenti strutturali dell'auto-attenzione (predefinito: 1.0) | FLOAT | No | 0.0 - 10.0 |
| `self_temporal` | Moltiplicatore per le componenti temporali dell'auto-attenzione (predefinito: 1.0) | FLOAT | No | 0.0 - 10.0 |
| `cross_structural` | Moltiplicatore per le componenti strutturali dell'attenzione incrociata (predefinito: 1.0) | FLOAT | No | 0.0 - 10.0 |
| `cross_temporal` | Moltiplicatore per le componenti temporali dell'attenzione incrociata (predefinito: 1.0) | FLOAT | No | 0.0 - 10.0 |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `model` | Il modello modificato con i pesi di attenzione regolati | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UNetTemporalAttentionMultiply/it.md)

---
**Source fingerprint (SHA-256):** `b43c7c51cbc71349dd267c4abe1704899a394e205a60a13b45869f690d83a0f0`
