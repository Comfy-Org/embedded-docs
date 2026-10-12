# Anteprima come Testo

PreviewAny converte qualsiasi valore di input in testo leggibile, così da poterlo ispezionare. Le stringhe passano invariate, i numeri e i booleani diventano testo semplice, mentre gli altri tipi di dati vengono serializzati in JSON quando possibile (con fallback alla loro forma di stringa semplice se la serializzazione fallisce). Il testo risultante viene mostrato nell'interfaccia utente e restituito anche come output di tipo stringa per ulteriori elaborazioni.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `source` | Accetta qualsiasi tipo di dato in input per la visualizzazione in anteprima. Se non viene fornito alcun valore, l'anteprima mostra 'None'. | ANY | Sì | Qualsiasi tipo di dato |

**Comportamento di conversione**

- I valori di tipo STRING vengono mostrati esattamente come forniti.
- I valori di tipo INT, FLOAT o BOOLEAN vengono convertiti in testo semplice.
- Qualsiasi altro valore non vuoto viene convertito in testo JSON con un rientro di 4 spazi; se la conversione fallisce, il nodo ricorre alla forma testuale semplice del valore. Se anche questa fallisce, l'anteprima mostra il messaggio 'source exists, but could not be serialized.'
- Se non è connesso alcun valore o il valore è vuoto, l'anteprima mostra 'None'.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `result` | Il valore di input convertito in formato testo. Lo stesso testo viene anche visualizzato nell'interfaccia utente. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PreviewAny/it.md)

---
**Source fingerprint (SHA-256):** `66b5283b2d7d43e679c0bc6cdcad54c92539a986763333972e722b39c7963be8`
