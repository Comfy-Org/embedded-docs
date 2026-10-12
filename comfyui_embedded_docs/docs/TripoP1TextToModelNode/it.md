# Tripo P1: Da testo a modello

Tripo P1 text-to-3D. Questo nodo genera un modello 3D da una descrizione testuale usando l'API Tripo P1. È ottimizzato per creare mesh low-poly pronte per il gioco con topologia stabile, rendendolo adatto ad applicazioni in tempo reale.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `output_mode` | Controlla se il modello generato contiene solo la geometria o anche texture di colore/PBR. "Geometry only" restituisce una mesh non texturizzata. "Textured" aggiunge mappe di colore/PBR e mostra le opzioni texture riportate sotto. | DYNAMIC_COMBO | Sì | `"Geometry only"`<br>`"Textured"` |
| `prompt` | La descrizione testuale del modello 3D che desideri generare. Fino a 1024 caratteri. Obbligatorio e non può essere vuoto. | STRING | Sì | Fino a 1024 caratteri |
| `negative_prompt` | Una descrizione testuale di ciò che non desideri nel modello generato. Fino a 255 caratteri. Predefinito: non impostato. | STRING | No | Fino a 255 caratteri |
| `image_seed` | Un valore di seed usato per controllare la casualità. Predefinito: 42. | INT | No | 0 to 2147483647 |
| `face_limit` | Numero target di facce, 48-20000. -1 lascia che Tripo scelga in modo adattivo. Predefinito: -1. | INT | No | -1 to 20000 |
| `model_seed` | Un valore di seed usato per controllare la casualità. Predefinito: 42. | INT | No | 0 to 2147483647 |
| `auto_size` | Scala l'output per approssimare metri del mondo reale. Predefinito: False. | BOOLEAN | No | True / False |
| `export_uv` | Esegue l'UV unwrap durante la generazione. Disattivare per esecuzioni più rapide di sola geometria. Predefinito: True. | BOOLEAN | No | True / False |
| `compress_geometry` | Applica la compressione geometrica meshopt (EXT_meshopt_compression). File più piccoli, ma l'anteprima 3D di ComfyUI non può visualizzarli; decomprimere prima di modificarli. Predefinito: False. | BOOLEAN | No | True / False |

### Input di sola geometria

Nessun input aggiuntivo è disponibile quando `output_mode` è impostato su `"Geometry only"`. In questa modalità i parametri relativi alle texture non vengono inviati a Tripo.

### Input con texture

Questi input compaiono solo quando `output_mode` è impostato su `"Textured"`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `pbr` | Include le mappe PBR. Quando è attivo, anche la texture di base viene forzata. Predefinito: True. | BOOLEAN | Sì | True / False |
| `texture_quality` | Preset di qualità della texture. detailed = texture HD, extreme = texture 8K Ultra. Predefinito: "standard". | COMBO | Sì | `"standard"`<br>`"detailed"`<br>`"extreme"` |
| `texture_seed` | Un valore di seed per la generazione della texture, usato per controllare la casualità. Predefinito: 42. | INT | Sì | 0 to 2147483647 |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `model_file` | Il nome del file del modello generato, mantenuto solo per compatibilità retroattiva. | STRING |
| `model task_id` | L'ID attività univoco per la richiesta di generazione del modello. | MODEL_TASK_ID |
| `GLB` | Il modello 3D generato in formato GLB. | FILE3DGLB |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1TextToModelNode/it.md)

---
**Source fingerprint (SHA-256):** `53a5573384294612b912558436e82f3481717d2ba3d50b73f1e40c3065aff2a0`
