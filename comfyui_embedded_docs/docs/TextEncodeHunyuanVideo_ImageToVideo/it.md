# TextEncodeHunyuanVideo_ImageToVideo

Il nodo TextEncodeHunyuanVideo_ImageToVideo crea dati di condizionamento per la generazione da immagine a video combinando un prompt testuale con le informazioni visive di un'immagine di riferimento. Utilizza un modello CLIP per elaborare sia il testo sia gli embedding dell'immagine da un output di CLIP vision, quindi genera token che combinano queste due fonti in base all'impostazione `image_interleave`.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `clip` | Il modello CLIP utilizzato per la tokenizzazione e la codifica. | CLIP | Sì | - |
| `clip_vision_output` | Gli embedding visivi da un modello CLIP vision che forniscono il contesto immagine per l'immagine di riferimento. | CLIP_VISION_OUTPUT | Sì | - |
| `prompt` | La descrizione testuale per guidare la generazione del video. Supporta input multilinea e prompt dinamici. Il prompt viene formattato usando un template che chiede al modello di descrivere il video in base all'immagine di riferimento, coprendo aspetti come contenuto principale, dettagli degli oggetti, azioni, sfondo e angolazioni della telecamera. | STRING | Sì | - |
| `image_interleave` | Quanto l'immagine influenza il risultato rispetto al prompt testuale. Un numero più alto indica una maggiore influenza del prompt testuale. Questa è un'impostazione avanzata (valore predefinito: 2). | INT | Sì | 1-512 |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `CONDITIONING` | I dati di condizionamento che combinano informazioni testuali e visive per la generazione del video. | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeHunyuanVideo_ImageToVideo/it.md)

---
**Source fingerprint (SHA-256):** `016b87ead6f7a6ca61eff220e57f59252018cc78e80ec8cff5b83223b8f90f73`
