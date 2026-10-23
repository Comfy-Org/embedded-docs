# ModelSamplingContinuousEdm

Questo nodo è progettato per migliorare le capacità di campionamento di un modello integrando tecniche di campionamento EDM (Energy-based Diffusion Models) continue. Consente la regolazione dinamica dei livelli di rumore all'interno del processo di campionamento del modello, offrendo un controllo più raffinato sulla qualità e sulla diversità della generazione.

## Input

| Parametro | Descrizione | Tipo di dato | Tipo Python |
| --- | --- | --- | --- |
| `model` | Il modello da potenziare con capacità di campionamento EDM continue. Funge da base per l'applicazione delle tecniche di campionamento avanzate. | `MODEL` | `torch.nn.Module` |
| `sampling` | Specifica il tipo di campionamento da applicare, ovvero 'eps' per il campionamento epsilon o 'v_prediction' per la predizione della velocità, influenzando il comportamento del modello durante il processo di campionamento. | COMBO[STRING] | `str` |
| `sigma_max` | Il valore massimo di sigma per il livello di rumore, che consente di controllare il limite superiore nel processo di iniezione del rumore durante il campionamento. | `FLOAT` | `float` |
| `sigma_min` | Il valore minimo di sigma per il livello di rumore, che imposta il limite inferiore per l'iniezione del rumore, influenzando così la precisione di campionamento del modello. | `FLOAT` | `float` |

## Output

| Parametro | Descrizione | Tipo di dato | Tipo Python |
| --- | --- | --- | --- |
| `model` | Il modello potenziato con capacità di campionamento EDM continue integrate, pronto per ulteriori utilizzi in attività di generazione. | MODEL | `torch.nn.Module` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingContinuousEDM/it.md)
