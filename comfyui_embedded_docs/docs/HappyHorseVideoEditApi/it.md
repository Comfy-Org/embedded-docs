# HappyHorseVideoEditApi

Modifica un video usando istruzioni testuali o immagini di riferimento con il modello HappyHorse. La durata dell'output è di 3-15 secondi e corrisponde al video di input; gli input più lunghi di 15 secondi vengono troncati.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello di editing video HappyHorse da utilizzare. Questa selezione determina quali opzioni di prompt, risoluzione, rapporto e immagini di riferimento sono disponibili. | DYNAMIC_COMBO | Sì | "happyhorse-1.0-video-edit" |
| `video` | Il video da modificare. | VIDEO | Sì | Da 3 a 60 secondi |
| `seed` | Seed da utilizzare per la generazione (predefinito: 0). | INT | Sì | 0 to 2147483647 |
| `watermark` | Indica se aggiungere una filigrana generata dall'IA al risultato (predefinito: False). Parametro avanzato. | BOOLEAN | Sì | True<br>False |

### Input di happyhorse-1.0-video-edit

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Istruzioni di modifica o requisiti di trasferimento di stile. Deve contenere almeno 1 carattere. | STRING | Sì | - |
| `resolution` | La risoluzione dell'output. | COMBO | Sì | "720P"<br>"1080P" |
| `ratio` | Rapporto d'aspetto. Se non viene modificato, approssima il rapporto del video di input. | COMBO | Sì | "16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |

### Input di riferimento

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `reference_images` | Slot espandibile: collega da 0 a 5 immagini di riferimento (`image1`...`image5`) per guidare la modifica. | IMAGE | No | Da 0 a 5 immagini |

**Nota:** Il video di input deve durare da 3 a 60 secondi. La durata dell'output è di 3-15 secondi e corrisponde al video di input; i video di input più lunghi di 15 secondi vengono troncati. Il parametro `prompt` deve contenere almeno 1 carattere.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `video` | Il video modificato in output. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HappyHorseVideoEditApi/it.md)

---
**Source fingerprint (SHA-256):** `396cad4b5a06d457746a421050df98c892fa9db6019e3de983b4d0c417842b57`
