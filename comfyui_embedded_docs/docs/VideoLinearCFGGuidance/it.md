# VideoLinearCfgGuidance

Il nodo VideoLinearCFGGuidance applica una scala di guida del condizionamento lineare a un modello video, regolando l'influenza delle componenti condizionate e non condizionate su un intervallo specificato. Ciò consente un controllo dinamico del processo di generazione, permettendo di ottimizzare l'output del modello in base al livello di condizionamento desiderato.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il parametro `model` rappresenta il modello video a cui verrà applicata la guida CFG lineare. È cruciale per definire il modello di base che verrà modificato con la scala di guida. | MODEL |
| `min_cfg` | Il parametro `min_cfg` specifica la scala minima di guida del condizionamento da applicare, fungendo da punto di partenza per la regolazione lineare della scala. Svolge un ruolo chiave nel determinare il limite inferiore della scala di guida, influenzando l'output del modello. | `FLOAT` |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | L'output è una versione modificata del modello di input, con la scala di guida CFG lineare applicata. Questo modello regolato è in grado di generare output con vari gradi di condizionamento, in base alla scala di guida specificata. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoLinearCFGGuidance/it.md)
