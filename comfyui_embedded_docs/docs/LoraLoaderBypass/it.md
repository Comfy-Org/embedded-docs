# LoraLoaderBypass

Il nodo LoraLoaderBypass applica un LoRA (Low-Rank Adaptation) a un modello di diffusione e a un modello CLIP in una speciale modalità "bypass". A differenza di un caricatore LoRA standard, questo metodo non modifica in modo permanente i pesi del modello base. Calcola invece il risultato aggiungendo il contributo del LoRA al normale passaggio forward del modello, il che è utile per l'addestramento o quando si lavora con modelli i cui pesi sono in offload.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello di diffusione a cui verrà applicato il LoRA. | MODEL | Sì | - |
| `clip` | Il modello CLIP a cui verrà applicato il LoRA. | CLIP | Sì | - |
| `lora_name` | Il nome del LoRA. I file LoRA disponibili vengono caricati dalla cartella `loras`. | COMBO | Sì | Elenco dei file LoRA disponibili |
| `strength_model` | Quanto fortemente modificare il modello di diffusione. Questo valore può essere negativo (predefinito: 1.0). | FLOAT | Sì | da -100.0 a 100.0 (passo: 0.01) |
| `strength_clip` | Quanto fortemente modificare il modello CLIP. Questo valore può essere negativo (predefinito: 1.0). | FLOAT | Sì | da -100.0 a 100.0 (passo: 0.01) |

**Nota:** Se sia `strength_model` sia `strength_clip` sono impostati su 0, il nodo restituisce gli input `model` e `clip` originali e non modificati, senza elaborazione.

**Nota:** Il file LoRA selezionato viene memorizzato nella cache dopo il primo caricamento. Viene riletto dal disco solo quando viene scelto un `lora_name` diverso.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `MODEL` | Il modello di diffusione modificato. | MODEL |
| `CLIP` | Il modello CLIP modificato. | CLIP |

**Nota:** Questo nodo è contrassegnato come sperimentale.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypass/it.md)

---
**Source fingerprint (SHA-256):** `025f0638a6690a53b1a6c4548dac24fb7e7f26e04ff4b1c88d29b061430037a8`
