# ModelMergeSD35_Large

Il nodo ModelMergeSD35_Large unisce due modelli Stable Diffusion 3.5 Large miscelando componenti interni specifici del secondo modello nel primo. Ogni componente ha un valore di miscelazione indipendente, offrendo un controllo granulare su quanto fortemente quel componente contribuisce al modello risultante dalla fusione.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model1` | Il modello di base che funge da fondamento per la fusione | MODEL | Sì | - |
| `model2` | Il modello secondario i cui componenti vengono miscelati nel modello di base | MODEL | Sì | - |
| `pos_embed.` | Controlla quanto dell'embedding di posizione di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `x_embedder.` | Controlla quanto dell'embedder x di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `context_embedder.` | Controlla quanto dell'embedder del contesto di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `y_embedder.` | Controlla quanto dell'embedder y di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `t_embedder.` | Controlla quanto dell'embedder t di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.0.` | Controlla quanto del blocco joint 0 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.1.` | Controlla quanto del blocco joint 1 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.2.` | Controlla quanto del blocco joint 2 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.3.` | Controlla quanto del blocco joint 3 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.4.` | Controlla quanto del blocco joint 4 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.5.` | Controlla quanto del blocco joint 5 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.6.` | Controlla quanto del blocco joint 6 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.7.` | Controlla quanto del blocco joint 7 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.8.` | Controlla quanto del blocco joint 8 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.9.` | Controlla quanto del blocco joint 9 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.10.` | Controlla quanto del blocco joint 10 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.11.` | Controlla quanto del blocco joint 11 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.12.` | Controlla quanto del blocco joint 12 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.13.` | Controlla quanto del blocco joint 13 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.14.` | Controlla quanto del blocco joint 14 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.15.` | Controlla quanto del blocco joint 15 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.16.` | Controlla quanto del blocco joint 16 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.17.` | Controlla quanto del blocco joint 17 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.18.` | Controlla quanto del blocco joint 18 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.19.` | Controlla quanto del blocco joint 19 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.20.` | Controlla quanto del blocco joint 20 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.21.` | Controlla quanto del blocco joint 21 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.22.` | Controlla quanto del blocco joint 22 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.23.` | Controlla quanto del blocco joint 23 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.24.` | Controlla quanto del blocco joint 24 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.25.` | Controlla quanto del blocco joint 25 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.26.` | Controlla quanto del blocco joint 26 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.27.` | Controlla quanto del blocco joint 27 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.28.` | Controlla quanto del blocco joint 28 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.29.` | Controlla quanto del blocco joint 29 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.30.` | Controlla quanto del blocco joint 30 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.31.` | Controlla quanto del blocco joint 31 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.32.` | Controlla quanto del blocco joint 32 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.33.` | Controlla quanto del blocco joint 33 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.34.` | Controlla quanto del blocco joint 34 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.35.` | Controlla quanto del blocco joint 35 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.36.` | Controlla quanto del blocco joint 36 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `joint_blocks.37.` | Controlla quanto del blocco joint 37 di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `final_layer.` | Controlla quanto del layer finale di model2 viene miscelato nel modello risultante dalla fusione (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |

**Nota:** Tutti i parametri di miscelazione accettano valori da 0.0 a 1.0 con un passo di 0.01. Un valore di 0.0 significa nessun contributo da model2, mentre un valore di 1.0 significa contributo completo da model2 per quello specifico componente.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il modello risultante dalla fusione che combina le caratteristiche di entrambi i modelli di input in base ai parametri di miscelazione specificati | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD35_Large/it.md)

---
**Source fingerprint (SHA-256):** `c489c710e18d01adcf4320d9c010ed587ca5e12babb468448f56d79acdc40f6c`
