# Renderizza mesh

Questo nodo renderizza una mesh 3D in un'immagine 2D tramite ray-casting da una singola vista. Può restituire la mesh texturizzata, i colori dei vertici, una superficie solida ombreggiata, le normali di superficie o la profondità. La camera e la trasformazione opzionale del modello possono provenire da un visualizzatore Load3D / Preview3D; se non è collegata alcuna camera, viene automaticamente inquadrata una vista frontale predefinita.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `mesh` | La mesh 3D da renderizzare. | MESH | Sì | — |
| `mode` | Cosa renderizzare. auto: texture se presente, altrimenti colori dei vertici, altrimenti clay ombreggiato. (predefinito: "auto") | COMBO | Sì | `"auto"`<br>`"texture"`<br>`"vertex colors"`<br>`"solid"`<br>`"normal"`<br>`"depth"` |
| `width` | Larghezza dell'immagine renderizzata in pixel. (predefinito: 1024) | INT | Sì | da 64 a 4096 (passo 8) |
| `height` | Altezza dell'immagine renderizzata in pixel. (predefinito: 1024) | INT | Sì | da 64 a 4096 (passo 8) |
| `background` | Colore di sfondo usato per i pixel non coperti dalla mesh. (predefinito: "#000000") | COLOR | Sì | — |
| `model_3d_info` | Trasformazione del modello dallo stesso visualizzatore Load3D / Preview3D. Collegalo con camera_info per corrispondere all'inquadratura del visualizzatore. | LOAD3D_MODEL_INFO | No | — |
| `camera_info` | Camera da un visualizzatore Load3D / Preview3D o da un nodo Create Camera Info. Se non ne è collegata nessuna, viene automaticamente inquadrata una vista frontale predefinita. | LOAD3D_CAMERA | No | — |

Nota: viene renderizzato solo il primo elemento di una mesh in batch — se il batch di mesh contiene più di un elemento, il nodo registra un avviso e usa il primo. La modalità `texture` richiede che la mesh abbia sia una texture sia gli UV, e la modalità `vertex colors` richiede i colori dei vertici; se i dati per la modalità selezionata non sono disponibili, il nodo ripiega sul rendering solido ombreggiato. La modalità `normal` usa le normali morbide dei vertici della mesh quando presenti, altrimenti la normale per faccia. In modalità `depth`, le superfici più vicine appaiono più luminose (vicino = bianco) e i pixel non coperti dalla mesh restano neri. `model_3d_info` e `camera_info` sono pensati per essere collegati insieme dallo stesso visualizzatore Load3D / Preview3D, così il rendering corrisponde all'inquadratura del visualizzatore.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `image` | L'immagine renderizzata della mesh. | IMAGE |
| `mask` | Una maschera che vale 1.0 dove è stata renderizzata la mesh e 0.0 altrove. | MASK |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RenderMesh/it.md)

---
**Source fingerprint (SHA-256):** `d23e85a904520eb2dfed899eb3e6a9cf45c980df00c034503687ac4eccc66ac4`
