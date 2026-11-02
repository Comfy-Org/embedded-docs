# MiniMax H3 Max Extend Video

Questo nodo continua un video con nuovo materiale video guidato da un prompt e da riferimenti audio opzionali. Il video sorgente viene caricato, la continuazione viene generata e il risultato viene restituito come video intero renderizzato nuovamente oppure solo come nuovo materiale video. Sono disponibili due modelli: "MiniMax H3 Max" e "MiniMax H3 Max Turbo", quest'ultimo più economico per unità.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Modello da usare per continuare il video. Entrambi i modelli espongono gli stessi input di seguito. | DYNAMIC_COMBO | Sì | "MiniMax H3 Max"<br>"MiniMax H3 Max Turbo" |

### Input dei modelli

Questi input si applicano a entrambi i modelli.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `video` | Video da estendere, lungo da 1,625 a 60 secondi, fino a 50 MB. Il rapporto d'aspetto deve essere compreso tra 0,4 e 2,5. | VIDEO | Sì | da 1.625 a 60 secondi |
| `prompt` | Cosa accade dopo. Descrivi la continuazione, non la sorgente. Fai riferimento agli audio di riferimento come `@Audio1`..`@Audio3`, ad esempio "@Audio1 per la voce". | STRING | Sì | da 1 a 50000 caratteri |
| `reference_audios` | Slot espandibile: collega fino a 3 clip audio (`audio_1`...`audio_3`) per il nuovo materiale video; ciascuna deve durare almeno 2 secondi e il totale non può superare 14,5 secondi. | AUDIO | No | da 0 a 3 clip |
| `duration` | Secondi di nuovo materiale video da aggiungere (predefinito: 5). | INT | Sì | da 1 a 15 |
| `resolution` | Risoluzione del video di output (predefinito: "768P"). | COMBO | Sì | "480P"<br>"768P"<br>"1080P"<br>"2K" |
| `aspect_ratio` | Rapporto d'aspetto dell'output. "auto" segue il video sorgente; gli altri valori ritagliano il video sul rapporto selezionato (predefinito: "auto"). | COMBO | Sì | "auto"<br>"21:9"<br>"16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16" |
| `output` | "extended" restituisce il video intero, renderizzato nuovamente alla risoluzione selezionata, con il nuovo materiale video. "continuation" restituisce solo il nuovo materiale video, iniziando con una ripetizione di 1,6 secondi della parte finale della sorgente (predefinito: "extended"). | COMBO | Sì | "extended"<br>"continuation" |
| `prompt_expansion` | Riscrive il prompt usando il video sorgente per mantenere coerente la continuazione. Disattiva questa opzione per ottenere risultati riproducibili con lo stesso seed (predefinito: true). | BOOLEAN | No | true<br>false |
| `seed` | Seed casuale. La stessa richiesta con lo stesso seed produce risultati simili, ma non necessariamente identici (predefinito: 42). | INT | Sì | da 0 a 4294967295 |

### Vincoli dei parametri

- Alla risoluzione 2K, l'output "extended" è limitato a 45 secondi in totale, considerando video sorgente e nuovo materiale video. Usa "continuation" o una risoluzione inferiore per clip più lunghe.
- Ogni clip audio di riferimento deve durare almeno 2 secondi e tutte insieme non possono superare 14,5 secondi.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `video` | Il video esteso o solo il nuovo materiale video, a seconda dell'impostazione `output`. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxExtendVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `db41a14db392fa450689c8d0d73d38b4ce9ea59ee30cfe4d6d2b0501cf0fc9a8`
