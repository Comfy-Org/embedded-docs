# Tripo P1: Multiview a Modello

Questo nodo genera un modello 3D da due a quattro immagini di riferimento di un oggetto o personaggio. Fornisci la vista frontale più una qualsiasi combinazione delle viste sinistra, posteriore e destra; il nodo restituisce il soggetto ricostruito come mesh GLB.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `image` | Vista frontale (0°). Obbligatoria. | IMAGE | Sì | - |
| `image_left` | Vista sinistra (90°), ovvero il lato sinistro del soggetto. | IMAGE | No | - |
| `image_back` | Vista posteriore (180°). | IMAGE | No | - |
| `image_right` | Vista destra (270°), ovvero il lato destro del soggetto. | IMAGE | No | - |
| `output_mode` | Scegli il tipo di modello da generare. "Geometry only" restituisce una mesh senza texture. "Textured" aggiunge mappe colore/PBR. | DYNAMIC_COMBO | Sì | "Geometry only"<br>"Textured" |
| `face_limit` | Numero di facce target, 48-20000. -1 lascia che Tripo scelga in modo adattivo. (predefinito: -1) | INT | No | da -1 a 20000 |
| `model_seed` | Seme per una generazione del modello riproducibile. (predefinito: 42) | INT | No | da 0 a 2147483647 |
| `auto_size` | Scala l'output per approssimare le dimensioni reali in metri. (predefinito: False) | BOOLEAN | No | True<br>False |
| `export_uv` | Esegue l'UV unwrap durante la generazione. Disattivalo per esecuzioni più rapide di sola geometria. (predefinito: True) | BOOLEAN | No | True<br>False |
| `compress_geometry` | Applica la compressione geometrica meshopt (EXT_meshopt_compression). File più piccoli, ma l'anteprima 3D di ComfyUI non può visualizzarli; decomprimi prima di modificarli. (predefinito: False) | BOOLEAN | No | True<br>False |

### Input di Geometry only

Per questa modalità non vengono mostrati input aggiuntivi. Il modello generato viene restituito senza texture.

### Input di Textured

Questi input vengono visualizzati quando `output_mode` è impostato su `"Textured"`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `pbr` | Include le mappe PBR. Quando è attivo, viene attivata forzatamente anche la texture di base. (predefinito: True) | BOOLEAN | Sì | True<br>False |
| `texture_quality` | Livello di qualità della texture. `detailed` = texture HD, `extreme` = texture 8K Ultra. (predefinito: "standard") | COMBO | Sì | "standard"<br>"detailed"<br>"extreme" |
| `texture_alignment` | Dai priorità alla fedeltà visiva rispetto all'immagine di origine oppure all'allineamento alla geometria della mesh. (predefinito: "original_image") | COMBO | Sì | "original_image"<br>"geometry" |
| `orientation` | Ruota l'output per corrispondere all'immagine di origine. Si applica solo quando è presente la texture. (predefinito: "default") | COMBO | Sì | "default"<br>"align_image" |
| `texture_seed` | Seme utilizzato per la generazione della texture. (predefinito: 42) | INT | Sì | da 0 a 2147483647 |

**Nota:** Devi fornire almeno 2 immagini: la vista frontale (`image`) più almeno una delle altre viste (`image_left`, `image_back` o `image_right`). Se vengono fornite meno di 2 immagini, il nodo genererà un errore.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `model_file` | Il nome file del modello GLB generato (solo per compatibilità con le versioni precedenti). | STRING |
| `model task_id` | L'ID attività univoco per questa richiesta di generazione del modello. | MODEL_TASK_ID |
| `GLB` | Il modello 3D generato in formato GLB. | FILE3DGLB |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1MultiviewToModelNode/it.md)

---
**Source fingerprint (SHA-256):** `1153f74ac76603829142959844e701f3c8f16be080e3de849951cffdda322d12`
