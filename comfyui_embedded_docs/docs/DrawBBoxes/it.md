# Disegna BBoxes

Il nodo DrawBBoxes visualizza i risultati del rilevamento degli oggetti disegnando bounding box, etichette e punteggi di confidenza su un'immagine. Se non viene fornita un'immagine di input, crea una tela vuota sufficientemente grande da contenere tutte le bounding box disegnate. Supporta l'elaborazione in batch, consentendo di disegnare insiemi diversi di rilevamenti per più immagini o di ripetere gli stessi rilevamenti su un batch.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `image` | L'immagine o le immagini di input su cui disegnare le bounding box. Se non fornita, verrà generata una tela vuota. | IMAGE | No | - |
| `bboxes` | Una lista di dizionari di bounding box. Ogni dizionario deve contenere le chiavi `x`, `y`, `width`, `height` e, facoltativamente, `label` e `score`. | BOUNDINGBOX | Sì | - |

**Vincoli di input:**
*   L'input `bboxes` è obbligatorio e deve essere fornito.
*   Il nodo gestisce automaticamente formati di input diversi per `bboxes`. Un singolo dizionario verrà applicato a tutte le immagini nel batch. Una lista semplice di dizionari verrà trattata come lo stesso insieme di rilevamenti per ogni immagine. Una lista di liste consente di specificare rilevamenti diversi per ciascuna immagine nel batch.
*   Se non viene fornito un `image`, il nodo creerà un'immagine vuota con dimensioni sufficientemente grandi da contenere tutte le bounding box fornite, con una dimensione minima predefinita di 640x640.
*   Il campo `label` in ciascun dizionario di bounding box viene confrontato con le classi del dataset COCO. Se l'etichetta non è una classe COCO riconosciuta, verrà ignorata e non verrà disegnata alcuna etichetta testuale per quella bounding box.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `out_image` | L'immagine o le immagini di output con le bounding box, le etichette e i punteggi di confidenza disegnati sopra. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DrawBBoxes/it.md)

---
**Source fingerprint (SHA-256):** `ce5da10ec83e579515d70b7184fc78dfa04df4c514faccdcb75130212f56c84f`
