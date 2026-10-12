# MinimaxHailuo03RegenerateNode

Questo nodo esegue nuovamente il rendering di un output video MiniMax H3 768P a risoluzione 2K. Carica il video 768P non modificato e il prompt esatto utilizzato per generarlo, avvia un processo di rigenerazione MiniMax H3 e restituisce il video 2K ri-renderizzato. Se la generazione originale utilizzava frame iniziali o finali o media di riferimento, allegare gli stessi input.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello da utilizzare per la rigenerazione video. Selezionando "MiniMax H3" vengono rivelate le impostazioni del prompt, della risoluzione e dei media di riferimento. | DYNAMIC_COMBO | Sì | "MiniMax H3" |
| `video` | Il video di output MiniMax H3 768P da ri-renderizzare. Collegare l'output non modificato di un nodo video MiniMax H3 (24 FPS, 4-15 secondi). Gli output 2K non possono essere utilizzati. | VIDEO | Sì | 24 FPS, 4-15 seconds |
| `first_frame` | Immagine del primo frame della generazione originale, se utilizzata. | IMAGE | No | Image |
| `last_frame` | Immagine dell'ultimo frame della generazione originale, se utilizzata. | IMAGE | No | Image |
| `watermark` | Se aggiungere una filigrana AIGC al video. Il valore predefinito è false. | BOOLEAN | Sì | false / true |

### Input di MiniMax H3

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Il prompt esatto utilizzato per generare il video sorgente. Non deve essere vuoto. | STRING | Sì | Text (multiline) |
| `resolution` | Risoluzione con cui eseguire nuovamente il rendering del video sorgente. | COMBO | Sì | "2K" |

### Input di riferimento

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `reference_images` | Slot espandibile: collegare da `image_1` a `image_9` (fino a 9 immagini). Immagini di riferimento dalla generazione originale, nello stesso ordine. | IMAGE | No | 0-9 images |
| `reference_videos` | Slot espandibile: collegare da `video_1` a `video_3` (fino a 3 video). Video di riferimento dalla generazione originale, nello stesso ordine. | VIDEO | No | 0-3 videos |
| `reference_audios` | Slot espandibile: collegare da `audio_1` a `audio_3` (fino a 3 clip). Riferimenti audio dalla generazione originale, nello stesso ordine. Non può essere utilizzato senza un'immagine o un video di riferimento. | AUDIO | No | 0-3 clips |

### Vincoli

- Il `prompt` non deve essere vuoto.
- Il `video` sorgente deve essere un output MiniMax H3 768P non modificato: 24 FPS, larghezza e altezza divisibili per 32, al massimo 1.032.192 pixel totali e da 107 a 362 frame con passi di 17 (da 4 a 15 secondi a 24 FPS). Gli output 2K non possono essere utilizzati come sorgente.
- `first_frame` e `last_frame` sono mutuamente esclusivi con i media di riferimento (`reference_images`, `reference_videos`, `reference_audios`). Utilizzare i frame per un prompt image-to-video, oppure i media di riferimento per un prompt reference-to-video.
- `reference_audios` richiede almeno un input `reference_images` o `reference_videos`.
- `first_frame`, `last_frame` e ogni `reference_image` devono avere un rapporto d'aspetto compreso tra 0.4 e 2.5 e essere almeno 256x256 pixel.
- `reference_videos`: ogni video deve essere da 23,976 a 60 FPS e durare da 2 a 15 secondi; la durata totale non può superare i 15 secondi.
- `reference_audios`: ogni clip deve durare da 2 a 15 secondi; la durata totale non può superare i 15 secondi.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `video` | Il video MiniMax H3 ri-renderizzato a risoluzione 2K. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03RegenerateNode/it.md)

---
**Source fingerprint (SHA-256):** `4b5aa6dee12364cf6f44e7ee78b984c3568529b97051637a6ac62db9761d3a77`
