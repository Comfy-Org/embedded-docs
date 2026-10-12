# Imposta Hook CLIP

Il nodo SetClipHooks consente di applicare hook personalizzati a un modello CLIP, abilitando modifiche avanzate al suo comportamento. Può applicare hook agli output di conditioning e, facoltativamente, abilitare la funzionalità di pianificazione clip. Questo nodo crea una copia clonata del modello CLIP di input con le configurazioni di hook specificate applicate.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `clip` | Il modello CLIP a cui applicare gli hook | CLIP | Sì | - |
| `apply_to_conds` | Se applicare gli hook agli output di conditioning (predefinito: True) | BOOLEAN | Sì | - |
| `schedule_clip` | Se abilitare la pianificazione clip (predefinito: False) | BOOLEAN | Sì | - |
| `hooks` | Gruppo di hook opzionale da applicare al modello CLIP | HOOKS | No | - |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `clip` | Un modello CLIP clonato con gli hook specificati applicati | CLIP |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetClipHooks/it.md)

---
**Source fingerprint (SHA-256):** `904a878638c015bdce1983ae0c11a2b580b271090fca39edb304f6ed90c8c66d`
