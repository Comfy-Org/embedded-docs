# ModelMergeMochiPreview

Questo nodo unisce due modelli Mochi AI utilizzando un approccio basato su blocchi con controllo granulare sui diversi componenti del modello. Consente di fondere i modelli regolando i pesi di interpolazione per sezioni specifiche, incluse le frequenze posizionali, gli strati di embedding e ciascuno dei 48 blocchi transformer individuali. Il processo di unione combina le architetture e i parametri di entrambi i modelli di input in base ai valori dei pesi specificati.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model1` | Il primo modello da unire | MODEL | Sì | - |
| `model2` | Il secondo modello da unire | MODEL | Sì | - |
| `pos_frequencies.` | Peso per l'interpolazione delle frequenze posizionali (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `t_embedder.` | Peso per l'interpolazione dell'embedder temporale (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `t5_y_embedder.` | Peso per l'interpolazione dell'embedder T5-Y (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `t5_yproj.` | Peso per l'interpolazione della proiezione T5-Y (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.0.` | Peso per l'interpolazione del blocco 0 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.1.` | Peso per l'interpolazione del blocco 1 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.2.` | Peso per l'interpolazione del blocco 2 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.3.` | Peso per l'interpolazione del blocco 3 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.4.` | Peso per l'interpolazione del blocco 4 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.5.` | Peso per l'interpolazione del blocco 5 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.6.` | Peso per l'interpolazione del blocco 6 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.7.` | Peso per l'interpolazione del blocco 7 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.8.` | Peso per l'interpolazione del blocco 8 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.9.` | Peso per l'interpolazione del blocco 9 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.10.` | Peso per l'interpolazione del blocco 10 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.11.` | Peso per l'interpolazione del blocco 11 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.12.` | Peso per l'interpolazione del blocco 12 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.13.` | Peso per l'interpolazione del blocco 13 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.14.` | Peso per l'interpolazione del blocco 14 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.15.` | Peso per l'interpolazione del blocco 15 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.16.` | Peso per l'interpolazione del blocco 16 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.17.` | Peso per l'interpolazione del blocco 17 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.18.` | Peso per l'interpolazione del blocco 18 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.19.` | Peso per l'interpolazione del blocco 19 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.20.` | Peso per l'interpolazione del blocco 20 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.21.` | Peso per l'interpolazione del blocco 21 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.22.` | Peso per l'interpolazione del blocco 22 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.23.` | Peso per l'interpolazione del blocco 23 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.24.` | Peso per l'interpolazione del blocco 24 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.25.` | Peso per l'interpolazione del blocco 25 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.26.` | Peso per l'interpolazione del blocco 26 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.27.` | Peso per l'interpolazione del blocco 27 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.28.` | Peso per l'interpolazione del blocco 28 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.29.` | Peso per l'interpolazione del blocco 29 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.30.` | Peso per l'interpolazione del blocco 30 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.31.` | Peso per l'interpolazione del blocco 31 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.32.` | Peso per l'interpolazione del blocco 32 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.33.` | Peso per l'interpolazione del blocco 33 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.34.` | Peso per l'interpolazione del blocco 34 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.35.` | Peso per l'interpolazione del blocco 35 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.36.` | Peso per l'interpolazione del blocco 36 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.37.` | Peso per l'interpolazione del blocco 37 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.38.` | Peso per l'interpolazione del blocco 38 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.39.` | Peso per l'interpolazione del blocco 39 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.40.` | Peso per l'interpolazione del blocco 40 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.41.` | Peso per l'interpolazione del blocco 41 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.42.` | Peso per l'interpolazione del blocco 42 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.43.` | Peso per l'interpolazione del blocco 43 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.44.` | Peso per l'interpolazione del blocco 44 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.45.` | Peso per l'interpolazione del blocco 45 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.46.` | Peso per l'interpolazione del blocco 46 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `blocks.47.` | Peso per l'interpolazione del blocco 47 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `final_layer.` | Peso per l'interpolazione dello strato finale (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `model` | Il modello unito che combina le caratteristiche di entrambi i modelli di input in base ai pesi specificati | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeMochiPreview/it.md)

---
**Source fingerprint (SHA-256):** `8fdf5d023d97ef04bf2b40577be5dbc4c16f8f4437586a98adbdbf7f9fa8a359`
