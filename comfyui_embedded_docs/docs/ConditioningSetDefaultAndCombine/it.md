# ConditioningSetDefaultAndCombine

Questo nodo combina un input di condizionamento primario con un input di condizionamento predefinito utilizzando un sistema basato su hook. Unisce le due fonti di condizionamento in un unico output, consentendo al condizionamento predefinito di fungere da fallback o base quando il condizionamento primario è incompleto.

## Input

| Parametro | Descrizione | Tipo di dato | Tipo di input | Predefinito | Intervallo |
| --- | --- | --- | --- | --- | --- |
| `cond` | L'input di condizionamento primario da elaborare e combinare | CONDITIONING | Obbligatorio | - | - |
| `cond_DEFAULT` | I dati di condizionamento predefiniti da combinare con il condizionamento primario | CONDITIONING | Obbligatorio | - | - |
| `hooks` | Configurazione opzionale degli hook che controlla come i dati di condizionamento vengono elaborati e combinati | HOOKS | Opzionale | - | - |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `CONDITIONING` | I dati di condizionamento combinati risultanti dall'unione degli input di condizionamento primario e predefinito | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetDefaultAndCombine/it.md)

---
**Source fingerprint (SHA-256):** `5e6c95f454c7e262878cc362c6b199e01abff10f803c81afe6e76a317c30d039`
