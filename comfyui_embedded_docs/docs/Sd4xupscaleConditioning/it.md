# Sd4xupscaleConditioning

Questo nodo è specializzato nell'aumentare la risoluzione delle immagini tramite un processo di upscale 4x, integrando elementi di condizionamento per perfezionare l'output. Sfrutta tecniche di diffusione per eseguire l'upscale delle immagini, consentendo al contempo la regolazione del rapporto di scala e dell'aumento del rumore per ottimizzare il processo di miglioramento.

## Input

| Parametro | Descrizione | Tipo Comfy |
| --- | --- | --- |
| `images` | Le immagini di input da sottoporre a upscale. Questo parametro è cruciale poiché influenza direttamente la qualità e la risoluzione delle immagini di output. | `IMAGE` |
| `positive` | Elementi di condizionamento positivi che guidano il processo di upscale verso attributi o caratteristiche desiderati nelle immagini di output. | `CONDITIONING` |
| `negative` | Elementi di condizionamento negativi che il processo di upscale dovrebbe evitare, contribuendo a orientare l'output lontano da attributi o caratteristiche indesiderati. | `CONDITIONING` |
| `scale_ratio` | Determina il fattore di aumento della risoluzione dell'immagine. Un rapporto di scala più alto produce un'immagine di output più grande, consentendo maggiori dettagli e nitidezza. | `FLOAT` |
| `noise_augmentation` | Controlla il livello di aumento del rumore applicato durante il processo di upscale. Può essere usato per introdurre variabilità e migliorare la robustezza delle immagini di output. | `FLOAT` |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `positive` | Gli elementi di condizionamento positivi perfezionati risultanti dal processo di upscale. | `CONDITIONING` |
| `negative` | Gli elementi di condizionamento negativi perfezionati risultanti dal processo di upscale. | `CONDITIONING` |
| `latent` | Una rappresentazione latente generata durante il processo di upscale, che può essere utilizzata in ulteriori elaborazioni o nell'addestramento del modello. | `LATENT` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Sd4xupscaleConditioning/it.md)
