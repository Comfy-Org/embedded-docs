# SamplerDPMPP_3M_SDE

Il nodo SamplerDPMPP_3M_SDE crea un campionatore DPM++ 3M SDE da usare nel processo di campionamento. Questo campionatore utilizza un metodo a più passi del terzo ordine basato su equazioni differenziali stocastiche, con parametri del rumore configurabili. Il nodo consente di scegliere se i calcoli del rumore vengono eseguiti sulla GPU o sulla CPU.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `eta` | Controlla la stocasticità del processo di campionamento (predefinito: 1.0) | FLOAT | Sì | 0.0 - 100.0 |
| `s_noise` | Controlla la quantità di rumore aggiunta durante il campionamento (predefinito: 1.0) | FLOAT | Sì | 0.0 - 100.0 |
| `noise_device` | Seleziona il dispositivo per i calcoli del rumore, GPU o CPU (predefinito: "gpu") | COMBO | Sì | "gpu"<br>"cpu" |

Nota: tutti e tre gli input sono parametri avanzati.

Quando `noise_device` è impostato su "cpu", viene creato il campionatore standard `dpmpp_3m_sde`; quando è impostato su "gpu", viene creato il campionatore `dpmpp_3m_sde_gpu` accelerato su GPU.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `sampler` | Restituisce un oggetto campionatore configurato da usare nei flussi di lavoro di campionamento | SAMPLER |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_3M_SDE/it.md)

---
**Source fingerprint (SHA-256):** `0f624398c67e50639fc41384b50b91bab93797bd785dda25f1f5fc649e46825b`
