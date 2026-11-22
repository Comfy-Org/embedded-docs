# Topaz Miglioramento Immagine (Legacy)

Il nodo Topaz Image Enhance fornisce upscaling e miglioramento delle immagini conformi agli standard del settore. Elabora una singola immagine di input utilizzando un modello AI basato su cloud per migliorare qualità, dettaglio e risoluzione. Il nodo offre un controllo granulare sul processo di miglioramento, incluse opzioni per la guida creativa, il focus sul soggetto e la preservazione del volto.

Questa versione del nodo è legacy ed è contrassegnata come deprecata nell'interfaccia.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `modello` | Il modello AI da utilizzare per il miglioramento dell'immagine. | COMBO | Sì | `"Reimagine"` |
| `immagine` | L'immagine di input da migliorare. È supportata una sola immagine. | IMAGE | Sì | - |
| `prompt` | Prompt testuale opzionale per guidare l'upscaling creativo (predefinito: vuoto). | STRING | No | - |
| `rilevamento_soggetto` | Controlla su quale parte dell'immagine si concentra il miglioramento (predefinito: "All"). | COMBO | No | `"All"`<br>`"Foreground"`<br>`"Background"` |
| `miglioramento_volto` | Migliora i volti (se presenti) durante l'elaborazione (predefinito: True). | BOOLEAN | No | - |
| `creatività_miglioramento_volto` | Imposta il livello di creatività per il miglioramento dei volti (predefinito: 0.0). | FLOAT | No | 0.0 - 1.0 |
| `intensità_miglioramento_volto` | Controlla quanto sono nitidi i volti migliorati rispetto allo sfondo (predefinito: 1.0). | FLOAT | No | 0.0 - 1.0 |
| `ritaglia_per_riempire` | Per impostazione predefinita, viene applicato il letterboxing all'immagine quando le proporzioni dell'output differiscono. Abilita per ritagliare l'immagine in modo da riempire le dimensioni dell'output (predefinito: False). | BOOLEAN | No | - |
| `larghezza_output` | Il valore zero indica il calcolo automatico (di solito sarà la dimensione originale o `output_height` se specificato) (predefinito: 0). | INT | No | 0 - 32000 |
| `altezza_output` | Il valore zero indica di restituire in output la stessa altezza dell'originale o la larghezza di output (predefinito: 0). | INT | No | 0 - 32000 |
| `creatività` | Controlla il livello di creatività complessivo del miglioramento (predefinito: 3). | INT | No | 1 - 9 |
| `preservazione_volto` | Preserva l'identità facciale dei soggetti (predefinito: True). | BOOLEAN | No | - |
| `preservazione_colore` | Preserva i colori originali (predefinito: True). | BOOLEAN | No | - |

**Nota:** Questo nodo può elaborare solo una singola immagine di input. Fornire un batch di più immagini causerà un errore.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `image` | L'immagine di output migliorata. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhance/it.md)

---
**Source fingerprint (SHA-256):** `1a0e708cdea9ec4f92f7f3aaabbdeea06a8fdab2f91a45ad2dea15f2bc2e8fa3`
