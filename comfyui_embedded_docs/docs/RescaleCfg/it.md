# RescaleCfg

Il nodo RescaleCFG è progettato per regolare le scale di condizionamento e incondizionamento dell'output di un modello in base a un moltiplicatore specificato, con l'obiettivo di ottenere un processo di generazione più bilanciato e controllato. Opera riscalando l'output del modello per modificare l'influenza delle componenti condizionate e incondizionate, migliorando potenzialmente le prestazioni del modello o la qualità dell'output.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il parametro `model` rappresenta il modello generativo da regolare. È cruciale poiché il nodo applica una funzione di riscalatura all'output del modello, influenzando direttamente il processo di generazione. | MODEL |
| `multiplier` | Il parametro `multiplier` controlla l'entità della riscalatura applicata all'output del modello. Determina l'equilibrio tra le componenti originali e quelle riscalate, influenzando le caratteristiche dell'output finale. | `FLOAT` |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il modello modificato con scale di condizionamento e incondizionamento regolate. Si prevede che questo modello produca output con caratteristiche potenzialmente migliorate grazie alla riscalatura applicata. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RescaleCfg/it.md)
