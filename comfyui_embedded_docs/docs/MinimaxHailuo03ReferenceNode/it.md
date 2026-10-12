# MinimaxHailuo03ReferenceNode

Questo nodo genera un video utilizzando i modelli MiniMax H3, condizionato da immagini, video e audio di riferimento. I riferimenti sono indicati nel prompt in base al loro ordine di connessione: "Image 1", "Image 2", "Video 1", "Audio 1", e così via. Sono disponibili due modelli: "MiniMax H3" e "MiniMax H3 Max".

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Modello da utilizzare per la generazione video (predefinito: "MiniMax H3"). Selezionando "MiniMax H3" si abilitano gli input di generazione e riferimento di MiniMax H3 riportati di seguito. Selezionando "MiniMax H3 Max" si abilitano gli input di generazione e riferimento di MiniMax H3 Max riportati di seguito. | DYNAMIC_COMBO | Sì | "MiniMax H3"<br>"MiniMax H3 Max" |
| `seed` | Seme casuale. La stessa richiesta con lo stesso seme produce risultati simili, ma non necessariamente identici (predefinito: 42). | INT | Sì | 0 a 4294967295 |
| `watermark` | Se aggiungere una filigrana AIGC al video (predefinito: false). Supportato solo dal modello MiniMax H3. | BOOLEAN | No | true<br>false |

### Input di MiniMax H3

Questi input sono disponibili quando è selezionato "MiniMax H3" come modello.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt testuale per la generazione video. È possibile fare riferimento ai media di riferimento in base al loro ordine, ad esempio "Image 1", "Image 2", "Video 1" o "Audio 1". | STRING | Sì | Minimo 1 carattere |
| `resolution` | Risoluzione del video in output (predefinito: "768P"). | COMBO | Sì | "768P"<br>"2K" |
| `ratio` | Proporzioni del video in output (predefinito: "adaptive"). | COMBO | Sì | "adaptive"<br>"16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | Durata del video in output in secondi (predefinito: 5). | INT | Sì | 4 a 15 |

### Input di MiniMax H3 Max

Questi input sono disponibili quando è selezionato "MiniMax H3 Max" come modello.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt testuale per la generazione video. È possibile fare riferimento ai media di riferimento in base al loro ordine, ad esempio "Image 1", "Image 2", "Video 1" o "Audio 1". | STRING | Sì | 1 a 50000 caratteri |
| `resolution` | Risoluzione del video in output (predefinito: "768P"). | COMBO | Sì | "480P"<br>"768P" |
| `ratio` | Proporzioni del video in output (predefinito: "adaptive"). | COMBO | Sì | "adaptive"<br>"16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | Durata del video in output in secondi (predefinito: 5). | INT | Sì | 5 a 15 |
| `prompt_expansion_mode` | Quanto sforzo viene impiegato per riscrivere il prompt prima della generazione (predefinito: "balanced"). | COMBO | Sì | "balanced"<br>"quality" |
| `reference_detail` | Livello di dettaglio con cui vengono inviate le immagini di riferimento. "high" le invia alla dimensione massima utilizzata dal modello (fino a un lato corto di 2048 pixel); "standard" le ridimensiona a un massimo di 2048x1024 per ridurre il costo del riferimento (predefinito: "standard"). | COMBO | Sì | "high"<br>"standard" |

### Input di riferimento

Questi input di riferimento sono condivisi da entrambi i modelli. Ciascuno è uno slot espandibile.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `reference_images` | Slot espandibile: collega fino a 9 elementi (`image_1`...`image_9`). Immagini di riferimento per soggetto o stile, indicate nel prompt come "Image 1".."Image 9" in ordine di connessione. Fino a 9 immagini. | IMAGE | No | 0 a 9 immagini |
| `reference_videos` | Slot espandibile: collega fino a 3 elementi (`video_1`...`video_3`). Video di riferimento per movimento o scena, indicati nel prompt come "Video 1".."Video 3" in ordine di connessione. Fino a 3 video, da 2 a 15 secondi ciascuno, 15 secondi in totale. | VIDEO | No | 0 a 3 video |
| `reference_audios` | Slot espandibile: collega fino a 3 elementi (`audio_1`...`audio_3`). Riferimenti audio, indicati nel prompt come "Audio 1".."Audio 3" in ordine di connessione. Fino a 3 clip, da 2 a 15 secondi ciascuna, 15 secondi in totale. Non può essere utilizzato senza un'immagine o un video di riferimento. | AUDIO | No | 0 a 3 clip |

### Vincoli dei parametri

- È richiesta almeno un'immagine o un video di riferimento. Il solo audio di riferimento non è accettato.
- Ogni immagine di riferimento deve avere un rapporto d'aspetto compreso tra circa 0,4 e 2,5 (2:5 a 5:2) e una larghezza e un'altezza minime di 256 pixel.
- Ogni video di riferimento deve durare tra 2 e 15 secondi con una frequenza di fotogrammi tra 23,976 e 60 FPS. La durata totale di tutti i video di riferimento non può superare i 15 secondi.
- Ogni clip audio di riferimento deve durare tra 2 e 15 secondi. La durata totale di tutte le clip audio di riferimento non può superare i 15 secondi.
- Quando è selezionato "MiniMax H3 Max", l'impostazione `watermark` deve essere disabilitata.
- Quando è selezionato "MiniMax H3 Max", il numero totale di file di riferimento (immagini, video e audio combinati) non può superare 12.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `video` | Il video generato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03ReferenceNode/it.md)

---
**Source fingerprint (SHA-256):** `b77eedb1f7757e60518c04484f1cc24c27cf6886b3ae31c15207ea49fd436a73`
