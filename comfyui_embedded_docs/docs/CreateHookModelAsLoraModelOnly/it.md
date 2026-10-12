# CreateHookModelAsLoraModelOnly

Questo nodo crea un hook che applica un modello LoRA (Low-Rank Adaptation) per modificare solo il componente del modello di una rete neurale. Carica un file checkpoint e lo applica con un'intensità specificata al modello, lasciando invariato il componente CLIP. Si tratta di un nodo sperimentale che estende la funzionalità della classe base CreateHookModelAsLora.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `ckpt_name` | Il file checkpoint da caricare come modello LoRA. Le opzioni disponibili dipendono dal contenuto della cartella checkpoints. | STRING | Sì | Più opzioni disponibili |
| `strength_model` | Il moltiplicatore di intensità per applicare il LoRA al componente del modello (predefinito: 1.0) | FLOAT | Sì | da -20.0 a 20.0 |
| `prev_hooks` | Hook precedenti opzionali da concatenare con questo hook | HOOKS | No | - |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `hooks` | Il gruppo di hook creato contenente la modifica del modello LoRA | HOOKS |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookModelAsLoraModelOnly/it.md)

---
**Source fingerprint (SHA-256):** `adbeaede65aa89d48c59225ca1c8edc4c9394a364f93a00dae4a83a2270f093b`
