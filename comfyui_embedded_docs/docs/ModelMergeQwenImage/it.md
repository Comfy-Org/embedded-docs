# ModelMergeQwenImage

Questo nodo unisce due modelli di immagini Qwen fondendo i rispettivi componenti con pesi regolabili. Ogni peso controlla quanto la parte corrispondente del secondo modello contribuisce al risultato unito, consentendoti di miscelare separatamente embedding posizionali, livelli di elaborazione del testo, livelli di input immagine, tutti i 60 blocchi transformer e la proiezione di output. Il risultato finale è un singolo MODEL che puoi usare ovunque sia previsto un modello normale.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model1` | Il primo modello da unire | MODEL | Sì | - |
| `model2` | Il secondo modello da unire | MODEL | Sì | - |
| `pos_embeds.` | Peso per la fusione degli embedding posizionali (predefinito: 1.0) | FLOAT | Sì | 0.0 to 1.0 (step: 0.01) |
| `img_in.` | Peso per la fusione dell'elaborazione dell'input immagine (predefinito: 1.0) | FLOAT | Sì | 0.0 to 1.0 (step: 0.01) |
| `txt_norm.` | Peso per la fusione della normalizzazione del testo (predefinito: 1.0) | FLOAT | Sì | 0.0 to 1.0 (step: 0.01) |
| `txt_in.` | Peso per la fusione dell'elaborazione dell'input testuale (predefinito: 1.0) | FLOAT | Sì | 0.0 to 1.0 (step: 0.01) |
| `time_text_embed.` | Peso per la fusione dell'embedding di tempo e testo (predefinito: 1.0) | FLOAT | Sì | 0.0 to 1.0 (step: 0.01) |
| da `transformer_blocks.0.` a `transformer_blocks.59.` | Peso per la fusione di ciascun blocco transformer (predefinito: 1.0). Il nodo espone un peso per ciascuno dei 60 blocchi transformer. | FLOAT | Sì | 0.0 to 1.0 (step: 0.01) |
| `proj_out.` | Peso per la fusione della proiezione di output (predefinito: 1.0) | FLOAT | Sì | 0.0 to 1.0 (step: 0.01) |

Nota: tutti gli input di peso sono obbligatori e condividono gli stessi limiti — un valore predefinito di 1.0 con un intervallo valido da 0.0 a 1.0, regolabile a passi di 0.01.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `model` | Il modello unito che combina componenti da entrambi i modelli di input con i pesi specificati | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeQwenImage/it.md)

---
**Source fingerprint (SHA-256):** `5f31f91f3d54d4c5085c684a98f64afd0a0f704693b6dd4f19bc35d3c5f74529`
