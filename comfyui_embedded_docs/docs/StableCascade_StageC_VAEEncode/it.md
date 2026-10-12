# StableCascade_StageC_VAEEncode

Il nodo StableCascade_StageC_VAEEncode elabora un'immagine di input attraverso un encoder VAE per generare rappresentazioni latenti per il modello Stable Cascade. Prima ridimensiona l'immagine in base a un fattore di compressione e al rapporto di downscale del VAE, poi codifica l'immagine ridimensionata. Il nodo restituisce due tensori latenti: uno per lo stage C (il risultato codificato effettivo) e uno per lo stage B (un segnaposto riempito di zeri).

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `image` | L'immagine di input da codificare nello spazio latente | IMAGE | Sì | - |
| `vae` | Il modello VAE utilizzato per codificare l'immagine | VAE | Sì | - |
| `compression` | Il fattore di compressione applicato all'immagine prima della codifica. Le dimensioni dell'immagine vengono divise per questo valore, quindi moltiplicate per il rapporto di downscale del VAE. Questo è un parametro avanzato. (predefinito: 42) | INT | Sì | 4-128 (step: 1) |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `stage_c` | La rappresentazione latente codificata per lo stage C del modello Stable Cascade | LATENT |
| `stage_b` | Una rappresentazione latente segnaposto per lo stage B. Attualmente restituisce un tensore riempito di zeri con dimensioni calcolate dalla dimensione dell'immagine di input. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_StageC_VAEEncode/it.md)

---
**Source fingerprint (SHA-256):** `1679aaac77057fcc359e5428906d5227f6c2dde721aabbfb5a32c08738ac376c`
