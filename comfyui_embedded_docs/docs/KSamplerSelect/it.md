# KSamplerSelect

Il nodo KSamplerSelect è progettato per selezionare un sampler specifico in base al nome del sampler fornito. Astrae la complessità della selezione del sampler, consentendo agli utenti di passare facilmente tra diverse strategie di campionamento per le proprie attività.

## Input

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `sampler_name` | Specifica il nome del sampler da selezionare. Questo parametro determina quale strategia di campionamento verrà utilizzata, influenzando il comportamento e i risultati complessivi del campionamento. | COMBO[STRING] |

## Output

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `sampler` | Restituisce l'oggetto sampler selezionato, pronto per essere utilizzato nelle attività di campionamento. | `SAMPLER` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSamplerSelect/it.md)
