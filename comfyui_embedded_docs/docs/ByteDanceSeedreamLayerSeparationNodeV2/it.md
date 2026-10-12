# ByteDanceSeedreamLayerSeparationNodeV2

ByteDance Seedream 5.0 Layer Separation decompone un'immagine in una lastra di sfondo più fino a 16 livelli trasparenti riposizionabili, ciascuno con ordine di sovrapposizione, bounding box, nome e descrizione. Restituisce lo sfondo, le immagini per livello con maschere, i riquadri di posizionamento e uno stack di livelli pronto per la modifica. Il selettore `model` sceglie tra Seedream 5.0 Pro e il più veloce Seedream 5.0 Flash.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello Seedream usato per la separazione. "seedream 5.0 pro" (predefinito) offre la massima qualità di separazione ed espone anche un controllo `prompt_optimization`; "seedream 5.0 flash" è più veloce ed economico e non ha un controllo di ottimizzazione del prompt. | DYNAMIC_COMBO | Sì | "seedream 5.0 pro"<br>"seedream 5.0 flash" |

### Input di Seedream 5.0 Pro e 5.0 Flash

Questi input sono disponibili con entrambi i modelli.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | L'immagine da separare. Esattamente un'immagine, di almeno 512x512 pixel, con rapporto d'aspetto compreso tra 1:16 e 16:1. Gli input più grandi di circa 4 MP vengono ridimensionati verso il basso prima del caricamento. | IMAGE | Sì | Immagine singola |
| `prompt` | Come separare l'immagine. Lasciare vuoto per rilevare automaticamente e separare tutti gli elementi principali. Descrivi gli elementi in linguaggio naturale per controllare la separazione, oppure individua regioni esatte con tag `<bbox>left top right bottom</bbox>` (coordinate in per mille da 0 a 1000). Predefinito: stringa vuota. | STRING | Sì | Testo multiriga |
| `size` | Livello di risoluzione dell'output. "auto" segue la dimensione dell'immagine di input (limitata all'intervallo 1K-2K). Predefinito: "auto". | COMBO | Sì | "auto"<br>"1K"<br>"1.5K"<br>"2K" |
| `seed` | Seed da usare per la generazione. Predefinito: 42. | INT | Sì | da 0 a 2147483647 |
| `watermark` | Indica se aggiungere una filigrana "AI generated" alle immagini. Predefinito: false. | BOOLEAN | Sì | false<br>true |
| `crop_layers` | Geometria degli output batch layers/masks (`layer_stack` non è interessato ed è sempre ritagliato in modo aderente). Full canvas: ogni livello su una tela delle dimensioni della base, nella posizione del suo bounding box - ricomponi direttamente con ImageCompositeMasked. Dimensione minima: ogni livello ritagliato sul suo bounding box (con padding fino al livello più grande per il batching) - tensor molto più piccoli; ricostruisci il posizionamento con Layers From Bounding Boxes usando l'output `bboxes`. Predefinito: false (full canvas). | BOOLEAN | Sì | false (full canvas)<br>true (minimal size) |

### Input solo per Seedream 5.0 Pro

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt_optimization` | Modalità di ottimizzazione del prompt: "standard" offre una qualità superiore, "fast" un tempo di generazione più breve. Disponibile solo con Seedream 5.0 Pro. Predefinito: "standard". | COMBO | Sì | "standard"<br>"fast" |

**Nota:** L'input `image` deve essere una singola immagine; i batch non sono supportati. L'immagine deve essere di almeno 512x512 pixel con un rapporto d'aspetto compreso tra 1:16 e 16:1. Seedream 5.0 Flash non ha un input `prompt_optimization`.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `base_image` | L'immagine di base (lastra di sfondo) su cui si impilano i livelli. | IMAGE |
| `base_mask` | Trasparenza dell'immagine di base (1 = trasparente, convenzione di LoadImage); attualmente sempre completamente opaca. | MASK |
| `layers` | Livelli trasparenti ordinati dal basso verso l'alto. Modalità full canvas: posizionati su una tela nera delle dimensioni della base, nella posizione del loro bounding box. Modalità dimensione minima: ritagliati sul loro bounding box, ancorati in alto a sinistra, con padding fino al livello più grande. | IMAGE |
| `masks` | Trasparenza per livello, allineata per indice al batch `layers` (1 = trasparente, convenzione di LoadImage). Per una composizione in stile ImageCompositeMasked, aggiungere prima InvertMask. | MASK |
| `bboxes` | Un riquadro di posizionamento per livello, allineato per indice al batch `layers` (fornisci entrambi, più `masks`, a Layers From Bounding Boxes per ricostruire il posizionamento per livello): `{x, y, width, height, metadata: {name, desc, z_index, native_size, content_rect, flags}}`. `content_rect = [left, top, width, height]` è la regione di contenuto del livello all'interno della sua cornice; si posiziona sulla tela nella posizione del riquadro più quell'offset. | BOUNDING_BOX |
| `layer_stack` | Documento di livelli pronto per la modifica per Create Layered Image: la lastra di base più ogni elemento come livello separato, denominato e ritagliato in modo aderente, nella sua posizione reale e nel suo ordine di sovrapposizione. Collegalo direttamente oppure estendilo con Add Layer. | LAYERS |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamLayerSeparationNodeV2/it.md)

---
**Source fingerprint (SHA-256):** `b106ca63d37aea68079f0032a1f7dfeefee9f759c71bb1605bbfe66c3d9dad62`
