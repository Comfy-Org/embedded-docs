# StringContains

Il nodo StringContains verifica se una determinata stringa contiene una sottostringa specificata. Può eseguire questo controllo con corrispondenza sensibile o non sensibile alle maiuscole/minuscole, restituendo un risultato booleano che indica se la sottostringa è stata trovata all'interno della stringa principale.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `string` | La stringa di testo principale in cui cercare | STRING | Sì | - |
| `substring` | Il testo da cercare all'interno della stringa principale | STRING | Sì | - |
| `case_sensitive` | Determina se la ricerca deve distinguere maiuscole e minuscole (predefinito: true) | BOOLEAN | No | - |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `contains` | Restituisce true se la sottostringa viene trovata nella stringa, altrimenti false | BOOLEAN |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringContains/it.md)

---
**Source fingerprint (SHA-256):** `9e85e51bc32c4041a66de8d5b11475aba3120eee1e8c5a37fedfaa470746888c`
