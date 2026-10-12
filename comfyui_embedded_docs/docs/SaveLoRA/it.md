# SaveLoRA

Il nodo SaveLoRA salva un modello LoRA (Low-Rank Adaptation) in un file. Prende in input un modello LoRA e lo scrive in un file `.safetensors` nella directory di output. È possibile specificare un prefisso del nome file e un conteggio opzionale degli step da includere nel nome file finale.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `lora` | Il modello LoRA da salvare. Non usare un modello con layer LoRA. | LORA_MODEL | Sì | N/A |
| `prefix` | Il prefisso da usare per il file LoRA salvato (predefinito: "loras/ComfyUI_trained_lora"). | STRING | Sì | N/A |
| `steps` | Opzionale: il numero di step per cui il LoRA è stato addestrato, usato per denominare il file salvato. | INT | No | N/A |

**Nota:** L'input `lora` deve essere un modello LoRA puro. Non fornire un modello di base a cui sono stati applicati layer LoRA.

**Nota:** Il file viene salvato nella directory di output di ComfyUI con estensione `.safetensors`. Il nome file viene costruito a partire dal `prefix` e da un contatore con zeri iniziali (5 cifre) per evitare di sovrascrivere file esistenti. Quando viene fornito `steps`, anche il conteggio degli step viene incluso nel nome file (ad esempio, `1000_steps` per 1000 step).

**Nota:** Questo nodo è contrassegnato come sperimentale.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| *None* | Questo nodo non restituisce alcun dato al flusso di lavoro. È un nodo di output che salva un file su disco. | N/A |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRA/it.md)

---
**Source fingerprint (SHA-256):** `02f1d15dd7a5181666f2dbf06c45c07b12c4a178985464e07b5f613bd628f906`
