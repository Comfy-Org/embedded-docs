# VAE Compute Dtype

Questo nodo imposta il dtype di calcolo utilizzato quando un VAE codifica o decodifica, senza modificare il resto del grafo del modello. Restituisce una copia del VAE di input con la precisione richiesta, così un flusso di lavoro può eseguire un ramo a una precisione superiore mentre gli altri restano invariati. "default" mantiene il dtype di calcolo già utilizzato dal VAE di input.

## Ingressi

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `vae` | VAE da regolare. Il nodo opera su una copia, quindi il VAE collegato non viene modificato. | VAE | Sì | - |
| `dtype` | Dtype di calcolo per la codifica e la decodifica VAE. "default" mantiene il dtype di calcolo del VAE di input (predefinito: "default"). | COMBO | Sì | "default"<br>"fp32"<br>"fp16"<br>"bf16" |

## Uscite

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `vae` | La copia del VAE con il dtype di calcolo selezionato applicato. | VAE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEComputeDtype/it.md)

---
**Source fingerprint (SHA-256):** `239e5829d76b4bd43ec300fc2b7c8c408b5bd4a93918da417ecf43817aee3e12`
