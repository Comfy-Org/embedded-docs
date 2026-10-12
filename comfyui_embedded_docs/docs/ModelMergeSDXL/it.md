# ModelMergeSDXL

Il nodo ModelMergeSDXL consente di fondere insieme due modelli SDXL regolando l'influenza di ciascun modello su diverse parti dell'architettura. È possibile controllare quanto ciascun modello contribuisce agli embedding temporali, agli embedding delle etichette e ai vari blocchi all'interno della struttura del modello. Questo crea un modello ibrido che combina le caratteristiche di entrambi i modelli di input.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model1` | Il primo modello SDXL da fondere | MODEL | Sì | - |
| `model2` | Il secondo modello SDXL da fondere | MODEL | Sì | - |
| `time_embed.` | Peso di miscelazione per i livelli di embedding temporale (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `label_emb.` | Peso di miscelazione per i livelli di embedding delle etichette (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `input_blocks.0` | Peso di miscelazione per il blocco di input 0 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `input_blocks.1` | Peso di miscelazione per il blocco di input 1 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `input_blocks.2` | Peso di miscelazione per il blocco di input 2 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `input_blocks.3` | Peso di miscelazione per il blocco di input 3 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `input_blocks.4` | Peso di miscelazione per il blocco di input 4 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `input_blocks.5` | Peso di miscelazione per il blocco di input 5 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `input_blocks.6` | Peso di miscelazione per il blocco di input 6 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `input_blocks.7` | Peso di miscelazione per il blocco di input 7 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `input_blocks.8` | Peso di miscelazione per il blocco di input 8 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `middle_block.0` | Peso di miscelazione per il blocco intermedio 0 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `middle_block.1` | Peso di miscelazione per il blocco intermedio 1 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `middle_block.2` | Peso di miscelazione per il blocco intermedio 2 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `output_blocks.0` | Peso di miscelazione per il blocco di output 0 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `output_blocks.1` | Peso di miscelazione per il blocco di output 1 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `output_blocks.2` | Peso di miscelazione per il blocco di output 2 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `output_blocks.3` | Peso di miscelazione per il blocco di output 3 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `output_blocks.4` | Peso di miscelazione per il blocco di output 4 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `output_blocks.5` | Peso di miscelazione per il blocco di output 5 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `output_blocks.6` | Peso di miscelazione per il blocco di output 6 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `output_blocks.7` | Peso di miscelazione per il blocco di output 7 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `output_blocks.8` | Peso di miscelazione per il blocco di output 8 (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `out.` | Peso di miscelazione per i livelli di output (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `model` | Il modello SDXL fuso che combina le caratteristiche di entrambi i modelli di input | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSDXL/it.md)

---
**Source fingerprint (SHA-256):** `9a1b0645ee19c2eddb274dd6ea3f9a05997115119cc654a7f055d58475745bb2`
