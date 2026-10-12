# Moltiplica Latent

Il nodo LatentMultiply è progettato per scalare la rappresentazione latente dei campioni tramite un moltiplicatore specificato. Questa operazione consente di regolare l'intensità o l'ampiezza delle caratteristiche all'interno dello spazio latente, permettendo di ottimizzare con precisione il contenuto generato o di esplorare variazioni all'interno di una data direzione latente.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `samples` | Il parametro `samples` rappresenta le rappresentazioni latenti da scalare. È cruciale per definire i dati di input sui quali verrà eseguita l'operazione di moltiplicazione. | `LATENT` |
| `multiplier` | Il parametro `multiplier` specifica il fattore di scala da applicare ai campioni latenti. Svolge un ruolo chiave nella regolazione dell'ampiezza delle caratteristiche latenti, consentendo un controllo preciso sull'output generato. | `FLOAT` |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `latent` | L'output è una versione modificata dei campioni latenti di input, scalata dal moltiplicatore specificato. Ciò consente di esplorare variazioni all'interno dello spazio latente regolando l'intensità delle sue caratteristiche. | `LATENT` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentMultiply/it.md)
