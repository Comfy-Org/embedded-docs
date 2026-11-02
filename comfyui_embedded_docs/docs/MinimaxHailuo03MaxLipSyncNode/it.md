# MiniMax H3 Max Lip Sync

Questo nodo anima un'immagine statica in modo che i movimenti della bocca seguano una traccia audio fornita. L'immagine e l'audio vengono caricati, il processo di lip-sync di Hailuo 03 Max viene monitorato e il video parlante viene restituito alla risoluzione scelta. Il video di output ha la stessa durata dell'audio.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Modello da utilizzare per la generazione video. | DYNAMIC_COMBO | Sì | "MiniMax H3 Max" |

### Input di MiniMax H3 Max

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `image` | Immagine da animare, almeno 256x256 pixel. Le proporzioni devono essere comprese tra 0,4 e 2,5. | IMAGE | Sì | Immagine singola |
| `audio` | Audio da sincronizzare con il movimento della bocca, lungo da 5 a 899 secondi. | AUDIO | Sì | Da 5 a 899 secondi |
| `resolution` | Risoluzione di output (predefinita: "768P"). Le proporzioni sono quelle supportate più vicine a quelle dell'immagine. | COMBO | Sì | "480P"<br>"768P"<br>"1080P"<br>"2K" |
| `transcription` | Trascrivi l'audio per guidare la sincronizzazione labiale (predefinito: false). | BOOLEAN | No | true<br>false |
| `seed` | Seme casuale. La stessa richiesta con lo stesso seed produce risultati simili, ma non necessariamente identici (predefinito: 42). | INT | Sì | Da 0 a 2147483647 |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `video` | Il video parlante, della stessa durata dell'audio di input. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxLipSyncNode/it.md)

---
**Source fingerprint (SHA-256):** `0af4166f9f3237cacc3506d6c6544c0374a330cf998f8bd2ef1f4f7162e2f9ab`
