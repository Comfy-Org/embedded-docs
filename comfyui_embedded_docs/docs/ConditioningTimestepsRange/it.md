# ConditioningTimestepsRange

Il nodo ConditioningTimestepsRange crea tre intervalli di timestep distinti per controllare quando gli effetti di condizionamento vengono applicati durante il processo di generazione. Accetta valori percentuali di inizio e fine e divide l'intero intervallo di timestep (da 0.0 a 1.0) in tre segmenti: l'intervallo principale compreso tra le percentuali specificate, l'intervallo precedente alla percentuale iniziale e l'intervallo successivo alla percentuale finale.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `start_percent` | La percentuale iniziale dell'intervallo di timestep (predefinito: 0.0) | FLOAT | Sì | 0.0 - 1.0 |
| `end_percent` | La percentuale finale dell'intervallo di timestep (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `TIMESTEPS_RANGE` | L'intervallo di timestep principale definito da start_percent e end_percent | TIMESTEPS_RANGE |
| `BEFORE_RANGE` | L'intervallo di timestep da 0.0 a start_percent | TIMESTEPS_RANGE |
| `AFTER_RANGE` | L'intervallo di timestep da end_percent a 1.0 | TIMESTEPS_RANGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningTimestepsRange/it.md)

---
**Source fingerprint (SHA-256):** `dee21b5ac80fabdeacf3f4a985550fff795702e02911400ae49a97baae834e5e`
