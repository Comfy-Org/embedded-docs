# Immagine Latent Vuota

Il nodo `EmptyLatentImage` è progettato per generare una rappresentazione vuota dello spazio latente con dimensioni e dimensione del batch specificate. Questo nodo costituisce un passo fondamentale nella generazione o manipolazione di immagini nello spazio latente, fornendo un punto di partenza per ulteriori processi di sintesi o modifica delle immagini.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `width` | Specifica la larghezza dell'immagine latente da generare. Questo parametro influenza direttamente le dimensioni spaziali della rappresentazione latente risultante. | `INT` |
| `height` | Determina l'altezza dell'immagine latente da generare. Questo parametro è cruciale per definire le dimensioni spaziali della rappresentazione dello spazio latente. | `INT` |
| `batch_size` | Controlla il numero di immagini latenti da generare in un singolo batch. Ciò consente di generare più rappresentazioni latenti simultaneamente, facilitando l'elaborazione batch. | `INT` |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `latent` | L'output è un tensore che rappresenta un batch di immagini latenti vuote, che funge da base per ulteriori generazioni o manipolazioni di immagini nello spazio latente. | `LATENT` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentImage/it.md)
