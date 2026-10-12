# Tripo P2: Testo in modello

Genera un modello 3D low-poly con topologia pulita a partire da un prompt testuale usando il modello P2 di Tripo. Il risultato viene restituito come mesh triangolare (GLB) oppure, quando `model.quad` è abilitato, come mesh a dominanza di quad (FBX).

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Modello Tripo serie P da usare. Selezionando un modello vengono mostrati qui sotto i relativi input. | DYNAMIC_COMBO | Sì | `"P2"` |

### Input di P2

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model.prompt` | Descrizione testuale del modello 3D da generare. Non deve essere vuota, fino a 1024 caratteri (predefinito: vuoto). | STRING | Sì | Fino a 1024 caratteri |
| `model.negative_prompt` | Descrizione testuale di ciò che va evitato nel modello generato (predefinito: vuoto). | STRING | No | Fino a 255 caratteri |
| `model.quad` | Restituisce una mesh a dominanza di quad sull'output FBX invece di una mesh triangolare sull'output GLB (predefinito: False). | BOOLEAN | Sì | True/False |
| `model.face_limit` | Numero target di facce. `-1` lascia scegliere a Tripo. Con `model.quad` abilitato il limite è da 48 a 25.000, altrimenti da 48 a 50.000 (predefinito: -1). | INT | Sì | -1, oppure da 48 a 50000 |
| `model.texture` | Risoluzione della texture del colore di base: standard è 2K, detailed 4K ed extreme 8K. `"none"` restituisce una mesh senza texture (predefinito: `"standard"`). | COMBO | Sì | `"standard"`<br>`"detailed"`<br>`"extreme"`<br>`"none"` |
| `model.pbr` | Aggiunge mappe metallic, roughness e normal al colore di base. Ignorato quando `model.texture` è `"none"` (predefinito: True). | BOOLEAN | Sì | True/False |
| `model.model_seed` | Seed per la geometria (predefinito: 42). | INT | Sì | da 0 a 2147483647 |
| `model.image_seed` | Seed per l'immagine che Tripo genera dal prompt prima della modellazione (predefinito: 42). Impostazione avanzata. | INT | Sì | da 0 a 2147483647 |
| `model.texture_seed` | Seed per le texture (predefinito: 42). Impostazione avanzata. | INT | Sì | da 0 a 2147483647 |
| `model.auto_size` | Scala il modello alla sua dimensione reale in metri tramite la trasformazione della scena. Ignorato quando `model.texture` è `"none"` (predefinito: False). Impostazione avanzata. | BOOLEAN | Sì | True/False |
| `model.export_uv` | Esegue l'UV unwrap della mesh quando non ha texture. Le mesh con texture vengono sempre sottoposte a UV unwrap (predefinito: True). Impostazione avanzata. | BOOLEAN | Sì | True/False |
| `model.compress_geometry` | Applica la compressione geometrica meshopt: file molto più piccoli, ma l'anteprima 3D di ComfyUI non può visualizzarli. Ignorato per le mesh a quad (predefinito: False). Impostazione avanzata. | BOOLEAN | Sì | True/False |

**Note:**

- `model.prompt` è obbligatorio; `model.negative_prompt` è opzionale e limitato a 255 caratteri.
- `model.face_limit` è un obiettivo più che un limite massimo rigido, quindi il risultato può contenere più facce di quelle richieste. `-1` lascia la scelta a Tripo.
- `model.quad` decide quale output trasporta la mesh. Se abilitato, il modello arriva sull'output FBX e l'output GLB rimane vuoto; se disabilitato, il modello arriva su GLB e FBX rimane vuoto. Il nodo genera un errore se l'output vuoto è quello che hai collegato.
- `model.texture`, `model.pbr`, `model.texture_seed` e `model.auto_size` si applicano solo ai modelli con texture: con `"none"` il nodo non invia impostazioni di texture e restituisce solo la geometria.
- `model.compress_geometry` non ha alcun effetto sulle mesh a quad.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model task_id` | L'ID attività univoco per la richiesta di generazione del modello. | MODEL_TASK_ID |
| `GLB` | Il modello 3D generato in formato GLB. Vuoto quando `model.quad` è abilitato. | FILE3DGLB |
| `FBX` | Il modello 3D generato in formato FBX. Popolato solo quando `model.quad` è abilitato. | FILE3DFBX |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoPSeriesTextToModelNode/it.md)

---
**Source fingerprint (SHA-256):** `e55596c1a237cf6b92e3bdead4359f380c6cba60992dcc61b5ee4e6b1bdd843b`
