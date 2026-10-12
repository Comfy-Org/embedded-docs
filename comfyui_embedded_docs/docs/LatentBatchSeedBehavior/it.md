# LatentBatchSeedBehavior

Il nodo LatentBatchSeedBehavior è progettato per modificare il comportamento del seed di un batch di campioni latenti. Consente di randomizzare o fissare il seed per l'intero batch, influenzando così il processo di generazione introducendo variabilità o mantenendo coerenza negli output generati.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `samples` | Il parametro `samples` rappresenta il batch di campioni latenti da elaborare. La sua modifica dipende dal comportamento del seed scelto e influisce sulla coerenza o sulla variabilità degli output generati. | `LATENT` |
| `seed_behavior` | Il parametro `seed_behavior` stabilisce se il seed per il batch di campioni latenti debba essere randomizzato o fissato. Questa scelta influisce in modo significativo sul processo di generazione, introducendo variabilità o garantendo coerenza nell'intero batch. | COMBO[STRING] |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `latent` | L'output è una versione modificata dei campioni latenti di input, con adeguamenti effettuati in base al comportamento del seed specificato. Mantiene o modifica l'indice del batch per riflettere il comportamento del seed scelto. | `LATENT` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentBatchSeedBehavior/it.md)
