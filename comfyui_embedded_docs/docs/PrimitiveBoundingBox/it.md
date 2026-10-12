# PrimitiveBoundingBox

Il nodo PrimitiveBoundingBox crea una semplice area rettangolare definita dalla sua posizione e dimensione. Accetta coordinate X e Y per l'angolo superiore sinistro, insieme ai valori di larghezza e altezza, e restituisce una struttura dati bounding box che può essere utilizzata da altri nodi in un workflow.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `x` | La coordinata X per l'angolo superiore sinistro del bounding box (predefinito: 0). | INT | Sì | 0 to 16384 |
| `y` | La coordinata Y per l'angolo superiore sinistro del bounding box (predefinito: 0). | INT | Sì | 0 to 16384 |
| `width` | La larghezza del bounding box (predefinito: 512). | INT | Sì | 1 to 16384 |
| `height` | L'altezza del bounding box (predefinito: 512). | INT | Sì | 1 to 16384 |

Nota: tutti i valori massimi seguono la costante MAX_RESOLUTION di ComfyUI, che definisce la dimensione massima dell'immagine accettata dal nodo.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `bounding_box` | Una struttura dati contenente le proprietà `x`, `y`, `width` e `height` del rettangolo definito. | BOUNDING_BOX |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveBoundingBox/it.md)

---
**Source fingerprint (SHA-256):** `dc50286b09b8aaf7ff21eb699b9a04317f099b3deedb6cb7d4a1ec7668edeb97`
