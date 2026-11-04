# Pika H3 Flex Video

Questo nodo genera un video con audio sincronizzato a partire da un prompt testuale, facoltativamente ancorato a un primo fotogramma, a un ultimo fotogramma o a entrambi. Pika H3 Flex è il modello MiniMax H3 post-addestrato di Pika: genera l'immagine e il relativo audio in un'unica passata; risoluzione, rapporto d'aspetto e durata vengono impostati dall'utente. Se non è collegato alcun fotogramma, il nodo esegue text to video; collegando un fotogramma passa a image to video.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Cosa accade nel video, incluso il suono desiderato. Non deve essere vuoto. Predefinito: "" (stringa vuota). | STRING | Sì | Da 1 a 8000 caratteri |
| `first_frame` | Immagine opzionale usata come fotogramma iniziale. Collegandola, si esegue image to video anziché text to video. | IMAGE | No | - |
| `last_frame` | Immagine opzionale usata come fotogramma finale. Può essere usata insieme a `first_frame` oppure da sola. | IMAGE | No | - |
| `resolution` | Risoluzione di output. `"1080p"` e superiori eseguono il rendering a 768p e applicano un upscale una volta. Lo stesso seed a 480p produce un video diverso. Predefinito: `"768p"`. | COMBO | Sì | `"480p"`<br>`"768p"`<br>`"1080p"`<br>`"2k"`<br>`"4k"` |
| `aspect_ratio` | Rapporto d'aspetto di output. `"auto"` segue il primo fotogramma collegato, altrimenti il prompt. Predefinito: `"auto"`. | COMBO | Sì | `"auto"`<br>`"21:9"`<br>`"16:9"`<br>`"3:2"`<br>`"4:3"`<br>`"5:4"`<br>`"1:1"`<br>`"4:5"`<br>`"3:4"`<br>`"2:3"`<br>`"9:16"`<br>`"9:21"` |
| `duration` | Durata della clip in secondi. La lunghezza dell'output segue una griglia di fotogrammi: 5 secondi producono 124 fotogrammi, circa 5,17 secondi. Predefinito: 5. | INT | Sì | Da 5 a 15 secondi |
| `rewrite_prompt` | Consenti a Pika di espandere prima il prompt. Lo stesso seed produce quindi un video diverso a ogni esecuzione. Predefinito: False. | BOOLEAN | Sì | true<br>false |
| `seed` | Seed per il campionamento. Con `rewrite_prompt` disattivato, lo stesso seed ripete esattamente il video, anche se un'esecuzione locale con lo stesso seed dà un risultato diverso. Predefinito: 42. | INT | Sì | Da 0 a 2147483647 |

**Vincoli:**

* Il prompt deve contenere tra 1 e 8000 caratteri.
* La fatturazione dipende dalla risoluzione selezionata e dalla durata della clip, calcolata per secondo di output.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `VIDEO` | La clip generata con il relativo audio sincronizzato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaH3FlexVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `63a90fc5874ed861db3c0821e702cfcd1a14650f09459b242b4ec5e3ba5b0cd5`
