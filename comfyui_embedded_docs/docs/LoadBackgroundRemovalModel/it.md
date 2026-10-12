# LoadBackgroundRemovalModel

Carica un modello di rimozione dello sfondo da un file. Questo nodo prepara il modello in modo che possa essere utilizzato da altri nodi per rimuovere gli sfondi dalle immagini.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `bg_removal_name` | Il modello utilizzato per rimuovere gli sfondi dalle immagini. Seleziona dall'elenco dei file di modello per la rimozione dello sfondo disponibili. | COMBO | Sì | Elenco dei file di modello disponibili (ordinati alfabeticamente) |

Nota: se il file selezionato non contiene un modello di rimozione dello sfondo valido, il nodo genera un RuntimeError.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `bg_model` | Il modello di rimozione dello sfondo caricato, pronto per essere utilizzato da altri nodi per l'elaborazione delle immagini. | BACKGROUND_REMOVAL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadBackgroundRemovalModel/it.md)

---
**Source fingerprint (SHA-256):** `76f6536eae849a8b63f46f11c6afcf8c89774e4e89a5976e051253acc6108bcc`
