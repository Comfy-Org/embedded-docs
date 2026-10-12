# LatentOperationBlend

Questo nodo crea un'operazione su latent che fonde un latent verso un latent di riferimento e restituisce tale operazione, così può essere collegata a nodi come Latent Apply Operation o Latent Apply Operation CFG. Quando il riferimento ha una dimensione spaziale diversa, viene ridimensionato alla dimensione del latent di destinazione con interpolazione nearest-neighbor, e un riferimento con un batch più piccolo viene ripetuto per corrispondere alla dimensione del batch di destinazione. Un valore di strength pari a 0 lascia il latent invariato. Questo nodo è contrassegnato come sperimentale.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `reference` | Il latent verso cui fondere. I suoi campioni vengono convertiti al device e al dtype del latent in elaborazione, poi ridimensionati e ripetuti per corrispondere a esso. | LATENT | Sì | - |
| `strength` | In che misura fondere verso il riferimento: 0 lascia il latent invariato, 1 corrisponde al latent di riferimento ridimensionato (predefinito: 1.0). | FLOAT | Sì | 0.0 to 1.0 (step 0.0001) |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `operation` | Un'operazione di fusione che può essere applicata ai campioni latent. | LATENT_OPERATION |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationBlend/it.md)

---
**Source fingerprint (SHA-256):** `5890089afddf83ddd4edd992606509b118aac9ef13eb89589f73fa75e0b9dd5a`
