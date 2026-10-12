# SamplerEulerAncestral

Il nodo SamplerEulerAncestral crea un sampler Euler Ancestral che può essere utilizzato durante la generazione delle immagini. Questo sampler combina l'integrazione di Euler con il campionamento ancestrale, che aggiunge un certo grado di casualità a ogni passaggio per produrre risultati vari. Il nodo consente di regolare quanta casualità viene applicata tramite le sue impostazioni.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `eta` | Controlla la dimensione del passo e la stocasticità del processo di campionamento (predefinito: 1.0). Questo è un parametro avanzato. | FLOAT | Sì | 0.0 - 100.0 |
| `s_noise` | Controlla la quantità di rumore aggiunto durante il campionamento (predefinito: 1.0). Questo è un parametro avanzato. | FLOAT | Sì | 0.0 - 100.0 |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `sampler` | Restituisce un sampler Euler Ancestral configurato che può essere utilizzato nella pipeline di campionamento. | SAMPLER |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestral/it.md)

---
**Source fingerprint (SHA-256):** `0d3c1f0ffe01eb6cc17fd53e743713f659218ec19001c670440472ae7d0d3887`
