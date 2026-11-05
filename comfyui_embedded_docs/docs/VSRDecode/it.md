# VSR Decode

VSR Decode riconverte i latent dei keyframe prodotti da RelayVSR Conditioning in un video completo con il decoder RelayVSR Flash. Il decoder aggiunge il proprio dettaglio sopra un upscale bicubico dei frame a bassa qualità forniti in input, secondo il fattore x2 o x4 del decoder. Il numero di frame rimane invariato.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `vae` | Il decoder RelayVSR Flash, caricato con Load VAE: `relayvsr_flash_vae_x2_fp32.safetensors` oppure `relayvsr_flash_vae_x4_fp32.safetensors`. I metadati del file impostano il fattore di upscale, quindi deve corrispondere al modello. | VAE | Sì | N/A |
| `samples` | Il latent restituito dal sampler, che contiene un frame per ogni keyframe. | LATENT | Sì | N/A |
| `images` | Lo stesso video a bassa qualità fornito a RelayVSR Conditioning. | IMAGE | Sì | N/A |
| `detail` | Quanto del dettaglio del decoder viene mantenuto sopra l'upscale bicubico: 1 è l'output completo del modello, 0 è il semplice upscale. (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 (passo 0.01) |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `images` | Il video sottoposto a upscale con tutti i frame ripristinati. | IMAGE |

## Note

- Fornisci lo stesso video a bassa qualità a entrambi i nodi. Il decoder lo legge frame per frame, quindi una discrepanza in lunghezza o risoluzione produce un risultato errato o corrotto.
- Ridurre `detail` attenua il dettaglio ripristinato e mantiene l'output più vicino a un semplice upscale bicubico, il che può aiutare con sorgenti molto rumorose.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VSRDecode/it.md)

---
**Source fingerprint (SHA-256):** `946ac04bc9f205fd6d1088554caaa16238086e570f212e747b166e3fb0d9b3c5`
