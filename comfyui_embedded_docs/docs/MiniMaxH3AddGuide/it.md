# MiniMaxH3AddGuide

Questo nodo ancora un'immagine, una breve clip, un audio o una clip con la sua traccia audio in qualsiasi frame di un video MiniMax H3. Aggiunge un keyframe guida al conditioning all'indice di frame scelto, e puoi concatenare diversi di questi nodi per ancorare più frame nello stesso video.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `positive` | Il conditioning a cui è collegato il keyframe guida. | CONDITIONING | Sì | - |
| `vae` | VAE video, necessario quando è collegata un'immagine. | VAE | No | - |
| `audio_vae` | VAE audio, necessario quando è collegato un audio. | VAE | No | - |
| `latent` | Il latent audio-video MiniMax H3 che definisce il video di destinazione. Deve essere un latent AV MiniMax H3 (annidato, con due tensori 5D, il tensore video con 24 canali). | LATENT | Sì | - |
| `image` | Immagine o frame video da ancorare. I batch multi-frame vengono ancorati come una clip e ritagliati alle lunghezze clip valide del modello: 5, 22, 39... (17k + 5) frame. I batch più corti di 5 frame utilizzano solo la prima immagine. | IMAGE | No | - |
| `audio` | Traccia audio da ancorare a partire dallo stesso indice di frame, ritagliata alla durata rimanente del video. | AUDIO | No | - |
| `frame_idx` | Indice del frame in cui ancorare l'immagine o il primo frame della clip. I valori negativi vengono contati dalla fine del video. (predefinito: 0) | INT | Sì | -9999 a 9999 |

**Vincoli:**
- Almeno uno tra `image` o `audio` deve essere fornito; altrimenti il nodo genera un errore.
- `vae` è obbligatorio quando `image` è collegato.
- `audio_vae` è obbligatorio quando `audio` è collegato.
- I batch `image` con meno di 5 frame utilizzano solo la prima immagine; i batch di 5 o più frame vengono ritagliati a una lunghezza clip valida (5, 22, 39, ecc.).
- `frame_idx` deve posizionare la guida all'interno dell'intervallo di frame del video, e una clip multi-frame deve rientrare interamente nel video; altrimenti il nodo genera un errore.
- Quando l'audio è collegato, l'indice del frame non deve superare la fine della traccia audio del video.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `positive` | Il conditioning con il keyframe guida aggiunto, contenente l'indice di frame risolto e, quando forniti, i latent dell'immagine o dell'audio codificati. | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3AddGuide/it.md)

---
**Source fingerprint (SHA-256):** `7a2f742421cc2655bd9c914258801e4538f1554a7c5e2b0836b2df1577f5a104`
