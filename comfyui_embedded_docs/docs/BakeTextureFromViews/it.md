# Bake Texture From Views

Proietta le immagini renderizzate sul layout UV della mesh. Renderizza la mesh con Render Mesh, modifica o rigenera le immagini, quindi esegui il bake con la stessa mesh e le stesse camere. I texel che nessuna vista copre mantengono la texture o i colori dei vertici della mesh.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `mesh` | La mesh con UV srotolate che è stata renderizzata. | MESH | Sì | - |
| `images` | Un'immagine per camera, nell'ordine delle camere (Batch Images). Qualsiasi risoluzione con le proporzioni del render; una risoluzione più alta produce un bake più nitido. | IMAGE | Sì | - |
| `camera_info` | Le camere con cui sono state renderizzate le immagini, come collegate a Render Mesh. Unisci i rig con Batch Cameras. Nessuna: vista frontale inquadrata automaticamente da Render Mesh. | LOAD3D_CAMERA | No | - |
| `resolution` | Risoluzione della texture quadrata. 0 mantiene la dimensione corrente della texture della mesh, oppure 2048 quando non ne ha una; altrimenti la texture corrente viene ricampionata a questa risoluzione. Predefinito: 0. | INT | No | 0 a 8192 (passo: 64) |
| `blend_exponent` | Le viste sono pesate tramite cos(angolo di vista)^esponente. Valori più alti favoriscono la vista più frontale (più nitida, cuciture più marcate); valori più bassi mediano più viste (risultato più morbido). Predefinito: 4.0. | FLOAT | No | 0.0 a 32.0 (passo: 0.5) |
| `fill_unseen` | I texel che nessuna vista vede assumono un colore propagato dalla superficie vista invece della texture o dei colori dei vertici della mesh. Usalo quando le viste sostituiscono l'intera texture. Predefinito: false. | BOOLEAN | No | true<br>false |
| `mask` | Aree modificate per vista; vengono proiettati solo i pixel mascherati. Una singola maschera si applica a ogni vista. | MASK | No | - |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `base_color` | La texture sottoposta a bake, per Apply Texture to Mesh. | IMAGE |
| `confidence` | Per ogni texel, quanto frontalmente è stato visto dalla vista migliore; 0 significa non visto. | MASK |

Nota: i render effettuati con una trasformazione del modello del visualizzatore non si allineano con il bake e viene usata solo la prima mesh di un batch.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeTextureFromViews/it.md)

---
**Source fingerprint (SHA-256):** `e5f2456977693dc09e69ce4d846f2ab775f2520115623d9f63a76807d6c9f797`
