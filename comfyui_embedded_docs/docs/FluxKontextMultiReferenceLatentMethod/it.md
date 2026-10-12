# FluxKontextMultiReferenceLatentMethod

Il nodo FluxKontextMultiReferenceLatentMethod aggiorna i dati di condizionamento memorizzando al loro interno un metodo scelto per i latenti di riferimento. Il metodo memorizzato viene poi utilizzato quando i latenti di riferimento vengono gestiti nelle fasi di generazione successive. Questo nodo è contrassegnato come sperimentale e appartiene al sistema di condizionamento Flux.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `conditioning` | I dati di condizionamento da modificare con il metodo dei latenti di riferimento | CONDITIONING | Sì | - |
| `reference_latents_method` | Il metodo usato per l'elaborazione dei latenti di riferimento. Se viene selezionato un valore contenente "uxo" o "uso", viene convertito in "uxo" prima di essere memorizzato. Questo parametro è contrassegnato come avanzato. | COMBO | Sì | `"offset"`<br>`"index"`<br>`"uxo/uno"`<br>`"index_timestep_zero"` |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `conditioning` | I dati di condizionamento modificati a cui è stato applicato il metodo dei latenti di riferimento | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextMultiReferenceLatentMethod/it.md)

---
**Source fingerprint (SHA-256):** `cbe069d0c9f8adbf7f8c909b1cd644d9cd3730e934f0e5856213ff06fa8ecc56`
