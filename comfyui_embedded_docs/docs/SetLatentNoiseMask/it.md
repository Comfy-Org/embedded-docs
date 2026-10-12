# SetLatentNoiseMask

Questo nodo è progettato per applicare una maschera di rumore a un insieme di campioni latenti. Modifica i campioni di input integrando una maschera specificata, alterandone così le caratteristiche di rumore.

## Input

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `samples` | I campioni latenti ai quali verrà applicata la maschera di rumore. Questo parametro è cruciale per determinare il contenuto di base che verrà modificato. | `LATENT` |
| `mask` | La maschera da applicare ai campioni latenti. Definisce le aree e l'intensità dell'alterazione del rumore all'interno dei campioni. | `MASK` |

## Output

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `latent` | I campioni latenti modificati con la maschera di rumore applicata. | `LATENT` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetLatentNoiseMask/it.md)
