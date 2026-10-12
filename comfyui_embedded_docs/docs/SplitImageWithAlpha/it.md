# SplitImageWithAlpha

Il nodo SplitImageWithAlpha è progettato per separare le componenti colore e alfa di un'immagine. Elabora un tensore immagine di input, estraendo i canali RGB come componente colore e il canale alfa come componente di trasparenza, facilitando le operazioni che richiedono la manipolazione di questi distinti aspetti dell'immagine.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `image` | Il parametro `image` rappresenta il tensore immagine di input da cui separare i canali RGB e alfa. È cruciale per l'operazione poiché fornisce i dati di origine per la separazione. | `IMAGE` |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `image` | L'output `image` rappresenta i canali RGB separati dell'immagine di input, fornendo la componente colore senza le informazioni di trasparenza. | `IMAGE` |
| `mask` | L'output `mask` rappresenta il canale alfa separato dell'immagine di input, fornendo le informazioni di trasparenza. | `MASK` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitImageWithAlpha/it.md)
