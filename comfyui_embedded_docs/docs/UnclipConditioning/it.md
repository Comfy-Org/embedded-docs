# UnclipConditioning

Questo nodo è progettato per integrare gli output della visione CLIP nel processo di condizionamento, regolando l'influenza di tali output in base ai parametri specificati di forza e aumento del rumore. Arricchisce il condizionamento con il contesto visivo, migliorando il processo di generazione.

## Input

| Parametro | Descrizione | Comfy dtype |
| --- | --- | --- |
| `conditioning` | I dati di condizionamento di base a cui devono essere aggiunti gli output della visione CLIP, che fungono da fondamento per ulteriori modifiche. | `CONDITIONING` |
| `clip_vision_output` | L'output di un modello di visione CLIP, che fornisce il contesto visivo integrato nel condizionamento. | `CLIP_VISION_OUTPUT` |
| `strength` | Determina l'intensità dell'influenza dell'output della visione CLIP sul condizionamento. | `FLOAT` |
| `noise_augmentation` | Specifica il livello di aumento del rumore da applicare all'output della visione CLIP prima di integrarlo nel condizionamento. | `FLOAT` |

## Output

| Parametro | Descrizione | Comfy dtype |
| --- | --- | --- |
| `conditioning` | I dati di condizionamento arricchiti, che ora contengono gli output della visione CLIP integrati con forza e aumento del rumore applicati. | `CONDITIONING` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UnclipConditioning/it.md)
