# Ridimensiona Immagine/Maschera

The Resize Image/Mask node fornisce molteplici metodi per modificare le dimensioni di un'immagine o maschera di input. Può ridimensionare tramite un moltiplicatore, impostare dimensioni specifiche, corrispondere alla dimensione di un altro input oppure adattarsi in base al numero di pixel, utilizzando diversi metodi di interpolazione per la qualità.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `input` | L'immagine o maschera da ridimensionare. | IMAGE or MASK | Sì | N/A |
| `resize_type` | Il metodo utilizzato per determinare la nuova dimensione. I parametri richiesti cambiano in base al tipo selezionato. | COMBO | Sì | `SCALE_BY`<br>`SCALE_DIMENSIONS`<br>`SCALE_LONGER_DIMENSION`<br>`SCALE_SHORTER_DIMENSION`<br>`SCALE_WIDTH`<br>`SCALE_HEIGHT`<br>`SCALE_TOTAL_PIXELS`<br>`MATCH_SIZE` |
| `multiplier` | Il fattore di scala. Richiesto quando `resize_type` è `SCALE_BY` (predefinito: 1.00). | FLOAT | No | 0.01 to 8.0 |
| `width` | La larghezza desiderata in pixel. Richiesto quando `resize_type` è `SCALE_DIMENSIONS` o `SCALE_WIDTH` (predefinito: 512). | INT | No | 0 to 8192 |
| `height` | L'altezza desiderata in pixel. Richiesto quando `resize_type` è `SCALE_DIMENSIONS` o `SCALE_HEIGHT` (predefinito: 512). | INT | No | 0 to 8192 |
| `crop` | Il metodo di ritaglio da applicare quando le dimensioni non corrispondono al rapporto d'aspetto. Disponibile solo quando `resize_type` è `SCALE_DIMENSIONS` o `MATCH_SIZE` (predefinito: "center"). | COMBO | No | `"disabled"`<br>`"center"` |
| `longer_size` | La dimensione desiderata per il lato più lungo dell'immagine. Richiesto quando `resize_type` è `SCALE_LONGER_DIMENSION` (predefinito: 512). | INT | No | 0 to 8192 |
| `shorter_size` | La dimensione desiderata per il lato più corto dell'immagine. Richiesto quando `resize_type` è `SCALE_SHORTER_DIMENSION` (predefinito: 512). | INT | No | 0 to 8192 |
| `megapixels` | Il numero totale di megapixel desiderato. Richiesto quando `resize_type` è `SCALE_TOTAL_PIXELS` (predefinito: 1.0). | FLOAT | No | 0.01 to 16.0 |
| `match` | Un'immagine o maschera le cui dimensioni verranno utilizzate per ridimensionare l'input. Richiesto quando `resize_type` è `MATCH_SIZE`. | IMAGE or MASK | No | N/A |
| `scale_method` | L'algoritmo di interpolazione utilizzato per il ridimensionamento (predefinito: "area"). | COMBO | Sì | `"nearest-exact"`<br>`"bilinear"`<br>`"area"`<br>`"bicubic"`<br>`"lanczos"` |

**Nota:** Il parametro `crop` è disponibile e rilevante solo quando il `resize_type` è impostato su `SCALE_DIMENSIONS` o `MATCH_SIZE`. Quando si utilizzano `SCALE_WIDTH` o `SCALE_HEIGHT`, l'altra dimensione viene ridimensionata automaticamente per mantenere il rapporto d'aspetto originale.

## Output

| Nome dell'output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `resized` | L'immagine o maschera ridimensionata, corrispondente al tipo di dato dell'input. | IMAGE or MASK |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImageMaskNode/it.md)

---
**Source fingerprint (SHA-256):** `9ac0b153608ac971bb11d9d12ebd1f0f4d6e926604e8727a1bc3a311d95fbc03`
