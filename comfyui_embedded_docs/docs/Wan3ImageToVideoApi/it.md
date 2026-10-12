# Wan 3.0 Da immagine a video

Questo nodo genera un video a partire da un'immagine di primo fotogramma utilizzando il modello Wan 3.0. È possibile fornire facoltativamente un'immagine di ultimo fotogramma per controllare come termina il video; il modello crea quindi un video che esegue la transizione dal primo fotogramma all'ultimo fotogramma.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Seleziona la variante del modello Wan 3.0 da usare e determina quali impostazioni specifiche del modello vengono mostrate di seguito. | DYNAMIC_COMBO | Sì | "wan3.0-video"<br>"wan3.0-video-prime" |
| `first_frame` | Immagine del primo fotogramma. È richiesta esattamente un'immagine. | IMAGE | Sì | Immagine singola |
| `last_frame` | Immagine dell'ultimo fotogramma. Il modello genera un video che esegue la transizione dal primo all'ultimo fotogramma. Facoltativa; se fornita, è richiesta esattamente un'immagine. | IMAGE | No | Immagine singola |
| `seed` | Seme da usare per la generazione (predefinito: 42). | INT | Sì | 0 - 2147483647 |
| `watermark` | Indica se aggiungere un watermark generato dall'IA al risultato (predefinito: false). | BOOLEAN | Sì | true<br>false |

### Input di wan3.0-video e wan3.0-video-prime

Queste impostazioni specifiche del modello sono condivise da entrambe le opzioni del modello e vengono visualizzate quando viene selezionato un modello.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt che descrive gli elementi e le caratteristiche visive. Supporta l'inglese e il cinese. Può essere lasciato vuoto (predefinito: vuoto). | STRING | Sì | Fino a 20000 caratteri |
| `resolution` | Risoluzione del video in output. | COMBO | Sì | "1080P"<br>"720P"<br>"480P" |
| `ratio` | Proporzioni del video in output. Con "adaptive", le dimensioni dell'output vengono derivate dal primo fotogramma. | COMBO | Sì | "adaptive"<br>"16:9"<br>"9:16"<br>"1:1"<br>"4:3"<br>"3:4" |
| `duration` | Durata dell'output in secondi. Con "auto", il modello sceglie una durata adatta al prompt. | COMBO | Sì | "auto"<br>"2" - "30" |
| `audio` | Indica se il video in output contiene una traccia audio (predefinito: true). | BOOLEAN | Sì | true<br>false |
| `prompt_extend` | Indica se migliorare il prompt con l'assistenza dell'IA (predefinito: true). | BOOLEAN | Sì | true<br>false |

Nota: il nodo accetta esattamente un'immagine `first_frame` e facoltativamente un'immagine `last_frame`. Se più di un'immagine è collegata a uno dei due input, viene generato un errore. Quando viene fornita `last_frame`, il video generato esegue la transizione dal primo fotogramma all'ultimo fotogramma. Il `prompt` è limitato a 20.000 caratteri. Il prezzo di un'esecuzione dipende dal `model`, dalla `resolution` e dalla `duration` selezionati.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `video` | Il video generato. Contiene una traccia audio quando l'opzione `audio` è abilitata. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan3ImageToVideoApi/it.md)

---
**Source fingerprint (SHA-256):** `ff9fce554fa7aa5fc8729b5f84b2f8bf89e8e7772ce1c32b1307d0dc4882200c`
