# TorchCompileModel

Il nodo TorchCompileModel applica la compilazione PyTorch a un modello per ottimizzarne le prestazioni. Crea una copia del modello di input e la avvolge con la funzionalità di compilazione di PyTorch utilizzando il backend specificato. Ciò può migliorare la velocità di esecuzione del modello durante l'inferenza.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello da compilare e ottimizzare | MODEL | Sì | - |
| `backend` | Il backend di compilazione PyTorch da utilizzare per l'ottimizzazione (predefinito: "inductor") | STRING | Sì | "inductor"<br>"cudagraphs" |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `model` | Il modello compilato con la compilazione PyTorch applicata | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TorchCompileModel/it.md)

---
**Source fingerprint (SHA-256):** `240c6eb84ce2b93fe4d7c04fcf69df571e662f17893a4fd8e721241ea082edc8`
