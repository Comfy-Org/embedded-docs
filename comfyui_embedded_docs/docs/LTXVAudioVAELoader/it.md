# Carica LTXV Audio VAE

Il nodo LTXV Audio VAE Loader carica un modello Audio Variational Autoencoder (VAE) pre-addestrato da un file checkpoint. Legge il checkpoint specificato, conserva i pesi dell'audio VAE e del vocoder e prepara il modello per l'uso in flussi di lavoro di generazione o elaborazione audio all'interno di ComfyUI.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `ckpt_name` | Checkpoint Audio VAE da caricare. Questa è una lista a discesa popolata con tutti i file presenti nella directory `checkpoints` di ComfyUI. | COMBO | Sì | Tutti i file nella cartella `checkpoints`. La lista viene generata in fase di esecuzione. |

Il file selezionato deve essere un checkpoint Audio VAE LTXV valido. Il nodo conserva solo i pesi dell'audio VAE e del vocoder dal file e genera un errore se il modello caricato non è un VAE valido.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `Audio VAE` | Il modello Audio Variational Autoencoder caricato, pronto per essere collegato ad altri nodi di elaborazione audio. | VAE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAELoader/it.md)

---
**Source fingerprint (SHA-256):** `c91956645a9de0b8f56191f6c0c6bef43f13724ba59078ec9a885168bf2650e8`
