# Kling 4.0 Da immagine a video

Genera un video da un insieme di fotogrammi chiave con il modello Kling 4.0, inclusi audio. Il primo fotogramma, fino a otto fotogrammi intermedi e l'ultimo fotogramma vengono inviati in ordine, i fotogrammi intermedi sono distribuiti uniformemente lungo la clip e l'output assume le proporzioni del primo fotogramma chiave. Usalo per animare un'immagine o per guidare un'inquadratura attraverso una sequenza di momenti chiave.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `modello` | Selettore del modello. `"kling-4.0"` supporta fino a 1080p e 30 secondi; `"kling-4.0-flash"` è limitato a 720p, 20 secondi e a un singolo primo fotogramma. Selezionando un modello, i relativi input vengono mostrati di seguito. | DYNAMIC_COMBO | Sì | `"kling-4.0"`<br>`"kling-4.0-flash"` |

### Input di kling-4.0

Questi input compaiono quando `model` è impostato su `"kling-4.0"`. Almeno uno degli input dei fotogrammi deve essere collegato.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `first_frame` | Fotogramma opzionale da cui inizia il video. | IMAGE | No | - |
| `middle_frames` | Slot opzionali espandibili per i fotogrammi tra il primo e l'ultimo, fino a 8. Sono distribuiti uniformemente lungo la clip. | AUTOGROW | No | 0 a 8 immagini |
| `last_frame` | Fotogramma opzionale su cui termina il video. | IMAGE | No | - |
| `prompt` | Descrizione opzionale del movimento. Fai riferimento ai fotogrammi collegati come `@Image1`, `@Image2` e così via, nell'ordine primo fotogramma, fotogrammi intermedi, ultimo fotogramma. Predefinito: stringa vuota. | STRING | Sì | Testo multiriga |
| `resolution` | Risoluzione del video di output. Predefinito: `"720p"`. | COMBO | Sì | `"720p"`<br>`"1080p"` |
| `duration` | Durata del video generato in secondi. Predefinito: 5. | INT | Sì | 3 a 30 |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. Predefinito: 42. | INT | Sì | 0 a 2147483647 |

### Input di kling-4.0-flash

Questi input compaiono quando `model` è impostato su `"kling-4.0-flash"`. Flash anima un singolo primo fotogramma.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `first_frame` | Fotogramma da cui inizia il video. | IMAGE | Sì | - |
| `prompt` | Descrizione opzionale del movimento. Fai riferimento al primo fotogramma come `@Image1`. Predefinito: stringa vuota. | STRING | Sì | Testo multiriga |
| `resolution` | Risoluzione del video di output. Flash esegue il rendering solo a 720p. Predefinito: `"720p"`. | COMBO | Sì | `"720p"` |
| `duration` | Durata del video generato in secondi. Predefinito: 5. | INT | Sì | 3 a 20 |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. Predefinito: 42. | INT | Sì | 0 a 2147483647 |

**Vincoli e comportamento:**

* È possibile collegare al massimo 10 fotogrammi in totale, contando il primo fotogramma, ogni fotogramma intermedio e l'ultimo fotogramma.
* Il video assume le proporzioni del primo fotogramma chiave, quindi non è necessario alcun input per le proporzioni.
* Ogni fotogramma deve essere di almeno 300x300 pixel, con proporzioni comprese tra 2:5 e 5:2.
* Un prompt che menziona `@ImageN` genera un errore quando sono collegati meno di N fotogrammi.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `video` | Il video generato, scaricato dal provider al completamento dell'attività. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4ImageToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `248ab33bf7a50afbc08baf1e64e5b1908a38905cda2a87d1303eeeb2755b5a6d`
