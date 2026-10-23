# VpScheduler

Il nodo VPScheduler è progettato per generare una sequenza di livelli di rumore (sigmas) basata sul metodo di scheduling Variance Preserving (VP). Questa sequenza è cruciale per guidare il processo di denoising nei modelli di diffusione, consentendo una generazione controllata di immagini o altri tipi di dati.

## Input

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `steps` | Specifica il numero di passaggi nel processo di diffusione, influenzando la granularità dei livelli di rumore generati. | INT |
| `beta_d` | Determina la distribuzione complessiva del livello di rumore, influenzando la varianza dei livelli di rumore generati. | FLOAT |
| `beta_min` | Imposta il limite minimo per il livello di rumore, garantendo che il rumore non scenda al di sotto di una determinata soglia. | FLOAT |
| `eps_s` | Regola il valore epsilon iniziale, perfezionando il livello di rumore iniziale nel processo di diffusione. | FLOAT |

## Output

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `sigmas` | Una sequenza di livelli di rumore (sigmas) generata in base al metodo di scheduling VP, utilizzata per guidare il processo di denoising nei modelli di diffusione. | SIGMAS |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VPScheduler/it.md)
