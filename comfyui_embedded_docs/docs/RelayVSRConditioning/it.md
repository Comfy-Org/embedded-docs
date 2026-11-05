# RelayVSRConditioning

RelayVSR Conditioning prepara il condizionamento e il latent vuoto per un upscale video RelayVSR. RelayVSR esegue il suo modello Wan 2.2 a un passo solo su ogni 15° frame della clip, più l'ultimo, quindi il latent che restituisce contiene solo quei keyframe. VSR Decode riempie poi i frame tra di essi.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello di diffusione RelayVSR, caricato con Load Model: `relayvsr_x2_lightx2v_int8_convrot.safetensors` o `relayvsr_x4_int8_convrot.safetensors`. | MODEL | Sì | N/A |
| `images` | Il video di bassa qualità alla sua risoluzione nativa. Il fattore di upscale del modello determina quanto grande sarà il risultato. | IMAGE | Sì | N/A |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `positive` | Condizionamento che veicola i keyframe selezionati come guida a bassa qualità. | CONDITIONING |
| `latent` | Latent vuoto con un frame per keyframe, pronto per il sampler. | LATENT |

## Utilizzo

Campiona il `latent` con un passo a CFG 1: non ci sono prompt né text encoder nel grafo. Invia l'output del sampler, gli stessi `images` e un RelayVSR Flash VAE a VSR Decode, e mantieni la coppia abbinata: il modello x2 con il decoder x2, il modello x4 con il decoder x4.

Vengono campionati solo i keyframe, quindi una clip di 150 frame diventa un latent di 11 frame. Il sampler lavora su una piccola frazione del video e VSR Decode ripristina il resto.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RelayVSRConditioning/it.md)

---
**Source fingerprint (SHA-256):** `fd1a86262240430e4f2a811c2c9d8d62f0b6cdfccb26d5285e36d0d6de3b186f`
