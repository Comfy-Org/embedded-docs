# TripoTextureNodeV2

Questo nodo aggiunge texture a un modello 3D esistente di un flusso di lavoro Tripo, identificato da un ID attività di un passaggio di generazione precedente. Può produrre mappe materiale PBR o una texture a tinta unita, e il risultato può essere guidato da un prompt testuale, un'immagine di stile o immagini di riferimento.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model_task_id` | ID attività del modello sorgente prodotto da un nodo Tripo precedente (generazione modello o segmentazione modello). | MODEL_TASK_ID / SEGMENT_TASK_ID | Sì | - |
| `pbr` | Mappe materiale PBR (colore base, metallico, rugosità, normali); disattivato produce una texture a tinta unita. (predefinito: true) | BOOLEAN | No | true<br>false |
| `texture_seed` | Seed utilizzato per la generazione della texture. (predefinito: 42) Input avanzato. | INT | No | 0 to 2147483647 |
| `texture_quality` | Qualità delle texture generate. `detailed` = texture HD, `extreme` = texture 8K Ultra. (predefinito: "standard") Input avanzato. | COMBO | No | "standard"<br>"detailed"<br>"extreme" |
| `texture_alignment` | Modalità di allineamento delle texture al modello. (predefinito: "original_image") Input avanzato. | COMBO | No | "original_image"<br>"geometry" |
| `texture_prompt` | Guida testuale opzionale per la texturizzazione. In pratica richiesto per i modelli importati (Tripo: Import Model), che non hanno un'immagine sorgente da cui dedurre i colori. Non può essere combinato con immagini di riferimento. (predefinito: vuoto) | STRING | No | - |
| `model_version` | Modello texture: v3.0 per mesh generate con v3.x, v2.5 per mesh generate con v2.5. (predefinito: v3_0_20250812) | COMBO | No | Versioni del modello texture Tripo, predefinito "v3_0_20250812" |
| `style_image` | Immagine di riferimento per lo stile artistico delle texture. Usata solo insieme a `texture_prompt`. | IMAGE | No | - |
| `reference` | Immagini di riferimento che guidano le texture. Non possono essere combinate con `texture_prompt` o `style_image`. (predefinito: "none") | DYNAMIC_COMBO | No | "none"<br>"image"<br>"multiview" |
| `part_names` | Nomi delle parti separati da virgola da Tripo: Segment Model da texturizzare. Se vuoto, applica la texture a ogni parte. (predefinito: vuoto) Input avanzato. | STRING | No | - |

### Input di riferimento immagine

Mostrati quando `reference` è impostato su "image".

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `reference_image` | Immagine di riferimento singola che le texture devono seguire. | IMAGE | Sì | - |

### Input di riferimento multivista

Mostrati quando `reference` è impostato su "multiview".

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image_front` | Vista frontale (0°). | IMAGE | Sì | - |
| `image_left` | Vista sinistra (90°). | IMAGE | Sì | - |
| `image_back` | Vista posteriore (180°). | IMAGE | Sì | - |
| `image_right` | Vista destra (270°). | IMAGE | Sì | - |

**Note sui vincoli dei parametri:**

- Le immagini di riferimento (modalità di riferimento "image" o "multiview") non possono essere combinate con `texture_prompt` o `style_image`.
- `style_image` richiede che venga fornito un `texture_prompt`.
- Quando non viene fornito alcun `texture_prompt`, il modello sorgente deve provenire da un'attività text-to-model, image-to-model, multiview-to-model o texture-model. I modelli senza immagine sorgente (modelli importati, segmentati, completati o retopologizzati) richiedono un `texture_prompt`, perché Tripo accetta immagini di riferimento solo per i modelli che ha generato esso stesso.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `model task_id` | ID attività dell'operazione di texturizzazione, che può essere passato ad altri nodi Tripo. | MODEL_TASK_ID |
| `GLB` | Modello texturizzato in formato GLB. Vuoto quando l'origine è una mesh quad o un import FBX. | FILE_3D_GLB |
| `FBX` | Modello texturizzato in formato FBX. Tripo restituisce FBX per mesh quad e import FBX; vuoto negli altri casi. | FILE_3D_FBX |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNodeV2/it.md)

---
**Source fingerprint (SHA-256):** `dd9b05e37fcdd29896a50451b92a267862ad94b59abfb8680c8b648390cca091`
