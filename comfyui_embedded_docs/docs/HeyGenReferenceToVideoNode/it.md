# HeyGen Video 1.0 da riferimento a video

Genera un video con dialogo e audio sincronizzati da un prompt testuale usando HeyGen Video 1.0, facoltativamente guidato da materiale di riferimento collegato. Immagini di persone, prodotti o luoghi, video da riutilizzare e clip audio che forniscono una voce possono tutti essere usati come riferimenti. Menziona ciascun riferimento nel prompt come @Image1, @Video1 o @Audio1, numerati per tipo nell'ordine in cui gli input sono collegati: questi tag vengono riscritti nelle etichette attese da HeyGen, e un tag che punta a un riferimento non collegato genera un errore. Senza alcuna immagine o video di riferimento, il nodo funziona come generazione da testo a video.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Versione del modello usata per la generazione. (predefinito: `"heygen-video-1"`) | DYNAMIC_COMBO | Sì | `"heygen-video-1"` |
| `prompt` | Descrizione del video, incluso qualsiasi dialogo. Fai riferimento ai riferimenti collegati come @Image1, @Video1, @Audio1, numerati per tipo nell'ordine di input. (predefinito: stringa vuota) | STRING | Sì | 1 a 16000 caratteri |
| `duration` | Durata del video di output in secondi. Più di 15 secondi è disponibile solo senza immagini e video di riferimento. (predefinito: 5) | INT | Sì | 5 a 30 |
| `resolution` | Risoluzione di output. 1080p e 2k richiedono il rapporto d'aspetto 16:9 o 9:16; `"auto"` funziona a queste risoluzioni solo senza riferimenti. (predefinito: `"768p"`) | COMBO | Sì | `"768p"`<br>`"480p"`<br>`"1080p"`<br>`"2k"` |
| `aspect_ratio` | Rapporto d'aspetto di output. `"auto"` è 16:9 quando non sono collegati riferimenti, altrimenti segue la prima immagine di riferimento, oppure il primo video di riferimento quando non sono collegate immagini. (predefinito: `"auto"`) | COMBO | Sì | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:3"`<br>`"3:4"`<br>`"21:9"` |
| `seed` | Seed per la generazione. I risultati possono comunque variare tra esecuzioni con lo stesso seed. (predefinito: 42) | INT | Sì | 0 a 4294967295 |
| `reference_images` | Slot espandibile: immagini di persone, prodotti o luoghi da usare nel video (`image_1` ... `image_9`); fai riferimento a esse come @Image1, @Image2, ... Ogni input deve contenere esattamente un'immagine, e ciascuna immagine deve avere un rapporto d'aspetto compreso tra 1:4 e 4:1. | IMAGE | No | 0 a 9 immagini |
| `reference_videos` | Slot espandibile: video da usare come riferimenti (`video_1` ... `video_3`); fai riferimento a essi come @Video1, @Video2, ... Vengono usati al massimo 15 secondi di filmato in totale. | VIDEO | No | 0 a 3 video |
| `reference_audios` | Slot espandibile: clip audio come una voce per un interlocutore (`audio_1` ... `audio_3`); fai riferimento a esse come @Audio1, @Audio2, ... Richiede almeno un'immagine o un video di riferimento. Un riferimento vocale necessita di alcuni secondi di parlato pulito, e le clip più corte di circa 2 secondi vengono di solito ignorate. | AUDIO | No | 0 a 3 clip audio |
| `auto_duration` | Se abilitato, la durata del video segue il dialogo racchiuso tra virgolette nel prompt (da 8 a 30 secondi, oppure da 8 a 15 con immagini o video di riferimento) e `duration` viene ignorato. (predefinito: `"disabled"`) | COMBO | No | `"disabled"`<br>`"enabled"` |

### Vincoli dei parametri

- **Limite di riferimenti:** al massimo 15 riferimenti in totale: fino a 9 immagini, 3 video e 3 clip audio. Collegarne di più genera un errore.
- **L'audio richiede immagine o video:** il riferimento audio viene rifiutato quando non è collegata alcuna immagine e nessun video di riferimento.
- **Regole per le immagini di riferimento:** ogni input `reference_images` deve contenere esattamente un'immagine (un batch viene rifiutato), e ciascuna immagine deve avere un rapporto d'aspetto compreso tra 1:4 e 4:1.
- **Tag del prompt:** `@ImageN`, `@VideoN` e `@AudioN` vengono confrontati senza distinzione tra maiuscole e minuscole. Il numero non deve superare il conteggio dei riferimenti collegati di quel tipo, e il prompt deve essere non vuoto dopo aver rimosso gli spazi bianchi.
- **Modalità:** con almeno un'immagine o un video di riferimento la richiesta è un'esecuzione con riferimento a video; senza alcuno è una semplice esecuzione da testo a video.
- **Risoluzione 1080p e 2k:** la `resolution` `"1080p"` o `"2k"` richiede che `aspect_ratio` sia `"16:9"` o `"9:16"`; `"auto"` è accettato a queste risoluzioni solo quando non sono collegate immagini di riferimento e nessun video di riferimento.
- **Durata:** con immagini o video di riferimento il video generato resta a 15 secondi o meno. I video più lunghi non necessitano di immagini o video di riferimento; `auto_duration` fa solo sì che `duration` venga ignorato (da 8 a 30 secondi dal dialogo, da 8 a 15 con riferimenti), non innalza quel limite.
- **Seed:** il seed decide solo se il nodo viene rieseguito; i risultati non sono riproducibili con lo stesso seed.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `VIDEO` | Il video generato con dialogo e audio sincronizzati. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenReferenceToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `415ffca1c385936e35bdb0451a23f03756e936b3b871d8d6a958da1ef8c56c36`
