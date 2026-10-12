# TripoPSeriesMultiviewToModelNode

Genera un modello 3D low-poly con topologia pulita da diverse viste dello stesso soggetto utilizzando il modello P2 di Tripo. La vista frontale è obbligatoria e si possono aggiungere da una a tre viste tra sinistra, posteriore e destra per migliorare il risultato. Il modello viene restituito come mesh triangolare (GLB) o, quando `model.quad` è abilitato, come mesh a prevalenza quad (FBX).

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Modello Tripo della serie P da utilizzare. Selezionando un modello vengono mostrati i suoi input specifici qui sotto. | DYNAMIC_COMBO | Sì | `"P2"` |

### Input di P2

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model.image` | Vista frontale (0°) del soggetto. | IMAGE | Sì | - |
| `model.image_left` | Vista sinistra (90°), il lato sinistro del soggetto stesso. | IMAGE | No | - |
| `model.image_back` | Vista posteriore (180°). | IMAGE | No | - |
| `model.image_right` | Vista destra (270°), il lato destro del soggetto stesso. | IMAGE | No | - |
| `model.quad` | Restituisce una mesh a prevalenza quad sull'output FBX invece di una mesh triangolare sull'output GLB (predefinito: False). | BOOLEAN | Sì | True/False |
| `model.face_limit` | Numero target di facce. `-1` lascia scegliere a Tripo. Con `model.quad` abilitato il limite è da 48 a 25,000, altrimenti da 48 a 50,000 (predefinito: -1). | INT | Sì | -1, oppure da 48 a 50000 |
| `model.texture` | Risoluzione della texture del colore di base: standard è 2K, detailed 4K ed extreme 8K. `"none"` restituisce una mesh senza texture (predefinito: `"standard"`). | COMBO | Sì | `"standard"`<br>`"detailed"`<br>`"extreme"`<br>`"none"` |
| `model.pbr` | Aggiunge mappe metallic, roughness e normal al colore di base. Ignorato quando `model.texture` è `"none"` (predefinito: True). | BOOLEAN | Sì | True/False |
| `model.model_seed` | Seed per la geometria (predefinito: 42). | INT | Sì | da 0 a 2147483647 |
| `model.texture_alignment` | Abbina i colori delle immagini di input, oppure adatta le texture alla geometria generata. Ignorato quando `model.texture` è `"none"` (predefinito: `"original_image"`). Impostazione avanzata. | COMBO | Sì | `"original_image"`<br>`"geometry"` |
| `model.orientation` | `"align_image"` ruota il modello verso il punto di vista delle immagini di input. Ignorato quando `model.texture` è `"none"` (predefinito: `"default"`). Impostazione avanzata. | COMBO | Sì | `"default"`<br>`"align_image"` |
| `model.texture_seed` | Seed per le texture (predefinito: 42). Impostazione avanzata. | INT | Sì | da 0 a 2147483647 |
| `model.auto_size` | Scala il modello alle sue dimensioni reali in metri tramite la trasformazione della scena. Ignorato quando `model.texture` è `"none"` (predefinito: False). Impostazione avanzata. | BOOLEAN | Sì | True/False |
| `model.export_uv` | Esegue l'UV unwrap della mesh quando non ha texture. Le mesh con texture vengono sempre unwrappate (predefinito: True). Impostazione avanzata. | BOOLEAN | Sì | True/False |
| `model.compress_geometry` | Applica la compressione geometrica meshopt: file molto più piccoli, ma l'anteprima 3D di ComfyUI non può visualizzarli. Ignorato per le mesh quad (predefinito: False). Impostazione avanzata. | BOOLEAN | Sì | True/False |

**Note:**

- `model.image` è obbligatorio e almeno uno tra `model.image_left`, `model.image_back` o `model.image_right` deve essere collegato; il nodo genera un errore se la vista frontale è l'unica immagine.
- Viene utilizzata solo la prima immagine di ogni batch.
- `model.face_limit` è un obiettivo più che un limite massimo, quindi il risultato può contenere più facce di quelle richieste. `-1` lascia la scelta a Tripo.
- `model.quad` decide quale output contiene la mesh. Quando è abilitato, il modello arriva sull'output FBX e l'output GLB resta vuoto; quando è disabilitato, il modello arriva su GLB e FBX resta vuoto. Il nodo genera un errore se l'output vuoto è quello collegato.
- `model.texture`, `model.pbr`, `model.texture_seed`, `model.auto_size`, `model.texture_alignment` e `model.orientation` si applicano solo ai modelli con texture: con `"none"` il nodo non invia impostazioni di texture e restituisce solo la geometria.
- `model.compress_geometry` non ha effetto sulle mesh quad.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model task_id` | L'ID univoco del task per la richiesta di generazione del modello. | MODEL_TASK_ID |
| `GLB` | Il modello 3D generato in formato GLB. Vuoto quando `model.quad` è abilitato. | FILE3DGLB |
| `FBX` | Il modello 3D generato in formato FBX. Popolato solo quando `model.quad` è abilitato. | FILE3DFBX |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoPSeriesMultiviewToModelNode/it.md)

---
**Source fingerprint (SHA-256):** `cea0a65ca001bc8298af9fbe2a83f592abf497987e634b0126482f3d2a18571c`
