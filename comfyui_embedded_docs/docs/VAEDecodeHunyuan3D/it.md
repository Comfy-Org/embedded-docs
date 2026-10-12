# VAEDecodeHunyuan3D

Il nodo VAEDecodeHunyuan3D converte le rappresentazioni latenti in dati voxel 3D utilizzando un decoder VAE. Elabora i campioni latenti attraverso il modello VAE con impostazioni configurabili di suddivisione in chunk e risoluzione per generare dati volumetrici adatti ad applicazioni 3D.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `samples` | La rappresentazione latente da decodificare in dati voxel 3D | LATENT | Sì | - |
| `vae` | Il modello VAE utilizzato per decodificare i campioni latenti | VAE | Sì | - |
| `num_chunks` | Il numero di chunk in cui suddividere l'elaborazione per la gestione della memoria. Parametro avanzato (predefinito: 8000) | INT | Sì | 1000-500000 |
| `octree_resolution` | La risoluzione della struttura octree utilizzata per la generazione di voxel 3D. Parametro avanzato (predefinito: 256) | INT | Sì | 16-512 |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `voxels` | I dati voxel 3D generati dalla rappresentazione latente decodificata | VOXEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeHunyuan3D/it.md)

---
**Source fingerprint (SHA-256):** `740e328e9e7817aa1a029c5fadddf5457c91bbb5ac12c7e8af2cd81bee6184a7`
