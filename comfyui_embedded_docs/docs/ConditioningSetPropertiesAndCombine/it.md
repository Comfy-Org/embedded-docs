# ConditioningSetPropertiesAndCombine

Il nodo ConditioningSetPropertiesAndCombine modifica i dati di condizionamento applicando le proprietà di un nuovo input di condizionamento a un input di condizionamento esistente. Combina i due insiemi di condizionamento controllando l'intensità del nuovo condizionamento e specificando come deve essere applicata l'area di condizionamento.

## Input

| Parametro | Descrizione | Tipo di dato | Tipo di input | Predefinito | Intervallo |
| --- | --- | --- | --- | --- | --- |
| `cond` | I dati di condizionamento originali da modificare | CONDITIONING | Obbligatorio | - | - |
| `cond_NEW` | I nuovi dati di condizionamento che forniscono le proprietà da applicare | CONDITIONING | Obbligatorio | - | - |
| `strength` | Controlla l'intensità delle proprietà del nuovo condizionamento | FLOAT | Obbligatorio | 1.0 | 0.0 - 10.0 |
| `set_cond_area` | Determina come viene applicata l'area di condizionamento | STRING | Obbligatorio | default | ["default", "mask bounds"] |
| `mask` | Maschera opzionale per definire aree specifiche per il condizionamento | MASK | Opzionale | - | - |
| `hooks` | Funzioni hook opzionali per l'elaborazione personalizzata | HOOKS | Opzionale | - | - |
| `timesteps` | Intervallo di timestep opzionale per controllare quando viene applicato il condizionamento | TIMESTEPS_RANGE | Opzionale | - | - |

**Nota:** Quando viene fornita `mask`, il parametro `set_cond_area` può usare "mask bounds" per limitare l'applicazione del condizionamento alle regioni mascherate.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `CONDITIONING` | I dati di condizionamento combinati con le proprietà modificate | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetPropertiesAndCombine/it.md)

---
**Source fingerprint (SHA-256):** `da57eeae428a103cbad77af063419ed0e85aeaa0b8805c8c197df27613477fa8`
