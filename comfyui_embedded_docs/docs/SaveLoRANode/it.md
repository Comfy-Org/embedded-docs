# SaveLoRANode

Il nodo SaveLoRA salva i modelli LoRA (Low-Rank Adaptation) nella directory di output. Prende in input un modello LoRA e crea un file safetensors con un nome file generato automaticamente. È possibile personalizzare il prefisso del nome file e, facoltativamente, includere nel nome file il numero di step di addestramento per una migliore organizzazione.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `lora` | Il modello LoRA da salvare. Non usare il modello con layer LoRA. | LORA_MODEL | Sì | - |
| `prefix` | Il prefisso da utilizzare per il file LoRA salvato (predefinito: "loras/ComfyUI_trained_lora"). | STRING | Sì | - |
| `steps` | Opzionale: il numero di step per cui il LoRA è stato addestrato, usato per denominare il file salvato. | INT | No | - |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| *None* | Questo nodo non restituisce alcun output ma salva il modello LoRA nella directory di output. | - |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRANode/it.md)

---
**Source fingerprint (SHA-256):** `06a1067433aa4b720b51050b09fbad4870caf12c5e92f788d44ea022a39efef4`
