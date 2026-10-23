# CombineHooks

Il nodo Combine Hooks [2] unisce due gruppi di hook in un unico gruppo combinato. Riceve due input opzionali di hook e li combina utilizzando la funzionalità di combinazione degli hook di ComfyUI. Questo consente di consolidare più configurazioni di hook per un'elaborazione semplificata.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Range |
| --- | --- | --- | --- | --- |
| `hooks_A` | Primo gruppo di hook da combinare | HOOKS | No | - |
| `hooks_B` | Secondo gruppo di hook da combinare | HOOKS | No | - |

**Nota:** Entrambi gli input sono opzionali, ma è necessario fornire almeno un gruppo di hook affinché il nodo funzioni. Se viene fornito un solo gruppo di hook, questo verrà restituito invariato.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `hooks` | Gruppo di hook combinato contenente tutti gli hook di entrambi i gruppi di input | HOOKS |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooks2/it.md)

---
**Source fingerprint (SHA-256):** `558ceef1cebedd0b7e045b7d1eb1afa4316ea6a3c35f982968af132dca164126`
