# Tronca testo

Questo nodo accorcia il testo troncandolo a una lunghezza massima specificata. Prende qualsiasi testo in input e restituisce solo la prima parte, fino al numero di caratteri impostato. È un modo semplice per assicurarsi che il testo non superi una certa dimensione.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `text` | La stringa di testo da troncare. | STRING | Sì | N/A |
| `max_length` | Lunghezza massima del testo. Il testo verrà troncato dopo questo numero di caratteri (predefinito: 77). | INT | Sì | 1 to 10000 |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `string` | Il testo troncato, contenente solo i primi `max_length` caratteri dell'input. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TruncateText/it.md)

---
**Source fingerprint (SHA-256):** `b23c92af425be8f7b15d793bbe7f321cab6f7f3137a995bb9724948ae00145e4`
