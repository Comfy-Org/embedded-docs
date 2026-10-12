# SetHookKeyframes

Il nodo Set Hook Keyframes consente di applicare la schedulazione dei keyframe ai gruppi di hook esistenti. Riceve un gruppo di hook e, facoltativamente, applica informazioni di temporizzazione dei keyframe per controllare quando i diversi hook vengono eseguiti durante il processo di generazione. Quando vengono forniti dei keyframe, il nodo clona il gruppo di hook e imposta la temporizzazione dei keyframe su tutti gli hook all'interno del gruppo.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `hooks` | Il gruppo di hook a cui applicare la schedulazione dei keyframe | HOOKS | Sì | - |
| `hook_kf` | Gruppo di keyframe opzionale contenente informazioni di temporizzazione per l'esecuzione degli hook | HOOK_KEYFRAMES | No | - |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `hooks` | Il gruppo di hook modificato con la schedulazione dei keyframe applicata (clonato se sono stati forniti dei keyframe) | HOOKS |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetHookKeyframes/it.md)

---
**Source fingerprint (SHA-256):** `48908e5247b18e5b7b1d894c2f1adcf6403e499125b0c3eb05978584b3d5759b`
