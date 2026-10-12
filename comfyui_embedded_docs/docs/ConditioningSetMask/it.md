# Conditioning (Imposta Maschera)

Questo nodo è progettato per modificare il condizionamento di un modello generativo applicando una maschera con una forza specificata a determinate aree. Consente regolazioni mirate all'interno del condizionamento, offrendo un controllo più preciso sul processo di generazione.

## Input

### Obbligatori

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `CONDITIONING` | I dati di condizionamento da modificare. Costituiscono la base per l'applicazione della maschera e delle regolazioni di forza. | CONDITIONING |
| `mask` | Un tensore maschera che specifica le aree all'interno del condizionamento da modificare. | `MASK` |
| `strength` | La forza dell'effetto della maschera sul condizionamento, che consente una messa a punto delle modifiche applicate. | `FLOAT` |
| `set_cond_area` | Determina se l'effetto della maschera viene applicato all'area predefinita o delimitato dalla maschera stessa, offrendo flessibilità nel selezionare regioni specifiche. | COMBO[STRING] |

## Output

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `CONDITIONING` | I dati di condizionamento modificati, con la maschera e le regolazioni di forza applicate. | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetMask/it.md)
