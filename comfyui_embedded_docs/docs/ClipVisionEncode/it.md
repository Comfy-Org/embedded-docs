# ClipVisionEncode

Il nodo `CLIP Vision Encode` è un nodo di codifica delle immagini in ComfyUI, utilizzato per convertire le immagini di input in vettori di caratteristiche visive tramite il modello CLIP Vision. Questo nodo è un importante ponte che collega la comprensione delle immagini e del testo, ed è ampiamente utilizzato in vari flussi di lavoro di generazione e elaborazione di immagini AI.

**Funzionalità del nodo**

- **Estrazione delle caratteristiche dell'immagine**: Converte le immagini di input in vettori di caratteristiche ad alta dimensionalità
- **Ponte multimodale**: Fornisce una base per l'elaborazione congiunta di immagini e testo
- **Generazione condizionata**: Fornisce condizioni visive per la generazione condizionata basata su immagini

## Input

| Nome parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `clip_vision` | Modello CLIP Vision, solitamente caricato tramite il nodo CLIPVisionLoader | CLIP_VISION |
| `image` | L'immagine di input da codificare | IMAGE |
| `crop` | Metodo di ritaglio dell'immagine, opzioni: center (ritaglio centrale), none (nessun ritaglio) | Menu a tendina |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| CLIP_VISION_OUTPUT | Caratteristiche visive codificate | CLIP_VISION_OUTPUT |

Questo oggetto di output contiene:

- `last_hidden_state`: L'ultimo stato nascosto
- `image_embeds`: Vettore di embedding dell'immagine
- `penultimate_hidden_states`: Il penultimo stato nascosto
- `mm_projected`: Risultato della proiezione multimodale (se disponibile)

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipVisionEncode/it.md)
