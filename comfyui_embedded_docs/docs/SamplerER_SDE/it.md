# SamplerER_SDE

Il nodo SamplerER_SDE fornisce metodi di campionamento specializzati per i modelli di diffusione, offrendo diversi tipi di solver: ER-SDE, Reverse-time SDE e ODE. Consente di controllare il comportamento stocastico e il numero di stadi computazionali del processo di campionamento. Il nodo regola automaticamente le impostazioni in base al tipo di solver scelto per mantenere il sampler funzionante correttamente.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `solver_type` | Il tipo di solver da usare per il campionamento. Determina l'approccio matematico per il processo di diffusione (predefinito: "ER-SDE"). | COMBO | Sì | "ER-SDE"<br>"Reverse-time SDE"<br>"ODE" |
| `max_stage` | Il numero massimo di stadi per il processo di campionamento (predefinito: 3). Controlla la complessità computazionale e la qualità. Questo è un parametro avanzato. | INT | Sì | 1-3 |
| `eta` | Intensità stocastica delle SDE.<br>Quando eta=0, si riducono a un'ODE deterministica.<br>Valori elevati di eta possono causare output non validi. In questo caso, prova a diminuire questo valore. (predefinito: 1.0). Questo è un parametro avanzato. | FLOAT | Sì | 0.0-10.0 (passo: 0.01) |
| `s_noise` | Fattore di scala del rumore per il processo di campionamento (predefinito: 1.0). Controlla la quantità di rumore applicata durante il campionamento. Questo è un parametro avanzato. | FLOAT | Sì | 0.0-100.0 (passo: 0.01) |

**Vincoli dei parametri:**

- Quando `solver_type` è impostato su "ODE" o quando `eta` è 0, il nodo passa alla modalità ODE e imposta `s_noise` a 0.0, indipendentemente dal valore inserito per `s_noise`.
- Il parametro `eta` controlla l'intensità stocastica sia per il tipo di solver "ER-SDE" sia per "Reverse-time SDE". Non ha effetto quando il solver è in modalità ODE.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `sampler` | Un oggetto sampler configurato che può essere usato nella pipeline di campionamento con le impostazioni del solver specificate. | SAMPLER |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerER_SDE/it.md)

---
**Source fingerprint (SHA-256):** `5299ae9b45444cdc7c36bcb3c5e5a0600f9f904e57ae614554033434afdffd30`
