# Kling 4.0 Edit Video

Modifica un video esistente con un prompt testuale usando il modello Kling 4.0, con la guida facoltativa di video di riferimento e immagini di riferimento. Il risultato mantiene la lunghezza del video di input. Usalo per cambiare ciò che accade in una clip, modificarne lo stile o scambiare elementi mantenendo intatta la temporizzazione originale.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Selettore del modello. È disponibile solo `"kling-4.0"`; selezionandolo vengono mostrati gli input seguenti. | DYNAMIC_COMBO | Sì | `"kling-4.0"` |

### Input di kling-4.0

Questi input compaiono quando `model` è impostato su `"kling-4.0"`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `video_1` | Il video da modificare, lungo da 3 a 30 secondi. L'output ne mantiene la lunghezza. | VIDEO | Sì | da 3 a 30 secondi |
| `reference_videos` | Slot espandibili per video di riferimento, fino a 4. Fai riferimento a essi nel prompt come `@Video2` e così via. Ogni video e tutti i video insieme devono essere lunghi da 3 a 30 secondi. | AUTOGROW | No | da 0 a 4 video |
| `reference_images` | Slot espandibili per immagini di riferimento, fino a 10. Fai riferimento a esse nel prompt come `@Image1`, `@Image2` e così via. | AUTOGROW | No | da 0 a 10 immagini |
| `prompt` | Descrizione di ciò che deve essere cambiato e di ciò che deve essere mantenuto. Fai riferimento al video da modificare come `@Video1`, ai video di riferimento come `@Video2` e così via, e alle immagini come `@Image1` e così via. | STRING | Sì | da 1 a 26000 caratteri |
| `resolution` | Risoluzione del video di output. Predefinito: `"720p"`. | COMBO | Sì | `"720p"`<br>`"1080p"` |
| `aspect_ratio` | Rapporto d'aspetto del video di output. `"adaptive"` mantiene il rapporto d'aspetto del video di input. Predefinito: `"adaptive"`. | COMBO | Sì | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"21:9"` |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. Predefinito: 42. | INT | Sì | da 0 a 2147483647 |

**Vincoli e comportamento:**

* Il video di input e ogni video di riferimento devono essere lunghi da 3 a 30 secondi, avere almeno 700x700 e al massimo 4553x4553 pixel, non più di 8.294.400 pixel in totale, un rapporto d'aspetto compreso tra 2:5 e 5:2 e una frequenza di fotogrammi di almeno 24 fps. Tutti i video insieme non devono superare i 30 secondi.
* Ogni immagine di riferimento deve essere di almeno 300x300 pixel con un rapporto d'aspetto compreso tra 2:5 e 5:2, e non è possibile collegare più di 10 immagini.
* Un prompt che menziona `@VideoN` o `@ImageN` genera un errore quando sono collegati meno di N input di quel tipo.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `video` | Il video modificato, scaricato dal provider una volta completata l'attività. Ha la stessa lunghezza del video di input. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Kling4EditVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `00e8de2529df9be6bc1fae5f2c2beda01f151143448e91b79f9cfb27436064ff`
