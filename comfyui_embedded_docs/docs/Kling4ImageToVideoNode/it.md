# Kling 4.0 Image to Video

Genera un video a partire da un insieme di fotogrammi chiave con il modello Kling 4.0, incluso l'audio. Il primo fotogramma, fino a otto fotogrammi intermedi e l'ultimo fotogramma vengono inviati in ordine; i fotogrammi intermedi sono distribuiti uniformemente lungo la clip e l'output assume le proporzioni del primo fotogramma chiave. Usalo per animare un'immagine o per guidare un'inquadratura attraverso una sequenza di momenti chiave.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Selettore del modello. È disponibile solo `"kling-4.0"`; selezionandolo vengono mostrati gli input seguenti. | DYNAMIC_COMBO | Sì | `"kling-4.0"` |

### Input di kling-4.0

Questi input compaiono quando `model` è impostato su `"kling-4.0"`. È necessario collegare almeno uno degli input dei fotogrammi.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `first_frame` | Fotogramma opzionale da cui inizia il video. | IMAGE | No | - |
| `middle_frames` | Slot espandibili opzionali per i fotogrammi tra il primo e l'ultimo, fino a 8. Sono distribuiti uniformemente lungo la clip. | AUTOGROW | No | da 0 a 8 immagini |
| `last_frame` | Fotogramma opzionale su cui termina il video. | IMAGE | No | - |
| `prompt` | Descrizione opzionale del movimento. Fai riferimento ai fotogrammi collegati come `@Image1`, `@Image2` e così via, nell'ordine: primo fotogramma, fotogrammi intermedi, ultimo fotogramma. Predefinito: stringa vuota. | STRING | Sì | Testo multiriga |
| `resolution` | Risoluzione del video in output. Predefinito: `"720p"`. | COMBO | Sì | `"720p"`<br>`"1080p"` |
| `duration` | Durata del video generato in secondi. Predefinito: 5. | INT | Sì | da 3 a 30 |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. Predefinito: 42. | INT | Sì | da 0 a 2147483647 |

**Vincoli e comportamento:**

* È possibile collegare al massimo 10 fotogrammi in totale, contando il primo fotogramma, tutti i fotogrammi intermedi e l'ultimo fotogramma.
* Il video assume le proporzioni del primo fotogramma chiave, quindi non è necessario alcun input per le proporzioni.
* Ogni fotogramma deve essere di almeno 300x300 pixel, con proporzioni comprese tra 2:5 e 5:2.
* Un prompt che menziona `@ImageN` genera un errore quando sono collegati meno di N fotogrammi.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `video` | Il video generato, scaricato dal provider una volta completata l'attività. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4ImageToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `762c350abd4a881b96355a7ce5b9e346d5c3ff22e9f11db820584d02aee12885`
