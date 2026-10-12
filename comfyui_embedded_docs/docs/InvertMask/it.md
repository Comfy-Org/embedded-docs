# Inverti Maschera

Il nodo InvertMask è progettato per invertire i valori di una maschera data, scambiando di fatto le aree mascherate e non mascherate. Questa operazione è fondamentale nelle attività di elaborazione delle immagini in cui l'attenzione deve essere spostata tra il primo piano e lo sfondo.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `mask` | Il parametro `mask` rappresenta la maschera di input da invertire. È cruciale per determinare le aree da scambiare durante il processo di inversione. | MASK |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `mask` | L'output è una versione invertita della maschera di input, con le aree precedentemente mascherate che diventano non mascherate e viceversa. | MASK |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InvertMask/it.md)
