# PairConditioningSetDefaultAndCombine

Il nodo **PairConditioningSetDefaultAndCombine** imposta i valori di condizionamento predefiniti e li combina con i dati di condizionamento di input. Riceve input di condizionamento positivi e negativi insieme alle rispettive controparti predefinite, quindi li elabora tramite il sistema di hook di ComfyUI per produrre output di condizionamento finali che incorporano i valori predefiniti.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `positive` | L'input di condizionamento positivo primario da elaborare | CONDITIONING | Sì | - |
| `negative` | L'input di condizionamento negativo primario da elaborare | CONDITIONING | Sì | - |
| `positive_DEFAULT` | I valori di condizionamento positivi predefiniti da usare come fallback | CONDITIONING | Sì | - |
| `negative_DEFAULT` | I valori di condizionamento negativi predefiniti da usare come fallback | CONDITIONING | Sì | - |
| `hooks` | Gruppo di hook opzionale per logica di elaborazione personalizzata | HOOKS | No | - |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `positive` | Il condizionamento positivo elaborato con i valori predefiniti incorporati | CONDITIONING |
| `negative` | Il condizionamento negativo elaborato con i valori predefiniti incorporati | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PairConditioningSetDefaultCombine/it.md)

---
**Source fingerprint (SHA-256):** `dfa47d0fe02e81db8b68d20ae9b765c2518773f4f7fc8caf774cb870267dbb21`
