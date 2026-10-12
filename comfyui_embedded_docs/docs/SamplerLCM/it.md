# SamplerLCM

Questo nodo fornisce un sampler LCM (Latent Consistency Model) con rumore regolabile per step. Consente di controllare quanto rumore viene applicato durante il campionamento: `s_noise` funge da moltiplicatore sulla scala di rumore di addestramento del modello, e il livello di rumore può variare dal primo all'ultimo step. Il sampler configurato può quindi essere inserito in un flusso di campionamento.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `s_noise` | Moltiplicatore del rumore per step al primo step (1.0 = corrisponde all'addestramento). Predefinito: 1.0. | FLOAT | Sì | da 0.0 a 64.0 (passo: 0.01) |
| `s_noise_end` | Moltiplicatore del rumore per step all'ultimo step. Impostare uguale a `s_noise` per una schedulazione costante. Predefinito: 1.0. | FLOAT | Sì | da 0.0 a 64.0 (passo: 0.01) |
| `noise_clip_std` | Limita il rumore per step a +/- N*std. 0 disabilita. Predefinito: 0.0. | FLOAT | Sì | da 0.0 a 10.0 (passo: 0.01) |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `SAMPLER` | L'oggetto sampler LCM configurato, pronto per essere usato in un flusso di campionamento. | SAMPLER |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerLCM/it.md)

---
**Source fingerprint (SHA-256):** `0d18f2f977ddadeedcd7807233b48ebcc4e94c6213f8540b9037a45a9c70c6cf`
