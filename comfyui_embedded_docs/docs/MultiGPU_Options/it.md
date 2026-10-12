# MultiGPU_Options

## Panoramica

Questo nodo consente di specificare le prestazioni relative di ciascuna GPU quando si utilizzano più schede grafiche con velocità diverse. Crea un gruppo di opzioni GPU che può essere usato per distribuire il lavoro tra i dispositivi, sebbene la distribuzione del carico basata sulla velocità non sia ancora implementata nella versione corrente.

## Input
| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `device_index` | Il numero di indice del dispositivo GPU da configurare (predefinito: 0) | INT | Sì | 0 to 64 |
| `relative_speed` | La velocità relativa di questa GPU rispetto alle altre, usata per la distribuzione del carico di lavoro (predefinito: 1.0, passo: 0.01) | FLOAT | Sì | 0.0 to unlimited |
| `gpu_options` | Un gruppo esistente di opzioni GPU a cui aggiungere le opzioni di questo dispositivo. Se non fornito, viene creato un nuovo gruppo | GPU_OPTIONS | No | - |

## Output
| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `GPU_OPTIONS` | Un gruppo di opzioni GPU contenente le impostazioni del dispositivo configurate, che può essere passato ad altri nodi per operazioni multi-GPU | GPU_OPTIONS |

**Nota:** Il parametro `relative_speed` è definito ma non è ancora usato dal pianificatore interno per distribuire il lavoro tra le GPU. Nell'implementazione attuale, il lavoro viene distribuito uniformemente tra tutti i dispositivi indipendentemente dalle loro velocità relative.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MultiGPU_Options/it.md)

---
**Source fingerprint (SHA-256):** `8010460560a69c57d4ee0d8c3728a7a5d999e56ef5316b557fba0c660c9f38b0`
