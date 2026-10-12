# Sottrai Latent

Il nodo LatentSubtract è progettato per sottrarre una rappresentazione latente da un'altra. Questa operazione può essere utilizzata per manipolare o modificare le caratteristiche degli output dei modelli generativi, rimuovendo efficacemente caratteristiche o attributi rappresentati in uno spazio latente da un altro.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `samples1` | Il primo insieme di campioni latenti da cui sottrarre. Funge da base per l'operazione di sottrazione. | `LATENT` |
| `samples2` | Il secondo insieme di campioni latenti che verrà sottratto dal primo insieme. Questa operazione può alterare l'output del modello generativo risultante rimuovendo attributi o caratteristiche. | `LATENT` |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `latent` | Il risultato della sottrazione del secondo insieme di campioni latenti dal primo. Questa rappresentazione latente modificata può essere utilizzata per ulteriori attività generative. | `LATENT` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentSubtract/it.md)
