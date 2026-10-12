# LatentApplyOperation

Il nodo LatentApplyOperation applica un'operazione latente specificata ai campioni latenti. Prende in input dati latenti e un'operazione, elabora i campioni latenti utilizzando l'operazione fornita e restituisce i dati latenti modificati. Questo nodo consente di trasformare o manipolare le rappresentazioni latenti nel flusso di lavoro. Questo nodo è attualmente contrassegnato come sperimentale.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `samples` | I campioni latenti da elaborare tramite l'operazione | LATENT | Sì | - |
| `operation` | L'operazione da applicare ai campioni latenti | LATENT_OPERATION | Sì | - |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `output` | I campioni latenti modificati dopo l'applicazione dell'operazione | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperation/it.md)

---
**Source fingerprint (SHA-256):** `cba55d019793fde8dcc0d4aeb4eb6020b6149f523c6bffc65d73c533aa2e2c6c`
