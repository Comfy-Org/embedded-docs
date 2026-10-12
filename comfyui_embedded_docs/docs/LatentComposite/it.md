# LatentComposite

Il nodo LatentComposite è progettato per fondere o unire due rappresentazioni latenti in un unico output. Questo processo è essenziale per creare immagini o caratteristiche composite combinando in modo controllato le caratteristiche dei latenti di input.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `samples_to` | La rappresentazione latente `samples_to` su cui verrà composto il latente `samples_from`. Funge da base per l'operazione di composizione. | `LATENT` |
| `samples_from` | La rappresentazione latente `samples_from` da comporre su `samples_to`. Contribuisce con le sue caratteristiche al risultato composito finale. | `LATENT` |
| `x` | La coordinata x (posizione orizzontale) in cui il latente `samples_from` verrà posizionato su `samples_to`. Determina l'allineamento orizzontale della composizione. | `INT` |
| `y` | La coordinata y (posizione verticale) in cui il latente `samples_from` verrà posizionato su `samples_to`. Determina l'allineamento verticale della composizione. | `INT` |
| `feather` | Un valore booleano che indica se il latente `samples_from` deve essere ridimensionato per corrispondere a `samples_to` prima della composizione. Ciò può influire sulla scala e sulle proporzioni del risultato composito. | `INT` |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `latent` | L'output è una rappresentazione latente composita, che combina le caratteristiche dei latenti `samples_to` e `samples_from` in base alle coordinate specificate e all'opzione di ridimensionamento. | `LATENT` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentComposite/it.md)
