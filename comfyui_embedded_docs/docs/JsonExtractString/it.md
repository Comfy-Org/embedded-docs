# JsonExtractString

Il nodo JsonExtractString analizza una stringa di testo alla ricerca del primo oggetto JSON valido ed estrae il valore associato a una chiave specifica, convertito in stringa. Qualsiasi testo prima o dopo l'oggetto JSON viene ignorato, quindi il nodo funziona anche con blocchi di codice Markdown e con risposte del modello che racchiudono il JSON in testo aggiuntivo. Se non viene trovato alcun oggetto JSON valido, se la chiave non viene trovata o se il valore è null, il nodo restituisce una stringa vuota.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `json_string` | Il testo in cui cercare un oggetto JSON. Questo campo supporta input multilinea e può contenere testo circostante o delimitatori di codice Markdown. | STRING | Sì | N/A |
| `key` | La chiave specifica di cui estrarre il valore dall'oggetto JSON. Questo campo supporta solo input su una singola riga. | STRING | Sì | N/A |

**Nota:** Il nodo estrae valori solo da oggetti JSON (dizionari). Prova ogni `{` nell'input in ordine e decodifica dalla prima posizione che produce un oggetto JSON valido, quindi il testo iniziale o finale viene ignorato. Se non è possibile decodificare alcun oggetto JSON o la chiave specificata non esiste al suo interno, l'output è una stringa vuota. Se il valore associato alla chiave è `null`, il nodo restituisce anch'esso una stringa vuota. I valori che non sono stringhe vengono restituiti come la loro rappresentazione in formato stringa.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `output` | Il valore stringa estratto dal JSON per la chiave specificata, oppure una stringa vuota se l'estrazione non riesce. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/JsonExtractString/it.md)

---
**Source fingerprint (SHA-256):** `ca697fd3bd2d4de764372470ad1102b345d9d60f6df1c151fa0573e85fab2382`
