# CombineHooksEight

Il nodo Combine Hooks [8] unisce fino a otto diversi gruppi di hook in un unico gruppo di hook combinato. Riceve più input di hook e li combina utilizzando la funzionalità di combinazione degli hook di ComfyUI. Ciò consente di consolidare più configurazioni di hook per un'elaborazione semplificata in flussi di lavoro avanzati.

## Input

| Parametro | Descrizione | Tipo di dati | Tipo di input | Predefinito | Intervallo |
| --- | --- | --- | --- | --- | --- |
| `hooks_A` | Primo gruppo di hook da combinare | HOOKS | opzionale | None | - |
| `hooks_B` | Secondo gruppo di hook da combinare | HOOKS | opzionale | None | - |
| `hooks_C` | Terzo gruppo di hook da combinare | HOOKS | opzionale | None | - |
| `hooks_D` | Quarto gruppo di hook da combinare | HOOKS | opzionale | None | - |
| `hooks_E` | Quinto gruppo di hook da combinare | HOOKS | opzionale | None | - |
| `hooks_F` | Sesto gruppo di hook da combinare | HOOKS | opzionale | None | - |
| `hooks_G` | Settimo gruppo di hook da combinare | HOOKS | opzionale | None | - |
| `hooks_H` | Ottavo gruppo di hook da combinare | HOOKS | opzionale | None | - |

**Nota:** Tutti i parametri di input sono opzionali. Il nodo combinerà solo i gruppi di hook forniti, ignorando quelli lasciati vuoti. È possibile fornire da uno a otto gruppi di hook per la combinazione.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `HOOKS` | Un singolo gruppo di hook combinato contenente tutte le configurazioni di hook fornite | HOOKS |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CombineHooksEight/it.md)

---
**Source fingerprint (SHA-256):** `8cd13ec6710a9b2905c14301cfd15be616c00f1b4140451cdf0915f091c77197`
