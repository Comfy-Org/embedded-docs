# StringFormat

## Panoramica

Questo nodo formatta il testo utilizzando il metodo di formattazione delle stringhe di Python. Funziona come un modello in cui si definisce un pattern di testo con segnaposto, quindi si forniscono i valori per riempire tali segnaposto. Supporta tutte le opzioni e funzionalità di formattazione di Python.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `f_string` | Il modello di stringa di formato con segnaposto (predefinito: `{a}`). Supporta input su più righe. | STRING | Sì | N/A |
| `values` | Input dinamico per fornire valori con cui riempire i segnaposto nella stringa di formato. È possibile aggiungere più input di valori secondo necessità. | STRING | Sì | N/A |

**Nota sull'input `values`:** Questo input è dinamico e può essere espanso per includere più valori denominati. Ogni input di valore è etichettato con una lettera (a, b, c, ecc.) e corrisponde a un segnaposto nella stringa di formato (ad es. `{a}`, `{b}`, `{c}`). È possibile aggiungere o rimuovere input di valori secondo necessità.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `STRING` | La stringa di testo formattata con tutti i segnaposto sostituiti dai valori corrispondenti. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StringFormat/it.md)

---
**Source fingerprint (SHA-256):** `72625287533829a8087687bb47f39bc265aced3d5f43066f615326d729725122`
