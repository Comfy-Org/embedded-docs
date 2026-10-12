# Affila Latent

Il nodo LatentOperationSharpen crea un'operazione di nitidezza per rappresentazioni latenti utilizzando un kernel basato su gaussiana. Normalizza i dati latenti, applica un kernel di nitidezza personalizzato tramite convoluzione e poi ripristina la luminanza originale, migliorando dettagli e bordi nella rappresentazione dello spazio latente.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `sharpen_radius` | Il raggio del kernel di nitidezza, che controlla la dimensione dell'area utilizzata per la nitidezza (predefinito: 9) | INT | Sì | 1-31 |
| `sigma` | La deviazione standard del kernel gaussiano utilizzato per costruire il kernel di nitidezza (predefinito: 1.0) | FLOAT | Sì | 0.1-10.0 |
| `alpha` | Il fattore di intensità della nitidezza; valori più alti producono un effetto di nitidezza più forte (predefinito: 0.1) | FLOAT | Sì | 0.0-5.0 |

Tutti e tre gli input sono parametri avanzati e hanno valori predefiniti, quindi il nodo può essere utilizzato senza modificarli. Questo nodo è contrassegnato come sperimentale.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `operation` | Restituisce un'operazione di nitidezza che può essere applicata ai dati latenti | LATENT_OPERATION |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentOperationSharpen/it.md)

---
**Source fingerprint (SHA-256):** `8f49b7e47d35547a7169e9ec209328adbe084ee861ac26b9f26e4e644ac14d6d`
