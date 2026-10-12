# Ritaglia immagine

Il nodo Crop Image estrae una sezione rettangolare da un'immagine di input. Si definisce la regione da mantenere specificando le coordinate del suo angolo superiore sinistro e la sua larghezza e altezza. Il nodo restituisce quindi la porzione ritagliata dell'immagine originale.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `image` | L'immagine di input da ritagliare. | IMAGE | Sì | N/A |
| `crop_region` | Definisce l'area rettangolare da estrarre dall'immagine. È specificata da `x` (inizio orizzontale), `y` (inizio verticale), `width` e `height`. Se la regione definita si estende oltre i bordi dell'immagine, verrà automaticamente adattata per rientrare nelle dimensioni dell'immagine. | BOUNDINGBOX | Sì | N/A |

**Nota sui vincoli della regione:** La regione di ritaglio viene automaticamente vincolata a rimanere entro i limiti dell'immagine di input. Se la coordinata `x` o `y` specificata è maggiore della larghezza o dell'altezza dell'immagine, verrà impostata alla posizione massima valida. La larghezza e l'altezza risultanti del ritaglio verranno adattate in modo che la regione non superi i bordi dell'immagine.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `image` | La sezione ritagliata dell'immagine di input originale. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCropV2/it.md)

---
**Source fingerprint (SHA-256):** `c09c68a46c4b0418903a627b98dd848264d53b58bd3ffe99e40ef125b15b3aae`
