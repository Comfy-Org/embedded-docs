# Trellis2UpsampleStage

Questo nodo esegue l'upscaling di un latent della forma a risoluzione 512 in coordinate sparse ad alta risoluzione e prepara il secondo passaggio di campionamento della fase della forma alla risoluzione target. Collega metadati per fase al condizionamento, così che il modello possa utilizzarli durante la generazione.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `positive` | Il condizionamento positivo a cui vengono collegati i metadati della forma della fase di upsampling. | CONDITIONING | Sì | |
| `negative` | Il condizionamento negativo a cui vengono collegati i metadati della forma della fase di upsampling. | CONDITIONING | Sì | |
| `shape_latent` | Il latent della forma a risoluzione 512 prodotto dal primo KSampler della fase della forma. | LATENT | Sì | |
| `vae` | Il VAE Trellis2 utilizzato per decodificare il latent della forma in coordinate sparse ad alta risoluzione. | VAE | Sì | |
| `target_resolution` | Risoluzione voxel della forma sottoposta a upsampling. Più alta = più dettagli, più VRAM. Predefinito: 1024. | INT | Sì | 1024 - 2048 (passo 128) |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `positive` | Condizionamento positivo con i metadati della forma della fase di upsampling collegati. | CONDITIONING |
| `negative` | Condizionamento negativo con i metadati della forma della fase di upsampling collegati. | CONDITIONING |
| `latent` | Latent riempito di zeri preparato per il secondo passaggio di campionamento della fase della forma alla risoluzione target, che trasporta le coordinate sottoposte a upsampling, i conteggi di coordinate per campione e i metadati di risoluzione delle coordinate. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2UpsampleStage/it.md)

---
**Source fingerprint (SHA-256):** `0582579bfab487718d69789de508a5ec243d98a0e06ad7165c406154a64677d6`
