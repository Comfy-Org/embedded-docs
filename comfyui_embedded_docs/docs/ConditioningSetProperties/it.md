# ConditioningSetProperties

Il nodo ConditioningSetProperties modifica le proprietà dei dati di condizionamento regolando `strength`, le impostazioni dell'area e applicando `mask`, hook o intervalli di timestep opzionali. Consente di controllare in che modo il condizionamento influenza il processo di generazione impostando parametri specifici che agiscono sull'applicazione dei dati di condizionamento durante la generazione delle immagini.

## Input

| Parametro | Descrizione | Tipo di dato | Tipo di input | Predefinito | Intervallo |
| --- | --- | --- | --- | --- | --- |
| `cond_NEW` | Dati di condizionamento da modificare | CONDITIONING | Obbligatorio | - | - |
| `strength` | Controlla l'intensità dell'effetto di condizionamento | FLOAT | Obbligatorio | 1.0 | 0.0 - 10.0 (passo: 0.01) |
| `set_cond_area` | Determina come viene applicata l'area di condizionamento. Scegli "default" per il comportamento standard o "mask bounds" per limitarla alla regione della maschera | STRING | Obbligatorio | default | ["default", "mask bounds"] |
| `mask` | Maschera opzionale per limitare dove viene applicato il condizionamento | MASK | Opzionale | - | - |
| `hooks` | Funzioni hook opzionali per l'elaborazione personalizzata | HOOKS | Opzionale | - | - |
| `timesteps` | Intervallo di timestep opzionale per limitare quando il condizionamento è attivo | TIMESTEPS_RANGE | Opzionale | - | - |

**Nota:** Quando viene fornita una `mask`, il parametro `set_cond_area` può essere impostato su "mask bounds" per limitare l'applicazione del condizionamento solo alla regione mascherata. Il parametro `hooks` consente l'elaborazione personalizzata tramite funzioni hook, mentre `timesteps` limita l'effetto di condizionamento a un intervallo specifico di timestep durante la generazione.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `CONDITIONING` | Dati di condizionamento modificati con proprietà aggiornate | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningSetProperties/it.md)

---
**Source fingerprint (SHA-256):** `5e3f5348f6df8f2fa1c1d42b883efcab3ee07d933e219f11fa48730aacc168d7`
