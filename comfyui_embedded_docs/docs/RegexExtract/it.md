# RegexExtract

Il nodo RegexExtract cerca pattern nel testo usando espressioni regolari. Può trovare la prima corrispondenza, tutte le corrispondenze, gruppi specifici dalle corrispondenze o tutti i gruppi in più corrispondenze. Il nodo supporta vari flag regex per la distinzione tra maiuscole e minuscole, la corrispondenza multilinea e il comportamento dotall.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `string` | Il testo di input in cui cercare i pattern | STRING | Sì | - |
| `regex_pattern` | Il pattern dell'espressione regolare da cercare | STRING | Sì | - |
| `mode` | La modalità di estrazione determina quali parti delle corrispondenze vengono restituite (predefinito: "First Match") | COMBO | Sì | "First Match"<br>"All Matches"<br>"First Group"<br>"All Groups" |
| `case_insensitive` | Indica se ignorare la distinzione tra maiuscole e minuscole durante la corrispondenza (predefinito: True) | BOOLEAN | No | - |
| `multiline` | Indica se trattare la stringa come più righe (predefinito: False) | BOOLEAN | No | - |
| `dotall` | Indica se il punto (.) corrisponde ai caratteri di nuova riga (predefinito: False) | BOOLEAN | No | - |
| `group_index` | L'indice del gruppo di cattura da estrarre quando si usano le modalità di gruppo (predefinito: 1) | INT | No | 0-100 |

**Nota:** Quando si usano le modalità "First Group" o "All Groups", il parametro `group_index` specifica quale gruppo di cattura estrarre. Il gruppo 0 rappresenta l'intera corrispondenza, mentre i gruppi 1+ rappresentano i gruppi di cattura numerati nel pattern dell'espressione regolare.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `output` | Il testo estratto in base alla modalità e ai parametri selezionati | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RegexExtract/it.md)

---
**Source fingerprint (SHA-256):** `a879e4fd7429edfada44b2f5778bb71e537a000be6c25d3f67359b9ee802812f`
