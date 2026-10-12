# WanFunControlToVideo

Questo nodo è stato aggiunto per supportare il modello Alibaba Wan Fun Control per la generazione video ed è stato introdotto dopo [questo commit](https://github.com/comfyanonymous/ComfyUI/commit/3661c833bcc41b788a7c9f0e7bc48524f8ee5f82).

- **Scopo:** Preparare le informazioni di condizionamento necessarie per la generazione video, utilizzando il modello Wan 2.1 Fun Control.

Il nodo WanFunControlToVideo è un'aggiunta a ComfyUI progettata per supportare i modelli Wan Fun Control per la generazione video, con l'obiettivo di utilizzare WanFun control per la creazione di video.

Questo nodo funge da punto di preparazione per le informazioni di condizionamento essenziali e inizializza il punto centrale dello spazio latente, guidando il successivo processo di generazione video con il modello Wan 2.1 Fun. Il nome del nodo indica chiaramente la sua funzione: accetta vari input e li converte in un formato adatto a controllare la generazione video all'interno del framework WanFun.

La posizione del nodo nella gerarchia dei nodi di ComfyUI indica che opera nelle fasi iniziali della pipeline di generazione video, concentrandosi sulla manipolazione dei segnali di condizionamento prima del campionamento o della decodifica effettivi dei fotogrammi video.

## Input

| Nome parametro | Descrizione | Obbligatorio | Tipo di dati | Valore predefinito |
| --- | --- | --- | --- | --- |
| positive | Dati di condizionamento positivo standard di ComfyUI, tipicamente da un nodo "CLIP Text Encode". Il prompt positivo descrive il contenuto, il soggetto e lo stile artistico che l'utente immagina per il video generato. | Sì | CONDITIONING | N/A |
| negative | Dati di condizionamento negativo standard di ComfyUI, tipicamente generati da un nodo "CLIP Text Encode". Il prompt negativo specifica elementi, stili o artefatti che l'utente vuole evitare nel video generato. | Sì | CONDITIONING | N/A |
| vae | Richiede un modello VAE (Variational Autoencoder) compatibile con la famiglia di modelli Wan 2.1 Fun, utilizzato per codificare e decodificare dati immagine/video. | Sì | VAE | N/A |
| width | La larghezza desiderata dei fotogrammi video di output in pixel, con valore predefinito 832, valore minimo 16, valore massimo determinato da nodes.MAX_RESOLUTION e passo di 16. | Sì | INT | 832 |
| height | L'altezza desiderata dei fotogrammi video di output in pixel, con valore predefinito 480, valore minimo 16, valore massimo determinato da nodes.MAX_RESOLUTION e passo di 16. | Sì | INT | 480 |
| length | Il numero totale di fotogrammi nel video generato, con valore predefinito 81, valore minimo 1, valore massimo determinato da nodes.MAX_RESOLUTION e passo di 4. | Sì | INT | 81 |
| batch_size | Il numero di video generati in un singolo batch, con valore predefinito 1, valore minimo 1 e valore massimo 4096. | Sì | INT | 1 |
| clip_vision_output | (Opzionale) Caratteristiche visive estratte da un modello CLIP vision, che consentono una guida allo stile visivo e al contenuto. | No | CLIP_VISION_OUTPUT | None |
| start_image | (Opzionale) Un'immagine iniziale che influenza l'inizio del video generato. | No | IMAGE | None |
| control_video | (Opzionale) Consente agli utenti di fornire un video di riferimento ControlNet preprocessato che guiderà il movimento e la potenziale struttura del video generato. | No | IMAGE | None |

## Output

| Nome parametro | Descrizione | Tipo di dati |
| --- | --- | --- |
| positive | Fornisce dati di condizionamento positivo migliorati, inclusi start_image e control_video codificati. | CONDITIONING |
| negative | Fornisce dati di condizionamento negativo anch'essi migliorati, contenenti lo stesso concat_latent_image. | CONDITIONING |
| latent | Un dizionario contenente un tensore latente vuoto con la chiave "samples". | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanFunControlToVideo/it.md)
