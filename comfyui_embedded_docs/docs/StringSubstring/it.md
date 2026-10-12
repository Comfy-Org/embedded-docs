# Sottostringa

Il nodo StringSubstring estrae una porzione di testo da una stringa più grande. Richiede una posizione iniziale e una posizione finale per definire la sezione da estrarre, quindi restituisce il testo compreso tra queste due posizioni.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `string` | La stringa di testo di input da cui estrarre. Supporta testo su più righe. | STRING | Sì | - |
| `start` | L'indice della posizione iniziale della sottostringa. Il primo carattere si trova all'indice 0. | INT | Sì | - |
| `end` | L'indice della posizione finale della sottostringa. Il carattere in questa posizione non è incluso nel risultato. | INT | Sì | - |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `output` | La sottostringa estratta dal testo di input, contenente tutti i caratteri dalla posizione `start` fino alla posizione `end` (esclusa). | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringSubstring/it.md)

---
**Source fingerprint (SHA-256):** `fd3ec23bbfe3a51f5481f1b0fe8b77f66e08469bb2a4bd3e266a7607f014e544`
