# FLUX 3 Image Layout Prompt

Costruisce la tabella di layout che FLUX 3 Image legge da un prompt. Prende gli elementi disegnati nel nodo Create Bounding Boxes e li aggiunge al prompt come elenco di riquadri, ciascuno con un id, le sue coordinate e la sua descrizione. Cita un riquadro nel prompt come `<obj_N>` per collegare le parole a quella regione, quindi collega l'output all'input prompt del nodo FLUX 3 Image. Se non è collegato alcun elemento, il prompt viene restituito invariato.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `prompt` | Il testo del prompt. Cita il riquadro N come `<obj_N>` per collegarvi le parole. | STRING | Sì | - |
| `element` | Gli elementi da inserire nel layout, presi dal nodo Create Bounding Boxes. Le palette di colori non vengono usate, quindi descrivi i colori nella descrizione. | ARRAY | Sì | - |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `prompt` | Il prompt con la tabella di layout dei riquadri aggiunta, pronto per essere passato al nodo FLUX 3 Image. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3LayoutPrompt/it.md)

---
**Source fingerprint (SHA-256):** `ac8f61701c8da0a6fc8361aeebf7fc5e7aa338ce6ad8689718904caa9c53e3b8`
