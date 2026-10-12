# StyleModelApply

Questo nodo applica un modello di stile a un condizionamento fornito, migliorandone o alterandone lo stile in base all'output di un modello CLIP vision. Integra il condizionamento del modello di stile nel condizionamento esistente, consentendo una fusione uniforme degli stili nel processo di generazione.

## Input

### Obbligatori

| Parametro | Descrizione | Tipo di dato Comfy |
| --- | --- | --- |
| `conditioning` | I dati di condizionamento originali ai quali verrà applicato il condizionamento del modello di stile. È cruciale per definire il contesto o lo stile di base che verrà migliorato o alterato. | `CONDITIONING` |
| `style_model` | Il modello di stile utilizzato per generare nuovo condizionamento in base all'output del modello CLIP vision. Svolge un ruolo chiave nel definire il nuovo stile da applicare. | `STYLE_MODEL` |
| `clip_vision_output` | L'output di un modello CLIP vision, utilizzato dal modello di stile per generare nuovo condizionamento. Fornisce il contesto visivo necessario per l'applicazione dello stile. | `CLIP_VISION_OUTPUT` |

## Output

| Parametro | Descrizione | Tipo di dato Comfy |
| --- | --- | --- |
| `conditioning` | Il condizionamento migliorato o alterato, che incorpora l'output del modello di stile. Rappresenta il condizionamento finale e stilizzato, pronto per ulteriori elaborazioni o generazioni. | `CONDITIONING` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StyleModelApply/it.md)
