# Interpolazione Latent

Il nodo LatentInterpolate è progettato per eseguire l'interpolazione tra due insiemi di campioni latenti in base a un rapporto specificato, combinando le caratteristiche di entrambi gli insiemi per produrre un nuovo insieme intermedio di campioni latenti.

## Input

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `samples1` | Il primo insieme di campioni latenti da interpolare. Funge da punto di partenza per il processo di interpolazione. | `LATENT` |
| `samples2` | Il secondo insieme di campioni latenti da interpolare. Funge da punto finale per il processo di interpolazione. | `LATENT` |
| `ratio` | Un valore a virgola mobile che determina il peso di ciascun insieme di campioni nell'output interpolato. Un rapporto pari a 0 produce una copia del primo insieme, mentre un rapporto pari a 1 produce una copia del secondo insieme. | `FLOAT` |

## Output

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `latent` | L'output è un nuovo insieme di campioni latenti che rappresenta uno stato interpolato tra i due insiemi di input, in base al rapporto specificato. | `LATENT` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentInterpolate/it.md)
