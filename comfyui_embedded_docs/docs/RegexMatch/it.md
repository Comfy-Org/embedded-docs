# Confronta Testo

Il nodo RegexMatch verifica se una stringa di testo contiene una corrispondenza per un determinato pattern di espressione regolare. Cerca nella stringa di input e restituisce un semplice risultato sì/no che indica se il pattern è stato trovato in qualsiasi punto del testo. Puoi modificare il funzionamento della ricerca abilitando opzioni come la corrispondenza senza distinzione tra maiuscole e minuscole o la modalità multilinea.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `string` | La stringa di testo in cui cercare corrispondenze | STRING | Sì | - |
| `regex_pattern` | Il pattern di espressione regolare da confrontare con la stringa | STRING | Sì | - |
| `case_insensitive` | Indica se ignorare la distinzione tra maiuscole e minuscole durante la corrispondenza (predefinito: True) | BOOLEAN | No | - |
| `multiline` | Indica se abilitare la modalità multilinea per la corrispondenza regex (predefinito: False) | BOOLEAN | No | - |
| `dotall` | Indica se abilitare la modalità dotall per la corrispondenza regex (predefinito: False) | BOOLEAN | No | - |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `matches` | Restituisce True se il pattern regex corrisponde a qualsiasi parte della stringa di input, False in caso contrario | BOOLEAN |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexMatch/it.md)

---
**Source fingerprint (SHA-256):** `4f0fa717bde7406e42d9a99599eab546690140166d2bb01bb4fde3c5d60e0397`
