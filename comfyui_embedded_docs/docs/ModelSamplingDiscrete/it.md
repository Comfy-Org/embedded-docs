# ModelSamplingDiscrete

Questo nodo è progettato per modificare il comportamento di campionamento di un modello applicando una strategia di campionamento discreto. Consente di selezionare diversi metodi di campionamento, come epsilon, v_prediction, lcm o x0, e regola facoltativamente la strategia di riduzione del rumore del modello in base all'impostazione zero-shot noise ratio (zsnr).

## Input

| Parametro | Descrizione | Tipo di dato | Python dtype |
| --- | --- | --- | --- |
| `model` | Il modello a cui verrà applicata la strategia di campionamento discreto. Questo parametro è cruciale poiché definisce il modello di base che sarà modificato. | MODEL | `torch.nn.Module` |
| `sampling` | Specifica il metodo di campionamento discreto da applicare al modello. La scelta del metodo influisce su come il modello genera i campioni, offrendo strategie di campionamento diverse. | COMBO[STRING] | `str` |
| `zsnr` | Un flag booleano che, se abilitato, regola la strategia di riduzione del rumore del modello in base al rapporto rumore zero-shot. Ciò può influenzare la qualità e le caratteristiche dei campioni generati. | `BOOLEAN` | `bool` |

## Output

| Parametro | Descrizione | Tipo di dato | Python dtype |
| --- | --- | --- | --- |
| `model` | Il modello modificato con la strategia di campionamento discreto applicata. Questo modello è ora in grado di generare campioni utilizzando il metodo e le regolazioni specificati. | MODEL | `torch.nn.Module` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingDiscrete/it.md)
