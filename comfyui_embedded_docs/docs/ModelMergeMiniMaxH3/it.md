# Model Merge MiniMax H3

Unisce due modelli MiniMax H3 compatibili per componente, con un rapporto separato per ciascuna parte dell'architettura. Aumentare un rapporto preleva una quota maggiore di quel componente da `model2`, così puoi mantenere le proiezioni patch e i blocchi di raffinamento di un modello sostituendo i blocchi transformer con quelli di un altro.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model1` | Primo modello MiniMax H3, la base da cui viene preso ogni componente (il peso predefinito si applica dove `model2` non viene utilizzato). | MODEL | Sì | - |
| `model2` | Secondo modello MiniMax H3 che fornisce i componenti da combinare. | MODEL | Sì | - |
| `video_patch_proj.` | Quota di `model2` per la proiezione patch video (predefinito: 1.0). | FLOAT | Sì | 0.0 a 1.0 (passo: 0.01) |
| `audio_patch_proj.` | Quota di `model2` per la proiezione patch audio (predefinito: 1.0). | FLOAT | Sì | 0.0 a 1.0 (passo: 0.01) |
| `condition_proj.` | Quota di `model2` per la proiezione di condizionamento (predefinito: 1.0). | FLOAT | Sì | 0.0 a 1.0 (passo: 0.01) |
| `time_embedder.` | Quota di `model2` per il time embedder (predefinito: 1.0). | FLOAT | Sì | 0.0 a 1.0 (passo: 0.01) |
| `token_refiner.blocks.0.` | Quota di `model2` per il primo blocco del token refiner (predefinito: 1.0). | FLOAT | Sì | 0.0 a 1.0 (passo: 0.01) |
| `token_refiner.blocks.1.` | Quota di `model2` per il secondo blocco del token refiner (predefinito: 1.0). | FLOAT | Sì | 0.0 a 1.0 (passo: 0.01) |
| `token_refiner.final_norm.` | Quota di `model2` per la normalizzazione finale del token refiner (predefinito: 1.0). | FLOAT | Sì | 0.0 a 1.0 (passo: 0.01) |
| `blocks.0.` fino a `blocks.49.` | Quota di `model2` per ciascuno dei 50 blocchi transformer, un widget per blocco (predefinito: 1.0). | FLOAT | Sì | 0.0 a 1.0 (passo: 0.01) |
| `final_layer.norm.` | Quota di `model2` per la normalizzazione del layer finale (predefinito: 1.0). | FLOAT | Sì | 0.0 a 1.0 (passo: 0.01) |
| `final_layer.adaln_proj.` | Quota di `model2` per la proiezione di normalizzazione adattiva finale (predefinito: 1.0). | FLOAT | Sì | 0.0 a 1.0 (passo: 0.01) |
| `final_layer.video_out.` | Quota di `model2` per il layer di output video (predefinito: 1.0). | FLOAT | Sì | 0.0 a 1.0 (passo: 0.01) |
| `final_layer.audio_out.` | Quota di `model2` per il layer di output audio (predefinito: 1.0). | FLOAT | Sì | 0.0 a 1.0 (passo: 0.01) |

Un rapporto pari a 0.0 mantiene quel componente interamente da `model1` e 1.0 lo prende interamente da `model2`; i valori intermedi combinano i due. I tensori che non hanno un rapporto, come le statistiche di normalizzazione, provengono sempre da `model1`. Entrambi gli input devono essere modelli MiniMax H3 con la stessa architettura; in caso contrario, la fusione produce un modello che non è eseguibile.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `MODEL` | Il modello MiniMax H3 fuso. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeMiniMaxH3/it.md)

---
**Source fingerprint (SHA-256):** `4fea4e588d16a8396c68aa071a59e671a2a0c645734606be6d7e221986ba88bd`
