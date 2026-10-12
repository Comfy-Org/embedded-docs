# MinimaxHailuo03ContextIRNode

## Panoramica

Questo nodo utilizza MiniMax H3 Context IR per analizzare la descrizione testuale e qualsiasi media allegato, quindi genera un prompt video strutturato e più efficace. Il prompt restituito è progettato per essere collegato all'input `prompt` di un nodo video MiniMax H3; se colleghi dei media lì, collega gli stessi media nello stesso ordine, perché il prompt migliorato fa riferimento ai media in base alla posizione.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modello da utilizzare per il miglioramento del prompt. | DYNAMIC_COMBO | Sì | `"MiniMax H3"` |
| `first_frame` | Primo frame del video che si intende generare. Non può essere combinato con media di riferimento. | IMAGE | No | Immagine singola |
| `last_frame` | Ultimo frame del video che si intende generare. Non può essere combinato con media di riferimento. | IMAGE | No | Immagine singola |

### Input di MiniMax H3

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Descrizione del video che si intende generare. Non può essere vuota. (predefinito: `""`) | STRING | Sì | Qualsiasi testo (non può essere vuoto) |
| `duration` | Durata del video che si intende generare, in secondi (4-15). (predefinito: 5) | INT | Sì | Da 4 a 15 |
| `ratio` | Rapporto d'aspetto del video che si intende generare. `"adaptive"` richiede almeno un input immagine, video o audio. (predefinito: `"adaptive"`) | COMBO | Sì | `"adaptive"`<br>`"16:9"`<br>`"4:3"`<br>`"1:1"`<br>`"3:4"`<br>`"9:16"`<br>`"21:9"` |

### Input di riferimento

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `reference_images` | Immagini di riferimento per soggetto o stile, indicate nel prompt come "Image 1".."Image 9" nell'ordine di connessione. Fino a 9 immagini. Slot espandibile: collega `image_1`...`image_9`. | IMAGE | No | Da 0 a 9 immagini |
| `reference_videos` | Video di riferimento per movimento o scena, indicati nel prompt come "Video 1".."Video 3" nell'ordine di connessione. Fino a 3 video, da 2 a 15 secondi ciascuno, 15 secondi in totale. Slot espandibile: collega `video_1`...`video_3`. | VIDEO | No | Da 0 a 3 video |
| `reference_audios` | Riferimenti audio, indicati nel prompt come "Audio 1".."Audio 3" nell'ordine di connessione. Fino a 3 clip, da 2 a 15 secondi ciascuna, 15 secondi in totale. Non possono essere usati senza un'immagine o un video di riferimento. Slot espandibile: collega `audio_1`...`audio_3`. | AUDIO | No | Da 0 a 3 clip |

### Vincoli dei parametri

- Gli input `prompt`, `duration`, `ratio`, `reference_images`, `reference_videos` e `reference_audios` fanno parte del gruppo di opzioni `model` e compaiono quando è selezionato "MiniMax H3".
- `first_frame` e `last_frame` non possono essere combinati con alcun media di riferimento.
- Il parametro `reference_audios` non può essere utilizzato a meno che non sia collegato anche almeno un `reference_image` o `reference_video`.
- Quando non sono collegati né frame né media di riferimento, `ratio` non può essere impostato su `"adaptive"`.
- I video di riferimento devono durare approssimativamente da 2 a 15 secondi ciascuno, con una durata totale non superiore a 15 secondi. La loro frequenza di fotogrammi deve essere compresa tra 23,9 e 60,5 FPS.
- Gli audio di riferimento devono durare approssimativamente da 2 a 15 secondi ciascuno, con una durata totale non superiore a 15 secondi.
- `first_frame`, `last_frame` e ogni immagine di riferimento devono essere di almeno 256x256 pixel e avere un rapporto d'aspetto compreso tra 0,4 e 2,5.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `STRING` | Il prompt video strutturato e migliorato generato da MiniMax H3 Context IR. Può essere collegato all'input `prompt` di un nodo di generazione video MiniMax H3. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03ContextIRNode/it.md)

---
**Source fingerprint (SHA-256):** `73015517f9c0f55f0aceeef935508a372e0d95668e4733d1c8100b53e4afa7e2`
