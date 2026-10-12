# TripoSplat Conditioning

Questo nodo codifica un'immagine di input con l'encoder di immagini DINOv3 e il VAE Flux2 per produrre dati di condizionamento positivi e negativi per il modello TripoSplat. Crea inoltre un target di rumore a dimensione fissa (latente più dati della camera) che funge da punto di partenza per il KSampler.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `clip_vision` | Encoder di immagini DINOv3 ViT-H/16+ | CLIP_VISION | Sì | - |
| `vae` | VAE Flux2 | VAE | Sì | - |
| `image` | L'immagine di input da codificare | IMAGE | Sì | - |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `positive` | Dati di condizionamento positivi contenenti la sequenza di feature DINOv3 e il latente VAE Flux2 trasportato come latente di riferimento | CONDITIONING |
| `negative` | Dati di condizionamento negativi contenenti feature DINOv3 riempite di zeri e un latente di riferimento VAE Flux2 riempito di zeri | CONDITIONING |
| `latent` | Il target di rumore a dimensione fissa (latente + camera) per il KSampler. Il latente è una sequenza di shape-code a forma costante (8192 x 16) abbinata a un singolo token camera (1 x 5) | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatConditioning/it.md)

---
**Source fingerprint (SHA-256):** `59ebeef272d125a2cc2045f4ff54f99268b1273d0a1fd46f7462e6d312f3a805`
