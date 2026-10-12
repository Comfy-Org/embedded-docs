# ReveImageRemixNode

Il nodo Reve Image Remix utilizza l'API Reve per generare una nuova immagine. Combina una o più immagini di riferimento con un prompt testuale per creare una nuova immagine remixata basata sulla descrizione fornita.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Versione del modello da usare per il remix. | DYNAMIC_COMBO | Sì | `"reve-remix@20250915"`<br>`"reve-remix-fast@20251030"` |
| `prompt` | Descrizione testuale dell'immagine desiderata. Può includere tag XML img per fare riferimento a immagini specifiche tramite indice, ad es. `<img>0</img>`, `<img>1</img>`, ecc. (predefinito: vuoto) | STRING | Sì | da 1 a 2560 caratteri |
| `upscale` | Ingrandisci l'immagine generata. Può comportare un costo aggiuntivo. (predefinito: "disabled") | DYNAMIC_COMBO | No | `"disabled"`<br>`"enabled"` |
| `remove_background` | Rimuovi lo sfondo dall'immagine generata. Può comportare un costo aggiuntivo. (predefinito: false) | BOOLEAN | No | `true`<br>`false` |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati sono non deterministici indipendentemente dal seed. (predefinito: 0) | INT | No | da 0 a 2147483647 |

### Input del modello (condivisi da reve-remix@20250915 e reve-remix-fast@20251030)

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `aspect_ratio` | Rapporto d'aspetto dell'immagine di output. (predefinito: "auto") | COMBO | Sì | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `test_time_scaling` | Valori più alti producono immagini migliori ma costano più crediti. (predefinito: 1) | INT | No | da 1 a 5 |

### Input di ingrandimento (compaiono quando `upscale` è impostato su "enabled")

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `upscale_factor` | Fattore di ingrandimento (2x, 3x o 4x). (predefinito: 2) | INT | No | da 2 a 4 |

### Input di riferimento

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Slot espandibile: collega da 1 a 6 immagini (`image_1` a `image_6`) da usare come base visiva per il remix. È richiesta almeno un'immagine di riferimento. | IMAGE | Sì | da 1 a 6 immagini |

**Nota:** Il prompt deve contenere tra 1 e 2560 caratteri. Quando `aspect_ratio` è impostato su "auto", il servizio determina il rapporto d'aspetto dell'immagine di output. Un valore di `test_time_scaling` pari a 1 applica l'elaborazione standard; valori più alti migliorano la qualità dell'immagine ma consumano più crediti. Il widget `upscale_factor` compare solo quando `upscale` è impostato su "enabled". I risultati del remix sono non deterministici indipendentemente dal valore del seed. Questo nodo è deprecato.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `image` | La nuova immagine generata dal processo di remix di Reve. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageRemixNode/it.md)

---
**Source fingerprint (SHA-256):** `9cf0c6653aa620179ed5d888a455fe248a240b0db04687eade6652730eb5f003`
