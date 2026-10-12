# Scala Immagine alla Dimensione Massima

Il nodo ImageScaleToMaxDimension ridimensiona le immagini per adattarle entro una dimensione massima specificata, mantenendo le proporzioni originali. Calcola se l'immagine è orientata verticalmente o orizzontalmente, quindi ridimensiona la dimensione maggiore per corrispondere alla dimensione target, adattando proporzionalmente la dimensione minore. Il nodo supporta molteplici metodi di upscaling per diversi requisiti di qualità e prestazioni.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `image` | L'immagine di input da ridimensionare | IMAGE | Sì | - |
| `upscale_method` | Il metodo di interpolazione utilizzato per ridimensionare l'immagine (predefinito: "area") | STRING | Sì | "area"<br>"lanczos"<br>"bilinear"<br>"nearest-exact"<br>"bilinear"<br>"bicubic" |
| `largest_size` | La dimensione massima per l'immagine ridimensionata (predefinito: 512) | INT | Sì | da 0 a 16384 |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `image` | L'immagine ridimensionata con la dimensione maggiore corrispondente alla dimensione specificata | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScaleToMaxDimension/it.md)

---
**Source fingerprint (SHA-256):** `83eba56d9f673fb570edc6504fd82f1274ead1d3e055a1a8bcc207c178388015`
