# Crea Keyframe Hook da Float

Questo nodo crea keyframe hook da un elenco di valori di forza in virgola mobile, distribuendoli uniformemente tra le percentuali di inizio e fine specificate. Genera una sequenza di keyframe in cui a ogni valore di forza è assegnata una posizione percentuale specifica nella timeline dell'animazione. Il nodo può creare un nuovo gruppo di keyframe oppure aggiungerli a uno esistente, con un'opzione per stampare i keyframe generati a scopo di debug.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `floats_strength` | Un singolo valore float o un elenco di valori float che rappresentano i valori di forza per i keyframe (predefinito: -1) | FLOATS | Sì | -1 a ∞ |
| `start_percent` | La posizione percentuale iniziale per il primo keyframe nella timeline (predefinito: 0.0) | FLOAT | Sì | 0.0 a 1.0 |
| `end_percent` | La posizione percentuale finale per l'ultimo keyframe nella timeline (predefinito: 1.0) | FLOAT | Sì | 0.0 a 1.0 |
| `print_keyframes` | Se abilitato, stampa nella console le informazioni sui keyframe generati (predefinito: False) | BOOLEAN | Sì | True/False |
| `prev_hook_kf` | Un gruppo di keyframe hook esistente a cui aggiungere i nuovi keyframe, oppure ne crea uno nuovo se non fornito | HOOK_KEYFRAMES | No | - |

**Nota:** Il parametro `floats_strength` accetta sia un singolo valore float sia un elenco iterabile di float. I keyframe vengono distribuiti linearmente tra `start_percent` e `end_percent` in base al numero di valori di forza forniti. Per il primo keyframe è garantito almeno uno step per assicurarne l'applicazione.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `HOOK_KF` | Un gruppo di keyframe hook contenente i keyframe appena creati, sia come nuovo gruppo, sia come aggiunta al gruppo di keyframe di input | HOOK_KEYFRAMES |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframesFromFloats/it.md)

---
**Source fingerprint (SHA-256):** `566864ec72062d913d95b38b3c53c655d4fdd971a01c4bec54669850b2feddc8`
