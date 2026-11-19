# Carica Modello Optical Flow

Carica un modello di flusso ottico dalla cartella `models/optical_flow/`. Attualmente è supportato solo il formato RAFT-large di torchvision, ovvero il modello utilizzato dal nodo VOIDWarpedNoise. ComfyUI non scarica automaticamente i pesi del flusso ottico; è necessario posizionare manualmente il file checkpoint nella directory `models/optical_flow/`.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model_name` | Modello di flusso ottico da caricare. I file devono essere inseriti nella cartella `optical_flow`. Attualmente è supportato solo `raft_large.pth` di torchvision. | COMBO | Sì | Elenco dei file nella cartella `models/optical_flow/` |

Nota: il checkpoint selezionato deve essere uno state dict RAFT-large di torchvision contenente chiavi con prefisso `feature_encoder.`, `context_encoder.` e `update_block.`. Se il file non corrisponde a questo formato, il nodo genera un ValueError.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `OPTICAL_FLOW` | Il modello di flusso ottico caricato, impostato in modalità valutazione, con precisione fp16 sui dispositivi che la supportano e senza `--force-fp32` (float32 altrimenti), racchiuso in un ModelPatcher per l'uso con altri nodi. | OPTICAL_FLOW |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpticalFlowLoader/it.md)

---
**Source fingerprint (SHA-256):** `82e5d747679ede113ec4d72fd6eda4b8f20d098832612bebf26ef65de8b4b3dc`
