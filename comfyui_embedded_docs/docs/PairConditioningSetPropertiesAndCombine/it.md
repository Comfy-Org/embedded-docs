# Cond Pair Set Props Combine

Il nodo PairConditioningSetPropertiesAndCombine modifica e combina coppie di condizionamento applicando nuovi dati di condizionamento agli input di condizionamento positivo e negativo esistenti. Consente di regolare la forza del condizionamento applicato e di controllare come viene impostata l'area di condizionamento. Questo nodo è particolarmente utile nei flussi di lavoro avanzati di manipolazione del condizionamento, dove è necessario fondere insieme più sorgenti di condizionamento.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `positivo` | L'input di condizionamento positivo originale | CONDITIONING | Sì | - |
| `negativo` | L'input di condizionamento negativo originale | CONDITIONING | Sì | - |
| `positivo_NUOVO` | Il nuovo condizionamento positivo da applicare | CONDITIONING | Sì | - |
| `negativo_NUOVO` | Il nuovo condizionamento negativo da applicare | CONDITIONING | Sì | - |
| `intensità` | Il fattore di forza per applicare il nuovo condizionamento (predefinito: 1.0) | FLOAT | Sì | 0.0 a 10.0 |
| `imposta_area_cond` | Controlla come viene applicata l'area di condizionamento (predefinito: "default") | STRING | Sì | "default"<br>"mask bounds" |
| `mask` | Maschera opzionale per limitare l'area di applicazione del condizionamento | MASK | No | - |
| `hooks` | Gruppo di hook opzionale per il controllo avanzato | HOOKS | No | - |
| `passi_temporali` | Specifica opzionale dell'intervallo di timestep | TIMESTEPS_RANGE | No | - |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `positive` | L'output di condizionamento positivo combinato | CONDITIONING |
| `negative` | L'output di condizionamento negativo combinato | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetPropertiesAndCombine/it.md)

---
**Source fingerprint (SHA-256):** `d434fdc1ccbe3ddee6293a6300cc55d30cb5bf357025b26777791746f51e755e`
