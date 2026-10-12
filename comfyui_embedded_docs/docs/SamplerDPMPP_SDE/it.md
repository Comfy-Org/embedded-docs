# SamplerDPMPP_SDE

## Panoramica

SamplerDPMPP_SDE crea un campionatore DPM++ SDE (Stochastic Differential Equation) da utilizzare nel processo di campionamento. Questo campionatore fornisce un metodo di campionamento stocastico con parametri di rumore configurabili e selezione del dispositivo. Restituisce un oggetto campionatore che può essere utilizzato nella pipeline di campionamento.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `eta` | Controlla la stocasticità del processo di campionamento (predefinito: 1.0) | FLOAT | Sì | 0.0 - 100.0 |
| `s_noise` | Controlla la quantità di rumore aggiunto durante il campionamento (predefinito: 1.0) | FLOAT | Sì | 0.0 - 100.0 |
| `r` | Un parametro che influenza il comportamento del campionamento (predefinito: 0.5) | FLOAT | Sì | 0.0 - 100.0 |
| `noise_device` | Seleziona il dispositivo in cui vengono eseguiti i calcoli del rumore. Se impostato su "cpu", viene creato il campionatore `dpmpp_sde`; se impostato su "gpu", viene creato il campionatore `dpmpp_sde_gpu` (predefinito: "gpu") | COMBO | Sì | "gpu"<br>"cpu" |

Nota: tutti gli input sono contrassegnati come parametri avanzati. La selezione `noise_device` cambia quale variante del campionatore viene creata: "cpu" corrisponde a `dpmpp_sde` e "gpu" corrisponde a `dpmpp_sde_gpu`.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `sampler` | Restituisce un oggetto campionatore DPM++ SDE configurato per l'uso nelle pipeline di campionamento | SAMPLER |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_SDE/it.md)

---
**Source fingerprint (SHA-256):** `56949712f245abfcc48c09d7d14a1a7778e80ba58535e538484c382d7e0d02c6`
