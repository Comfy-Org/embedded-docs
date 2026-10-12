# Ridimensiona Immagini per Lato Più Corto (DEPRECATO)

Questo nodo ridimensiona le immagini in modo che il lato più corto corrisponda a una lunghezza specificata, preservando le proporzioni originali. Calcola le nuove dimensioni in base alla lunghezza target per il lato più corto e restituisce l'immagine ridimensionata.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `image` | L'immagine di input da ridimensionare. | IMAGE | Sì | - |
| `shorter_edge` | Dimensione target per il lato più corto. (predefinito: 512) | INT | Sì | da 1 a 8192 |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | L'immagine ridimensionata con il lato più corto che corrisponde alla lunghezza target specificata. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImagesByShorterEdge/it.md)

---
**Source fingerprint (SHA-256):** `6bb3e1c974108ee7b75b47406ea02b3f47ca14305f9ee54d3d379eefbb7f26cd`
