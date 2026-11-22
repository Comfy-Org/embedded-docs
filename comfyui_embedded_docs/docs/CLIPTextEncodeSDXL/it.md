# ClipTextEncodeSdxl

Questo nodo è progettato per codificare l'input testuale utilizzando un modello CLIP specificamente personalizzato per l'architettura SDXL. Utilizza un sistema a doppio encoder (CLIP-L e CLIP-G) per elaborare le descrizioni testuali, ottenendo una generazione di immagini più accurata.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `clip` | Istanza del modello CLIP utilizzata per la codifica del testo. | CLIP |
| `larghezza` | Specifica la larghezza dell'immagine in pixel; valore predefinito 1024. | INT |
| `altezza` | Specifica l'altezza dell'immagine in pixel; valore predefinito 1024. | INT |
| `ritaglio_larghezza` | Larghezza dell'area di ritaglio in pixel; valore predefinito 0. | INT |
| `ritaglio_altezza` | Altezza dell'area di ritaglio in pixel; valore predefinito 0. | INT |
| `larghezza_target` | Larghezza target per l'immagine di output; valore predefinito 1024. | INT |
| `altezza_target` | Altezza target per l'immagine di output; valore predefinito 1024. | INT |
| `testo_g` | Descrizione testuale globale per la descrizione complessiva della scena. | STRING |
| `testo_l` | Descrizione testuale locale per la descrizione dei dettagli. | STRING |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `CONDITIONING` | Contiene il testo codificato e le informazioni di condizionamento necessarie per la generazione dell'immagine. | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSDXL/it.md)
