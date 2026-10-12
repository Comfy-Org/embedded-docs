# Wan3ReferenceToVideoApi

Questo nodo genera un video da un prompt testuale e da immagini, video e audio di riferimento opzionali usando il modello Wan 3.0. I media di riferimento possono essere combinati liberamente e menzionati nel prompt come @Image1, @Video1 e @Audio1. Il nodo invia la richiesta di generazione all'API Wan e restituisce il video completato.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Seleziona la variante del modello Wan 3.0 usata per la generazione. | DYNAMIC_COMBO | Sì | `wan3.0-video`<br>`wan3.0-video-prime` |
| `seed` | Seed da usare per la generazione. Predefinito: 42. | INT | Sì | da 0 a 2147483647 |
| `watermark` | Indica se aggiungere un watermark generato dall'IA al risultato. Predefinito: false. | BOOLEAN | Sì | true<br>false |

### Input di wan3.0-video e wan3.0-video-prime

Entrambe le opzioni del modello condividono lo stesso insieme di parametri.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt che descrive gli elementi e le caratteristiche visive. Supporta l'inglese e il cinese. Fai riferimento ai media di riferimento collegati come @Image1, @Video1, @Audio1, numerati per tipo nell'ordine di input. Predefinito: vuoto. | STRING | Sì | Fino a 20,000 caratteri |
| `resolution` | Risoluzione del video di output. | COMBO | Sì | "1080P"<br>"720P"<br>"480P" |
| `ratio` | Proporzioni del video di output. Con "adaptive", le dimensioni di output derivano dai media di input. | COMBO | Sì | "adaptive"<br>"16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |
| `duration` | Durata di output in secondi. Con "auto", il modello sceglie una durata adatta al prompt e ai media di riferimento. La durata combinata dei video di riferimento e dell'output non deve superare i 30 secondi. | COMBO | Sì | "auto"<br>da "2" a "30" (secondi interi) |
| `audio` | Indica se il video di output contiene una traccia audio. Predefinito: true. | BOOLEAN | Sì | true<br>false |
| `prompt_extend` | Indica se migliorare il prompt con l'assistenza IA. Predefinito: true. | BOOLEAN | Sì | true<br>false |

### Input di riferimento

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `reference_images` | Slot espandibile: collega da 1 a 10 immagini di riferimento. I riferimenti sono numerati come image1 fino a image10 nell'ordine di input. | IMAGE | No | da 0 a 10 immagini |
| `reference_videos` | Slot espandibile: collega da 1 a 5 video di riferimento. I riferimenti sono numerati come video1 fino a video5 nell'ordine di input. | VIDEO | No | da 0 a 5 video |
| `reference_audios` | Slot espandibile: collega da 1 a 5 clip audio di riferimento. I riferimenti sono numerati come audio1 fino a audio5 nell'ordine di input. | AUDIO | No | da 0 a 5 clip audio |

**Vincoli:**

- Il prompt deve contenere almeno un carattere non vuoto, oppure deve essere collegato almeno un input di riferimento di tipo immagine, video o audio.
- I tag di riferimento nel prompt devono corrispondere agli input collegati. Ad esempio, @Image1 si riferisce alla prima immagine di riferimento collegata, @Video2 al secondo video di riferimento collegato e @Audio1 alla prima clip audio di riferimento collegata. I tag sono numerati separatamente per tipo nell'ordine di input.
- Ogni immagine di riferimento collegata deve contenere esattamente un'immagine, non un batch.
- Ogni video di riferimento deve durare 15 secondi o meno. La durata totale di tutti i video di riferimento non deve superare i 15 secondi.
- Ogni audio di riferimento deve durare 15 secondi o meno. La durata totale di tutti gli audio di riferimento non deve superare i 15 secondi.
- Quando `duration` non è "auto", la durata totale di tutti i video di riferimento più la durata di output selezionata non deve superare i 30 secondi.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `video` | Il file video generato. Include una traccia audio quando il parametro `audio` è abilitato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan3ReferenceToVideoApi/it.md)

---
**Source fingerprint (SHA-256):** `09caa8142d71235417a3dfc5676c5f6accc2af1287fad3b7050844dd9453cc64`
