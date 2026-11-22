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
| `blocco 0.` | Peso di miscelazione del blocco 0 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocco 1.` | Peso di miscelazione del blocco 1 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocco 2.` | Peso di miscelazione del blocco 2 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocco 3.` | Peso di miscelazione del blocco 3 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocco 4.` | Peso di miscelazione del blocco 4 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocco 5.` | Peso di miscelazione del blocco 5 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocco 6.` | Peso di miscelazione del blocco 6 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocco 7.` | Peso di miscelazione del blocco 7 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocco 8.` | Peso di miscelazione del blocco 8 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocco 9.` | Peso di miscelazione del blocco 9 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocco 10.` | Peso di miscelazione del blocco 10 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocco 11.` | Peso di miscelazione del blocco 11 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocco 12.` | Peso di miscelazione del blocco 12 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocco 13.` | Peso di miscelazione del blocco 13 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocco 14.` | Peso di miscelazione del blocco 14 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocco 15.` | Peso di miscelazione del blocco 15 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocco 16.` | Peso di miscelazione del blocco 16 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocco 17.` | Peso di miscelazione del blocco 17 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocco 18.` | Peso di miscelazione del blocco 18 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocco 19.` | Peso di miscelazione del blocco 19 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocco 20.` | Peso di miscelazione del blocco 20 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocco 21.` | Peso di miscelazione del blocco 21 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocco 22.` | Peso di miscelazione del blocco 22 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocco 23.` | Peso di miscelazione del blocco 23 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocco 24.` | Peso di miscelazione del blocco 24 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocco 25.` | Peso di miscelazione del blocco 25 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocco 26.` | Peso di miscelazione del blocco 26 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocco 27.` | Peso di miscelazione del blocco 27 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocco 28.` | Peso di miscelazione del blocco 28 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocco 29.` | Peso di miscelazione del blocco 29 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocco 30.` | Peso di miscelazione del blocco 30 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocco 31.` | Peso di miscelazione del blocco 31 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocco 32.` | Peso di miscelazione del blocco 32 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocco 33.` | Peso di miscelazione del blocco 33 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocco 34.` | Peso di miscelazione del blocco 34 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocco 35.` | Peso di miscelazione del blocco 35 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `final_layer.` | Peso di miscelazione dello strato finale (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |

**Nota:** Tutti i parametri di peso di miscelazione accettano valori tra 0.0 e 1.0 con incrementi di 0.01, dove 0.0 significa nessun contributo da model2 e 1.0 significa contributo completo da model2 per quello specifico componente.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il modello fuso che combina le caratteristiche di entrambi i modelli di input | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmosPredict2_14B/it.md)

---
**Source fingerprint (SHA-256):** `a5f34deda62dc03f22613517e43996b908a8673dc5da10d8f1b7f6411ece2f0a`
