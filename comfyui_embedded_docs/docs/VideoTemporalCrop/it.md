# VideoTemporalCrop

Questo nodo ritaglia un intervallo continuo di fotogrammi da un video. Funziona in modalità completamente lazy, ovvero elabora solo la porzione selezionata del video quando serve più avanti nel workflow.

## Input
| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `video` | Video di input. | VIDEO | Sì | – |
| `start_frame` | Indice del fotogramma iniziale (predefinito: 0). | INT | Sì | da 0 a 99999 |
| `length` | Numero di fotogrammi da mantenere (predefinito: 16). | INT | Sì | da 1 a 99999 |

Nota: `start_frame` è limitato all'ultimo fotogramma del video, e `length` viene ridotto se supererebbe i fotogrammi disponibili.

## Output
| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `video` | Video ritagliato (lazy). | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTemporalCrop/it.md)

---
**Source fingerprint (SHA-256):** `1d28a55399c9fe7ca47f0aaa872751ac89c5419a6f6be6636fbf7f020a02749d`
