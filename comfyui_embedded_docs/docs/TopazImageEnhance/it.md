# TopazImageEnhance

Il nodo Topaz Image Enhance fornisce upscaling e miglioramento delle immagini conformi agli standard del settore. Elabora una singola immagine di input utilizzando un modello AI basato su cloud per migliorare qualità, dettaglio e risoluzione. Il nodo offre un controllo granulare sul processo di miglioramento, incluse opzioni per la guida creativa, il focus sul soggetto e la preservazione del volto.

Questa versione del nodo è legacy ed è contrassegnata come deprecata nell'interfaccia.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Il modello AI da utilizzare per il miglioramento dell'immagine. | COMBO | Sì | `"Reimagine"` |
| `image` | L'immagine di input da migliorare. È supportata una sola immagine. | IMAGE | Sì | - |
| `prompt` | Prompt testuale opzionale per guidare l'upscaling creativo (predefinito: vuoto). | STRING | No | - |
| `subject_detection` | Controlla su quale parte dell'immagine si concentra il miglioramento (predefinito: "All"). | COMBO | No | `"All"`<br>`"Foreground"`<br>`"Background"` |
| `face_enhancement` | Migliora i volti (se presenti) durante l'elaborazione (predefinito: True). | BOOLEAN | No | - |
| `face_enhancement_creativity` | Imposta il livello di creatività per il miglioramento dei volti (predefinito: 0.0). | FLOAT | No | 0.0 - 1.0 |
| `face_enhancement_strength` | Controlla quanto sono nitidi i volti migliorati rispetto allo sfondo (predefinito: 1.0). | FLOAT | No | 0.0 - 1.0 |
| `crop_to_fill` | Per impostazione predefinita, viene applicato il letterboxing all'immagine quando le proporzioni dell'output differiscono. Abilita per ritagliare l'immagine in modo da riempire le dimensioni dell'output (predefinito: False). | BOOLEAN | No | - |
| `output_width` | Il valore zero indica il calcolo automatico (di solito sarà la dimensione originale o `output_height` se specificato) (predefinito: 0). | INT | No | 0 - 32000 |
| `output_height` | Il valore zero indica di restituire in output la stessa altezza dell'originale o la larghezza di output (predefinito: 0). | INT | No | 0 - 32000 |
| `creativity` | Controlla il livello di creatività complessivo del miglioramento (predefinito: 3). | INT | No | 1 - 9 |
| `face_preservation` | Preserva l'identità facciale dei soggetti (predefinito: True). | BOOLEAN | No | - |
| `color_preservation` | Preserva i colori originali (predefinito: True). | BOOLEAN | No | - |

**Nota:** Questo nodo può elaborare solo una singola immagine di input. Fornire un batch di più immagini causerà un errore.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `image` | L'immagine di output migliorata. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhance/it.md)

---
**Source fingerprint (SHA-256):** `1a0e708cdea9ec4f92f7f3aaabbdeea06a8fdab2f91a45ad2dea15f2bc2e8fa3`
