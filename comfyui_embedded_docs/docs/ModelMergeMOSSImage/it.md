# ModelMergeMOSSImage

Il nodo ModelMergeMOSSImage unisce due modelli immagine MOSS fondendo i pesi corrispondenti blocco per blocco, così una parte del risultato può provenire da un modello di base e il resto da un fine-tune o da un secondo modello. Ogni componente principale dell'architettura ha il proprio rapporto: il video embedder, il text embedder, il time embedding, la modulazione condivisa dei blocchi, tutti i 42 layer transformer e le teste di output.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model1` | Il primo modello da unire. Tutto ciò a cui il secondo modello non contribuisce viene mantenuto da questo modello | MODEL | Sì | - |
| `model2` | Il secondo modello da unire. I suoi pesi vengono fusi in base ai rapporti indicati di seguito | MODEL | Sì | - |
| `video_embedder.` | Rapporto di fusione per il blocco video embedder (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `text_embedder.proj.` | Rapporto di fusione per il layer di proiezione del text embedder (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `text_embedder.blocks.0.` e `text_embedder.blocks.1.` | Rapporto di fusione per ciascuno dei due blocchi del text embedder (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `time_embedding.` | Rapporto di fusione per il blocco time embedding (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `shared_block_modulation.` | Rapporto di fusione per il layer di modulazione condiviso utilizzato dai blocchi transformer (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `layers.0.` fino a `layers.41.` | Rapporto di fusione per ciascuno dei 42 layer transformer (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `final_norm_video.` | Rapporto di fusione per la normalizzazione finale dello stream video (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `final_linear_video.` | Rapporto di fusione per il layer lineare finale dello stream video (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |
| `video_head_modulation.` | Rapporto di fusione per il layer di modulazione della testa di output video (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo: 0.01) |

Un rapporto di 0.0 mantiene quel componente così com'è in `model1`, un rapporto di 1.0 lo prende interamente da `model2` e i valori intermedi producono una fusione ponderata. Entrambi gli input devono essere modelli immagine MOSS con la stessa architettura; i pesi che non corrispondono a nessuno dei prefissi sopra riportati ricadono sul rapporto di `video_embedder.`.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `MODEL` | Il modello unito, che combina entrambi gli input secondo i rapporti specificati | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeMOSSImage/it.md)

---
**Source fingerprint (SHA-256):** `3b7d9c806a8d53ad00044bf30f5e63431fea7ee565414acb70a56e3059164288`
