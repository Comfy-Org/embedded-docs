# SamplerDpmpp2mSde

Questo nodo è progettato per generare un sampler per il modello DPMPP_2M_SDE, consentendo la creazione di campioni in base a tipi di solver specificati, livelli di rumore e preferenze relative al dispositivo di calcolo. Astrae le complessità della configurazione del sampler, offrendo un'interfaccia semplificata per generare campioni con impostazioni personalizzate.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `solver_type` | Specifica il tipo di solver da utilizzare nel processo di campionamento, offrendo le opzioni 'midpoint' e 'heun'. Questa scelta influenza il metodo di integrazione numerica applicato durante il campionamento. | COMBO[STRING] |
| `eta` | Determina la dimensione del passo nell'integrazione numerica, influenzando la granularità del processo di campionamento. Un valore più alto indica una dimensione del passo maggiore. | `FLOAT` |
| `s_noise` | Controlla il livello di rumore introdotto durante il processo di campionamento, influenzando la variabilità dei campioni generati. | `FLOAT` |
| `noise_device` | Indica il dispositivo di calcolo ('gpu' o 'cpu') sul quale viene eseguito il processo di generazione del rumore, influenzando prestazioni ed efficienza. | COMBO[STRING] |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `sampler` | L'output è un sampler configurato in base ai parametri specificati, pronto per generare campioni. | `SAMPLER` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDpmpp2mSde/it.md)
