# Ridimensiona Immagini per Lato Più Lungo (DEPRECATO)

Il nodo Resize Images by Longer Edge ridimensiona una o più immagini in modo che il loro lato più lungo corrisponda a una lunghezza target specificata. Determina automaticamente se la larghezza o l'altezza è maggiore e ridimensiona proporzionalmente l'altra dimensione per preservare le proporzioni originali. Questo nodo è deprecato ed è stato sostituito dal nodo Resize Image/Mask con il tipo di ridimensionamento impostato su "scale longer dimension".

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `image` | L'immagine o il batch di immagini di input da ridimensionare. | IMAGE | Sì | - |
| `longer_edge` | Dimensione target per il lato più lungo. Il lato più corto verrà ridimensionato proporzionalmente. (predefinito: 1024) | INT | Sì | 1 - 8192 |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `image` | L'immagine o il batch di immagini ridimensionate. L'output avrà lo stesso numero di immagini dell'input, con il lato più lungo di ciascuna che corrisponde alla lunghezza `longer_edge` specificata. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImagesByLongerEdge/it.md)

---
**Source fingerprint (SHA-256):** `bf66808acbc654d5a9ea58b062b5b89d6c13dbec0929d6d92aaa3c8914dcece0`
