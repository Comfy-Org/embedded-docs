# LoraLoaderModelOnly

Questo nodo rileva i modelli presenti nella cartella `ComfyUI/models/loras` e legge anche i modelli dai percorsi aggiuntivi configurati nel file extra_model_paths.yaml. A volte potrebbe essere necessario **aggiornare l'interfaccia di ComfyUI** affinché legga i file dei modelli dalla cartella corrispondente.

Questo nodo è specializzato nel caricamento di un modello LoRA senza richiedere un modello CLIP, concentrandosi sul miglioramento o sulla modifica di un dato modello in base ai parametri LoRA. Consente la regolazione dinamica della forza del modello tramite i parametri LoRA, agevolando un controllo accurato del comportamento del modello.

## Input

| Campo | Descrizione | Tipo di dato Comfy |
| --- | --- | --- |
| `model` | Il modello di base da modificare, a cui verranno applicate le regolazioni LoRA. | `MODEL` |
| `lora_name` | Il nome del file LoRA da caricare, che specifica le regolazioni da applicare al modello. | `COMBO[STRING]` |
| `strength_model` | Determina l'intensità delle regolazioni LoRA; valori più alti indicano modifiche più forti. | `FLOAT` |

## Output

| Campo | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il modello modificato con le regolazioni LoRA applicate, che riflette cambiamenti nel comportamento o nelle capacità del modello. | `MODEL` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderModelOnly/it.md)
