# Stablezero123Conditioning

Questo nodo è progettato per elaborare e condizionare i dati per l'uso nei modelli StableZero123, concentrandosi sulla preparazione dell'input in un formato specifico compatibile e ottimizzato per questi modelli.

## Input

| Parametro | Descrizione | Tipo Comfy |
| --- | --- | --- |
| `clip_vision` | Elabora dati visivi per allinearli ai requisiti del modello, migliorando la comprensione del contesto visivo da parte del modello. | `CLIP_VISION` |
| `init_image` | Funge da immagine iniziale di input per il modello, stabilendo la base per ulteriori operazioni basate su immagini. | `IMAGE` |
| `vae` | Integra gli output dell'autoencoder variazionale, facilitando la capacità del modello di generare o modificare immagini. | `VAE` |
| `width` | Specifica la larghezza dell'immagine di output, consentendo un ridimensionamento dinamico in base alle esigenze del modello. | `INT` |
| `height` | Determina l'altezza dell'immagine di output, consentendo la personalizzazione delle dimensioni di output. | `INT` |
| `batch_size` | Controlla il numero di immagini elaborate in un singolo batch, ottimizzando l'efficienza computazionale. | `INT` |
| `elevation` | Regola l'angolo di elevazione per il rendering di modelli 3D, migliorando la comprensione spaziale del modello. | `FLOAT` |
| `azimuth` | Modifica l'angolo di azimut per la visualizzazione di modelli 3D, migliorando la percezione dell'orientamento da parte del modello. | `FLOAT` |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `positive` | Genera vettori di condizionamento positivi, contribuendo al rafforzamento delle caratteristiche positive da parte del modello. | `CONDITIONING` |
| `negative` | Produce vettori di condizionamento negativi, aiutando il modello a evitare determinate caratteristiche. | `CONDITIONING` |
| `latent` | Crea rappresentazioni latenti, facilitando una comprensione più approfondita dei dati da parte del modello. | `LATENT` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Stablezero123Conditioning/it.md)
