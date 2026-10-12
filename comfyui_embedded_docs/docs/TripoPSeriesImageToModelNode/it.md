# TripoPSeriesImageToModelNode

Genera un modello 3D low-poly con topologia pulita a partire da una singola immagine usando il modello P2 di Tripo. Il risultato viene restituito come mesh triangolare (GLB) o, quando `model.quad` è abilitato, come mesh a prevalenza di quad (FBX).

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Modello Tripo della serie P da usare. Selezionando un modello vengono mostrati i relativi input di seguito. | DYNAMIC_COMBO | Sì | `"P2"` |

### Input di P2

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model.image` | L'immagine da cui viene generato il modello. | IMAGE | Sì | - |
| `model.quad` | Restituisce una mesh a prevalenza di quad sull'output FBX invece di una mesh triangolare sull'output GLB (predefinito: False). | BOOLEAN | Sì | True/False |
| `model.face_limit` | Numero di facce desiderato. `-1` lascia scegliere a Tripo. Con `model.quad` abilitato il limite è da 48 a 25.000, altrimenti da 48 a 50.000 (predefinito: -1). | INT | Sì | -1, oppure da 48 a 50000 |
| `model.texture` | Risoluzione della texture di colore di base: standard è 2K, detailed 4K ed extreme 8K. `"none"` restituisce una mesh non texturizzata (predefinito: `"standard"`). | COMBO | Sì | `"standard"`<br>`"detailed"`<br>`"extreme"`<br>`"none"` |
| `model.pbr` | Aggiunge mappe metallic, roughness e normal al colore di base. Ignorato quando `model.texture` è `"none"` (predefinito: True). | BOOLEAN | Sì | True/False |
| `model.model_seed` | Seed per la geometria (predefinito: 42). | INT | Sì | da 0 a 2147483647 |
| `model.texture_alignment` | Abbina i colori dell'immagine di input oppure adatta le texture alla geometria generata. Ignorato quando `model.texture` è `"none"` (predefinito: `"original_image"`). Impostazione avanzata. | COMBO | Sì | `"original_image"`<br>`"geometry"` |
| `model.orientation` | `"align_image"` ruota il modello in base al punto di vista dell'immagine di input. Ignorato quando `model.texture` è `"none"` (predefinito: `"default"`). Impostazione avanzata. | COMBO | Sì | `"default"`<br>`"align_image"` |
| `model.enable_image_autofix` | Consente a Tripo di migliorare un'immagine a bassa risoluzione o di bassa qualità prima della modellazione (predefinito: False). Impostazione avanzata. | BOOLEAN | Sì | True/False |
| `model.texture_seed` | Seed per le texture (predefinito: 42). Impostazione avanzata. | INT | Sì | da 0 a 2147483647 |
| `model.auto_size` | Ridimensiona il modello alle sue dimensioni reali in metri tramite la trasformazione della scena. Ignorato quando `model.texture` è `"none"` (predefinito: False). Impostazione avanzata. | BOOLEAN | Sì | True/False |
| `model.export_uv` | Esegue l'UV unwrap della mesh quando non è texturizzata. Le mesh texturizzate vengono sempre unwrappate (predefinito: True). Impostazione avanzata. | BOOLEAN | Sì | True/False |
| `model.compress_geometry` | Applica la compressione geometrica meshopt: file molto più piccoli, ma l'anteprima 3D di ComfyUI non può visualizzarli. Ignorato per le mesh quad (predefinito: False). Impostazione avanzata. | BOOLEAN | Sì | True/False |

**Note:**

- `model.image` è obbligatorio e viene utilizzata solo la prima immagine del batch.
- `model.face_limit` è un obiettivo, non un limite massimo rigido, quindi il risultato può contenere più facce di quelle richieste. `-1` lascia la scelta a Tripo.
- `model.quad` decide quale output contiene la mesh. Se abilitato, il modello arriva sull'output FBX e l'output GLB rimane vuoto; se disabilitato, il modello arriva su GLB e FBX rimane vuoto. Il nodo genera un errore se l'output vuoto è quello a cui ti sei collegato.
- `model.texture`, `model.pbr`, `model.texture_seed`, `model.auto_size`, `model.texture_alignment` e `model.orientation` si applicano solo ai modelli texturizzati: con `"none"` il nodo non invia impostazioni di texture e restituisce la sola geometria.
- `model.compress_geometry` non ha effetto sulle mesh quad.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model task_id` | L'ID univoco dell'attività per la richiesta di generazione del modello. | MODEL_TASK_ID |
| `GLB` | Il modello 3D generato in formato GLB. Vuoto quando `model.quad` è abilitato. | FILE3DGLB |
| `FBX` | Il modello 3D generato in formato FBX. Valorizzato solo quando `model.quad` è abilitato. | FILE3DFBX |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoPSeriesImageToModelNode/it.md)

---
**Source fingerprint (SHA-256):** `9bfad31ee00546d0603ce3273502cfc93c79e3b125941fed255866aa83f770a5`
