# Crea Keyframe Hook Interpolati

Crea una sequenza di keyframe hook con valori di strength interpolati tra un punto iniziale e uno finale. Il nodo genera molteplici keyframe che effettuano una transizione fluida del parametro strength attraverso un intervallo percentuale specificato del processo di generazione, usando vari metodi di interpolazione per controllare la curva di transizione.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `strength_start` | Il valore di strength iniziale per la sequenza di interpolazione (predefinito: 1.0) | FLOAT | Sì | 0.0 - 10.0 |
| `strength_end` | Il valore di strength finale per la sequenza di interpolazione (predefinito: 1.0) | FLOAT | Sì | 0.0 - 10.0 |
| `interpolation` | Il metodo di interpolazione usato per la transizione tra i valori di strength (predefinito: LINEAR) | COMBO | Sì | `LINEAR`<br>`EASE_IN`<br>`EASE_OUT`<br>`EASE_IN_OUT`<br>`EASE_OUT_IN`<br>`SINE`<br>`CUBIC`<br>`QUARTIC`<br>`QUINTIC`<br>`EXPO`<br>`CIRC`<br>`BACK`<br>`BOUNCE`<br>`ELASTIC` |
| `start_percent` | La posizione percentuale iniziale nel processo di generazione (predefinito: 0.0) | FLOAT | Sì | 0.0 - 1.0 |
| `end_percent` | La posizione percentuale finale nel processo di generazione (predefinito: 1.0) | FLOAT | Sì | 0.0 - 1.0 |
| `keyframes_count` | Il numero di keyframe da generare nella sequenza di interpolazione (predefinito: 5) | INT | Sì | 2 - 100 |
| `print_keyframes` | Se stampare nel log le informazioni sui keyframe generati (predefinito: False) | BOOLEAN | Sì | True/False |
| `prev_hook_kf` | Gruppo di keyframe hook precedente opzionale a cui aggiungere | HOOK_KEYFRAMES | No | - |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `HOOK_KF` | Il gruppo di keyframe hook generato contenente la sequenza interpolata | HOOK_KEYFRAMES |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframesInterpolated/it.md)

---
**Source fingerprint (SHA-256):** `f90c96745ca1f02bbb02e08d2d82be1bbb1f3c80ac5d53a4c6bc07a0e2b8d76f`
