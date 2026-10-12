# ImageUpscaleWithModel

Questo nodo è progettato per eseguire l'upscaling delle immagini utilizzando un modello di upscale specificato. Gestisce in modo efficiente il processo di upscaling adattando l'immagine al dispositivo appropriato, ottimizzando l'utilizzo della memoria e applicando il modello di upscale in modalità a tasselli per prevenire potenziali errori di memoria esaurita.

## Input

| Parametro | Descrizione | Comfy dtype |
| --- | --- | --- |
| `upscale_model` | Il modello di upscale da utilizzare per eseguire l'upscaling dell'immagine. È cruciale per definire l'algoritmo di upscaling e i suoi parametri. | `UPSCALE_MODEL` |
| `image` | L'immagine da sottoporre a upscaling. Questo input è essenziale per determinare il contenuto di origine che sarà interessato dal processo di upscaling. | `IMAGE` |

## Output

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | L'immagine sottoposta a upscaling, elaborata dal modello di upscale. Questo output è il risultato dell'operazione di upscaling, che mostra la risoluzione o la qualità migliorata. | `IMAGE` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageUpscaleWithModel/it.md)
