# SamplerEulerAncestralCFG++

Il nodo SamplerEulerAncestralCFG++ crea un sampler che utilizza il metodo Euler Ancestral con classifier-free guidance (CFG++) per la generazione di immagini. Questo sampler combina tecniche di campionamento ancestrale con il condizionamento di guida per produrre varie variazioni dell'immagine mantenendo la coerenza e consente una messa a punto tramite parametri che controllano il rumore e la regolazione della dimensione del passo.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `eta` | Controlla la dimensione del passo durante il campionamento; valori più alti producono aggiornamenti più aggressivi (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `s_noise` | Regola la quantità di rumore aggiunta durante il processo di campionamento (predefinito: 1.0) | FLOAT | Sì | 0.0 - 10.0 |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `sampler` | Restituisce un oggetto sampler configurato che può essere utilizzato nella pipeline di generazione di immagini | SAMPLER |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerEulerAncestralCFGPP/it.md)

---
**Source fingerprint (SHA-256):** `de83cb4c3e9aeee60f1554ad1af8181adb4fa62e3d23cec02a6f4396b96500c1`
