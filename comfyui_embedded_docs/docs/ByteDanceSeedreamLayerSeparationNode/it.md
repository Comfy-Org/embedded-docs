# ByteDance Seedream 5.0 Pro Separazione livelli (legacy)

ByteDance Seedream 5.0 Pro Layer Separation scompone un'immagine in una lastra di sfondo più fino a 16 livelli trasparenti riposizionabili, ciascuno con ordine di sovrapposizione, bounding box, nome e descrizione. Restituisce lo sfondo, le immagini per livello con maschere, i riquadri di posizionamento e uno stack di livelli pronto per la modifica.

**Nota:** questo nodo è contrassegnato come deprecato nel codice sorgente.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `image` | L'immagine da separare. Esattamente un'immagine, almeno 512x512 pixel, rapporto d'aspetto tra 1:16 e 16:1. Gli input più grandi di circa 4MP vengono ridimensionati verso il basso prima del caricamento. | IMAGE | Sì | Immagine singola |
| `prompt` | Come separare l'immagine. Lasciare vuoto per rilevare automaticamente e separare tutti gli elementi principali. Descrivere gli elementi in linguaggio naturale per controllare la separazione, oppure individuare regioni esatte con i tag `<bbox>left top right bottom</bbox>` (coordinate 0-1000 per mille). Predefinito: stringa vuota. | STRING | Sì | Testo multilinea |
| `size` | Livello di risoluzione dell'output. "auto" segue la dimensione dell'immagine di input (limitata all'intervallo 1K-2K). Predefinito: "auto". | COMBO | Sì | "auto"<br>"1K"<br>"1.5K"<br>"2K" |
| `seed` | Seed da utilizzare per la generazione. Predefinito: 0. | INT | Sì | 0 a 2147483647 |
| `prompt_optimization` | Modalità di ottimizzazione del prompt: "standard" offre una qualità superiore, "fast" un tempo di generazione più breve. Predefinito: "standard". | COMBO | No | "standard"<br>"fast" |
| `watermark` | Indica se aggiungere una filigrana "AI generated" alle immagini. Predefinito: false. | BOOLEAN | No | false<br>true |
| `crop_layers` | Geometria degli output batch di livelli/maschere (layer_stack non è influenzato ed è sempre ritagliato in modo aderente). Canvas completo: ogni livello su una tela delle dimensioni della base, nella posizione del suo bounding box - ricomponi direttamente con ImageCompositeMasked. Dimensione minima: ogni livello ritagliato al suo bounding box (con padding fino al livello più grande per il batching) - tensori molto più piccoli; ricostruisci il posizionamento con Layers From Bounding Boxes usando l'output bboxes. Predefinito: false (canvas completo). | BOOLEAN | No | false (canvas completo)<br>true (dimensione minima) |

Nota: l'input `image` deve essere una singola immagine; i batch non sono supportati. L'immagine deve essere di almeno 512x512 pixel con un rapporto d'aspetto tra 1:16 e 16:1.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `base_image` | L'immagine di base (lastra di sfondo) su cui si sovrappongono i livelli. | IMAGE |
| `base_mask` | Trasparenza dell'immagine di base (1 = trasparente, convenzione LoadImage); attualmente sempre completamente opaca. | MASK |
| `layers` | Livelli trasparenti ordinati dal basso verso l'alto. Modalità canvas completo: posizionati su una tela nera delle dimensioni della base, nella posizione del loro bounding box. Modalità dimensione minima: ritagliati al loro bounding box, ancorati in alto a sinistra, con padding fino al livello più grande. | IMAGE |
| `masks` | Trasparenza per livello, allineata per indice con il batch layers (1 = trasparente, convenzione LoadImage). Per una composizione in stile ImageCompositeMasked, aggiungere prima InvertMask. | MASK |
| `bboxes` | Un riquadro di posizionamento per livello, allineato per indice con il batch layers (passare entrambi, insieme a masks, a Layers From Bounding Boxes per ricostruire il posizionamento per livello): `{x, y, width, height, metadata: {name, desc, z_index, native_size, content_rect, flags}}`. `content_rect = [left, top, width, height]` è la regione di contenuto del livello all'interno del suo frame; si colloca sulla tela nella posizione del riquadro più quell'offset. | BOUNDING_BOX |
| `layer_stack` | Documento di livelli pronto per la modifica per Create Layered Image: la lastra di base più ogni elemento come livello con nome proprio, ritagliato in modo aderente, nella sua posizione reale e ordine di sovrapposizione. Collegare direttamente oppure estendere con Add Layer. | LAYERS |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamLayerSeparationNode/it.md)

---
**Source fingerprint (SHA-256):** `7c0d8ca76ee4b8d6a34fec2edbb753982a05160540ae1d1867efb79c9f9c5498`
