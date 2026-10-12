# VOIDWarpedNoiseSource

Questo nodo converte un LATENT (come l'output del nodo VOIDWarpedNoise) in una sorgente NOISE. Ciò consente di fornire rumore distorto precalcolato a nodi che si aspettano una sorgente di rumore, come SamplerCustomAdvanced.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `warped_noise` | Latent di rumore distorto da VOIDWarpedNoise | LATENT | Sì | N/A |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `NOISE` | Una sorgente di rumore che racchiude il latent fornito, utilizzabile con SamplerCustomAdvanced | NOISE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDWarpedNoiseSource/it.md)

---
**Source fingerprint (SHA-256):** `61d7c82cb8a2acba28f980c4c42c6d4be12788b27676a5d30885799cf9c36185`
