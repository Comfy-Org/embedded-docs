# LTXVConditioning

Il nodo LTXVConditioning aggiunge informazioni sulla frequenza dei fotogrammi sia agli input di condizionamento positivo sia a quelli negativi per i modelli di generazione video. Prende i dati di condizionamento esistenti e applica il valore di frequenza dei fotogrammi specificato a entrambi i set di condizionamento, rendendoli adatti all'elaborazione da parte dei modelli video.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `positive` | L'input di condizionamento positivo a cui verranno applicate le informazioni sulla frequenza dei fotogrammi | CONDITIONING | Sì | - |
| `negative` | L'input di condizionamento negativo a cui verranno applicate le informazioni sulla frequenza dei fotogrammi | CONDITIONING | Sì | - |
| `frame_rate` | Il valore della frequenza dei fotogrammi da applicare a entrambi i set di condizionamento (predefinito: 25.0) | FLOAT | Sì | 0.0 - 1000.0 (passo: 0.01) |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `positive` | Il condizionamento positivo con le informazioni sulla frequenza dei fotogrammi applicate | CONDITIONING |
| `negative` | Il condizionamento negativo con le informazioni sulla frequenza dei fotogrammi applicate | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConditioning/it.md)

---
**Source fingerprint (SHA-256):** `c8546b691329f2934995f97a6db2e1393d2928bf1a7438fd079d52f87bee1c35`
