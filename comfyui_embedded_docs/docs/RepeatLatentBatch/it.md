# RepeatLatentBatch

Il nodo RepeatLatentBatch è progettato per replicare un determinato batch di rappresentazioni latenti un numero specificato di volte, includendo potenzialmente dati aggiuntivi come maschere di rumore e indici di batch. Questa funzionalità è cruciale per le operazioni che richiedono più istanze degli stessi dati latenti, come il data augmentation o specifiche attività generative.

## Input

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `samples` | Il parametro 'samples' rappresenta le rappresentazioni latenti da replicare. È essenziale per definire i dati che saranno sottoposti a ripetizione. | `LATENT` |
| `amount` | Il parametro 'amount' specifica il numero di volte in cui i campioni di input devono essere ripetuti. Influisce direttamente sulla dimensione del batch di output, incidendo così sul carico computazionale e sulla diversità dei dati generati. | `INT` |

## Output

| Parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| `latent` | L'output è una versione modificata delle rappresentazioni latenti di input, replicate in base al valore specificato di 'amount'. Può includere maschere di rumore replicate e indici di batch adattati, se applicabile. | `LATENT` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RepeatLatentBatch/it.md)
