# EasyCache

Il nodo EasyCache aggiunge un sistema di caching nativo a un modello di diffusione che velocizza il campionamento riutilizzando i risultati dei passaggi calcolati in precedenza invece di ricalcolare ogni passaggio. Si attiva solo tra un punto iniziale e uno finale configurabili del processo di campionamento e salta i passaggi quando la variazione stimata dell'output rimane al di sotto di una soglia definita dall'utente. Questo è un nodo sperimentale pensato per un uso di debug avanzato.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello a cui aggiungere EasyCache. | MODEL | Sì | - |
| `reuse_threshold` | La soglia per riutilizzare i passaggi memorizzati nella cache (predefinito: 0.2). | FLOAT | Sì | 0.0 - 3.0 |
| `start_percent` | Il passo di campionamento relativo per iniziare a usare EasyCache (predefinito: 0.15). | FLOAT | Sì | 0.0 - 1.0 |
| `end_percent` | Il passo di campionamento relativo per terminare l'uso di EasyCache (predefinito: 0.95). | FLOAT | Sì | 0.0 - 1.0 |
| `verbose` | Se registrare informazioni dettagliate (predefinito: False). | BOOLEAN | Sì | - |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il modello con la funzionalità EasyCache aggiunta. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EasyCache/it.md)

---
**Source fingerprint (SHA-256):** `3e10ac65f8df58ce8649fdf599e62bfb86f2d4166840bed5622c0aa2c419cd38`
