# Ottieni Latent da Batch

Questo nodo è progettato per estrarre un sottoinsieme specifico di campioni latenti da un batch dato, in base all'indice batch e alla lunghezza specificati. Consente l'elaborazione selettiva dei campioni latenti, facilitando le operazioni su segmenti più piccoli del batch per efficienza o manipolazione mirata.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `samples` | La raccolta di campioni latenti da cui verrà estratto un sottoinsieme. Questo parametro è cruciale per determinare il batch sorgente di campioni da elaborare. | `LATENT` |
| `batch_index` | Specifica l'indice iniziale all'interno del batch da cui inizierà il sottoinsieme di campioni. Questo parametro consente l'estrazione mirata di campioni da posizioni specifiche nel batch. | `INT` |
| `length` | Definisce il numero di campioni da estrarre dall'indice iniziale specificato. Questo parametro controlla la dimensione del sottoinsieme da elaborare, consentendo una manipolazione flessibile dei segmenti del batch. | `INT` |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `latent` | Il sottoinsieme estratto di campioni latenti, ora disponibile per ulteriori elaborazioni o analisi. | `LATENT` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentFromBatch/it.md)
