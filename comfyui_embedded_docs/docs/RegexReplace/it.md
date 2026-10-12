# Sostituisci Testo (Regex)

Il nodo RegexReplace trova e sostituisce testo nelle stringhe utilizzando espressioni regolari. Consente di cercare pattern di testo e sostituirli con nuovo testo, con opzioni per controllare il funzionamento della corrispondenza dei pattern, inclusi sensibilità alle maiuscole/minuscole, corrispondenza multilinea e limitazione del numero di sostituzioni.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `string` | La stringa di testo di input in cui cercare e sostituire | STRING | Sì | - |
| `regex_pattern` | Il pattern di espressione regolare da cercare nella stringa di input | STRING | Sì | - |
| `replace` | Il testo di sostituzione da usare al posto dei pattern corrispondenti | STRING | Sì | - |
| `case_insensitive` | Se abilitato, fa sì che la corrispondenza dei pattern ignori le differenze tra maiuscole e minuscole (predefinito: True) | BOOLEAN | No | - |
| `multiline` | Se abilitato, modifica il comportamento di ^ e $ in modo che corrispondano all'inizio/fine di ogni riga anziché solo all'inizio/fine dell'intera stringa (predefinito: False) | BOOLEAN | No | - |
| `dotall` | Se abilitato, il carattere punto (.) corrisponderà a qualsiasi carattere, inclusi i caratteri di nuova riga. Se disabilitato, i punti non corrisponderanno ai caratteri di nuova riga (predefinito: False) | BOOLEAN | No | - |
| `count` | Numero massimo di sostituzioni da effettuare. Impostare a 0 per sostituire tutte le occorrenze (predefinito). Impostare a 1 per sostituire solo la prima corrispondenza, 2 per le prime due corrispondenze, ecc. (predefinito: 0) | INT | No | 0-100 |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `output` | La stringa modificata con le sostituzioni specificate applicate | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexReplace/it.md)

---
**Source fingerprint (SHA-256):** `58d4ec055aa5901b0e536bb2ca6993053ea85a9269d09cdcdf584df935d6876d`
