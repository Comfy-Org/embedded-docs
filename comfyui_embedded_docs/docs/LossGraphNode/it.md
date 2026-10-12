# Traccia grafico della perdita

Il nodo LossGraphNode crea un grafico a linee dei valori di loss di addestramento nel corso degli step di addestramento e lo mostra come immagine di anteprima. Legge i valori di loss da un nodo di addestramento, li traccia su un grafico con assi etichettati e valori di loss minimo/massimo, e restituisce il grafico come anteprima immagine nell'interfaccia utente. Questo nodo è contrassegnato come sperimentale ed è un nodo di output.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `loss` | Mappa di loss dal nodo di addestramento. Deve contenere una chiave `loss` con una lista di valori di loss numerici. | LOSS_MAP | Sì | - |
| `filename_prefix` | Prefisso per l'immagine del grafico di loss salvata. (predefinito: "loss_graph") | STRING | Sì | - |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `ui.images` | L'immagine del grafico di loss generata, visualizzata come anteprima. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LossGraphNode/it.md)

---
**Source fingerprint (SHA-256):** `b1f0b72a03d4ce2d9461fc6e312bd1e847455f7dd5227667876a945494ea8cdb`
