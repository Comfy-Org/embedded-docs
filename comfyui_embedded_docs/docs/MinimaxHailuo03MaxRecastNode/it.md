# MiniMax H3 Max Recast

Recast sostituisce le persone in un video con quelle provenienti da foto di riferimento, mantenendo movimento, camera, tagli e audio della clip sorgente. Il video viene caricato, il job Hailuo 03 Max viene monitorato tramite polling e il video recast viene restituito alla risoluzione scelta.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Modello da utilizzare per la generazione video. | DYNAMIC_COMBO | Sì | "MiniMax H3 Max" |

### Input di MiniMax H3 Max

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `video` | Video sorgente, della durata da 5 a 30 secondi; ogni inquadratura deve durare 15 secondi o meno. Le proporzioni devono essere comprese tra 0,4 e 2,5. | VIDEO | Sì | da 5 a 30 secondi |
| `reference_images` | Slot espandibile: collega da 1 a 4 foto (`image_1`...`image_4`), una per ogni nuova persona, di almeno 256x256 pixel. Per impostazione predefinita sostituiscono le persone principali nel video da sinistra a destra. | IMAGE | Sì | da 1 a 4 immagini |
| `prompt` | Opzionale. Chi diventa chi, oppure cos’altro mantenere o modificare. Fai riferimento alle foto come `@Image1`..`@Image4`, ad esempio "l’uomo diventa @Image2". | STRING | Sì | da 0 a 2000 caratteri |
| `resolution` | Risoluzione del video di output (predefinita: "768P"). | COMBO | Sì | "768P"<br>"1080P" |
| `enhance_realism` | Texture della pelle più naturali e migliore integrazione delle nuove persone nella scena (predefinito: false). | BOOLEAN | No | true<br>false |
| `seed` | Seme casuale. La stessa richiesta con lo stesso seed produce risultati simili, ma non garantiti come identici (predefinito: 42). | INT | Sì | 0 a 4294967295 |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `video` | Il video recast con le nuove persone al loro posto. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxRecastNode/it.md)

---
**Source fingerprint (SHA-256):** `a9e6f9edf12653f9f361992a097d1d57e7ba14b3e7dd20008b0e022cabc14c1b`
