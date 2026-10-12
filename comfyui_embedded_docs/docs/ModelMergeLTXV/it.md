# ModelMergeLTXV

Il nodo ModelMergeLTXV unisce due modelli LTXV fondendo i loro componenti corrispondenti. Ogni parte del modello — come i blocchi transformer, i layer di proiezione e la tabella scale shift — può essere fusa separatamente con il proprio peso, offrendo un controllo granulare su come i due modelli vengono combinati.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model1` | Il primo modello da unire | MODEL | Sì | - |
| `model2` | Il secondo modello da unire | MODEL | Sì | - |
| `patchify_proj.` | Peso di interpolazione per i layer di proiezione patchify (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `adaln_single.` | Peso di interpolazione per i layer singoli di normalizzazione adattiva (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `caption_projection.` | Peso di interpolazione per i layer di proiezione delle didascalie (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `transformer_blocks.0.` | Peso di interpolazione per il blocco transformer 0 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `transformer_blocks.1.` | Peso di interpolazione per il blocco transformer 1 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `transformer_blocks.2.` | Peso di interpolazione per il blocco transformer 2 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `transformer_blocks.3.` | Peso di interpolazione per il blocco transformer 3 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `transformer_blocks.4.` | Peso di interpolazione per il blocco transformer 4 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `transformer_blocks.5.` | Peso di interpolazione per il blocco transformer 5 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `transformer_blocks.6.` | Peso di interpolazione per il blocco transformer 6 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `transformer_blocks.7.` | Peso di interpolazione per il blocco transformer 7 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `transformer_blocks.8.` | Peso di interpolazione per il blocco transformer 8 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `transformer_blocks.9.` | Peso di interpolazione per il blocco transformer 9 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `transformer_blocks.10.` | Peso di interpolazione per il blocco transformer 10 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `transformer_blocks.11.` | Peso di interpolazione per il blocco transformer 11 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `transformer_blocks.12.` | Peso di interpolazione per il blocco transformer 12 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `transformer_blocks.13.` | Peso di interpolazione per il blocco transformer 13 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `transformer_blocks.14.` | Peso di interpolazione per il blocco transformer 14 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `transformer_blocks.15.` | Peso di interpolazione per il blocco transformer 15 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `transformer_blocks.16.` | Peso di interpolazione per il blocco transformer 16 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `transformer_blocks.17.` | Peso di interpolazione per il blocco transformer 17 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `transformer_blocks.18.` | Peso di interpolazione per il blocco transformer 18 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `transformer_blocks.19.` | Peso di interpolazione per il blocco transformer 19 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `transformer_blocks.20.` | Peso di interpolazione per il blocco transformer 20 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `transformer_blocks.21.` | Peso di interpolazione per il blocco transformer 21 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `transformer_blocks.22.` | Peso di interpolazione per il blocco transformer 22 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `transformer_blocks.23.` | Peso di interpolazione per il blocco transformer 23 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `transformer_blocks.24.` | Peso di interpolazione per il blocco transformer 24 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `transformer_blocks.25.` | Peso di interpolazione per il blocco transformer 25 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `transformer_blocks.26.` | Peso di interpolazione per il blocco transformer 26 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `transformer_blocks.27.` | Peso di interpolazione per il blocco transformer 27 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `scale_shift_table` | Peso di interpolazione per la tabella scale shift (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `proj_out.` | Peso di interpolazione per i layer di proiezione dell'output (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il modello unito che combina le caratteristiche di entrambi i modelli di input in base ai pesi di interpolazione specificati | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeLTXV/it.md)

---
**Source fingerprint (SHA-256):** `0ff5f93aee831259066679a27fff8f7cbd4a9686242091f1bc7dd3805725566e`
