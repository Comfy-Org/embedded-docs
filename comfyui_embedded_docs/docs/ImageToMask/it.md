# ImageToMask

Il nodo ImageToMask è progettato per convertire un'immagine in una maschera in base a un canale di colore specificato. Consente l'estrazione di livelli di maschera corrispondenti ai canali rosso, verde, blu o alpha di un'immagine, facilitando operazioni che richiedono mascheramento o elaborazione specifici per canale.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `image` | Il parametro `image` rappresenta l'immagine di input da cui verrà generata una maschera in base al canale di colore specificato. Svolge un ruolo cruciale nel determinare il contenuto e le caratteristiche della maschera risultante. | `IMAGE` |
| `channel` | Il parametro `channel` specifica quale canale di colore (rosso, verde, blu o alpha) dell'immagine di input deve essere utilizzato per generare la maschera. Questa scelta influenza direttamente l'aspetto della maschera e quali parti dell'immagine vengono evidenziate o mascherate. | COMBO[STRING] |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `mask` | L'output `mask` è una rappresentazione binaria o in scala di grigi del canale di colore specificato dell'immagine di input, utile per ulteriori elaborazioni dell'immagine o operazioni di mascheramento. | `MASK` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageToMask/it.md)
