# MagnificImageUpscalerPreciseV2Node

Il nodo Magnific Image Upscale (Precise V2) esegue un upscaling delle immagini ad alta fedeltà con un controllo preciso su nitidezza, grana e miglioramento dei dettagli. Elabora le immagini tramite un'API esterna, supportando una risoluzione massima in output fino a 10060×10060 pixel. Il nodo offre diversi stili di elaborazione e può ridimensionare automaticamente l'input verso il basso se l'output richiesto supererebbe la dimensione massima consentita.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | L'immagine di input da sottoporre a upscaling. È richiesta esattamente un'immagine. Le dimensioni minime sono 160x160 pixel. Le proporzioni devono essere comprese tra 1:3 e 3:1. | IMAGE | Sì | - |
| `scale_factor` | Il moltiplicatore di upscaling desiderato. | COMBO | Sì | `"2x"`<br>`"4x"`<br>`"8x"`<br>`"16x"` |
| `flavor` | Stile di elaborazione: sublime per uso generale, photo per fotografie, photo_denoiser per foto rumorose. | COMBO | Sì | `"sublime"`<br>`"photo"`<br>`"photo_denoiser"` |
| `sharpen` | Intensità della nitidezza dell'immagine. Valori più alti aumentano la definizione dei bordi e la chiarezza. Predefinito: 7. | INT | Sì | 0 a 100 |
| `smart_grain` | Miglioramento intelligente di grana/trama per evitare che l'immagine appaia troppo liscia o artificiale. Predefinito: 7. | INT | Sì | 0 a 100 |
| `ultra_detail` | Controlla i dettagli fini, le texture e i micro-dettagli aggiunti durante l'upscaling. Predefinito: 30. | INT | Sì | 0 a 100 |
| `auto_downscale` | Ridimensiona automaticamente l'immagine di input verso il basso se l'output supererebbe la risoluzione massima. Predefinito: False. Questa è un'impostazione avanzata. | BOOLEAN | Sì | - |

**Nota:** Se `auto_downscale` è disabilitato e la dimensione di output richiesta (dimensioni input × `scale_factor`) supera 10060x10060 pixel, il nodo genererà un errore. Quando `auto_downscale` è abilitato, il nodo tenterà di trovare un fattore di scala ottimale che mantenga minima la perdita di qualità.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `image` | L'immagine risultante dopo l'upscaling. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MagnificImageUpscalerPreciseV2Node/it.md)

---
**Source fingerprint (SHA-256):** `aeb2b3569fd7b1d2417890586b8ac84ff921c4405f63f190188af93044ccfd28`
