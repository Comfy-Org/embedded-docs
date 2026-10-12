# SvdImg2vidConditioning

Questo nodo è progettato per generare dati di condizionamento per attività di generazione video, specificamente adattato per l'uso con modelli SVD_img2vid. Accetta vari input, tra cui immagini iniziali, parametri video e un modello VAE, per produrre dati di condizionamento che possono essere usati per guidare la generazione dei fotogrammi video.

## Input

| Parametro | Descrizione | Comfy dtype |
| --- | --- | --- |
| `clip_vision` | Rappresenta il modello CLIP vision usato per codificare le caratteristiche visive dall'immagine iniziale, svolgendo un ruolo cruciale nella comprensione del contenuto e del contesto dell'immagine per la generazione video. | `CLIP_VISION` |
| `init_image` | L'immagine iniziale da cui verrà generato il video, che funge da punto di partenza per il processo di generazione video. | `IMAGE` |
| `vae` | Un modello Variational Autoencoder (VAE) usato per codificare l'immagine iniziale in uno spazio latente, facilitando la generazione di fotogrammi video coerenti e continui. | `VAE` |
| `width` | La larghezza desiderata dei fotogrammi video da generare, consentendo la personalizzazione della risoluzione del video. | `INT` |
| `height` | L'altezza desiderata dei fotogrammi video, consentendo il controllo delle proporzioni e della risoluzione del video. | `INT` |
| `video_frames` | Specifica il numero di fotogrammi da generare per il video, determinando la lunghezza del video. | `INT` |
| `motion_bucket_id` | Un identificatore per categorizzare il tipo di movimento da applicare nella generazione video, aiutando nella creazione di video dinamici e coinvolgenti. | `INT` |
| `fps` | La frequenza di fotogrammi al secondo (fps) del video, che influenza la fluidità e il realismo del video generato. | `INT` |
| `augmentation_level` | Un parametro che controlla il livello di aumento applicato all'immagine iniziale, influenzando la diversità e la variabilità dei fotogrammi video generati. | `FLOAT` |

## Output

| Parametro | Descrizione | Comfy dtype |
| --- | --- | --- |
| `positive` | I dati di condizionamento positivi, costituiti da caratteristiche codificate e parametri per guidare il processo di generazione video in una direzione desiderata. | `CONDITIONING` |
| `negative` | I dati di condizionamento negativi, che forniscono un contrasto al condizionamento positivo, utilizzabili per evitare determinati pattern o caratteristiche nel video generato. | `CONDITIONING` |
| `latent` | Rappresentazioni latenti generate per ogni fotogramma del video, che fungono da componente di base per il processo di generazione video. | `LATENT` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SvdImg2vidConditioning/it.md)
