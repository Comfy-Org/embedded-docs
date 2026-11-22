# Pruna P-Video-2 Pro Reference to Video

Genera un video da un prompt guidato da immagini, video e audio di riferimento con Pruna P-Video-2 Pro Reference to Video. Indica ciascun riferimento con un numero nel prompt e il modello trasferisce il soggetto, lo stile o il movimento del riferimento nel risultato.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `modello` | Modello video Pruna da usare. Selezionando un modello vengono mostrati i relativi input di seguito. | DYNAMIC_COMBO | Sì | `"p-video-2-pro-reference"` |

### Input di P-Video-2 Pro Reference

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model.images` | Slot espandibile per immagini di riferimento (`image_1`, `image_2`, ...), a cui si fa riferimento nel prompt come `@Image1` fino a `@Image9` nell'ordine di connessione. Fino a 9 immagini, contando il primo e l'ultimo fotogramma. | AUTOGROW | No | 0 a 9 immagini |
| `model.videos` | Slot espandibile per video di riferimento (`video_1`, `video_2`, ...), a cui si fa riferimento come `@Video1` fino a `@Video3`. Ciascuno da 2 a 15 secondi a un massimo di 60 fps, per un totale di 15 secondi. I video superiori a 1080p vengono ridotti di risoluzione. | AUTOGROW | No | 0 a 3 video |
| `model.audios` | Slot espandibile per audio di riferimento (`audio_1`, `audio_2`, ...), a cui si fa riferimento come `@Audio1` fino a `@Audio3`. Fino a 15 secondi in totale. | AUTOGROW | No | 0 a 3 clip audio |
| `prompt` | Descrive il video. Fai riferimento ai riferimenti come `@Image1`, `@Video1` o `@Audio1` (predefinito: vuoto). Fino a 5000 caratteri. | STRING | Sì | 1 a 5000 caratteri |
| `model.first_frame` | Immagine da cui inizia il video. Conta ai fini del limite di 9 immagini. | IMAGE | No | - |
| `model.last_frame` | Immagine su cui termina il video. Conta ai fini del limite di 9 immagini. | IMAGE | No | - |
| `keep_audio` | Usa l'audio connesso come colonna sonora e genera il video in modo che vi si adatti (predefinito: False). Richiede esattamente un audio: se l'audio è più breve, viene seguito da suono generato; se è più lungo, viene tagliato alla durata. | BOOLEAN | Sì | `True`<br>`False` |
| `durata` | Durata del video in secondi (predefinito: `"5"`). | COMBO | Sì | `"5"`<br>`"6"`<br>`"7"`<br>`"8"`<br>`"9"`<br>`"10"`<br>`"11"`<br>`"12"`<br>`"13"`<br>`"14"` |
| `risoluzione` | Risoluzione di output (predefinito: `"768p"`). 1080p, 2k e 4k effettuano l'upscaling del video generato a 768p. | COMBO | Sì | `"480p"`<br>`"768p"`<br>`"1080p"`<br>`"2k"`<br>`"4k"` |
| `modalità` | `"cost"` è più economico, `"speed"` esegue il rendering più velocemente (predefinito: `"speed"`). | COMBO | Sì | `"cost"`<br>`"speed"` |
| `aspect_ratio` | Proporzioni del video di output (predefinito: `"16:9"`). `"adaptive"` usa il rapporto più comune tra i riferimenti e, con `enhance_prompt` attivo, è il prompt riscritto a scegliere il rapporto. | COMBO | Sì | `"adaptive"`<br>`"16:9"`<br>`"9:16"`<br>`"4:3"`<br>`"3:4"`<br>`"3:2"`<br>`"2:3"`<br>`"1:1"` |
| `enhance_prompt` | Riscrive il prompt con maggiori dettagli prima della generazione; `"max"` è più lento (predefinito: `"turbo"`). Mantienilo attivo quando il prompt fa riferimento ai riferimenti tramite numero; un primo o ultimo fotogramma usa sempre `"turbo"`. Impostazione avanzata. | COMBO | Sì | `"off"`<br>`"turbo"`<br>`"max"` |
| `seme` | Seed per la generazione (predefinito: 42). Lo stesso seed riproduce un risultato esattamente solo quando `model.enhance_prompt` è disattivato. | INT | Sì | 0 a 2147483647<br>Passo: 1 |

**Note:**

- Collega almeno un'immagine di riferimento, un video, un primo fotogramma o un ultimo fotogramma, altrimenti il nodo si interrompe con un errore.
- Sono consentite 9 immagini, inclusi il primo e l'ultimo fotogramma, e 12 riferimenti in totale tra immagini, fotogrammi, video e audio.
- Il video di riferimento e l'audio di riferimento sono limitati ciascuno a 15 secondi in totale, e ogni singolo video di riferimento deve durare da 2 a 15 secondi a un massimo di 60 fps.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `video` | Il video generato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrunaReferenceToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `d6e295b394984c924386ea6432532c7653b4512c646b1f86793be9b98583eef3`
