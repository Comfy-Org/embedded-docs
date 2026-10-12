# SamplerSEEDS2

Questo nodo fornisce un campionatore configurabile per la generazione di immagini. Si basa su un risolutore di equazioni differenziali stocastiche (SDE) e può comportarsi come diversi campionatori specifici in base alle sue impostazioni, tra cui `seeds_2`, `exp_heun_2_x0` e `exp_heun_2_x0_sde`.

## Input

| Parametro | Descrizione | Tipo di dati | Richiesto | Intervallo |
| --- | --- | --- | --- | --- |
| `solver_type` | Seleziona l'algoritmo risolutore sottostante per il campionatore. | COMBO | Sì | "phi_1"<br>"phi_2" |
| `eta` | Forza stocastica (predefinito: 1.0). | FLOAT | No | 0.0 - 100.0 |
| `s_noise` | Moltiplicatore di rumore SDE (predefinito: 1.0). | FLOAT | No | 0.0 - 100.0 |
| `r` | Dimensione relativa del passo per lo stadio intermedio (nodo c2) (predefinito: 0.5). | FLOAT | No | 0.01 - 1.0 |

**Nota:** La descrizione del nodo definisce le seguenti preimpostazioni del campionatore:
- `seeds_2`: impostazioni predefinite
- `exp_heun_2_x0`: `solver_type` = "phi_2", `r` = 1.0, `eta` = 0.0
- `exp_heun_2_x0_sde`: `solver_type` = "phi_2", `r` = 1.0, `eta` = 1.0, `s_noise` = 1.0

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `sampler` | Un oggetto campionatore configurato che può essere passato ad altri nodi di campionamento. | SAMPLER |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SamplerSEEDS2/it.md)

---
**Source fingerprint (SHA-256):** `f48744a706a49ef93d41845bf8c308af971853f6150afd00ded45f0317ffc4f9`
