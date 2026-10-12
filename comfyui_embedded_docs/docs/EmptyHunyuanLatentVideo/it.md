# EmptyHunyuanLatentVideo

Il nodo `EmptyHunyuanLatentVideo` è simile al nodo `EmptyLatentImage`. Puoi considerarlo come una tela vuota per la generazione video, in cui larghezza, altezza e lunghezza definiscono le proprietà della tela, mentre la dimensione del batch determina il numero di tele da creare. Questo nodo crea tele vuote pronte per le successive attività di generazione video.

## Input

| Parametro | Descrizione | Tipo Comfy |
| --- | --- | --- |
| `width` | Larghezza video, predefinita 848, minima 16, massima `nodes.MAX_RESOLUTION`, passo 16. | `INT` |
| `height` | Altezza video, predefinita 480, minima 16, massima `nodes.MAX_RESOLUTION`, passo 16. | `INT` |
| `length` | Lunghezza video, predefinita 25, minima 1, massima `nodes.MAX_RESOLUTION`, passo 4. | `INT` |
| `batch_size` | Dimensione del batch, predefinita 1, minima 1, massima 4096. | `INT` |

## Output

| Parametro | Descrizione | Tipo Comfy |
| --- | --- | --- |
| `samples` | Campioni latenti video generati contenenti tensori di zeri, pronti per attività di elaborazione e generazione. | `LATENT` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanLatentVideo/it.md)
