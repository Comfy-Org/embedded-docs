# Crea Hook LoRA

Il nodo Create Hook LoRA genera oggetti hook per applicare modifiche LoRA (Low-Rank Adaptation) ai modelli. Carica un file LoRA specificato e crea hook che possono regolare le intensità del modello e di CLIP, quindi combina questi hook con eventuali hook esistenti passati al nodo. Il nodo gestisce efficientemente il caricamento dei LoRA memorizzando nella cache i file LoRA già caricati per evitare operazioni ridondanti.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `lora_name` | Il nome del file LoRA da caricare dalla directory loras | STRING | Sì | Più opzioni disponibili |
| `strength_model` | Il moltiplicatore di intensità per le regolazioni del modello (predefinito: 1.0) | FLOAT | Sì | da -20.0 a 20.0 |
| `strength_clip` | Il moltiplicatore di intensità per le regolazioni di CLIP (predefinito: 1.0) | FLOAT | Sì | da -20.0 a 20.0 |
| `prev_hooks` | Gruppo di hook esistente opzionale da combinare con i nuovi hook LoRA | HOOKS | No | N/A |

**Vincoli dei parametri:**

- Se sia `strength_model` sia `strength_clip` sono impostati a 0, il nodo salta la creazione di nuovi hook LoRA e restituisce invariati gli hook esistenti
- Il nodo memorizza nella cache l'ultimo file LoRA caricato per ottimizzare le prestazioni quando lo stesso LoRA viene usato ripetutamente

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `HOOKS` | Un gruppo di hook contenente gli hook LoRA combinati e eventuali hook precedenti | HOOKS |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookLora/it.md)

---
**Source fingerprint (SHA-256):** `42d5d776bfc9b239191952e2bce23513d183f904fc3c15039469381a547486f8`
