# ModelMergeCosmosPredict2_14B

Il nodo ModelMergeCosmosPredict2_14B combina due modelli AI in un unico modello fondendo i loro componenti interni corrispondenti. Consente di controllare quanto del secondo modello viene miscelato nel primo regolando un peso separato per ciascun embedder, blocco e strato finale.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model1` | Il modello di base con cui eseguire la fusione | MODEL | Sì | - |
| `model2` | Il modello secondario da fondere nel modello di base | MODEL | Sì | - |
| `pos_embedder.` | Peso di miscelazione dell'embedder di posizione (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `x_embedder.` | Peso di miscelazione dell'embedder di input (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `t_embedder.` | Peso di miscelazione dell'embedder temporale (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `t_embedding_norm.` | Peso di miscelazione della normalizzazione dell'embedding temporale (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.0.` | Peso di miscelazione del blocco 0 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.1.` | Peso di miscelazione del blocco 1 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.2.` | Peso di miscelazione del blocco 2 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.3.` | Peso di miscelazione del blocco 3 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.4.` | Peso di miscelazione del blocco 4 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.5.` | Peso di miscelazione del blocco 5 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.6.` | Peso di miscelazione del blocco 6 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.7.` | Peso di miscelazione del blocco 7 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.8.` | Peso di miscelazione del blocco 8 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.9.` | Peso di miscelazione del blocco 9 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.10.` | Peso di miscelazione del blocco 10 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.11.` | Peso di miscelazione del blocco 11 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.12.` | Peso di miscelazione del blocco 12 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.13.` | Peso di miscelazione del blocco 13 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.14.` | Peso di miscelazione del blocco 14 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.15.` | Peso di miscelazione del blocco 15 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.16.` | Peso di miscelazione del blocco 16 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.17.` | Peso di miscelazione del blocco 17 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.18.` | Peso di miscelazione del blocco 18 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.19.` | Peso di miscelazione del blocco 19 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.20.` | Peso di miscelazione del blocco 20 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.21.` | Peso di miscelazione del blocco 21 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.22.` | Peso di miscelazione del blocco 22 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.23.` | Peso di miscelazione del blocco 23 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.24.` | Peso di miscelazione del blocco 24 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.25.` | Peso di miscelazione del blocco 25 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.26.` | Peso di miscelazione del blocco 26 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.27.` | Peso di miscelazione del blocco 27 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.28.` | Peso di miscelazione del blocco 28 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.29.` | Peso di miscelazione del blocco 29 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.30.` | Peso di miscelazione del blocco 30 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.31.` | Peso di miscelazione del blocco 31 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.32.` | Peso di miscelazione del blocco 32 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.33.` | Peso di miscelazione del blocco 33 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.34.` | Peso di miscelazione del blocco 34 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.35.` | Peso di miscelazione del blocco 35 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `final_layer.` | Peso di miscelazione dello strato finale (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |

**Nota:** Tutti i parametri di peso di miscelazione accettano valori tra 0.0 e 1.0 con incrementi di 0.01, dove 0.0 significa nessun contributo da model2 e 1.0 significa contributo completo da model2 per quello specifico componente.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il modello fuso che combina le caratteristiche di entrambi i modelli di input | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmosPredict2_14B/it.md)

---
**Source fingerprint (SHA-256):** `a5f34deda62dc03f22613517e43996b908a8673dc5da10d8f1b7f6411ece2f0a`
