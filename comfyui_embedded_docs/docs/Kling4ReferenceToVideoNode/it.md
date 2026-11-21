# Kling 4.0 Da riferimento a video

Genera un video da immagini di riferimento e video di riferimento con il modello Kling 4.0, audio incluso. I riferimenti guidano soggetto, stile e movimento, mentre un primo e un ultimo fotogramma opzionali fissano l'inizio e la fine della clip. Usalo per mantenere coerenti un personaggio o una scena all'interno di un'inquadratura mentre descrivi l'azione nel prompt.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Selettore del modello. `"kling-4.0"` supporta fino a 4K HDR, clip da 30 secondi e un ultimo fotogramma; `"kling-4.0-flash"` è limitato a 720p e 20 secondi e non ha l'input `last_frame`. Selezionando un modello vengono mostrati i relativi input di seguito. | DYNAMIC_COMBO | Sì | `"kling-4.0"`<br>`"kling-4.0-flash"` |

### Input di kling-4.0

Questi input compaiono quando `model` è impostato su `"kling-4.0"`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `reference_images` | Slot espandibili per le immagini di riferimento, fino a 10. Fai riferimento a esse nel prompt come `@Image1`, `@Image2` e così via, nell'ordine di connessione. | AUTOGROW | No | 0 a 10 immagini |
| `reference_videos` | Slot espandibili per i video di riferimento, fino a 5. Fai riferimento a essi nel prompt come `@Video1`, `@Video2` e così via. Ogni video e tutti i video insieme devono durare da 3 a 30 secondi. | AUTOGROW | No | 0 a 5 video |
| `first_frame` | Fotogramma opzionale da cui inizia il video. Conteggia ai fini del limite di 10 immagini insieme alle immagini di riferimento. | IMAGE | No | - |
| `last_frame` | Fotogramma opzionale su cui termina il video. Conteggia ai fini del limite di 10 immagini insieme alle immagini di riferimento. | IMAGE | No | - |
| `prompt` | Descrizione del video da generare. Fai riferimento agli input come `@Image1`, `@Image2` e così via, e `@Video1`, `@Video2` e così via. | STRING | Sì | 1 a 26000 caratteri |
| `resolution` | Risoluzione del video di output; un'opzione con `HDR` nel nome restituisce un video HDR. Predefinito: `"720p"`. | COMBO | Sì | `"720p"`<br>`"1080p"`<br>`"4k"`<br>`"1080p HDR"`<br>`"4k HDR"` |
| `aspect_ratio` | Rapporto d'aspetto del video di output. `"adaptive"` segue il prompt, poi il primo fotogramma o i video di riferimento e, in caso contrario, ricade su 16:9. Predefinito: `"adaptive"`. | COMBO | Sì | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | Durata del video generato in secondi. Predefinito: 5. | INT | Sì | 3 a 30 |
| `seed` | Il seed controlla se il nodo deve rieseguirsi; i risultati non sono deterministici indipendentemente dal seed. Predefinito: 42. | INT | Sì | 0 a 2147483647 |

### Input di kling-4.0-flash

Questi input compaiono quando `model` è impostato su `"kling-4.0-flash"`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `reference_images` | Slot espandibili per le immagini di riferimento, fino a 10. Fai riferimento a esse nel prompt come `@Image1`, `@Image2` e così via, nell'ordine di connessione. | AUTOGROW | No | 0 a 10 immagini |
| `reference_videos` | Slot espandibili per i video di riferimento, fino a 5. Fai riferimento a essi nel prompt come `@Video1`, `@Video2` e così via. Ogni video e tutti i video insieme devono durare da 3 a 20 secondi. | AUTOGROW | No | 0 a 5 video |
| `first_frame` | Fotogramma opzionale da cui inizia il video. Conteggia ai fini del limite di 10 immagini insieme alle immagini di riferimento. | IMAGE | No | - |
| `prompt` | Descrizione del video da generare. Fai riferimento agli input come `@Image1`, `@Image2` e così via, e `@Video1`, `@Video2` e così via. | STRING | Sì | 1 a 26000 caratteri |
| `resolution` | Risoluzione del video di output. Flash esegue il rendering solo a 720p. Predefinito: `"720p"`. | COMBO | Sì | `"720p"` |
| `aspect_ratio` | Rapporto d'aspetto del video di output. `"adaptive"` segue il prompt, poi il primo fotogramma o i video di riferimento e, in caso contrario, ricade su 16:9. Predefinito: `"adaptive"`. | COMBO | Sì | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"`<br>`"4:3"`<br>`"3:4"` |
| `duration` | Durata del video generato in secondi. Predefinito: 5. | INT | Sì | 3 a 20 |
| `seed` | Il seed controlla se il nodo deve rieseguirsi; i risultati non sono deterministici indipendentemente dal seed. Predefinito: 42. | INT | Sì | 0 a 2147483647 |

**Vincoli e comportamento:**

* Le immagini sono limitate a 10 in totale, contando le immagini di riferimento, il primo fotogramma e l'ultimo fotogramma.
* Ogni immagine deve essere di almeno 300x300 pixel con un rapporto d'aspetto compreso tra 2:5 e 5:2.
* Ogni video di riferimento deve durare da 3 a 30 secondi (da 3 a 20 con `kling-4.0-flash`), essere di almeno 700x700 e al massimo 4553x4553 pixel, non superare 8.294.400 pixel in totale, avere un rapporto d'aspetto compreso tra 2:5 e 5:2 e una frequenza dei fotogrammi di almeno 24 fps. Tutti i video di riferimento insieme non devono superare lo stesso limite.
* Un prompt che menziona `@ImageN` o `@VideoN` genera un errore quando sono connessi meno di N input di quel tipo.
* Quando è connesso un primo o un ultimo fotogramma, il nodo aggiunge un'istruzione affinché il video inizi o termini esattamente su quel fotogramma.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `video` | Il video generato, scaricato dal provider al completamento dell'attività. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4ReferenceToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `d1048c637074d79fa41da1f903a1f4b2c895563dde4c5ee761c20460a8d2e383`
