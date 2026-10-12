# KarrasScheduler

Il nodo KarrasScheduler è progettato per generare una sequenza di livelli di rumore (sigmas) basata sulla schedulazione del rumore di Karras et al. (2022). Questo scheduler è utile per controllare il processo di diffusione nei modelli generativi, consentendo regolazioni fini dei livelli di rumore applicati a ogni passo del processo di generazione.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `steps` | Specifica il numero di passi nella schedulazione del rumore, influenzando la granularità della sequenza di sigmas generata. | INT |
| `sigma_max` | Il valore massimo di sigma nella schedulazione del rumore, che imposta il limite superiore dei livelli di rumore. | FLOAT |
| `sigma_min` | Il valore minimo di sigma nella schedulazione del rumore, che imposta il limite inferiore dei livelli di rumore. | FLOAT |
| `rho` | Un parametro che controlla la forma della curva di schedulazione del rumore, influenzando il modo in cui i livelli di rumore progrediscono da sigma_min a sigma_max. | FLOAT |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `sigmas` | La sequenza generata di livelli di rumore (sigmas) che segue la schedulazione del rumore di Karras et al. (2022). | SIGMAS |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KarrasScheduler/it.md)
