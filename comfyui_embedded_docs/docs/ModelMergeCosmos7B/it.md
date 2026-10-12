# ModelMergeCosmos7B

Il nodo ModelMergeCosmos7B unisce due modelli AI tramite una fusione ponderata di componenti specifici. Consente un controllo granulare su come le diverse parti dei modelli vengono combinate, regolando i pesi individuali per gli embedding di posizione, i blocchi transformer e i layer finali.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model1` | Primo modello da unire | MODEL | Sì | - |
| `model2` | Secondo modello da unire | MODEL | Sì | - |
| `pos_embedder.` | Peso per il componente di embedding della posizione (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `extra_pos_embedder.` | Peso per il componente aggiuntivo di embedding della posizione (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `x_embedder.` | Peso per il componente di embedding x (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `t_embedder.` | Peso per il componente di embedding t (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `affline_norm.` | Peso per il componente di normalizzazione affine (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.block0.` | Peso per il blocco transformer 0 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.block1.` | Peso per il blocco transformer 1 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.block2.` | Peso per il blocco transformer 2 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.block3.` | Peso per il blocco transformer 3 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.block4.` | Peso per il blocco transformer 4 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.block5.` | Peso per il blocco transformer 5 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.block6.` | Peso per il blocco transformer 6 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.block7.` | Peso per il blocco transformer 7 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.block8.` | Peso per il blocco transformer 8 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.block9.` | Peso per il blocco transformer 9 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.block10.` | Peso per il blocco transformer 10 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.block11.` | Peso per il blocco transformer 11 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.block12.` | Peso per il blocco transformer 12 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.block13.` | Peso per il blocco transformer 13 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.block14.` | Peso per il blocco transformer 14 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.block15.` | Peso per il blocco transformer 15 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.block16.` | Peso per il blocco transformer 16 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.block17.` | Peso per il blocco transformer 17 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.block18.` | Peso per il blocco transformer 18 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.block19.` | Peso per il blocco transformer 19 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.block20.` | Peso per il blocco transformer 20 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.block21.` | Peso per il blocco transformer 21 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.block22.` | Peso per il blocco transformer 22 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.block23.` | Peso per il blocco transformer 23 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.block24.` | Peso per il blocco transformer 24 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.block25.` | Peso per il blocco transformer 25 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.block26.` | Peso per il blocco transformer 26 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `blocks.block27.` | Peso per il blocco transformer 27 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `final_layer.` | Peso per il componente del layer finale (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |

Tutti i parametri di peso accettano valori da 0.0 a 1.0 con passi di 0.01 e hanno valore predefinito 1.0.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il modello unito che combina le caratteristiche di entrambi i modelli di input | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmos7B/it.md)

---
**Source fingerprint (SHA-256):** `2cc4dcaa3576c5383c630e233cef55dedc8d742c20197cc83f5832dc9e887dac`
