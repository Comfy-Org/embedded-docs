# PolyexponentialScheduler

Il nodo PolyexponentialScheduler è progettato per generare una sequenza di livelli di rumore (sigmas) basata su una schedulazione del rumore poliesponenziale. Questa schedulazione è una funzione polinomiale nel logaritmo di sigma, che consente una progressione flessibile e personalizzabile dei livelli di rumore durante il processo di diffusione.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `steps` | Specifica il numero di passaggi nel processo di diffusione, influenzando la granularità dei livelli di rumore generati. | INT |
| `sigma_max` | Il livello massimo di rumore, che imposta il limite superiore della schedulazione del rumore. | FLOAT |
| `sigma_min` | Il livello minimo di rumore, che imposta il limite inferiore della schedulazione del rumore. | FLOAT |
| `rho` | Un parametro che controlla la forma della schedulazione del rumore poliesponenziale, influenzando il modo in cui i livelli di rumore progrediscono tra i valori minimo e massimo. | FLOAT |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `sigmas` | L'output è una sequenza di livelli di rumore (sigmas) adattata alla schedulazione del rumore poliesponenziale specificata. | SIGMAS |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PolyexponentialScheduler/it.md)
