# ByteDance Seedance 2.5 Da riferimento a video (Legacy)

Questo nodo genera, modifica o estende video utilizzando i modelli AI Seedance 2.5 o Seedance 2.0 di ByteDance. Descrivi il video in un prompt testuale e puoi allegare immagini, video e audio di riferimento per guidare il risultato, con supporto per riferimento multimodale, modifica video ed estensione video. Questa è la versione legacy, deprecata del nodo Seedance reference-to-video.

## Input

Selezionare un `model` determina quali dei parametri seguenti sono disponibili. `video_editing` e `output_format` compaiono solo quando è selezionato Seedance 2.5. Gli slot di riferimento espandibili e le opzioni di ridimensionamento automatico dei video di riferimento sono condivisi da tutti i modelli e sono descritti in Input di riferimento.

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Il modello AI utilizzato per generare il video. Seedance 2.5 per il modello più recente, video fino a 30 secondi, output 4k e mp4/mov; Seedance 2.0 per la massima qualità e 4k; Fast per l'ottimizzazione della velocità; Mini per la generazione più veloce e a basso costo. Selezionando un modello vengono mostrati gli input specifici del modello elencati di seguito. | DYNAMIC_COMBO | Sì | `"Seedance 2.5"`<br>`"Seedance 2.0"`<br>`"Seedance 2.0 Fast"`<br>`"Seedance 2.0 Mini"` |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed (predefinito: 0). | INT | Sì | 0 a 2147483647<br>Passo: 1 |
| `watermark` | Se aggiungere una filigrana al video (predefinito: False). Impostazione avanzata. | BOOLEAN | Sì | `True`<br>`False` |

### Input di Seedance 2.5

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt testuale per la generazione del video. Inserisci le battute parlate tra virgolette doppie per guidare il dialogo generato. Deve contenere almeno un carattere non di spaziatura (predefinito: vuoto). | STRING | Sì | Qualsiasi testo |
| `resolution` | Risoluzione del video di output (predefinito: `"720p"`). | COMBO | Sì | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Rapporto d'aspetto del video di output (predefinito: `"16:9"`). | COMBO | Sì | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Durata del video di output in secondi (predefinito: 5). | INT | Sì | 4 a 30<br>Passo: 1 |
| `generate_audio` | Abilita la generazione audio per il video di output (predefinito: True). | BOOLEAN | Sì | `True`<br>`False` |
| `video_editing` | Abilita quando il prompt modifica un video di riferimento collegato, ad esempio sostituendo un oggetto al suo interno. L'output mantiene quindi la lunghezza e il rapporto d'aspetto del clip sorgente, e i widget duration e ratio vengono ignorati. Lascia disabilitato per generare un nuovo video, o per estenderne uno alla durata impostata (predefinito: False). | BOOLEAN | Sì | `True`<br>`False` |
| `output_format` | Formato contenitore del video di output (predefinito: `"mp4"`). | COMBO | Sì | `"mp4"` |

### Input di Seedance 2.0

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt testuale per la generazione del video. Deve contenere almeno un carattere non di spaziatura (predefinito: vuoto). | STRING | Sì | Qualsiasi testo |
| `resolution` | Risoluzione del video di output. | COMBO | Sì | `"480p"`<br>`"720p"`<br>`"1080p"`<br>`"4k"` |
| `ratio` | Rapporto d'aspetto del video di output (predefinito: `"adaptive"`). | COMBO | Sì | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Durata del video di output in secondi (predefinito: 7). | INT | Sì | 4 a 15<br>Passo: 1 |
| `generate_audio` | Abilita la generazione audio per il video di output (predefinito: True). | BOOLEAN | Sì | `True`<br>`False` |

### Input di Seedance 2.0 Fast e Seedance 2.0 Mini

Condivisi da Seedance 2.0 Fast e Seedance 2.0 Mini. Questi due modelli espongono lo stesso set di input di Seedance 2.0, tranne per il fatto che `resolution` è limitato a 480p e 720p.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Prompt testuale per la generazione del video. Deve contenere almeno un carattere non di spaziatura (predefinito: vuoto). | STRING | Sì | Qualsiasi testo |
| `resolution` | Risoluzione del video di output. | COMBO | Sì | `"480p"`<br>`"720p"` |
| `ratio` | Rapporto d'aspetto del video di output (predefinito: `"adaptive"`). | COMBO | Sì | `"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"`<br>`"adaptive"` |
| `duration` | Durata del video di output in secondi (predefinito: 7). | INT | Sì | 4 a 15<br>Passo: 1 |
| `generate_audio` | Abilita la generazione audio per il video di output (predefinito: True). | BOOLEAN | Sì | `True`<br>`False` |

### Input di riferimento

Disponibili per tutti i modelli. Il numero massimo di slot dipende dal modello selezionato: Seedance 2.5 supporta più riferimenti rispetto ai modelli Seedance 2.0.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Slot espandibile: collega una o più immagini di riferimento (`image_1`, `image_2`, ...) che guidano la generazione del video. Le immagini vengono automaticamente ridimensionate a una dimensione massima di 6000 pixel e devono essere almeno 300x300 pixel con un rapporto d'aspetto compreso tra 0.4 e 2.5. | IMAGE | No | Fino a 30 (Seedance 2.5)<br>Fino a 9 (modelli Seedance 2.0) |
| `reference_videos` | Slot espandibile: collega uno o più video di riferimento (`video_1`, `video_2`, ...) che guidano la generazione del video; utilizzati per la modifica e l'estensione video. | VIDEO | No | Fino a 10 (Seedance 2.5)<br>Fino a 3 (modelli Seedance 2.0) |
| `reference_audios` | Slot espandibile: collega uno o più clip audio di riferimento (`audio_1`, `audio_2`, ...) che guidano la generazione del video. | AUDIO | No | Fino a 10 (Seedance 2.5)<br>Fino a 3 (modelli Seedance 2.0) |
| `auto_downscale` | Ridimensiona automaticamente i video di riferimento che superano il budget di pixel del modello per la risoluzione selezionata. Il rapporto d'aspetto viene preservato; i video già entro i limiti non vengono modificati (predefinito: True). | BOOLEAN | No | `True`<br>`False` |
| `auto_upscale` | Impostazione avanzata. Ridimensiona automaticamente i video di riferimento che sono al di sotto del numero minimo di pixel del modello per la risoluzione selezionata. Il rapporto d'aspetto viene preservato; i video che già soddisfano il minimo non vengono modificati. Nota: il ridimensionamento di una sorgente a bassa risoluzione non aggiunge dettagli reali e può produrre generazioni di qualità inferiore (predefinito: False). | BOOLEAN | No | `True`<br>`False` |
| `reference_assets` | Slot espandibile: ID di asset della libreria virtuale Seedance creati in precedenza (Immagine, Video o Audio) da utilizzare come riferimenti (`asset_1`, `asset_2`, ...). Ogni asset deve esistere e avere lo stato Attivo. Nel prompt, gli asset possono essere indicati come `asset1`, `asset 1`, ecc.; il nodo sostituisce questi token con etichette come "Image 2". | STRING | No | Fino a 30 (Seedance 2.5)<br>Fino a 9 (modelli Seedance 2.0) |

**Vincoli importanti:**

* È richiesto almeno un riferimento. Per Seedance 2.0, 2.0 Fast e 2.0 Mini, devi fornire almeno un riferimento immagine o video (tramite `reference_images`, `reference_videos`, o una voce immagine o video in `reference_assets`). Seedance 2.5 accetta inoltre riferimenti solo audio (tramite `reference_audios` o una voce audio in `reference_assets`).
* I conteggi dei riferimenti dipendono dal modello e vengono convalidati combinando input diretti e riferimenti ad asset: Seedance 2.5 consente fino a 30 `reference_images`, 10 `reference_videos`, 10 `reference_audios` e 30 `reference_assets`; i modelli Seedance 2.0 consentono fino a 9 immagini, 3 video, 3 clip audio e 9 asset.
* Ogni video di riferimento deve durare almeno 1.8 secondi, e ogni clip audio di riferimento deve durare almeno 1.8 secondi. La durata totale di tutti i video di riferimento e di tutti gli audio di riferimento deve rimanere entro il limite del modello selezionato (15.1 secondi per i modelli Seedance 2.0).
* I video di riferimento devono inoltre rispettare i limiti di conteggio pixel del modello per la risoluzione selezionata. Con `auto_downscale` abilitato (predefinito), i video sovradimensionati vengono ridimensionati automaticamente; con `auto_upscale` abilitato, i video sottodimensionati vengono ingranditi. Se una delle due regolazioni automatiche è disabilitata, i video al di fuori del limite corrispondente generano un errore.
* Quando `video_editing` è abilitato su Seedance 2.5, gli input `duration` e `ratio` vengono ignorati; l'output corrisponde alla lunghezza e al rapporto d'aspetto del video di riferimento. Se il provider interpreta il prompt come modifica di un video di riferimento, la generazione fallisce a meno che `video_editing` non sia abilitato o il prompt non venga riformulato per descrivere un nuovo video.
* Se il provider rifiuta la traccia audio generata per il video (ad esempio, una possibile corrispondenza di copyright), l'attività fallisce; disabilitando `generate_audio` si produce un video silenzioso.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `video` | Il file video generato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2ReferenceNode/it.md)

---
**Source fingerprint (SHA-256):** `2c8ff29bb772b9ef005e264dd5c07b36f83b5b7068eebefa83ed567029187184`
