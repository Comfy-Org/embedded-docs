# StableCascade_SuperResolutionControlnet

Questo nodo fa parte del gruppo sperimentale Stable Cascade. Prepara gli input per l'elaborazione di super-risoluzione di Stable Cascade codificando un'immagine di input con un VAE per creare un input per ControlNet e generando segnaposto latenti vuoti (riempiti di zeri) per lo stage C e lo stage B della pipeline di Stable Cascade.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `image` | L'immagine di input da elaborare per la super-risoluzione. Per la codifica vengono utilizzati solo i primi 3 canali di colore (RGB) dell'immagine. | IMAGE | Sì | - |
| `vae` | Il modello VAE utilizzato per codificare l'immagine di input | VAE | Sì | - |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `controlnet_input` | La rappresentazione dell'immagine codificata dal VAE, adatta come input per ControlNet | IMAGE |
| `stage_c` | Rappresentazione latente segnaposto (riempita di zeri) per lo stage C dell'elaborazione Stable Cascade, con 16 canali e dimensioni basate sulla dimensione dell'immagine di input divisa per 16 | LATENT |
| `stage_b` | Rappresentazione latente segnaposto (riempita di zeri) per lo stage B dell'elaborazione Stable Cascade, con 4 canali e dimensioni basate sulla dimensione dell'immagine di input divisa per 2 | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StableCascade_SuperResolutionControlnet/it.md)

---
**Source fingerprint (SHA-256):** `d9eff373ac7736f2e2f9788d1b43c04bb3212422aa1703d1d58ac512ce476925`
