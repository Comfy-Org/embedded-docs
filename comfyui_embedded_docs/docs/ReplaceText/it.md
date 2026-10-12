# ReplaceText

Il nodo Replace Text esegue una semplice sostituzione di testo. Cerca una specifica porzione di testo all'interno dell'input e sostituisce ogni occorrenza con una nuova porzione di testo. L'operazione viene applicata a tutti gli input di testo forniti al nodo.

**Nota:** questo nodo è deprecato ed è stato sostituito dall'altro nodo Replace Text.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `text` | Il testo da elaborare. | STRING | Sì | - |
| `find` | Testo da trovare (predefinito: stringa vuota). | STRING | Sì | - |
| `replace` | Testo con cui sostituire (predefinito: stringa vuota). | STRING | Sì | - |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `text` | Il testo elaborato con tutte le occorrenze del testo `find` sostituite dal testo `replace`. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceText/it.md)

---
**Source fingerprint (SHA-256):** `38beeabc232b19efedf2dcf4e2490f537d9a07d60c89de2811b7a4bddb98cf57`
