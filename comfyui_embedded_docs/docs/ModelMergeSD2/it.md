# ModelMergeSD2

Il nodo ModelMergeSD2 unisce due modelli Stable Diffusion 2.x combinando le rispettive componenti corrispondenti, con un peso separato per l'embedding temporale, l'embedding delle etichette e ogni blocco di input, intermedio e di output. La disposizione dei blocchi è la stessa di ModelMergeSD1, quindi entrambi i nodi espongono lo stesso insieme di rapporti.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model1` | Il primo modello da unire. Tutte le componenti a cui il secondo modello non contribuisce vengono mantenute da questo modello | MODEL | Sì | - |
| `model2` | Il secondo modello da unire. I suoi pesi vengono combinati secondo i rapporti riportati di seguito | MODEL | Sì | - |
| `time_embed.` | Rapporto di fusione per il livello di embedding temporale (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 (passo: 0.01) |
| `label_emb.` | Rapporto di fusione per il livello di embedding delle etichette (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 (passo: 0.01) |
| da `input_blocks.0.` a `input_blocks.11.` | Rapporto di fusione per ciascuno dei 12 blocchi di input (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 (passo: 0.01) |
| da `middle_block.0.` a `middle_block.2.` | Rapporto di fusione per ciascuno dei 3 blocchi intermedi (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 (passo: 0.01) |
| da `output_blocks.0.` a `output_blocks.11.` | Rapporto di fusione per ciascuno dei 12 blocchi di output (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 (passo: 0.01) |
| `out.` | Rapporto di fusione per il livello di output (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 (passo: 0.01) |

Un rapporto di 0.0 mantiene quella componente così com'è in `model1`, un rapporto di 1.0 la prende interamente da `model2`, mentre i valori intermedi producono una fusione ponderata. Entrambi gli input devono essere modelli Stable Diffusion 2.x con la stessa struttura a blocchi.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `MODEL` | Il modello unito, che combina entrambi gli input secondo i rapporti specificati | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD2/it.md)

---
**Source fingerprint (SHA-256):** `b9d53f126139412fbd8b21be72e1dcdb02736519ab4dc9e28c7840d69acb7c87`
