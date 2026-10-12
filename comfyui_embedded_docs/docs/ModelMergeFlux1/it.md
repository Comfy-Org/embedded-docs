# ModelMergeFlux1

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model1` | Primo modello sorgente da unire | MODEL | Sì | - |
| `model2` | Secondo modello sorgente da unire | MODEL | Sì | - |
| `img_in.` | Peso di interpolazione per l'input immagine (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `time_in.` | Peso di interpolazione per l'embedding temporale (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `guidance_in` | Peso di interpolazione per il meccanismo di guida (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `vector_in.` | Peso di interpolazione per l'input vettoriale (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `txt_in.` | Peso di interpolazione per il codificatore di testo (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `double_blocks.0.` | Peso di interpolazione per il blocco doppio 0 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `double_blocks.1.` | Peso di interpolazione per il blocco doppio 1 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `double_blocks.2.` | Peso di interpolazione per il blocco doppio 2 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `double_blocks.3.` | Peso di interpolazione per il blocco doppio 3 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `double_blocks.4.` | Peso di interpolazione per il blocco doppio 4 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `double_blocks.5.` | Peso di interpolazione per il blocco doppio 5 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `double_blocks.6.` | Peso di interpolazione per il blocco doppio 6 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `double_blocks.7.` | Peso di interpolazione per il blocco doppio 7 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `double_blocks.8.` | Peso di interpolazione per il blocco doppio 8 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `double_blocks.9.` | Peso di interpolazione per il blocco doppio 9 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `double_blocks.10.` | Peso di interpolazione per il blocco doppio 10 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `double_blocks.11.` | Peso di interpolazione per il blocco doppio 11 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `double_blocks.12.` | Peso di interpolazione per il blocco doppio 12 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `double_blocks.13.` | Peso di interpolazione per il blocco doppio 13 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `double_blocks.14.` | Peso di interpolazione per il blocco doppio 14 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `double_blocks.15.` | Peso di interpolazione per il blocco doppio 15 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `double_blocks.16.` | Peso di interpolazione per il blocco doppio 16 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `double_blocks.17.` | Peso di interpolazione per il blocco doppio 17 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `double_blocks.18.` | Peso di interpolazione per il blocco doppio 18 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.0.` | Peso di interpolazione per il blocco singolo 0 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.1.` | Peso di interpolazione per il blocco singolo 1 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.2.` | Peso di interpolazione per il blocco singolo 2 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.3.` | Peso di interpolazione per il blocco singolo 3 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.4.` | Peso di interpolazione per il blocco singolo 4 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.5.` | Peso di interpolazione per il blocco singolo 5 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.6.` | Peso di interpolazione per il blocco singolo 6 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.7.` | Peso di interpolazione per il blocco singolo 7 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.8.` | Peso di interpolazione per il blocco singolo 8 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.9.` | Peso di interpolazione per il blocco singolo 9 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.10.` | Peso di interpolazione per il blocco singolo 10 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.11.` | Peso di interpolazione per il blocco singolo 11 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.12.` | Peso di interpolazione per il blocco singolo 12 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.13.` | Peso di interpolazione per il blocco singolo 13 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.14.` | Peso di interpolazione per il blocco singolo 14 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.15.` | Peso di interpolazione per il blocco singolo 15 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.16.` | Peso di interpolazione per il blocco singolo 16 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.17.` | Peso di interpolazione per il blocco singolo 17 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.18.` | Peso di interpolazione per il blocco singolo 18 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.19.` | Peso di interpolazione per il blocco singolo 19 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.20.` | Peso di interpolazione per il blocco singolo 20 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.21.` | Peso di interpolazione per il blocco singolo 21 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.22.` | Peso di interpolazione per il blocco singolo 22 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.23.` | Peso di interpolazione per il blocco singolo 23 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.24.` | Peso di interpolazione per il blocco singolo 24 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.25.` | Peso di interpolazione per il blocco singolo 25 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.26.` | Peso di interpolazione per il blocco singolo 26 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.27.` | Peso di interpolazione per il blocco singolo 27 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.28.` | Peso di interpolazione per il blocco singolo 28 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.29.` | Peso di interpolazione per il blocco singolo 29 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.30.` | Peso di interpolazione per il blocco singolo 30 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.31.` | Peso di interpolazione per il blocco singolo 31 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.32.` | Peso di interpolazione per il blocco singolo 32 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.33.` | Peso di interpolazione per il blocco singolo 33 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.34.` | Peso di interpolazione per il blocco singolo 34 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.35.` | Peso di interpolazione per il blocco singolo 35 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.36.` | Peso di interpolazione per il blocco singolo 36 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `single_blocks.37.` | Peso di interpolazione per il blocco singolo 37 (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |
| `final_layer.` | Peso di interpolazione per lo strato finale (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 1.0 |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `model` | Modello unito che combina le caratteristiche di entrambi i modelli di input | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeFlux1/it.md)

---
**Source fingerprint (SHA-256):** `4a1cc4dd2c253bbeb94144969e921af40a7f12a1ec23ed7c23da89107767dc26`
