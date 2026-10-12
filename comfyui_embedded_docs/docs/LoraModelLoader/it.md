# Carica modello LoRA

Il nodo LoraModelLoader applica pesi LoRA (Low-Rank Adaptation) addestrati a un modello di diffusione. Modifica il modello base caricando i pesi LoRA da un modello LoRA addestrato e regolandone la forza di influenza. Ciò consente di personalizzare il comportamento dei modelli di diffusione senza riaddestrarli da zero, includendo una modalità bypass che lascia invariati i pesi del modello base.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello di diffusione a cui verrà applicato il LoRA. | MODEL | Sì | - |
| `lora` | Il modello LoRA da applicare al modello di diffusione. | LORA_MODEL | Sì | - |
| `strength_model` | Quanto intensamente modificare il modello di diffusione. Questo valore può essere negativo (predefinito: 1.0). | FLOAT | Sì | -100.0 to 100.0 |
| `bypass` | Se abilitato, applica LoRA in modalità bypass senza modificare i pesi del modello base. Utile per l'addestramento e quando i pesi del modello sono offloaded (predefinito: False). | BOOLEAN | Sì | True or False |

**Nota:** Quando `strength_model` è impostato su 0, il nodo restituisce il modello originale senza applicare alcuna modifica LoRA.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il modello di diffusione modificato con i pesi LoRA applicati. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraModelLoader/it.md)

---
**Source fingerprint (SHA-256):** `81eb2a9b0376fe7453f6e7e422414472e80a3d1b92bb6874b91df6de8aed0d9a`
