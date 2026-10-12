# Ottieni Parametri IC-LoRA

Questo nodo legge i metadati da un modello caricato con LoRA per estrarre i parametri IC-LoRA, come il fattore di downscale di riferimento. Restituisce questi parametri come un oggetto strutturato che può essere collegato al nodo LTXVAddGuide quando un LoRA richiede una gestione speciale delle guide.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `iclora_model` | Output diretto di un LoRA Loader per lo specifico IC-LoRA da cui estrarre i metadati. | MODEL | Sì | N/A |

Nota: se i metadati del LoRA mancano o non contengono una voce `reference_downscale_factor`, il nodo restituisce un valore predefinito di 1. Quando presente, il fattore viene arrotondato e impostato a un minimo di 1.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `iclora_parameters` | Parametri IC-LoRA estratti dai metadati del LoRA (ad es., reference_downscale_factor). Collegare a LTXVAddGuide se il LoRA richiede una gestione speciale delle guide. | IC_LORA_PARAMETERS |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetICLoRAParameters/it.md)

---
**Source fingerprint (SHA-256):** `5f6becad0c7673b8cde1e099bd7ba5be7106da958b8967f8e693ba2a704baaef`
