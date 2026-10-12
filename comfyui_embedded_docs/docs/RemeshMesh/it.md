# RemeshMesh

Remesh Mesh ricostruisce una mesh con una tassellatura pulita e uniforme campionando un campo di distanza a banda stretta attorno alla superficie originale ed estraendolo con Dual Contouring. Questo normalizza topologie disordinate, non-manifold o auto-intersecanti ed è pensato per essere eseguito prima di Decimate Mesh per raggiungere un numero esatto di facce. L'elaborazione viene eseguita sul dispositivo di calcolo attivo e la mesh di output rimane saldata.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `mesh` | La mesh di input da rimagliare. | MESH | Sì | — |
| `resolution` | Risoluzione della griglia voxel (densità di output). 256 ~ 100k facce, 512 ~ 1M. Per un numero esatto di facce, proseguire con Decimate Mesh. (predefinito: 512) | INT | Sì | 32 - 2048 |
| `sign_mode` | Modalità di estrazione della superficie. "udf" è robusta per input disordinati/non-manifold; "sdf" produce una superficie singola pulita con recupero di feature nette tramite QEF (Quadratic Error Function), ma richiede un winding coerente. Selezionando una modalità si rivelano le relative sotto-opzioni. (predefinito: "udf") | DYNAMIC_COMBO | Sì | "udf"<br>"sdf" |
| `band` | Larghezza della banda stretta in unità voxel. In modalità UDF applica anche un offset alla superficie. (avanzato, predefinito: 1.0) | FLOAT | Sì | 0.5 - 4.0 |
| `project_back` | Interpola linearmente i vertici verso la superficie originale (0 = DC puro, 1 = agganciato). (avanzato, predefinito: 0.0) | FLOAT | Sì | 0.0 - 1.0 |
| `fix_poles` | Collassa coppie di vertici con valenza 3 (artefatto T-junction di DC). (avanzato, predefinito: false) | BOOLEAN | Sì | true / false |
| `smooth_iters` | Iterazioni di smoothing Taubin (0 = disattivato). 2-3 puliscono artefatti a scaletta di DC; valori più alti smoothano eccessivamente i bordi QEF. (predefinito: 0) | INT | Sì | 0 - 20 |
| `drop_small_components` | Scarta le componenti sotto questa frazione del numero di facce della più grande. 0 disabilita. (avanzato, predefinito: 0.01) | FLOAT | Sì | 0.0 - 0.5 |
| `precluster_max_verts` | Limita il numero di vertici di input prima delle query sul campo; gli input superiori a questo valore vengono prima decimati in cluster fino a tale soglia. Previene OOM su mesh enormi. (avanzato, predefinito: 20,000,000) | INT | Sì | 0 - 100,000,000 |

### Input della modalità "udf"

Questi parametri compaiono quando `sign_mode` è impostato su `"udf"`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `qef` | Posizionamento dual-vertex tramite QEF (Quadratic Error Function) per bordi più netti. (avanzato, predefinito: false) | BOOLEAN | No | true / false |
| `drop_inverted_components` | Scarta le componenti chiuse con normali rivolte verso l'interno (volume negativo) — il guscio interno dell'UDF. (avanzato, predefinito: false) | BOOLEAN | No | true / false |
| `drop_enclosed_components` | Scarta le componenti all'interno della bbox della più grande che non superano un raycast point-in-mesh. Disabilitare per parti annidate legittime. (avanzato, predefinito: false) | BOOLEAN | No | true / false |

### Input della modalità "sdf"

Questi parametri compaiono quando `sign_mode` è impostato su `"sdf"`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `qef` | Posizionamento dual-vertex tramite QEF (Quadratic Error Function) (recupera feature nette) rispetto al centroide di attraversamento degli edge. (predefinito: true) | BOOLEAN | No | true / false |
| `manifold` | Manifold Dual Contouring: 1-4 vertici duali/voxel per casi multi-sheet. Più lento. (predefinito: false) | BOOLEAN | No | true / false |

Nota: l'opzione `qef` ha un valore predefinito diverso a seconda della modalità selezionata — false in modalità "udf", true in modalità "sdf". Quando `precluster_max_verts` è maggiore di 0 e la mesh di input ha più vertici di questo valore, la mesh viene decimata in cluster fino a quel target prima delle query sul campo. Dopo l'elaborazione, il nodo mostra la variazione del numero di facce da input a output direttamente sul nodo (ad esempio, "faces: 1.23M → 200K (-84%)").

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `mesh` | La mesh rimagliata con tassellatura uniforme e topologia saldata. I colori dei vertici vengono preservati quando presenti sull'input; eventuali UV, normali e tangenti non vengono trasferiti. | MESH |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemeshMesh/it.md)

---
**Source fingerprint (SHA-256):** `aa9b7e4465196fab81a4a484ca9dd03d999b4621a611aed2b39d618e53702a06`
