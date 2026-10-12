# Crea Bounding Boxes

Questo nodo fornisce un'interfaccia canvas per disegnare bounding box attorno a oggetti o regioni di testo in un'immagine. Restituisce le coordinate delle bounding box nello spazio in pixel, dati strutturati degli elementi compatibili con la formattazione dei prompt di Ideogram e un'immagine di anteprima che mostra le caselle disegnate con etichette e palette di colori.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `background` | Immagine opzionale usata come sfondo nel canvas e nell'anteprima. | IMAGE | No | - |
| `bboxes` | Bounding box, elementi o una stringa JSON per inizializzare il canvas. Un nuovo valore a monte inizializza il canvas; le modifiche apportate sul canvas hanno priorità e vengono mantenute finché il valore a monte non cambia di nuovo. | BOUNDING_BOX, ARRAY, STRING | No | - |
| `width` | Larghezza del canvas e della griglia in pixel per le bounding box (predefinito: 1024). | INT | Sì | 64 a 16384 (passo: 16) |
| `height` | Altezza del canvas e della griglia in pixel per le bounding box (predefinito: 1024). | INT | Sì | 64 a 16384 (passo: 16) |
| `editor_state` | Disegna bounding box e imposta per ciascuna casella tipo, testo, descrizione e palette di colori. Inizia con l'elemento di sfondo per primo e quello in primo piano per ultimo. | BOUNDING_BOXES | Sì | - |
| `last_incoming` | Stato interno gestito dal canvas: il valore bboxes a monte che lo ha inizializzato per ultimo. Lasciare vuoto per reinizializzare il canvas dall'input bboxes alla successiva esecuzione. | BOUNDING_BOXES | No | - |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `preview` | Un'immagine RGB che mostra il canvas con tutte le bounding box renderizzate, incluse etichette, campioni della palette di colori e testo descrittivo. | IMAGE |
| `bboxes` | Un elenco di bounding box in coordinate pixel, in cui ogni casella contiene i valori x, y, larghezza e altezza. | BOUNDING_BOX |
| `elements` | Un array strutturato di oggetti elemento, ciascuno contenente tipo, coordinate della bounding box (normalizzate 0-1000), testo (per il tipo testo), descrizione e palette di colori. | ARRAY |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateBoundingBoxes/it.md)

---
**Source fingerprint (SHA-256):** `dc5545dffefdccf14f3919ff4d9966dbfd1a497dcd64e1863556d5728659ee94`
