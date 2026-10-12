# SamplerDPMPP_2S_Ancestral

Il nodo SamplerDPMPP_2S_Ancestral crea un sampler che utilizza il metodo di campionamento DPM++ 2S Ancestral per generare immagini. Questo sampler combina elementi deterministici e stocastici per produrre risultati variati mantenendo una certa coerenza. Consente di controllare la casualità e i livelli di rumore durante il processo di campionamento.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `eta` | Controlla la quantità di rumore stocastico aggiunto durante il campionamento (predefinito: 1.0) | FLOAT | Sì | 0.0 - 100.0 (passo 0.01) |
| `s_noise` | Controlla la scala del rumore applicato durante il processo di campionamento (predefinito: 1.0) | FLOAT | Sì | 0.0 - 100.0 (passo 0.01) |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `sampler` | Restituisce un oggetto sampler configurato che può essere utilizzato nella pipeline di campionamento | SAMPLER |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2S_Ancestral/it.md)

---
**Source fingerprint (SHA-256):** `8d20ec21e6c699965753413d9ef8b6191553c4b7b606d93c10470aa9d988a308`
