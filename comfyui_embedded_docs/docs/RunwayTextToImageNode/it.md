# RunwayTextToImageNode

Il nodo Runway Text to Image genera immagini da prompt testuali utilizzando il modello Gen 4 di Runway. Puoi fornire una descrizione testuale e, facoltativamente, includere un'immagine di riferimento per guidare il processo di generazione dell'immagine. Il nodo gestisce la comunicazione con l'API e restituisce l'immagine generata.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt testuale per la generazione (predefinito: "") | STRING | Sì | - |
| `ratio` | Proporzioni per l'immagine generata | COMBO | Sì | "16:9"<br>"1:1"<br>"21:9"<br>"2:3"<br>"3:2"<br>"4:5"<br>"5:4"<br>"9:16"<br>"9:21" |
| `reference_image` | Immagine di riferimento opzionale per guidare la generazione | IMAGE | No | - |

**Nota:** L'immagine di riferimento deve avere dimensioni non superiori a 7999x7999 pixel e un rapporto d'aspetto compreso tra 0,5 e 2,0. Quando viene fornita un'immagine di riferimento, questa guida il processo di generazione dell'immagine.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `output` | L'immagine generata in base al prompt testuale e all'immagine di riferimento opzionale | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayTextToImageNode/it.md)

---
**Source fingerprint (SHA-256):** `c9403da2e9ad8f663d3eea32eb549843696262e4472fc8d58c1f56ef9cc5aa7d`
