# Pika H3 Flex Reference to Video

Questo nodo genera o modifica un video con audio sincronizzato, guidato da immagini, video e clip audio di riferimento. Pika H3 Flex è il modello MiniMax H3 post-addestrato di Pika. Collega i riferimenti e indirizzali nel prompt come `@Image1`, `@Video1` o `@Audio1` nell'ordine di connessione. È richiesta almeno un'immagine o un video di riferimento e si possono collegare al massimo 12 riferimenti in totale.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Fino a 9 immagini, indirizzate nel prompt come `@Image1` fino a `@Image9` nell'ordine di connessione. È richiesta almeno un'immagine o un video. | AUTOGROW | No | 0 a 9 immagini |
| `reference_videos` | Fino a 3 clip, indirizzate nel prompt come `@Video1` fino a `@Video3` nell'ordine di connessione. Ogni clip deve durare da 2 a 15 secondi e le clip devono totalizzare 15 secondi o meno. Fatturazione al secondo. | AUTOGROW | No | 0 a 3 video |
| `reference_audios` | Fino a 3 clip, indirizzate nel prompt come `@Audio1` fino a `@Audio3`. Ogni clip deve durare da 2 a 15 secondi e le clip devono totalizzare 15 secondi o meno. Quando vengono copiate nell'output, le clip vengono riprodotte nell'ordine di connessione, prima dell'audio dei video collegati. | AUTOGROW | No | 0 a 3 clip audio |
| `prompt` | Cosa generare o la modifica da apportare. Indica i riferimenti come `@Image1`, `@Video1`, `@Audio1` oppure come `<Picture 1>`, `<Video 1>`, `<Audio 1>`. Non deve essere vuoto. Predefinito: "" (stringa vuota). | STRING | Sì | 1 a 8000 caratteri |
| `reference_video_audio` | Copia l'audio dei video collegati nell'output. Disattivalo per una nuova atmosfera sonora o per il trasferimento di movimento con nuova musica. Un primo piano parlante senza dialogo nel prompt riceve quindi un parlato inventato. Predefinito: True. | BOOLEAN | Sì | true<br>false |
| `resolution` | Risoluzione dell'output. `"1080p"` e superiori vengono renderizzate a 768p e sottoposte a upscale una volta. Lo stesso seed a 480p produce un video diverso. Predefinito: `"768p"`. | COMBO | Sì | `"480p"`<br>`"768p"`<br>`"1080p"`<br>`"2k"`<br>`"4k"` |
| `aspect_ratio` | Rapporto d'aspetto dell'output. `"auto"` segue un video di riferimento, altrimenti il prompt. Le immagini di riferimento non lo influenzano. Predefinito: `"auto"`. | COMBO | Sì | `"auto"`<br>`"21:9"`<br>`"16:9"`<br>`"3:2"`<br>`"4:3"`<br>`"5:4"`<br>`"1:1"`<br>`"4:5"`<br>`"3:4"`<br>`"2:3"`<br>`"9:16"`<br>`"9:21"` |
| `duration` | Durata della clip in secondi. La lunghezza dell'output segue una griglia di frame: 5 secondi producono 124 frame, circa 5,17 secondi. Predefinito: 5. | INT | Sì | 5 a 15 secondi |
| `rewrite_prompt` | Consenti a Pika di espandere prima il prompt. Lo stesso seed produce quindi un video diverso a ogni esecuzione. Predefinito: False. | BOOLEAN | Sì | true<br>false |
| `seed` | Seed per il campionamento. Con `rewrite_prompt` disattivato, lo stesso seed ripete esattamente il video, anche se un'esecuzione locale con lo stesso seed dà un risultato diverso. Predefinito: 42. | INT | Sì | 0 a 2147483647 |

**Vincoli:**

* È richiesta almeno un'immagine o un video di riferimento.
* Si possono collegare al massimo 12 riferimenti in totale, contando insieme immagini, video e clip audio.
* Ogni video e ogni clip audio di riferimento devono durare da 2 a 15 secondi; i video devono totalizzare 15 secondi o meno e le clip audio 15 secondi o meno.
* Il prompt deve contenere da 1 a 8000 caratteri.
* Il riferimento a uno slot non collegato, ad esempio `@Image3` con due immagini fornite, genera un errore.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `VIDEO` | La clip generata o modificata con il suo audio sincronizzato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaH3FlexReferenceVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `c6d8700e3bb0c4ed7663aff55d477314af566568bd6db353fc21d6249ddd93bd`
