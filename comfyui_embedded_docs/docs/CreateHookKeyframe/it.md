# Crea Keyframe Hook

Il nodo Create Hook Keyframe consente di definire punti specifici in un processo di generazione in cui il comportamento degli hook cambia. Crea keyframe che modificano la forza degli hook a determinate percentuali dell'avanzamento della generazione, e questi keyframe possono essere concatenati tra loro per creare schemi di pianificazione complessi.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `strength_mult` | Moltiplicatore per la forza dell'hook in questo keyframe (predefinito: 1.0) | FLOAT | Sì | Da -20.0 a 20.0 |
| `start_percent` | Il punto percentuale nel processo di generazione in cui questo keyframe ha effetto (predefinito: 0.0) | FLOAT | Sì | Da 0.0 a 1.0 |
| `prev_hook_kf` | Gruppo precedente opzionale di hook keyframe a cui aggiungere questo keyframe | HOOK_KEYFRAMES | No | - |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `HOOK_KF` | Un gruppo di hook keyframe che include il keyframe appena creato | HOOK_KEYFRAMES |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframe/it.md)

---
**Source fingerprint (SHA-256):** `51893311a0623cafcf8c2d8af00e4005ca2fea2df9474e87d7d4b332b38435c3`
