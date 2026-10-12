# SamplerDpmppSde

Questo nodo è progettato per generare un sampler per il modello DPM++ SDE (Equazione Differenziale Stocastica). Si adatta sia agli ambienti di esecuzione CPU che GPU, ottimizzando l'implementazione del sampler in base all'hardware disponibile.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `eta` | Specifica la dimensione del passo per il risolutore SDE, influenzando la granularità del processo di campionamento. | FLOAT |
| `s_noise` | Determina il livello di rumore da applicare durante il processo di campionamento, influenzando la diversità dei campioni generati. | FLOAT |
| `r` | Controlla il rapporto di riduzione del rumore nel processo di campionamento, influenzando la nitidezza e la qualità dei campioni generati. | FLOAT |
| `noise_device` | Seleziona l'ambiente di esecuzione (CPU o GPU) per il sampler, ottimizzando le prestazioni in base all'hardware disponibile. | COMBO[STRING] |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `sampler` | Il sampler generato, configurato con i parametri specificati, pronto per l'uso nelle operazioni di campionamento. | SAMPLER |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDpmppSde/it.md)
