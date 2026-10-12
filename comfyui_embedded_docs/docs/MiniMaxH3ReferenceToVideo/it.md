# MiniMaxH3ReferenceToVideo

MiniMax H3 Reference to Video crea il condizionamento testuale e il latente audio-video vuoto necessari per la generazione reference-to-video di MiniMax H3. Fornisci un prompt più immagini, video e clip audio di riferimento opzionali, e il nodo codifica questi riferimenti in un condizionamento che il modello può usare durante la generazione. Il prompt fa riferimento ai riferimenti con i tag `<Picture i>`, `<Video k>` e `<Audio j>`.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `clip` | Modello CLIP utilizzato per tokenizzare il prompt e codificare i contenuti multimediali di riferimento in token di condizionamento. | CLIP | Sì | |
| `vae` | VAE video. Senza di esso, le immagini/video di riferimento condizionano solo il codificatore di testo. | VAE | No | |
| `audio_vae` | VAE audio. Senza di esso, l'audio di riferimento condiziona solo il codificatore di testo. | VAE | No | |
| `prompt` | Prompt testuale per il video. È possibile fare riferimento ai contenuti multimediali di riferimento con i tag `<Picture i>`, `<Video k>` e `<Audio j>` (indicizzati a partire da 1 per tipo). Supporta prompt multilinea e dinamici. | STRING | Sì | |
| `width` | Larghezza del video generato in pixel (predefinito: 1344). | INT | Sì | da 32 a 16384 (passo 32) |
| `height` | Altezza del video generato in pixel (predefinito: 768). | INT | Sì | da 32 a 16384 (passo 32) |
| `length` | Numero di fotogrammi a 24 fps (124 = ~5 s, l'intervallo addestrato è ~124-362) (predefinito: 124). | INT | Sì | da 5 a 3600 (passo 17) |
| `ref_image_size` | Dimensionamento delle immagini di riferimento. `match` scala ciascun riferimento (solo verso il basso, mantenendo le proporzioni) all'area in pixel della generazione; `max` usa il lato corto di 2048px della pipeline di riferimento per la migliore fedeltà dell'identità. I token di riferimento attraversano ogni passaggio di campionamento, quindi `max` può essere diverse volte più lento (predefinito: `match`). | COMBO | Sì | `"match"`<br>`"max"` |
| `ref_images` | Slot espandibile: collega fino a 9 immagini di riferimento (`ref_image_1` ... `ref_image_9`). Immagine di riferimento (ridimensionata al lato corto di 2048 se più grande, mai ingrandita). | IMAGE | No | da 0 a 9 |
| `ref_videos` | Slot espandibile: collega fino a 3 video di riferimento (`ref_video_1` ... `ref_video_3`). Fotogrammi video di riferimento a 24 fps (2-15 s). | IMAGE | No | da 0 a 3 |
| `ref_video_audios` | Slot espandibile: collega fino a 3 tracce audio (`ref_video_audio_1` ... `ref_video_audio_3`). Traccia audio del video di riferimento con lo stesso numero. | AUDIO | No | da 0 a 3 |
| `ref_audios` | Slot espandibile: collega fino a 3 clip audio di riferimento autonome (`ref_audio_1` ... `ref_audio_3`). Audio di riferimento autonomo. | AUDIO | No | da 0 a 3 |

Note:

- Il prompt fa riferimento ai contenuti multimediali di riferimento con tag indicizzati a partire da 1 per tipo: `<Picture i>` per le immagini, `<Video k>` per i video e `<Audio j>` per l'audio. I riferimenti vengono presentati al modello in un ordine fisso: immagini, poi video (con l'etichetta `<Audio j>` di ciascuna traccia audio subito prima del relativo `<Video k>`), quindi audio autonomo.
- Una traccia audio collegata a `ref_video_audio_N` viene usata con il video di riferimento collegato a `ref_video_N`.
- I video di riferimento devono contenere almeno 5 fotogrammi (~0,2 secondi a 24 fps), altrimenti il nodo genera un errore. I fotogrammi oltre la `length` richiesta vengono tagliati, e il numero di fotogrammi rimanente viene adattato a un valore supportato dal modello.
- La `length` richiesta viene allineata a un numero di fotogrammi supportato prima che il latente venga creato.
- Senza `vae`, le immagini e i video di riferimento condizionano solo il codificatore di testo (non vengono prodotti latenti di riferimento). Senza `audio_vae`, l'audio di riferimento condiziona solo il codificatore di testo.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `positive` | Condizionamento contenente il prompt codificato. Quando vengono forniti i contenuti multimediali di riferimento e i VAE pertinenti, contiene anche il contenuto codificato di immagini, video e audio di riferimento usato dal modello MiniMax H3. | CONDITIONING |
| `latent` | Latente audio-video vuoto con la `width`, la `height` e la `length` richieste (numero di fotogrammi), incluso il latente video allineato e il latente audio. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ReferenceToVideo/it.md)

---
**Source fingerprint (SHA-256):** `47df0d6d13cb02aa4f69b50a7f8d0f6c1639c1fb5e0f69bf8fc57dd4cb752db8`
