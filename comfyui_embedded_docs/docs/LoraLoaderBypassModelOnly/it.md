# Carica LoRA (Bypass, solo modello) (per debug)

Questo nodo applica una LoRA (Low-Rank Adaptation) a un modello per modificarne il comportamento, ma influisce solo sulla componente del modello stessa. Carica un file LoRA specificato e regola i pesi del modello in base a una determinata intensità, lasciando invariati altri componenti come il codificatore di testo CLIP.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Range |
| --- | --- | --- | --- | --- |
| `model` | Il modello di base a cui verranno applicate le modifiche LoRA. | MODEL | Sì | - |
| `lora_name` | Il nome del file LoRA da caricare e applicare. Le opzioni sono popolate dai file presenti nella directory `loras`. | STRING | Sì | (Elenco dei file LoRA disponibili) |
| `strength_model` | L'intensità dell'effetto della LoRA sui pesi del modello. Un valore positivo applica la LoRA, un valore negativo ne applica l'inverso, mentre un valore pari a 0 non ha alcun effetto (predefinito: 1.0). | FLOAT | Sì | -100.0 to 100.0 |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il modello modificato con le regolazioni LoRA applicate ai suoi pesi. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderBypassModelOnly/it.md)

---
**Source fingerprint (SHA-256):** `e0e1ad2d6481a1b9771d7eae833ffab0737a967d4af6e57b946d1b2223fe45bf`
