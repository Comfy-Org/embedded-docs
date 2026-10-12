# ClipTextEncodeSdxl

Questo nodo è progettato per codificare l'input testuale utilizzando un modello CLIP specificamente personalizzato per l'architettura SDXL. Utilizza un sistema a doppio encoder (CLIP-L e CLIP-G) per elaborare le descrizioni testuali, ottenendo una generazione di immagini più accurata.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `clip` | Istanza del modello CLIP utilizzata per la codifica del testo. | CLIP |
| `width` | Specifica la larghezza dell'immagine in pixel; valore predefinito 1024. | INT |
| `height` | Specifica l'altezza dell'immagine in pixel; valore predefinito 1024. | INT |
| `crop_w` | Larghezza dell'area di ritaglio in pixel; valore predefinito 0. | INT |
| `crop_h` | Altezza dell'area di ritaglio in pixel; valore predefinito 0. | INT |
| `target_width` | Larghezza target per l'immagine di output; valore predefinito 1024. | INT |
| `target_height` | Altezza target per l'immagine di output; valore predefinito 1024. | INT |
| `text_g` | Descrizione testuale globale per la descrizione complessiva della scena. | STRING |
| `text_l` | Descrizione testuale locale per la descrizione dei dettagli. | STRING |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `CONDITIONING` | Contiene il testo codificato e le informazioni di condizionamento necessarie per la generazione dell'immagine. | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipTextEncodeSdxl/it.md)
