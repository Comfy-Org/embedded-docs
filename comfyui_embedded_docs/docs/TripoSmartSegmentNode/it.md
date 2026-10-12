# TripoSmartSegmentNode

Suddivide un modello 3D in parti semanticamente significative e assegna un nome a ciascuna parte. Può segmentare un modello esistente (fornito tramite un ID attività) oppure generare prima un modello da un'immagine e poi segmentarlo. Il `segment task_id` risultante può essere usato da altri nodi Tripo, come Complete Mesh Parts, Retopology, Texture model e Convert model, allo stesso modo di un risultato di Tripo: Segment Model.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `source` | Segmenta un modello esistente oppure genera un modello da un'immagine e lo segmenta. L'opzione selezionata determina quali input aggiuntivi vengono mostrati. | DYNAMIC_COMBO | Sì | `"model"`<br>`"image"` |

### Input del modello

Mostrato quando `source` è impostato su `"model"`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model_task_id` | Un risultato GLB. Le mesh quad (FBX) devono prima passare attraverso Tripo: Convert model (GLTF). | MODEL_TASK_ID | Sì | - |
| `granularity` | Quanto finemente il modello viene suddiviso in parti (predefinito: "medium"). | COMBO | No | `"coarse"`<br>`"medium"`<br>`"fine"` |
| `hint` | Testo opzionale che nomina le parti da cercare, ad es. "personaggio di un gioco con spada e armatura" (predefinito: vuoto). | STRING | No | - |

### Input immagine

Mostrato quando `source` è impostato su `"image"`. Tripo genera prima un modello dall'immagine, poi lo segmenta.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | L'immagine utilizzata per generare il modello che verrà segmentato. | IMAGE | Sì | - |
| `granularity` | Quanto finemente il modello viene suddiviso in parti (predefinito: "medium"). | COMBO | No | `"coarse"`<br>`"medium"`<br>`"fine"` |
| `hint` | Testo opzionale che nomina le parti da cercare, ad es. "personaggio di un gioco con spada e armatura" (predefinito: vuoto). | STRING | No | - |

**Note:**

- `granularity` e `hint` sono condivisi da entrambe le opzioni di `source` e sono opzionali. Quando `hint` viene lasciato vuoto, nessun hint viene inviato al servizio.
- Quando `source` è `"model"`, sono accettati solo modelli GLB. Altri formati, come le mesh quad (FBX), devono essere convertiti prima con Tripo: Convert model (GLTF).
- Viene eseguito il polling dell'attività finché non raggiunge uno stato terminale, con una durata stimata di circa 180 secondi. Se Tripo restituisce un risultato di segmentazione incompleto, il nodo segnala un errore.
- Badge del prezzo: circa 0,85 USD quando `source` è `"image"` e circa 0,55 USD quando `source` è `"model"` (valori mostrati come approssimativi).

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `segment task_id` | ID attività dell'attività di segmentazione, utilizzabile come input per altri nodi Tripo. | SEGMENT_TASK_ID |
| `model task_id` | Il modello che è stato segmentato (generato dall'immagine o importato). | MODEL_TASK_ID |
| `GLB` | Il file del modello 3D segmentato. | FILE3DGLB |
| `part_names` | Nomi delle parti separati da virgola. | STRING |
| `parts` | Descrizione fornita da Tripo delle parti trovate. | STRING |
| `mask` | Immagine maschera prodotta dalla segmentazione. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSmartSegmentNode/it.md)

---
**Source fingerprint (SHA-256):** `ba041da49e20b1ac085770078cce6ac87ef70eee927ba0ee9e5655a058893f1c`
