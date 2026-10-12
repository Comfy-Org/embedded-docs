# LumaRay32KeyframeNode

Questo nodo ancora un'immagine guida a una posizione specifica sulla timeline del video di output di Luma Ray 3.2. Collega questo nodo all'input "keyframes" del nodo Luma Ray 3.2 Keyframes to Video e concatena diversi keyframe collegando l'input opzionale "keyframes".

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | Immagine guida da posizionare nel momento scelto del video di output. | IMAGE | Sì | - |
| `position` | Come posizionare questa immagine sulla timeline del video di output. | DYNAMIC_COMBO | Sì | "Fraction of duration (0.0-1.0)"<br>"Absolute time (seconds)" |
| `keyframes` | Keyframe precedenti opzionali da concatenare con questo. | LUMA_RAY32_KEYFRAME | No | - |

### Input di Fraction of duration (0.0-1.0)

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `fraction` | Dove si applica questa immagine nel video di output (0.0 = inizio, 1.0 = fine). Predefinito: 0.0. | FLOAT | Sì | 0.0 a 1.0 (passo: 0.01) |

### Input di Absolute time (seconds)

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `seconds` | Tempo in secondi dall'inizio del video di output in cui si applica questa immagine. Predefinito: 0.0. | FLOAT | Sì | 0.0 a 10.0 (passo: 0.1) |

Il parametro `position` determina quale valore viene usato per posizionare l'immagine sulla timeline. Vengono mostrati e utilizzati solo i sottoparametri appartenenti all'opzione selezionata: `fraction` per "Fraction of duration (0.0-1.0)" e `seconds` per "Absolute time (seconds)".

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `keyframes` | Una catena di keyframe che include il nuovo keyframe combinato con eventuali keyframe precedenti opzionali. | LUMA_RAY32_KEYFRAME |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaRay32KeyframeNode/it.md)

---
**Source fingerprint (SHA-256):** `b49d879888e6e83d6937068e799ea583ed5c90284e829ac496821eea330fe9c7`
