# CreateHookLoraModelOnly

Questo nodo crea un hook LoRA (Low-Rank Adaptation) che si applica solo alla componente modello, lasciando la componente CLIP completamente invariata. Carica un file LoRA e lo applica con una forza specificata al modello, impostando la forza CLIP a zero. Il nodo può essere concatenato con hook precedenti per costruire pipeline di modifica complesse.

## Input
| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `lora_name` | Il nome del file LoRA da caricare dalla cartella loras | STRING | Sì | Opzioni multiple disponibili |
| `strength_model` | Il moltiplicatore di forza per applicare il LoRA alla componente modello (predefinito: 1.0) | FLOAT | Sì | -20.0 a 20.0 |
| `prev_hooks` | Hook precedenti opzionali da concatenare con questo hook | HOOKS | No | - |

## Output
| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `hooks` | L'hook LoRA creato che può essere applicato all'elaborazione del modello | HOOKS |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookLoraModelOnly/it.md)

---
**Source fingerprint (SHA-256):** `10adbdfc2e37fcf317e93130f87d9a7038d00b091cb6d1b45f4658c81632ef80`
