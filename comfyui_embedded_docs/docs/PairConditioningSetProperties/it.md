# PairConditioningSetProperties

Il nodo **PairConditioningSetProperties** consente di modificare contemporaneamente le proprietà delle coppie di condizionamento positivo e negativo. Applica regolazioni dell'intensità, impostazioni dell'area di condizionamento e controlli opzionali di mascheramento o temporizzazione a entrambi gli input di condizionamento, restituendo i dati di condizionamento positivo e negativo modificati.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `positive_NEW` | L'input di condizionamento positivo da modificare | CONDITIONING | Sì | - |
| `negative_NEW` | L'input di condizionamento negativo da modificare | CONDITIONING | Sì | - |
| `strength` | Il moltiplicatore di intensità applicato al condizionamento (predefinito: 1.0) | FLOAT | Sì | da 0.0 a 10.0 |
| `set_cond_area` | Determina come viene calcolata l'area di condizionamento (predefinito: "default") | STRING | Sì | "default"<br>"mask bounds" |
| `mask` | Maschera opzionale per limitare l'area di condizionamento | MASK | No | - |
| `hooks` | Gruppo di hook opzionale per modifiche avanzate al condizionamento | HOOKS | No | - |
| `timesteps` | Intervallo di timestep opzionale per limitare quando viene applicato il condizionamento | TIMESTEPS_RANGE | No | - |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `positive` | Il condizionamento positivo modificato con le proprietà applicate | CONDITIONING |
| `negative` | Il condizionamento negativo modificato con le proprietà applicate | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetProperties/it.md)

---
**Source fingerprint (SHA-256):** `3f750c270665b4f3567790ab1ae0bdbfa176527d4f8d96cf10570a5c5deb9636`
