# KSamplerAdvanced

Il nodo KSamplerAdvanced è progettato per migliorare il processo di campionamento fornendo configurazioni e tecniche avanzate. Mira a offrire opzioni più sofisticate per generare campioni da un modello, migliorando le funzionalità di base di KSampler.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Specifica il modello da cui generare i campioni, svolgendo un ruolo cruciale nel processo di campionamento. | MODEL |
| `add_noise` | Determina se aggiungere rumore al processo di campionamento, influenzando la diversità e la qualità dei campioni generati. | COMBO[STRING] |
| `noise_seed` | Imposta il seme per la generazione del rumore, garantendo la riproducibilità nel processo di campionamento. | INT |
| `steps` | Definisce il numero di passi da eseguire nel processo di campionamento, influenzando il dettaglio e la qualità dell'output. | INT |
| `cfg` | Controlla il fattore di condizionamento, influenzando la direzione e lo spazio del processo di campionamento. | FLOAT |
| `sampler_name` | Seleziona lo specifico sampler da utilizzare, consentendo la personalizzazione della tecnica di campionamento. | COMBO[STRING] |
| `scheduler` | Sceglie lo scheduler per controllare il processo di campionamento, influenzando la progressione e la qualità dei campioni. | COMBO[STRING] |
| `positive` | Specifica il condizionamento positivo per guidare il campionamento verso gli attributi desiderati. | CONDITIONING |
| `negative` | Specifica il condizionamento negativo per allontanare il campionamento da determinati attributi. | CONDITIONING |
| `latent_image` | Fornisce l'immagine latente iniziale da utilizzare nel processo di campionamento, fungendo da punto di partenza. | LATENT |
| `start_at_step` | Determina il passo iniziale del processo di campionamento, consentendo di controllare la progressione del campionamento. | INT |
| `end_at_step` | Imposta il passo finale del processo di campionamento, definendo l'ambito del campionamento. | INT |
| `return_with_leftover_noise` | Indica se restituire il campione con il rumore residuo, influenzando l'aspetto dell'output finale. | COMBO[STRING] |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `latent` | L'output rappresenta l'immagine latente generata dal modello, riflettendo le configurazioni e le tecniche applicate. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KSamplerAdvanced/it.md)
