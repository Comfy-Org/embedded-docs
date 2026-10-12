# ScaleROPE

Il nodo ScaleROPE consente di modificare il Rotary Position Embedding (ROPE) di un modello applicando fattori separati di scala e spostamento alle sue componenti X, Y e T (tempo). È un nodo avanzato e sperimentale utilizzato per regolare il comportamento della codifica posizionale del modello.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello i cui parametri ROPE verranno modificati. | MODEL | Sì | - |
| `scale_x` | Il fattore di scala da applicare alla componente X del ROPE (predefinito: 1.0). | FLOAT | Sì | 0.0 - 100.0 (step 0.1) |
| `shift_x` | Il valore di spostamento da applicare alla componente X del ROPE (predefinito: 0.0). | FLOAT | Sì | -256.0 - 256.0 (step 0.1) |
| `scale_y` | Il fattore di scala da applicare alla componente Y del ROPE (predefinito: 1.0). | FLOAT | Sì | 0.0 - 100.0 (step 0.1) |
| `shift_y` | Il valore di spostamento da applicare alla componente Y del ROPE (predefinito: 0.0). | FLOAT | Sì | -256.0 - 256.0 (step 0.1) |
| `scale_t` | Il fattore di scala da applicare alla componente T (tempo) del ROPE (predefinito: 1.0). | FLOAT | Sì | 0.0 - 100.0 (step 0.1) |
| `shift_t` | Il valore di spostamento da applicare alla componente T (tempo) del ROPE (predefinito: 0.0). | FLOAT | Sì | -256.0 - 256.0 (step 0.1) |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `model` | Il modello con i nuovi parametri di scala e spostamento del ROPE applicati. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ScaleROPE/it.md)

---
**Source fingerprint (SHA-256):** `5d5ab0182b78c8c12ceaf44685a91e666ce15fa099fd194e3605bbdb9cc3c961`
