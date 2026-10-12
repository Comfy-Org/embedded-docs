# HeyGenReferenceToVideoNode

Genera un video con dialogo e audio sincronizzati a partire da un prompt testuale usando HeyGen Video 1.0, facoltativamente guidato da materiale di riferimento collegato. Immagini di persone, prodotti o luoghi, video da riutilizzare e clip audio che forniscono una voce possono essere usati come riferimenti. Menziona ogni riferimento nel prompt come @Image1, @Video1 o @Audio1, numerati per tipo nell'ordine in cui gli input vengono collegati: questi tag vengono riscritti nelle etichette che HeyGen si aspetta, e un tag che punta a un riferimento non collegato genera un errore. Senza alcuna immagine o video di riferimento, il nodo funziona come generazione text-to-video.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Versione del modello utilizzata per la generazione. (predefinito: `"heygen-video-1"`) | DYNAMIC_COMBO | Sì | `"heygen-video-1"` |
| `prompt` | Descrizione del video, incluso qualsiasi dialogo. Fai riferimento ai riferimenti collegati come @Image1, @Video1, @Audio1, numerati per tipo nell'ordine di input. (predefinito: stringa vuota) | STRING | Sì | da 1 a 32000 caratteri |
| `duration` | Durata del video di output in secondi. (predefinito: 5) | INT | Sì | da 5 a 15 |
| `resolution` | Risoluzione di output. 2k richiede il rapporto d'aspetto 16:9 o 9:16; `"auto"` funziona a 2k solo senza riferimenti. (predefinito: `"768p"`) | COMBO | Sì | `"768p"`<br>`"480p"`<br>`"2k"` |
| `aspect_ratio` | Rapporto d'aspetto dell'output. `"auto"` è 16:9 quando non è collegato alcun riferimento, altrimenti segue la prima immagine di riferimento, oppure il primo video di riferimento quando non sono collegate immagini. (predefinito: `"auto"`) | COMBO | Sì | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"` |
| `seed` | Seed per la generazione. I risultati possono comunque variare tra esecuzioni con lo stesso seed. (predefinito: 42) | INT | Sì | da 0 a 4294967295 |
| `reference_images` | Slot espandibile: immagini di persone, prodotti o luoghi da usare nel video (`image_1` ... `image_9`); fai riferimento a esse come @Image1, @Image2, ... Ogni input deve contenere esattamente un'immagine, e ogni immagine deve avere un rapporto d'aspetto compreso tra 1:4 e 4:1. | IMAGE | No | da 0 a 9 immagini |
| `reference_videos` | Slot espandibile: video da usare come riferimenti (`video_1` ... `video_3`); fai riferimento a essi come @Video1, @Video2, ... | VIDEO | No | da 0 a 3 video |
| `reference_audios` | Slot espandibile: clip audio come una voce per un parlante (`audio_1` ... `audio_3`); fai riferimento a esse come @Audio1, @Audio2, ... Richiede almeno un'immagine o un video di riferimento. Un riferimento vocale necessita di alcuni secondi di parlato pulito, e le clip più corte di circa 2 secondi vengono solitamente ignorate. | AUDIO | No | da 0 a 3 clip audio |

### Vincoli dei parametri

- **Limite di riferimenti:** al massimo 12 riferimenti in totale tra `reference_images`, `reference_videos` e `reference_audios`; collegarne di più genera un errore.
- **L'audio richiede un'immagine o un video:** l'audio di riferimento viene rifiutato quando non è collegata alcuna immagine di riferimento né alcun video di riferimento.
- **Regole sulle immagini di riferimento:** ogni input `reference_images` deve contenere esattamente un'immagine (un batch viene rifiutato), e ogni immagine deve avere un rapporto d'aspetto compreso tra 1:4 e 4:1.
- **Tag del prompt:** `@ImageN`, `@VideoN` e `@AudioN` vengono confrontati senza distinzione tra maiuscole e minuscole. Il numero non deve superare il numero di riferimenti collegati di quel tipo, e il prompt deve essere non vuoto dopo aver rimosso gli spazi bianchi ai bordi.
- **Modalità:** con almeno un'immagine o un video di riferimento la richiesta è un'esecuzione reference-to-video; senza alcuno, è una semplice esecuzione text-to-video.
- **Risoluzione 2k:** `resolution` `"2k"` richiede `aspect_ratio` `"16:9"` o `"9:16"`; `"auto"` è accettato a 2k solo quando non sono collegate immagini di riferimento né video di riferimento.
- **Seed:** il seed decide solo se il nodo viene rieseguito; i risultati non sono riproducibili con lo stesso seed.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `VIDEO` | Il video generato con dialogo e audio sincronizzati. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenReferenceToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `f3fae5dce59c90d65ad8eff2c992819f29a71e3a3e13fa91c1e7479a9cd6fcdc`
