# ExponentialScheduler

Il nodo `ExponentialScheduler` è progettato per generare una sequenza di valori sigma seguendo una schedulazione esponenziale per i processi di campionamento della diffusione. Fornisce un approccio personalizzabile per controllare i livelli di rumore applicati a ogni passo del processo di diffusione, consentendo di ottimizzare finemente il comportamento di campionamento.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `steps` | Specifica il numero di passi nel processo di diffusione. Influisce sulla lunghezza della sequenza sigma generata e quindi sulla granularità dell'applicazione del rumore. | INT |
| `sigma_max` | Definisce il valore massimo di sigma, impostando il limite superiore dell'intensità del rumore nel processo di diffusione. Svolge un ruolo cruciale nel determinare l'intervallo dei livelli di rumore applicati. | FLOAT |
| `sigma_min` | Imposta il valore minimo di sigma, stabilendo il limite inferiore dell'intensità del rumore. Questo parametro aiuta a ottimizzare finemente il punto di partenza dell'applicazione del rumore. | FLOAT |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `sigmas` | Una sequenza di valori sigma generata secondo la schedulazione esponenziale. Questi valori vengono utilizzati per controllare i livelli di rumore a ogni passo del processo di diffusione. | SIGMAS |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ExponentialScheduler/it.md)
