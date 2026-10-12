# Codifica VAE (a blocchi)

VAEEncodeTiled elabora le immagini suddividendole in tile più piccole e codificandole utilizzando un autoencoder variazionale. Questo approccio a tile permette di gestire immagini di grandi dimensioni che altrimenti potrebbero superare i limiti di memoria. Il nodo supporta sia VAE per immagini che VAE per video, con controlli di suddivisione in tile separati per le dimensioni spaziali e temporali.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `pixels` | I dati dell'immagine di input da codificare. | IMAGE | Sì | - |
| `vae` | Il modello autoencoder variazionale utilizzato per la codifica. | VAE | Sì | - |
| `tile_size` | La dimensione di ciascuna tile per l'elaborazione spaziale (predefinito: 512). Impostazione avanzata. | INT | Sì | 64-4096 (step: 64) |
| `overlap` | La quantità di sovrapposizione tra tile adiacenti (predefinito: 64). Impostazione avanzata. | INT | Sì | 0-4096 (step: 32) |
| `temporal_size` | Utilizzato solo per VAE video: numero di frame da codificare alla volta (predefinito: 64). Impostazione avanzata. | INT | Sì | 8-4096 (step: 4) |
| `temporal_overlap` | Utilizzato solo per VAE video: numero di frame da sovrapporre (predefinito: 8). Impostazione avanzata. | INT | Sì | 4-4096 (step: 4) |

**Nota:** I parametri `temporal_size` e `temporal_overlap` sono rilevanti solo quando si utilizzano VAE video e non hanno alcun effetto sui VAE standard per immagini.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `LATENT` | La rappresentazione latente codificata dell'immagine di input. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeTiled/it.md)

---
**Source fingerprint (SHA-256):** `c36b02f8eeed5c72f9efa2392e2013e89be7644c022d987d413d4da088dfbaad`
