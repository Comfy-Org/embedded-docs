# Kling 4.0 Modifica video

Modifica un video esistente con un prompt testuale usando il modello Kling 4.0, facoltativamente guidato da video di riferimento e immagini di riferimento. Il risultato mantiene la durata del video di input. Usalo per cambiare ciò che accade in una clip, cambiarne lo stile o scambiare elementi mantenendo intatta la temporizzazione originale.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `modello` | Selettore del modello. `"kling-4.0"` supporta modifiche fino a 4K HDR e 30 secondi; `"kling-4.0-flash"` è limitato a 720p e 20 secondi. Selezionando un modello vengono mostrati i relativi input di seguito. | DYNAMIC_COMBO | Sì | `"kling-4.0"`<br>`"kling-4.0-flash"` |

### Input di kling-4.0

Questi input compaiono quando `model` è impostato su `"kling-4.0"`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `video_1` | Il video da modificare, di durata da 3 a 30 secondi. L'output ne mantiene la durata. | VIDEO | Sì | 3 a 30 secondi |
| `reference_videos` | Slot espandibili per video di riferimento, fino a 4. Fai riferimento a essi nel prompt come `@Video2` e così via. Ogni video e tutti i video insieme devono durare da 3 a 30 secondi. | AUTOGROW | No | 0 a 4 video |
| `reference_images` | Slot espandibili per immagini di riferimento, fino a 10. Fai riferimento a esse nel prompt come `@Image1`, `@Image2` e così via. | AUTOGROW | No | 0 a 10 immagini |
| `prompt` | Descrizione di cosa cambiare e cosa mantenere. Fai riferimento al video in modifica come `@Video1`, ai video di riferimento come `@Video2` e così via, e alle immagini come `@Image1` e così via. | STRING | Sì | 1 a 26000 caratteri |
| `resolution` | Risoluzione del video di output; un'opzione con `HDR` nel nome restituisce un video HDR. Predefinito: `"720p"`. | COMBO | Sì | `"720p"`<br>`"1080p"`<br>`"4k"`<br>`"1080p HDR"`<br>`"4k HDR"` |
| `aspect_ratio` | Proporzioni del video di output. `"adaptive"` mantiene le proporzioni del video di input. Predefinito: `"adaptive"`. | COMBO | Sì | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"`<br>`"4:3"`<br>`"3:4"` |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. Predefinito: 42. | INT | Sì | 0 a 2147483647 |
| `audio` | `"native"` genera nuovo audio per il video modificato, `"original"` mantiene l'audio del video di input. Predefinito: `"native"`. | COMBO | No | `"native"`<br>`"original"` |

### Input di kling-4.0-flash

Questi input compaiono quando `model` è impostato su `"kling-4.0-flash"`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `video_1` | Il video da modificare, di durata da 3 a 20 secondi. L'output ne mantiene la durata. | VIDEO | Sì | 3 a 20 secondi |
| `reference_videos` | Slot espandibili per video di riferimento, fino a 4. Fai riferimento a essi nel prompt come `@Video2` e così via. Ogni video e tutti i video insieme devono durare da 3 a 20 secondi. | AUTOGROW | No | 0 a 4 video |
| `reference_images` | Slot espandibili per immagini di riferimento, fino a 10. Fai riferimento a esse nel prompt come `@Image1`, `@Image2` e così via. | AUTOGROW | No | 0 a 10 immagini |
| `prompt` | Descrizione di cosa cambiare e cosa mantenere. Fai riferimento al video in modifica come `@Video1`, ai video di riferimento come `@Video2` e così via, e alle immagini come `@Image1` e così via. | STRING | Sì | 1 a 26000 caratteri |
| `resolution` | Risoluzione del video di output. Flash esegue il rendering solo a 720p. Predefinito: `"720p"`. | COMBO | Sì | `"720p"` |
| `aspect_ratio` | Proporzioni del video di output. `"adaptive"` mantiene le proporzioni del video di input. Predefinito: `"adaptive"`. | COMBO | Sì | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"`<br>`"4:3"`<br>`"3:4"` |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. Predefinito: 42. | INT | Sì | 0 a 2147483647 |
| `audio` | `"native"` genera nuovo audio per il video modificato, `"original"` mantiene l'audio del video di input. Predefinito: `"native"`. | COMBO | No | `"native"`<br>`"original"` |

**Vincoli e comportamento:**

* Il video di input e ogni video di riferimento devono durare da 3 a 30 secondi (da 3 a 20 con `kling-4.0-flash`), essere almeno 700x700 e al massimo 4553x4553 pixel, non superare 8.294.400 pixel in totale, avere un rapporto d'aspetto compreso tra 2:5 e 5:2 e una frequenza di frame di almeno 24 fps. Tutti i video insieme non devono superare lo stesso limite.
* Ogni immagine di riferimento deve essere almeno 300x300 pixel con un rapporto d'aspetto compreso tra 2:5 e 5:2, e possono essere collegate al massimo 10 immagini.
* Un prompt che menziona `@VideoN` o `@ImageN` genera un errore quando sono collegati meno di N input di quel tipo.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `video` | Il video modificato, scaricato dal provider al completamento dell'attività. Ha la stessa durata del video di input. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4EditVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `7b7f48c3292a0c380f5fceecca2291dc74d99d5d73e4049bd67d33822cd0696e`
