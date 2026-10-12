# Livelli da Riquadri di Selezione

Questo nodo converte un batch di immagini e le relative bounding box in uno stack di livelli, creando un livello per ogni fotogramma e posizionando ciascun livello in base alla sua box corrispondente. Usalo quando un nodo restituisce livelli come batch, perché un batch porta con sé un solo posizionamento per ogni fotogramma e le posizioni individuali andrebbero altrimenti perse.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | Batch di immagini; ogni fotogramma diventa un livello. | IMAGE | Sì | — |
| `bboxes` | Box di posizionamento, allineate per indice con il batch di immagini. Accetta bounding box (x, y, larghezza, altezza), elementi normalizzati (con una "bbox" — questi richiedono canvas_width/canvas_height per essere risolti in pixel), o una stringa JSON di uno dei due. I fotogrammi senza una box corrispondente vengono posizionati all'origine. La larghezza/altezza di una box scala il livello per adattarlo. metadata.name (o desc) e metadata.z_index vengono usati quando presenti, e metadata.content_rect (relativo al fotogramma) ritaglia il fotogramma al suo contenuto reale. | BOUNDING_BOX, ARRAY, o STRING | Sì | — |
| `mask` | Trasparenza per fotogramma, allineata per indice con il batch di immagini (1 = trasparente, convenzione LoadImage). | MASK | No | — |
| `layers` | Stack di livelli a cui aggiungere. Lascia non connesso per iniziare un nuovo stack. | LAYERS | No | — |
| `crop_to_content` | Ritaglia ogni fotogramma a metadata.content_rect dove presente e posiziona il contenuto nella posizione della box più l'offset del rect. Lascia attivo per batch i cui fotogrammi sono padding — mantiene solo il contenuto reale nella sua posizione corretta. (predefinito: true) | BOOLEAN | No | true<br>false |
| `canvas_width` | Larghezza della canvas del documento. 0 la deriva dai livelli posizionati. (predefinito: 0) | INT | No | 0 to MAX_RESOLUTION |
| `canvas_height` | Altezza della canvas del documento. 0 la deriva dai livelli posizionati. (predefinito: 0) | INT | No | 0 to MAX_RESOLUTION |

Note:

- `bboxes` e `mask` devono essere allineati per indice con `image`: l'ennesima box e l'ennesimo fotogramma mask corrispondono all'ennesimo fotogramma image. I fotogrammi senza una box corrispondente vengono posizionati all'origine.
- Quando `bboxes` contiene elementi normalizzati (con una "bbox"), `canvas_width` e `canvas_height` devono essere forniti affinché quelle posizioni normalizzate possano essere risolte in pixel.
- `canvas_width` e `canvas_height` devono entrambi essere maggiori di 0 per impostare esplicitamente la canvas del documento. Se uno dei due è 0, la canvas viene derivata dai livelli posizionati o ereditata dallo stack `layers` connesso.
- Quando `layers` è connesso, i nuovi livelli vengono aggiunti ad esso e ricevono valori z-index superiori al più alto z-index già presente nello stack.
- Quando `crop_to_content` è abilitato e un fotogramma ha un metadata.content_rect, il fotogramma viene ritagliato a quel rect e la scalatura larghezza/altezza della box non viene applicata; invece, l'offset del rect viene aggiunto alla posizione della box.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `LAYERS` | Lo stack di livelli, pronto per Create Layered Image. | LAYERS |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LayersFromBoundingBoxes/it.md)

---
**Source fingerprint (SHA-256):** `a70956bf0d7ea8bdbd16767ed8b19600b274a6eeb745728f95219578adc73712`
