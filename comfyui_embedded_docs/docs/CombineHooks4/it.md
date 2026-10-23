# CombineHooksFour

Il nodo Combine Hooks [4] unisce fino a quattro gruppi di hook separati in un unico gruppo di hook combinato. Accetta qualsiasi combinazione dei quattro input di hook disponibili e li combina utilizzando il sistema di combinazione degli hook di ComfyUI. Ciò consente di consolidare più configurazioni di hook per un'elaborazione ottimizzata in flussi di lavoro avanzati.

## Input

| Parametro | Descrizione | Tipo di dato | Tipo di input | Predefinito | Intervallo |
| --- | --- | --- | --- | --- | --- |
| `hooks_A` | Primo gruppo di hook da combinare | HOOKS | opzionale | Nessuno | - |
| `hooks_B` | Secondo gruppo di hook da combinare | HOOKS | opzionale | Nessuno | - |
| `hooks_C` | Terzo gruppo di hook da combinare | HOOKS | opzionale | Nessuno | - |
| `hooks_D` | Quarto gruppo di hook da combinare | HOOKS | opzionale | Nessuno | - |

**Nota:** Tutti e quattro gli input di hook sono opzionali. Il nodo combinerà solo i gruppi di hook forniti e restituirà un gruppo di hook vuoto se non è connesso alcun input.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `HOOKS` | Gruppo di hook combinato contenente tutte le configurazioni di hook fornite | HOOKS |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooks4/it.md)

---
**Source fingerprint (SHA-256):** `92a8038e7b5a7491afcbd48830a1e278fe4d697321fb874821ebf7edd09d5815`
