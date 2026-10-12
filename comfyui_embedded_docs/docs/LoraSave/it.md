# Estrai e salva LoRA

Il nodo LoraSave estrae e salva file LoRA (Low-Rank Adaptation) dalle differenze tra modelli. Può elaborare differenze di modelli di diffusione, differenze di text encoder, o entrambe, convertendole in formato LoRA con rango e tipo specificati. Il file LoRA risultante viene salvato nella directory di output per utilizzarlo in seguito.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `filename_prefix` | Il prefisso per il nome del file di output (predefinito: "loras/ComfyUI_extracted_lora") | STRING | Sì | - |
| `rank` | Il valore di rango per il LoRA, che controlla dimensione e complessità (predefinito: 8) | INT | Sì | 1-4096 |
| `lora_type` | Il tipo di LoRA da creare. "standard" estrae matrici a basso rango tramite SVD; "full_diff" salva l'intera differenza dei pesi (predefinito: "standard") | COMBO | Sì | `"standard"`<br>`"full_diff"` |
| `bias_diff` | Indica se includere le differenze di bias nel calcolo del LoRA (predefinito: True) | BOOLEAN | Sì | - |
| `model_diff` | L'output di ModelSubtract da convertire in un LoRA | MODEL | No | - |
| `text_encoder_diff` | L'output di CLIPSubtract da convertire in un LoRA | CLIP | No | - |

**Nota:** Almeno uno tra `model_diff` o `text_encoder_diff` deve essere fornito affinché il nodo funzioni. Se entrambi vengono omessi, il nodo non produrrà alcun output.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| - | Questo nodo salva un file LoRA nella directory di output ma non restituisce alcun dato attraverso il workflow | - |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraSave/it.md)

---
**Source fingerprint (SHA-256):** `642510bfe083130cb2724d7ae38d30d4694c85a43c7ce27230690ddd9fe76b79`
