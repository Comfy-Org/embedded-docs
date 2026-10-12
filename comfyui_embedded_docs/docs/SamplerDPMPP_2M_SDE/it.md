# SamplerDPMPP_2M_SDE

Il nodo SamplerDPMPP_2M_SDE crea un campionatore DPM++ 2M SDE per i modelli di diffusione. Questo campionatore utilizza risolutori di equazioni differenziali del secondo ordine con equazioni differenziali stocastiche per generare campioni. Fornisce diversi tipi di risolutore e opzioni di gestione del rumore per controllare il processo di campionamento.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `solver_type` | Il tipo di risolutore di equazioni differenziali da utilizzare per il processo di campionamento (predefinito: "midpoint") | COMBO | Sì | `"midpoint"`<br>`"heun"` |
| `eta` | Controlla la stocasticità del processo di campionamento (predefinito: 1.0) | FLOAT | Sì | 0.0 - 100.0 |
| `s_noise` | Controlla la quantità di rumore aggiunto durante il campionamento (predefinito: 1.0) | FLOAT | Sì | 0.0 - 100.0 |
| `noise_device` | Il dispositivo in cui vengono eseguiti i calcoli del rumore. Se impostato su "cpu", il campionatore utilizza la generazione del rumore basata su CPU; se impostato su "gpu", utilizza la generazione del rumore basata su GPU per prestazioni potenzialmente più rapide (predefinito: "gpu") | COMBO | Sì | `"gpu"`<br>`"cpu"` |

Nota: `eta`, `s_noise` e `noise_device` sono contrassegnati come parametri avanzati e compaiono nella sezione avanzata dell'interfaccia utente del nodo.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `sampler` | Un oggetto campionatore configurato pronto per l'uso nella pipeline di campionamento | SAMPLER |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerDPMPP_2M_SDE/it.md)

---
**Source fingerprint (SHA-256):** `42f5f098fa7573ca8a1a6085b72675ee6cb0ae8e7865c5793a815a6ef2495f82`
