# SamplerCustom

Il nodo SamplerCustom è progettato per fornire un meccanismo di campionamento flessibile e personalizzabile per diverse applicazioni. Consente agli utenti di selezionare e configurare diverse strategie di campionamento adattate alle proprie esigenze specifiche, migliorando l'adattabilità e l'efficienza del processo di campionamento.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il tipo di input 'model' specifica il modello da utilizzare per il campionamento, svolgendo un ruolo cruciale nel determinare il comportamento del campionamento e l'output. | `MODEL` |
| `add_noise` | Il tipo di input 'add_noise' consente agli utenti di specificare se aggiungere rumore al processo di campionamento, influenzando la diversità e le caratteristiche dei campioni generati. | `BOOLEAN` |
| `noise_seed` | Il tipo di input 'noise_seed' fornisce un seed per la generazione del rumore, garantendo riproducibilità e coerenza nel processo di campionamento quando si aggiunge rumore. | `INT` |
| `cfg` | Il tipo di input 'cfg' imposta la configurazione per il processo di campionamento, consentendo una messa a punto dei parametri e del comportamento del campionamento. | `FLOAT` |
| `positive` | Il tipo di input 'positive' rappresenta informazioni di condizionamento positive, guidando il processo di campionamento verso la generazione di campioni che si allineano con gli attributi positivi specificati. | `CONDITIONING` |
| `negative` | Il tipo di input 'negative' rappresenta informazioni di condizionamento negative, orientando il processo di campionamento lontano dalla generazione di campioni che presentano gli attributi negativi specificati. | `CONDITIONING` |
| `sampler` | Il tipo di input 'sampler' seleziona la specifica strategia di campionamento da impiegare, incidendo direttamente sulla natura e sulla qualità dei campioni generati. | `SAMPLER` |
| `sigmas` | Il tipo di input 'sigmas' definisce i livelli di rumore da utilizzare nel processo di campionamento, influenzando l'esplorazione dello spazio dei campioni e la diversità dell'output. | `SIGMAS` |
| `latent_image` | Il tipo di input 'latent_image' fornisce un'immagine latente iniziale per il processo di campionamento, fungendo da punto di partenza per la generazione dei campioni. | `LATENT` |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `output` | Il valore 'output' rappresenta il risultato principale del processo di campionamento, contenente i campioni generati. | `LATENT` |
| `denoised_output` | Il valore 'denoised_output' rappresenta i campioni dopo l'applicazione di un processo di denoising, migliorando potenzialmente la chiarezza e la qualità dei campioni generati. | `LATENT` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerCustom/it.md)
