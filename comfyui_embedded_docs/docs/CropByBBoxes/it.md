# Ritaglia per riquadri di delimitazione

Il nodo CropByBBoxes estrae e ridimensiona regioni rettangolari specifiche da un batch di immagini in input. Utilizza le coordinate dei bounding box fornite per definire l'area da ritagliare da ciascuna immagine. Le regioni ritagliate vengono poi ridimensionate a una dimensione di output specificata, con opzioni per allungare il ritaglio o aggiungere padding per preservarne le proporzioni originali.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `image` | Il batch di immagini di input da ritagliare. | IMAGE | Sì | - |
| `bboxes` | L'elenco dei bounding box che definiscono le regioni da ritagliare. Questo input è forzato, quindi deve essere collegato. | BOUNDINGBOX | Sì | - |
| `output_width` | La larghezza a cui viene ridimensionato ciascun ritaglio (predefinita: 512). | INT | No | 64 - 4096 |
| `output_height` | L'altezza a cui viene ridimensionato ciascun ritaglio (predefinita: 512). | INT | No | 64 - 4096 |
| `padding` | Padding aggiuntivo in pixel aggiunto su ciascun lato del bounding box prima del ritaglio (predefinito: 0). | INT | No | 0 - 1024 |
| `keep_aspect` | Se allungare il ritaglio per adattarlo alla dimensione di output oppure riempire con pixel neri per preservarne le proporzioni (predefinito: "stretch"). | COMBO | No | `"stretch"`<br>`"pad"` |

**Nota:** Il nodo elabora un frame immagine alla volta. Se vengono forniti più bounding box per un singolo frame, calcola un'unica regione di ritaglio che è l'unione (il più piccolo rettangolo che contiene tutti i bounding box) di tutti i bounding box forniti. Se una regione di ritaglio calcolata non è valida (ad es. larghezza o altezza pari a zero), il nodo creerà un ritaglio di fallback dalla parte superiore centrale dell'immagine.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `image` | Tutte le regioni ritagliate e ridimensionate, impilate in un unico batch di immagini. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CropByBBoxes/it.md)

---
**Source fingerprint (SHA-256):** `7524d629e61f5af2475f819bc9431d4f4173feb5ad59f9bcf81d822330fb3e22`
