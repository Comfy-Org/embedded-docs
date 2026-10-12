# Confronta Testo

Il nodo StringCompare confronta due stringhe di testo utilizzando diversi metodi di confronto. Può verificare se una stringa inizia con un'altra, termina con un'altra, oppure se entrambe le stringhe sono esattamente uguali. Il confronto può essere eseguito considerando o meno le differenze tra maiuscole e minuscole.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `string_a` | La prima stringa da confrontare | STRING | Sì | - |
| `string_b` | La seconda stringa con cui confrontare | STRING | Sì | - |
| `mode` | Il metodo di confronto da usare (predefinito: "Starts With") | COMBO | Sì | "Starts With"<br>"Ends With"<br>"Equal" |
| `case_sensitive` | Indica se considerare le differenze tra maiuscole e minuscole durante il confronto (predefinito: true) | BOOLEAN | No | - |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `output` | Restituisce true se la condizione di confronto è soddisfatta, false altrimenti | BOOLEAN |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringCompare/it.md)

---
**Source fingerprint (SHA-256):** `18599228c31543f270afde0f3b838512ee12d1998b8de42c4d3e7852b1a5d8b2`
