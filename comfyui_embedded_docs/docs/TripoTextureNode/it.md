# Tripo: Modello texture (Legacy)

Il nodo Tripo: Texture model (Legacy) aggiunge texture a un modello 3D Tripo esistente tramite l'API Tripo. Riceve l'ID attività di un modello creato da un altro nodo Tripo e restituisce un modello GLB o FBX texturizzato al termine del processo di texturing. È possibile controllare le mappe dei materiali, la qualità delle texture, l'allineamento e il seed, e guidare le texture con un prompt testuale, un'immagine di stile o immagini di riferimento. Questo nodo è una versione legacy dello strumento di texturing.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model_task_id` | L'ID attività Tripo del modello da texturizzare. Accetta ID attività di modello e ID attività di segmentazione. | MODEL_TASK_ID, SEGMENT_TASK_ID | Sì | - |
| `texture` | Ignorato: questo nodo genera sempre le texture. Mantenuto per flussi di lavoro precedenti. (predefinito: True) | BOOLEAN | No | true<br>false |
| `pbr` | Mappe materiali PBR (colore base, metallico, rugosità, normale); disattivato fornisce una texture a tinta unita. (predefinito: True) | BOOLEAN | No | true<br>false |
| `texture_seed` | Seed casuale per la generazione delle texture. (predefinito: 42) | INT | No | 0 – 2147483647 |
| `texture_quality` | Qualità della risoluzione delle texture: detailed = texture HD, extreme = texture 8K Ultra. (predefinito: "standard"). Costo approssimativo: standard $0.10, detailed $0.20, extreme $0.30. | COMBO | No | "standard"<br>"detailed"<br>"extreme" |
| `texture_alignment` | Metodo utilizzato per allineare le texture generate al modello. (predefinito: "original_image") | COMBO | No | "original_image"<br>"geometry" |
| `texture_prompt` | Guida testuale opzionale per il texturing. In pratica obbligatoria per i modelli importati (Tripo: Import Model), che non hanno un'immagine di origine da cui inferire i colori. Non può essere combinata con immagini di riferimento. (predefinito: "") | STRING | No | - |
| `model_version` | Modello di texture: v3.0 per mesh generate con v3.x, v2.5 per mesh generate con v2.5. (predefinito: v3.0_20250812) | COMBO | No | Più opzioni disponibili |
| `style_image` | Immagine di riferimento per lo stile artistico delle texture. Utilizzata solo insieme a `texture_prompt`. | IMAGE | No | - |
| `reference` | Immagini di riferimento che guidano le texture. Non può essere combinato con `texture_prompt` o `style_image`. (predefinito: "none") | DYNAMIC_COMBO | No | "none"<br>"image"<br>"multiview" |
| `part_names` | Nomi delle parti separati da virgola da Tripo: Segment Model da texturizzare. Se vuoto, texturizza ogni parte. (predefinito: "") | STRING | No | - |

### Input di riferimento `image`

Questi input sono disponibili quando `reference` è impostato su `"image"`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `reference_image` | Immagine di riferimento singola che le texture devono seguire. | IMAGE | Sì | - |

### Input di riferimento `multiview`

Questi input sono disponibili quando `reference` è impostato su `"multiview"`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image_front` | Vista frontale (0°). | IMAGE | Sì | - |
| `image_left` | Vista sinistra (90°). | IMAGE | Sì | - |
| `image_back` | Vista posteriore (180°). | IMAGE | Sì | - |
| `image_right` | Vista destra (270°). | IMAGE | Sì | - |

**Nota:** Le modalità di riferimento `"image"` e `"multiview"` non possono essere combinate con un `texture_prompt` non vuoto o con `style_image`. L'input `style_image` richiede un `texture_prompt` non vuoto. Quando `texture_prompt` viene lasciato vuoto, il modello di origine deve già avere una propria immagine di origine (ad esempio, modelli prodotti da text-to-model, image-to-model, multiview-to-model o un'attività di texturing precedente). I modelli che non hanno un'immagine di origine — come modelli importati, segmentati, completati o retopologizzati — devono essere texturizzati con un `texture_prompt`; le immagini di riferimento sono accettate solo per i modelli generati direttamente dall'API Tripo. L'input `part_names` può essere lasciato vuoto per texturizzare ogni parte.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `model_file` | Il file del modello generato (solo per compatibilità con le versioni precedenti). | STRING |
| `model task_id` | L'ID attività dell'attività di generazione texture completata, utilizzabile come input per altri nodi Tripo. | MODEL_TASK_ID |
| `GLB` | Il modello texturizzato generato in formato GLB. Vuoto quando l'origine è una mesh quad o un'importazione FBX. | FILE3DGLB |
| `FBX` | Il modello texturizzato generato in formato FBX. Tripo restituisce FBX per mesh quad e importazioni FBX; vuoto negli altri casi. | FILE3DFBX |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/it.md)

---
**Source fingerprint (SHA-256):** `850685123b5f14cded5829d86a7307452a1e812e78d11f52806e64ea41d66350`
