# ModelMergeCosmosPredict2_2B

Il nodo ModelMergeCosmosPredict2_2B unisce due modelli di diffusione utilizzando un approccio basato su blocchi, con controllo granulare sui diversi componenti del modello. Consente di fondere parti specifiche di due modelli regolando i pesi di interpolazione per embedder di posizione, embedder temporali, blocchi Transformer e layer finali. Ciò fornisce un controllo preciso su come i diversi componenti architetturali di ciascun modello contribuiscono al risultato finale unito.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model1` | Il primo modello da unire | MODEL | Sì | - |
| `model2` | Il secondo modello da unire | MODEL | Sì | - |
| `pos_embedder.` | Peso di interpolazione dell'embedder di posizione (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `x_embedder.` | Peso di interpolazione dell'embedder di input (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `t_embedder.` | Peso di interpolazione dell'embedder temporale (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `t_embedding_norm.` | Peso di interpolazione della normalizzazione dell'embedding temporale (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.0.` | Peso di interpolazione del blocco Transformer 0 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.1.` | Peso di interpolazione del blocco Transformer 1 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.2.` | Peso di interpolazione del blocco Transformer 2 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.3.` | Peso di interpolazione del blocco Transformer 3 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.4.` | Peso di interpolazione del blocco Transformer 4 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.5.` | Peso di interpolazione del blocco Transformer 5 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.6.` | Peso di interpolazione del blocco Transformer 6 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.7.` | Peso di interpolazione del blocco Transformer 7 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.8.` | Peso di interpolazione del blocco Transformer 8 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.9.` | Peso di interpolazione del blocco Transformer 9 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.10.` | Peso di interpolazione del blocco Transformer 10 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.11.` | Peso di interpolazione del blocco Transformer 11 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.12.` | Peso di interpolazione del blocco Transformer 12 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.13.` | Peso di interpolazione del blocco Transformer 13 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.14.` | Peso di interpolazione del blocco Transformer 14 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.15.` | Peso di interpolazione del blocco Transformer 15 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.16.` | Peso di interpolazione del blocco Transformer 16 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.17.` | Peso di interpolazione del blocco Transformer 17 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.18.` | Peso di interpolazione del blocco Transformer 18 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.19.` | Peso di interpolazione del blocco Transformer 19 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.20.` | Peso di interpolazione del blocco Transformer 20 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.21.` | Peso di interpolazione del blocco Transformer 21 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.22.` | Peso di interpolazione del blocco Transformer 22 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.23.` | Peso di interpolazione del blocco Transformer 23 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.24.` | Peso di interpolazione del blocco Transformer 24 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.25.` | Peso di interpolazione del blocco Transformer 25 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.26.` | Peso di interpolazione del blocco Transformer 26 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.27.` | Peso di interpolazione del blocco Transformer 27 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `final_layer.` | Peso di interpolazione del layer finale (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `model` | Il modello unito che combina le caratteristiche di entrambi i modelli di input | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmosPredict2_2B/it.md)

---
**Source fingerprint (SHA-256):** `3586868201320ae9a326a08f6a9bd74511a5342bf8496e7efcb9f45cf4b7c55d`
