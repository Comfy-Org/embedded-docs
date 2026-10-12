# CFGOverride

Il nodo CFG Override sovrascrive la scala CFG (Classifier-Free Guidance) impostandola su un valore fisso per un intervallo percentuale (sigma) del processo di campionamento. Quando si utilizzano più nodi CFG Override, l'override più vicino al sampler prevale sugli intervalli sovrapposti.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello a cui applicare l'override CFG. | MODEL | Sì | |
| `cfg` | Il valore fisso della scala CFG da usare durante l'intervallo di override. Predefinito: 1.0. | FLOAT | Sì | da 0.0 a 100.0 (passo: 0.1) |
| `start_percent` | Il punto iniziale dell'intervallo di override come percentuale del processo di campionamento. Predefinito: 0.0. | FLOAT | Sì | da 0.0 a 1.0 (passo: 0.001) |
| `end_percent` | Il punto finale dell'intervallo di override come percentuale del processo di campionamento. Predefinito: 1.0. | FLOAT | Sì | da 0.0 a 1.0 (passo: 0.001) |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `MODEL` | Il modello con il wrapper di override CFG applicato. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGOverride/it.md)

---
**Source fingerprint (SHA-256):** `94c7d3751d90b42479f9cec4bdb3c95eeda405f51224f85d313ff12ec071ec58`
