# ModelMergeCosmos14B

Il nodo **ModelMergeCosmos14B** unisce due modelli AI usando un approccio basato su blocchi progettato specificamente per l'architettura del modello Cosmos 14B. Consente di fondere diversi componenti dei modelli regolando i valori di peso tra 0.0 e 1.0 per ciascun blocco del modello e livello di embedding.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model1` | Primo modello da unire | MODEL | Sì | - |
| `model2` | Secondo modello da unire | MODEL | Sì | - |
| `pos_embedder.` | Peso per il componente position embedder (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `extra_pos_embedder.` | Peso per il componente extra position embedder (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `x_embedder.` | Peso per il componente x embedder (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `t_embedder.` | Peso per il componente t embedder (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `affline_norm.` | Peso per il componente di normalizzazione affine (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `blocks.block0.` | Peso per il blocco 0 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `blocks.block1.` | Peso per il blocco 1 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `blocks.block2.` | Peso per il blocco 2 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `blocks.block3.` | Peso per il blocco 3 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `blocks.block4.` | Peso per il blocco 4 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `blocks.block5.` | Peso per il blocco 5 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `blocks.block6.` | Peso per il blocco 6 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `blocks.block7.` | Peso per il blocco 7 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `blocks.block8.` | Peso per il blocco 8 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `blocks.block9.` | Peso per il blocco 9 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `blocks.block10.` | Peso per il blocco 10 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `blocks.block11.` | Peso per il blocco 11 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `blocks.block12.` | Peso per il blocco 12 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `blocks.block13.` | Peso per il blocco 13 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `blocks.block14.` | Peso per il blocco 14 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `blocks.block15.` | Peso per il blocco 15 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `blocks.block16.` | Peso per il blocco 16 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `blocks.block17.` | Peso per il blocco 17 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `blocks.block18.` | Peso per il blocco 18 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `blocks.block19.` | Peso per il blocco 19 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `blocks.block20.` | Peso per il blocco 20 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `blocks.block21.` | Peso per il blocco 21 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `blocks.block22.` | Peso per il blocco 22 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `blocks.block23.` | Peso per il blocco 23 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `blocks.block24.` | Peso per il blocco 24 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `blocks.block25.` | Peso per il blocco 25 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `blocks.block26.` | Peso per il blocco 26 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `blocks.block27.` | Peso per il blocco 27 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `blocks.block28.` | Peso per il blocco 28 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `blocks.block29.` | Peso per il blocco 29 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `blocks.block30.` | Peso per il blocco 30 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `blocks.block31.` | Peso per il blocco 31 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `blocks.block32.` | Peso per il blocco 32 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `blocks.block33.` | Peso per il blocco 33 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `blocks.block34.` | Peso per il blocco 34 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `blocks.block35.` | Peso per il blocco 35 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |
| `final_layer.` | Peso per il layer finale (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (step: 0.01) |

Tutti i parametri di peso accettano valori da 0.0 a 1.0 con incrementi di 0.01 e ognuno di essi ha valore predefinito 1.0. I parametri dei blocchi coprono 36 blocchi transformer, numerati da `blocks.block0.` a `blocks.block35.`.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `model` | Il modello unito che combina le caratteristiche di entrambi i modelli di input | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmos14B/it.md)

---
**Source fingerprint (SHA-256):** `1d1e5dc176643f577723bb0bb9375748a392a6fafa5c9e5e78ef4c4d8289f77c`
