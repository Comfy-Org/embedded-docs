# VideoRandomTemporalCrop

Ritaglia casualmente un intervallo continuo di fotogrammi da un video di input. Il numero di fotogrammi da mantenere è impostato dal parametro `length`, e la posizione iniziale viene scelta casualmente usando il parametro `seed`. Il nodo opera in modalità lazy, ovvero non elabora l'intero video finché l'output non viene utilizzato a valle.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `video` | Video di input. | VIDEO | Sì | – |
| `length` | Numero di fotogrammi da mantenere. Se `length` è maggiore del numero totale di fotogrammi nel video, viene mantenuto l'intero video. (predefinito: 16) | INT | Sì | min: 1, max: 99999 |
| `seed` | Seme casuale. (predefinito: 0) | INT | Sì | min: 0, max: 0xFFFFFFFFFFFFFFFF |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `video` | Video ritagliato (lazy). | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoRandomTemporalCrop/it.md)

---
**Source fingerprint (SHA-256):** `8249feb5ac3607fcabf3de0ec4d2eb90ab4aa46c18613040c341b825c9db1b1e`
