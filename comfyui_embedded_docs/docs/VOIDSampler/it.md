# VOIDSampler

VOIDSampler è un sampler DDIM specializzato progettato per i modelli di inpainting VOID. Riproduce esattamente il processo di denoising con cui VOID è stato addestrato, saltando la scalatura del rumore che i KSampler standard applicano. Usa questo nodo insieme a SamplerCustom o SamplerCustomAdvanced, abbinato a RandomNoise o VOIDWarpedNoiseSource.

## Input

Questo nodo non ha parametri di input configurabili. È un sampler autonomo che applica un algoritmo di campionamento DDIM fisso.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| *Nessun input* | Questo nodo non accetta alcun parametro di input. | - | - | - |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `SAMPLER` | Un oggetto sampler che implementa l'algoritmo DDIM di VOID, pronto per essere collegato ai nodi SamplerCustom o SamplerCustomAdvanced. | SAMPLER |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VOIDSampler/it.md)

---
**Source fingerprint (SHA-256):** `b8bb6d3d7220cca4a6dd252efe9c92953b1c5c67c14365e5e0583bc9bdb133be`
