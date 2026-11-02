# MiniMax H3 Max Insert Video

Questo nodo sostituisce la parte di un video compresa tra il tempo di inizio e quello di ripresa con una scena appena generata, guidata da un prompt e da immagini e video di riferimento opzionali. Il video di origine viene tagliato in corrispondenza di `start_time` e riprende in corrispondenza di `resume_time`; l'intervallo rimosso viene rigenerato e reinserito. Usalo per correggere un'inquadratura, sostituire un'azione o collegare due parti di una clip.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Modello da utilizzare per la generazione video. | DYNAMIC_COMBO | Sì | "MiniMax H3 Max" |

### Input di MiniMax H3 Max

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `video` | Video di origine, fino a 60 secondi di durata. Le proporzioni devono essere comprese tra 0,4 e 2,5. | VIDEO | Sì | da 0 a 60 secondi |
| `reference_images` | Slot espandibile: collega fino a 9 immagini di riferimento opzionali (`image_1`...`image_9`) per la nuova scena, di almeno 256x256 pixel. Nel prompt vengono indicate come `@Image1`..`@Image9` nell'ordine di connessione. | IMAGE | No | da 0 a 9 immagini |
| `reference_videos` | Slot espandibile: collega fino a 3 video di riferimento opzionali (`video_1`...`video_3`) per la nuova scena, da 2 a 15 secondi ciascuno e 15 secondi in totale. Nel prompt vengono indicati come `@Video1`..`@Video3` nell'ordine di connessione. | VIDEO | No | da 0 a 3 video |
| `prompt` | La nuova scena. È richiesto un prompt o almeno un riferimento; i riferimenti senza prompt vengono spesso ignorati. | STRING | Sì | da 0 a 50000 caratteri |
| `start_time` | Secondo in cui il video di origine si interrompe e inizia la nuova scena (predefinito: 2.0). | FLOAT | Sì | da 1.625 a 60.0 |
| `resume_time` | Secondo in cui il video di origine riprende dopo la nuova scena (predefinito: 3.0). Deve essere successivo a `start_time` e almeno 1.375 secondi prima della fine del video. La parte del video di origine compresa tra `start_time` e `resume_time` viene rimossa. | FLOAT | Sì | da 1.625 a 60.0 |
| `duration` | Durata della nuova scena in secondi (predefinito: 5). | INT | Sì | da 5 a 13 |
| `resolution` | Risoluzione del video di output (predefinito: "768P"). | COMBO | Sì | "480P"<br>"768P" |
| `color_match` | Abbina i colori della nuova scena a quelli del video di origine (predefinito: true). | BOOLEAN | No | true<br>false |
| `prompt_expansion` | Riscrive il prompt usando il video di origine. Disattivalo per ottenere risultati riproducibili con lo stesso seed (predefinito: true). | BOOLEAN | No | true<br>false |
| `seed` | Seed casuale. La stessa richiesta con lo stesso seed produce risultati simili, ma non necessariamente identici (predefinito: 42). | INT | Sì | da 0 a 2147483647 |

### Vincoli dei parametri

- `resume_time` deve essere maggiore di `start_time` e almeno 1.375 secondi prima della fine del video; in caso contrario, la richiesta viene rifiutata.
- Ogni video di riferimento deve durare tra 2 e 15 secondi e, complessivamente, la loro durata non può superare i 15 secondi.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `video` | Il video di origine con la nuova scena inserita tra il tempo di inizio e quello di ripresa. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxInsertVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `623ad0b37f51ce4640c0058676e008697e31563c2a77a3da79ba7936af2d3f99`
