# VaeDecodeShapeTrellis

Questo nodo decodifica le rappresentazioni latenti di forma di Trellis2 in una mesh 3D. Utilizza un VAE per convertire dati latenti sparsi di forma in geometria mesh e restituisce anche i dati di suddivisione della forma generati durante la decodifica. Il nodo supporta input latenti singoli e in batch e regola automaticamente l'orientamento della mesh al sistema di coordinate previsto.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `samples` | I campioni latenti da decodificare, inclusi il tensore dei campioni e i dati sparsi delle coordinate. Il dizionario latente può anche contenere campi opzionali: `coord_counts` per forme in batch, `coord_resolution` per controllare la risoluzione della mesh e `model_frame` per l'orientamento delle coordinate. | LATENT | Sì | None |
| `vae` | Il modello VAE utilizzato per decodificare il latente di forma in una mesh. | VAE | Sì | None |

### Note su `samples`

- L'input `samples` è un dizionario latente che deve contenere il tensore `samples` e le coordinate sparse `coords`.
- Se `coord_counts` è presente, deve essere un tensore 1D di interi non negativi e la somma di tutti i conteggi deve essere uguale al numero totale di righe delle coordinate. Ogni conteggio rappresenta una forma nel batch.
- Se `coord_resolution` è fornito, la risoluzione della mesh viene calcolata come `coord_resolution * 16`. In caso contrario, viene usato il buffer di risoluzione integrato del VAE (valore predefinito: 1024).
- Se `model_frame` è impostato su `"z_up"`, i vertici della mesh decodificata vengono ruotati da un sistema di coordinate Z-up alla convenzione Y-up usata da glTF. Il valore predefinito è `"y_up"`.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `mesh` | La mesh 3D decodificata, contenente le posizioni dei vertici e gli indici delle facce. Quando si decodificano più forme, le mesh vengono restituite come un singolo tensore impilato se condividono tutte la stessa forma, oppure come un batch compatto a dimensione variabile in caso contrario. | MESH |
| `shape_subdivides` | Dati di suddivisione della forma prodotti in ogni fase del processo di decodifica. | SHAPE_SUBDIVIDES |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeDecodeShapeTrellis/it.md)

---
**Source fingerprint (SHA-256):** `28bd0f69c0ea58ca499f6523471cf6071c041c21242126715d56f362484377a2`
