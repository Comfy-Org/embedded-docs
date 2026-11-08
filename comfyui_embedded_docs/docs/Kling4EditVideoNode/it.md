# Kling 4.0 Modifica video

Modifica un video esistente con un prompt testuale utilizzando il modello Kling 4.0, facoltativamente guidato da video di riferimento e immagini di riferimento. Il risultato mantiene la durata del video di input. Usalo per cambiare ciò che accade in una clip, riapplicare uno stile o sostituire elementi mantenendo invariata la tempistica originale.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `modello` | Selettore del modello. `"kling-4.0"` supporta modifiche a 1080p fino a 30 secondi; `"kling-4.0-flash"` è limitato a 720p e 20 secondi. Selezionando un modello vengono mostrati i relativi input di seguito. | DYNAMIC_COMBO | Sì | `"kling-4.0"`<br>`"kling-4.0-flash"` |

### Input di kling-4.0

Questi input vengono visualizzati quando `model` è impostato su `"kling-4.0"`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `video_1` | Il video da modificare, lungo da 3 a 30 secondi. L'output ne mantiene la durata. | VIDEO | Sì | 3 a 30 secondi |
| `reference_videos` | Slot espandibili per video di riferimento, fino a 4. Fare riferimento ad essi nel prompt come `@Video2` e così via. Ogni video e tutti i video insieme devono durare da 3 a 30 secondi. | AUTOGROW | No | 0 a 4 video |
| `reference_images` | Slot espandibili per immagini di riferimento, fino a 10. Fare riferimento ad esse nel prompt come `@Image1`, `@Image2` e così via. | AUTOGROW | No | 0 a 10 immagini |
| `prompt` | Descrizione di cosa modificare e cosa mantenere. Fare riferimento al video in modifica come `@Video1`, ai video di riferimento come `@Video2` e così via, e alle immagini come `@Image1` e così via. | STRING | Sì | 1 a 26000 caratteri |
| `resolution` | Risoluzione del video di output. Predefinito: `"720p"`. | COMBO | Sì | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Proporzioni del video di output. `"adaptive"` mantiene le proporzioni del video di input. Predefinito: `"adaptive"`. | COMBO | Sì | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"` |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. Predefinito: 42. | INT | Sì | 0 a 2147483647 |
| `audio` | `"native"` genera un nuovo audio per il video modificato, `"original"` mantiene l'audio del video di input. Predefinito: `"native"`. | COMBO | No | `"native"`<br>`"original"` |

### Input di kling-4.0-flash

Questi input vengono visualizzati quando `model` è impostato su `"kling-4.0-flash"`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `video_1` | Il video da modificare, lungo da 3 a 20 secondi. L'output ne mantiene la durata. | VIDEO | Sì | 3 a 20 secondi |
| `reference_videos` | Slot espandibili per video di riferimento, fino a 4. Fare riferimento ad essi nel prompt come `@Video2` e così via. Ogni video e tutti i video insieme devono durare da 3 a 20 secondi. | AUTOGROW | No | 0 a 4 video |
| `reference_images` | Slot espandibili per immagini di riferimento, fino a 10. Fare riferimento ad esse nel prompt come `@Image1`, `@Image2` e così via. | AUTOGROW | No | 0 a 10 immagini |
| `prompt` | Descrizione di cosa modificare e cosa mantenere. Fare riferimento al video in modifica come `@Video1`, ai video di riferimento come `@Video2` e così via, e alle immagini come `@Image1` e così via. | STRING | Sì | 1 a 26000 caratteri |
| `resolution` | Risoluzione del video di output. Flash esegue il rendering solo a 720p. Predefinito: `"720p"`. | COMBO | Sì | `"720p"` |
| `aspect_ratio` | Proporzioni del video di output. `"adaptive"` mantiene le proporzioni del video di input. Predefinito: `"adaptive"`. | COMBO | Sì | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"` |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. Predefinito: 42. | INT | Sì | 0 a 2147483647 |
| `audio` | `"native"` genera un nuovo audio per il video modificato, `"original"` mantiene l'audio del video di input. Predefinito: `"native"`. | COMBO | No | `"native"`<br>`"original"` |

**Vincoli e comportamento:**

* Il video di input e ogni video di riferimento devono durare da 3 a 30 secondi (da 3 a 20 con `kling-4.0-flash`), avere dimensioni minime di 700x700 e massime di 4553x4553 pixel, non superare un totale di 8.294.400 pixel, con un rapporto d'aspetto compreso tra 2:5 e 5:2 e una frequenza di frame di almeno 24 fps. Tutti i video insieme non devono superare lo stesso limite.
* Ogni immagine di riferimento deve essere di almeno 300x300 pixel con un rapporto d'aspetto compreso tra 2:5 e 5:2, e possono essere collegate al massimo 10 immagini.
* Un prompt che menziona `@VideoN` o `@ImageN` genera un errore quando sono collegati meno di N input di quel tipo.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `video` | Il video modificato, scaricato dal provider al termine dell'attività. Ha la stessa durata del video di input. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4EditVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `c682db61e1426059dc565b12c0da749944394f77f34aaa71b97c69f984cb0931`
