# FluxKontextImageScale

Questo nodo ridimensiona l'immagine di input a una dimensione ottimale utilizzata durante l'addestramento del modello Flux Kontext tramite l'algoritmo di Lanczos, in base alle proporzioni dell'immagine di input. Questo nodo è particolarmente utile quando si inseriscono immagini di grandi dimensioni, poiché input sovradimensionati possono portare a una qualità dell'output del modello degradata o a problemi come la comparsa di più soggetti nell'output.

## Input

| Nome parametro | Descrizione | Tipo di dati | Tipo di input | Valore predefinito | Intervallo di valori |
| --- | --- | --- | --- | --- | --- |
| `image` | Immagine di input da ridimensionare | IMAGE | Obbligatorio | - | - |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | Immagine ridimensionata | IMAGE |

## Elenco delle dimensioni predefinite

Di seguito è riportato un elenco delle dimensioni standard utilizzate durante l'addestramento del modello. Il nodo selezionerà la dimensione più vicina alle proporzioni dell'immagine di input:

| Larghezza | Altezza | Rapporto d'aspetto |
|-------|--------|--------------|
| 672   | 1568   | 0.429       |
| 688   | 1504   | 0.457       |
| 720   | 1456   | 0.494       |
| 752   | 1392   | 0.540       |
| 800   | 1328   | 0.603       |
| 832   | 1248   | 0.667       |
| 880   | 1184   | 0.743       |
| 944   | 1104   | 0.855       |
| 1024  | 1024   | 1.000       |
| 1104  | 944    | 1.170       |
| 1184  | 880    | 1.345       |
| 1248  | 832    | 1.500       |
| 1328  | 800    | 1.660       |
| 1392  | 752    | 1.851       |
| 1456  | 720    | 2.022       |
| 1504  | 688    | 2.186       |
| 1568  | 672    | 2.333       |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextImageScale/it.md)
