# CreateHookModelAsLora

Questo nodo crea un modello hook come LoRA (Low-Rank Adaptation) caricando i pesi del checkpoint e applicando regolazioni di intensità sia al modello sia ai componenti CLIP. Consente di applicare modifiche in stile LoRA ai modelli esistenti tramite un approccio basato su hook, abilitando fine-tuning e adattamento senza modifiche permanenti al modello. Il nodo può combinarsi con hook precedenti e memorizza nella cache i pesi caricati per efficienza.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `ckpt_name` | Il file checkpoint da cui caricare i pesi (seleziona tra i checkpoint disponibili) | STRING | Sì | Opzioni multiple disponibili |
| `strength_model` | Il moltiplicatore di intensità applicato ai pesi del modello (predefinito: 1.0) | FLOAT | Sì | da -20.0 a 20.0 |
| `strength_clip` | Il moltiplicatore di intensità applicato ai pesi CLIP (predefinito: 1.0) | FLOAT | Sì | da -20.0 a 20.0 |
| `prev_hooks` | Hook precedenti opzionali da combinare con i nuovi hook LoRA creati | HOOKS | No | - |

**Vincoli sui parametri:**

- Il parametro `ckpt_name` carica i checkpoint dalla cartella dei checkpoint disponibili
- Entrambi i parametri di intensità accettano valori da -20.0 a 20.0 con incrementi di 0.01
- Quando `prev_hooks` non viene fornito, il nodo crea un nuovo gruppo di hook
- Il nodo memorizza nella cache i pesi caricati per evitare di ricaricare più volte lo stesso checkpoint

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `HOOKS` | Gli hook LoRA creati, combinati con eventuali hook precedenti se forniti | HOOKS |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookModelAsLora/it.md)

---
**Source fingerprint (SHA-256):** `8c0dd6b2e8e99e1d7dbc864aa802c0713842fb0d4ee018ea5cbedfb7896a770d`
