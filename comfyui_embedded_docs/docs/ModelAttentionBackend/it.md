# Backend di attenzione del modello

Questo nodo seleziona l'implementazione di attenzione densa per un modello, clona il modello, applica il backend scelto e restituisce il clone con patch. Se usato con Block Sparse Attention, questo backend viene utilizzato ogni volta che l'attenzione sparsa è inattiva o non supportata. Se il backend selezionato non è disponibile, il nodo esegue automaticamente il fallback all'attenzione PyTorch.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Il modello a cui applicare la patch. | MODEL | Sì |  |
| `attention` | Il backend di attenzione densa da applicare. Comfy Kitchen attention usa attenzione quantizzata INT8 ed è disponibile solo su GPU Nvidia e AMD. Predefinito: "pytorch attention". Se il backend selezionato non è disponibile, viene usata l'attenzione PyTorch come fallback. | COMBO | Sì | "pytorch attention"<br>"comfy kitchen attention" |

Nota: l'opzione "comfy kitchen attention" viene elencata solo quando il modulo di attenzione INT8 di Comfy Kitchen è disponibile nell'ambiente corrente.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `model` | Un clone del modello di input con il backend di attenzione selezionato applicato. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelAttentionBackend/it.md)

---
**Source fingerprint (SHA-256):** `4f6e4800c2a3bb09b47b7c8f0481e1b6de3070f57234e610df5d3ce60dfdb309`
