# EpsilonScaling

Implementa il metodo Epsilon Scaling dall'articolo di ricerca "Elucidating the Exposure Bias in Diffusion Models." Questo metodo migliora la qualità dei campioni scalando il rumore previsto durante il processo di campionamento. Utilizza una pianificazione uniforme per mitigare il bias di esposizione nei modelli di diffusione.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello a cui applicare Epsilon Scaling | MODEL | Sì | - |
| `scaling_factor` | Il fattore utilizzato per scalare il rumore previsto (predefinito: 1.005) | FLOAT | No | 0.5 - 1.5 |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `model` | Il modello a cui è stato applicato Epsilon Scaling | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EpsilonScaling/it.md)
