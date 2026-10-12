# ImageColorToMask

Il nodo `ImageColorToMask` è progettato per convertire un colore specificato in un'immagine in una maschera. Elabora un'immagine e un colore di destinazione, generando una maschera in cui il colore specificato è evidenziato, facilitando operazioni come la segmentazione basata sul colore o l'isolamento di oggetti.

## Input

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | Il parametro `image` rappresenta l'immagine di input da elaborare. È cruciale per determinare le aree dell'immagine che corrispondono al colore specificato da convertire in una maschera. | `IMAGE` |
| `color` | Il parametro `color` specifica il colore di destinazione nell'immagine da convertire in una maschera. Svolge un ruolo chiave nell'identificare le specifiche aree di colore da evidenziare nella maschera risultante. | `INT` |

## Output

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `mask` | L'output è una maschera che evidenzia le aree dell'immagine di input che corrispondono al colore specificato. Questa maschera può essere utilizzata per ulteriori attività di elaborazione delle immagini, come la segmentazione o l'isolamento di oggetti. | `MASK` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageColorToMask/it.md)
