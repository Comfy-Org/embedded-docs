# ModelMergeSD3_2B

Il nodo ModelMergeSD3_2B consente di unire due modelli Stable Diffusion 3 2B fondendo i loro componenti con pesi regolabili. Offre controllo individuale su livelli di embedding, blocchi transformer e livello finale, consentendo combinazioni finemente calibrate dei due modelli.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model1` | Il primo modello da unire | MODEL | Sì | - |
| `model2` | Il secondo modello da unire | MODEL | Sì | - |
| `pos_embed.` | Peso di interpolazione dell'embedding di posizione (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `x_embedder.` | Peso di interpolazione dell'embedding di input (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `context_embedder.` | Peso di interpolazione dell'embedding di contesto (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `y_embedder.` | Peso di interpolazione dell'embedding Y (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `t_embedder.` | Peso di interpolazione dell'embedding temporale (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `joint_blocks.0.` | Peso di interpolazione del blocco congiunto 0 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `joint_blocks.1.` | Peso di interpolazione del blocco congiunto 1 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `joint_blocks.2.` | Peso di interpolazione del blocco congiunto 2 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `joint_blocks.3.` | Peso di interpolazione del blocco congiunto 3 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `joint_blocks.4.` | Peso di interpolazione del blocco congiunto 4 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `joint_blocks.5.` | Peso di interpolazione del blocco congiunto 5 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `joint_blocks.6.` | Peso di interpolazione del blocco congiunto 6 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `joint_blocks.7.` | Peso di interpolazione del blocco congiunto 7 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `joint_blocks.8.` | Peso di interpolazione del blocco congiunto 8 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `joint_blocks.9.` | Peso di interpolazione del blocco congiunto 9 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `joint_blocks.10.` | Peso di interpolazione del blocco congiunto 10 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `joint_blocks.11.` | Peso di interpolazione del blocco congiunto 11 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `joint_blocks.12.` | Peso di interpolazione del blocco congiunto 12 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `joint_blocks.13.` | Peso di interpolazione del blocco congiunto 13 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `joint_blocks.14.` | Peso di interpolazione del blocco congiunto 14 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `joint_blocks.15.` | Peso di interpolazione del blocco congiunto 15 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `joint_blocks.16.` | Peso di interpolazione del blocco congiunto 16 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `joint_blocks.17.` | Peso di interpolazione del blocco congiunto 17 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `joint_blocks.18.` | Peso di interpolazione del blocco congiunto 18 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `joint_blocks.19.` | Peso di interpolazione del blocco congiunto 19 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `joint_blocks.20.` | Peso di interpolazione del blocco congiunto 20 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `joint_blocks.21.` | Peso di interpolazione del blocco congiunto 21 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `joint_blocks.22.` | Peso di interpolazione del blocco congiunto 22 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `joint_blocks.23.` | Peso di interpolazione del blocco congiunto 23 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `final_layer.` | Peso di interpolazione del livello finale (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `model` | Il modello unito che combina le caratteristiche di entrambi i modelli di input | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD3_2B/it.md)

---
**Source fingerprint (SHA-256):** `db27b10ade457933f6225218bb806aafcf9fc4478cac85b1623a75d110103529`
