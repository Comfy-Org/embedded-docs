# TripoImageToModelNodeV2

Il nodo Tripo: Image to Model trasforma una singola immagine di riferimento in un modello 3D utilizzando il servizio image-to-model di Tripo. Carica l'immagine, invia un'attività di generazione, attende il completamento dell'attività e restituisce il file 3D risultante insieme all'ID dell'attività. Questo è un nodo API, quindi richiede una chiave API Comfy valida.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | L'immagine di riferimento usata per generare il modello 3D. | IMAGE | Sì | — |
| `model_version` | La versione del modello da usare per la generazione. Se non impostata, il nodo utilizza come fallback la versione v3.1 (20260211) di Tripo. | COMBO | No | Elenco delle versioni del modello Tripo |
| `texture` | Genera mappe di texture. Se disattivato, restituisce solo la geometria e ignora `pbr` (predefinito: true). | BOOLEAN | No | true<br>false |
| `pbr` | Mappe di materiale PBR (colore di base, metallico, rugosità, normale). Richiede `texture` (predefinito: true). | BOOLEAN | No | true<br>false |
| `model_seed` | Seed usato per la fase di generazione della geometria (predefinito: 42). | INT | No | da 0 a 2147483647 |
| `orientation` | Impostazione di orientamento applicata al modello generato (predefinito: DEFAULT). | COMBO | No | Opzioni di orientamento Tripo, predefinito `DEFAULT` |
| `texture_seed` | Seed usato per la fase di generazione della texture (predefinito: 42). | INT | No | da 0 a 2147483647 |
| `texture_quality` | detailed = texture HD, extreme = texture Ultra 8K (predefinito: "standard"). | COMBO | No | "standard"<br>"detailed"<br>"extreme" |
| `texture_alignment` | Come vengono allineate le texture sulla geometria generata (predefinito: "original_image"). | COMBO | No | "original_image"<br>"geometry" |
| `face_limit` | Numero massimo di facce. -1 lascia che Tripo scelga in modo adattivo (circa 1.4M di facce su v3.x standard, 2M su detailed). Tripo applica limiti silenziosamente: v2.5 a 500,000, mesh quad a 150,000 (predefinito: -1). | INT | No | da -1 a 2000000 |
| `quad` | Output mesh quad. Tripo fornisce le mesh quad come FBX, quindi il risultato arriva sull'output FBX e l'output GLB rimane vuoto (predefinito: false). | BOOLEAN | No | true<br>false |
| `geometry_quality` | Il livello di qualità della geometria generata (predefinito: "standard"). | COMBO | No | "standard"<br>"detailed" |
| `smart_low_poly` | Mesh low-poly con topologia pulita in stile artigianale (500-20,000 facce, quad 500-10,000). Ideale per soggetti semplici; quelli complessi potrebbero fallire (predefinito: false). | BOOLEAN | No | true<br>false |
| `auto_size` | Ridimensiona i modelli con texture alla loro dimensione reale in metri. Tripo memorizza la dimensione come trasformazione di scena del modello e la incorpora quando il modello viene convertito, riggato o retargettato; ignorato senza texture (predefinito: true). | BOOLEAN | No | true<br>false |

**Note:**

- `image` è obbligatorio; il nodo genera un errore se non viene fornita alcuna immagine.
- Quando `smart_low_poly` è abilitato e `face_limit` è impostato a un valore diverso da -1, il limite deve essere compreso tra 500 e 20,000 per le mesh triangolari, oppure tra 500 e 10,000 quando `quad` è abilitato. Gli altri valori generano un errore.
- Quando `texture` è disabilitato, `pbr` viene forzato su off indipendentemente dalla sua impostazione, e `auto_size` non ha alcun effetto.
- Un `face_limit` di -1 viene inviato a Tripo come "nessun limite", lasciando che il servizio scelga in modo adattivo.
- Un nuovo formato di file 3D che il nodo non può restituire (qualsiasi cosa diversa da GLB o FBX) causa un errore.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `model task_id` | L'ID dell'attività Tripo del job di generazione. | MODEL_TASK_ID |
| `GLB` | Il modello generato come file GLB. Vuoto quando `quad` è abilitato. | FILE3DGLB |
| `FBX` | Il modello generato come file FBX. Popolato solo quando `quad` è abilitato. | FILE3DFBX |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToModelNodeV2/it.md)

---
**Source fingerprint (SHA-256):** `c8c069432f67a019995b9f4dedbf5ca3f7594ae4004104277068106821189c11`
