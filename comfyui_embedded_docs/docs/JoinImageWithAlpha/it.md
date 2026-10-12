# JoinImageWithAlpha

Questo nodo è progettato per operazioni di compositing, in particolare per unire un'immagine con la relativa maschera alpha e produrre un'unica immagine di output. Combina efficacemente il contenuto visivo con le informazioni di trasparenza, consentendo la creazione di immagini in cui determinate aree sono trasparenti o semi-trasparenti.

## Input

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | Il contenuto visivo principale da combinare con una maschera alpha. Rappresenta l'immagine senza informazioni di trasparenza. | `IMAGE` |
| `alpha` | La maschera alpha che definisce la trasparenza dell'immagine corrispondente. Viene utilizzata per determinare quali parti dell'immagine devono essere trasparenti o semi-trasparenti. | `MASK` |

## Output

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | L'output è un'unica immagine che combina l'immagine di input con la maschera alpha, incorporando le informazioni di trasparenza nel contenuto visivo. | `IMAGE` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/JoinImageWithAlpha/it.md)
