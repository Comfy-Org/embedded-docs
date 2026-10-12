# Ribalta Latent

Il nodo LatentFlip è progettato per manipolare le rappresentazioni latenti capovolgendole verticalmente o orizzontalmente. Questa operazione consente la trasformazione dello spazio latente, rivelando potenzialmente nuove variazioni o prospettive all'interno dei dati.

## Input

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `samples` | Il parametro 'samples' rappresenta le rappresentazioni latenti da capovolgere. L'operazione di capovolgimento modifica queste rappresentazioni, verticalmente o orizzontalmente, a seconda del parametro 'flip_method', trasformando così i dati nello spazio latente. | `LATENT` |
| `flip_method` | Il parametro 'flip_method' specifica l'asse lungo il quale verranno capovolti i campioni latenti. Può essere 'x-axis: vertically' o 'y-axis: horizontally', determinando la direzione del capovolgimento e quindi la natura della trasformazione applicata alle rappresentazioni latenti. | COMBO[STRING] |

## Output

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `latent` | L'output è una versione modificata delle rappresentazioni latenti di input, essendo state capovolte secondo il metodo specificato. Questa trasformazione può introdurre nuove variazioni all'interno dello spazio latente. | `LATENT` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentFlip/it.md)
