# Batch Latent (DEPRECATO)

Il nodo LatentBatch è progettato per unire due insiemi di campioni latenti in un unico batch, ridimensionando potenzialmente un insieme per adattarlo alle dimensioni dell'altro prima della concatenazione. Questa operazione facilita la combinazione di diverse rappresentazioni latenti per ulteriori attività di elaborazione o generazione.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `samples1` | Il primo insieme di campioni latenti da unire. Svolge un ruolo cruciale nel determinare la forma finale del batch unito. | `LATENT` |
| `samples2` | Il secondo insieme di campioni latenti da unire. Se le sue dimensioni differiscono da quelle del primo insieme, viene ridimensionato per garantirne la compatibilità prima dell'unione. | `LATENT` |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `latent` | L'insieme unito di campioni latenti, ora combinato in un unico batch per ulteriori elaborazioni. | `LATENT` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentBatch/it.md)
