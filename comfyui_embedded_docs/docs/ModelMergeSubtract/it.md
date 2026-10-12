# ModelMergeSubtract

Questo nodo è progettato per operazioni avanzate di fusione di modelli, in particolare per sottrarre i parametri di un modello da quelli di un altro in base a un moltiplicatore specificato. Consente di personalizzare il comportamento dei modelli regolando l'influenza dei parametri di un modello su un altro, facilitando la creazione di nuovi modelli ibridi.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model1` | Il modello di base da cui verranno sottratti i parametri. | `MODEL` |
| `model2` | Il modello i cui parametri verranno sottratti dal modello di base. | `MODEL` |
| `multiplier` | Un valore in virgola mobile che scala l'effetto di sottrazione sui parametri del modello di base. | `FLOAT` |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il modello risultante dopo aver sottratto i parametri di un modello da quelli di un altro, scalato dal moltiplicatore. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSubtract/it.md)
