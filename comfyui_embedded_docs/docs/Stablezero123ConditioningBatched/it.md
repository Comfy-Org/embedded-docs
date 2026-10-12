# Stablezero123ConditioningBatched

Questo nodo è progettato per elaborare informazioni di condizionamento in modalità batch, specificamente adattata al modello StableZero123. Si concentra sulla gestione efficiente di più set di dati di condizionamento contemporaneamente, ottimizzando il flusso di lavoro per scenari in cui l'elaborazione batch è cruciale.

## Input

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `clip_vision` | Gli embedding di visione CLIP che forniscono contesto visivo per il processo di condizionamento. | `CLIP_VISION` |
| `init_image` | L'immagine iniziale su cui applicare il condizionamento, che funge da punto di partenza per il processo di generazione. | `IMAGE` |
| `vae` | L'autoencoder variazionale utilizzato per codificare e decodificare immagini nel processo di condizionamento. | `VAE` |
| `width` | La larghezza dell'immagine di output. | `INT` |
| `height` | L'altezza dell'immagine di output. | `INT` |
| `batch_size` | Il numero di set di condizionamento da elaborare in un singolo batch. | `INT` |
| `elevation` | L'angolo di elevazione per il condizionamento del modello 3D, che influenza la prospettiva dell'immagine generata. | `FLOAT` |
| `azimuth` | L'angolo di azimut per il condizionamento del modello 3D, che influenza l'orientamento dell'immagine generata. | `FLOAT` |
| `elevation_batch_increment` | La variazione incrementale dell'angolo di elevazione lungo il batch, che consente prospettive variate. | `FLOAT` |
| `azimuth_batch_increment` | La variazione incrementale dell'angolo di azimut lungo il batch, che consente orientamenti variati. | `FLOAT` |

## Output

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `positive` | L'output di condizionamento positivo, progettato per promuovere determinate caratteristiche o aspetti nel contenuto generato. | `CONDITIONING` |
| `negative` | L'output di condizionamento negativo, progettato per sfavorire determinate caratteristiche o aspetti nel contenuto generato. | `CONDITIONING` |
| `latent` | La rappresentazione latente derivata dal processo di condizionamento, pronta per ulteriori elaborazioni o passaggi di generazione. | `LATENT` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Stablezero123ConditioningBatched/it.md)
