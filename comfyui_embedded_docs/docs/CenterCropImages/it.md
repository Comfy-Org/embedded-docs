# Ritaglia Immagine (Centro)

Il nodo Center Crop Images ritaglia un'immagine dal centro secondo una larghezza e un'altezza specificate. Calcola la regione centrale dell'immagine di input ed estrae un'area rettangolare delle dimensioni definite. Se la dimensione di ritaglio richiesta è maggiore dell'immagine, il ritaglio verrà limitato ai bordi dell'immagine.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `image` | L'immagine di input da ritagliare. | IMAGE | Sì | - |
| `width` | La larghezza dell'area di ritaglio (predefinita: 512). | INT | Sì | 1 to 8192 |
| `height` | L'altezza dell'area di ritaglio (predefinita: 512). | INT | Sì | 1 to 8192 |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | L'immagine risultante dopo l'operazione di ritaglio centrale. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CenterCropImages/it.md)

---
**Source fingerprint (SHA-256):** `1b22529602e3aca816b583158c4bb5aa51de3478ac8068c2a69a3392fb12746f`
