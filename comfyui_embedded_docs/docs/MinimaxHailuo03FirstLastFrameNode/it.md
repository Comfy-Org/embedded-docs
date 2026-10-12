# MiniMax H3 Da Primo-Ultimo Frame a Video

Questo nodo genera un video a partire da un'immagine del primo frame e, facoltativamente, da un'immagine dell'ultimo frame usando i modelli MiniMax H3. Il selettore `model` cambia quali impostazioni e vincoli di generazione si applicano, e il rapporto d'aspetto del video generato segue le immagini fornite.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Range |
|-----------|-------------|--------------|--------------|-------|
| `model` | Modello da usare per la generazione video. Selezionando un modello vengono mostrate sotto le relative impostazioni specifiche. | DYNAMIC_COMBO | Sì | "MiniMax H3"<br>"MiniMax H3 Max"<br>"MiniMax H3 Max Turbo" |
| `first_frame` | Immagine del primo frame per il video. Il video generato segue il rapporto d'aspetto di questa immagine. | IMAGE | Sì | - |
| `last_frame` | Immagine opzionale dell'ultimo frame per il video. Se fornita, il video viene generato dal primo frame verso questo ultimo frame. | IMAGE | No | - |
| `seed` | Seme casuale. La stessa richiesta con lo stesso seme produce risultati simili, ma non garantisce che siano identici. Include un'opzione "control after generate". Predefinito: 42. | INT | Sì | 0 - 4294967295 |
| `watermark` | Indica se aggiungere un watermark AIGC al video. Questo è un parametro avanzato. Supportato solo dal modello `MiniMax H3`. Predefinito: False. | BOOLEAN | Sì | True<br>False |

### Input di MiniMax H3

Queste impostazioni vengono mostrate quando `MiniMax H3` è selezionato nel selettore `model`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Range |
|-----------|-------------|--------------|--------------|-------|
| `prompt` | Prompt testuale per la generazione video. Deve contenere almeno un carattere diverso da spazi bianchi. | STRING | Sì | Testo multiriga |
| `resolution` | Risoluzione del video in output. | COMBO | Sì | "768P"<br>"2K" |
| `duration` | Durata del video in output in secondi. Predefinito: 5. | INT | Sì | 4 - 15 |

### Input di MiniMax H3 Max e MiniMax H3 Max Turbo

Queste impostazioni sono condivise sia da `MiniMax H3 Max` sia da `MiniMax H3 Max Turbo`. Selezionando uno dei due modelli vengono mostrate le stesse impostazioni.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Range |
|-----------|-------------|--------------|--------------|-------|
| `prompt` | Prompt testuale per la generazione video. Non deve essere vuoto o composto solo da spazi bianchi ed è limitato a 50.000 caratteri. | STRING | Sì | Testo multiriga |
| `resolution` | Risoluzione del video in output. Predefinito: 768P. | COMBO | Sì | "480P"<br>"768P" |
| `duration` | Durata del video in output in secondi. Predefinito: 5. | INT | Sì | 5 - 15 |
| `prompt_expansion_mode` | Quanto sforzo viene impiegato per riscrivere il prompt prima della generazione. Predefinito: balanced. | COMBO | Sì | "balanced"<br>"quality" |

**Note sui vincoli:**

- Il prompt deve contenere testo: i prompt vuoti o composti solo da spazi bianchi vengono rifiutati.
- Qualsiasi immagine di frame fornita deve essere larga almeno 256 pixel e alta almeno 256 pixel, con un rapporto d'aspetto larghezza-altezza compreso tra 0,4 e 2,5 (approssimativamente da 2:5 a 5:2). Questo requisito si applica a `first_frame` e, quando fornita, a `last_frame`.
- Quando `last_frame` è omesso, il video viene generato solo dal primo frame.
- Il video in output segue il rapporto d'aspetto delle immagini fornite.
- `watermark` è supportato solo da `MiniMax H3`. Abilitarlo con `MiniMax H3 Max` o `MiniMax H3 Max Turbo` genera un errore.
- La durata va da 4 a 15 secondi per `MiniMax H3` e da 5 a 15 secondi per `MiniMax H3 Max` e `MiniMax H3 Max Turbo`.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `video` | Il video generato creato dal primo frame e dall'ultimo frame opzionale usando il modello MiniMax H3 selezionato. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03FirstLastFrameNode/it.md)

---
**Source fingerprint (SHA-256):** `6eaf895e6e9e46b9a1efb1dd13e951040e12e865cc73d7741ab7546f5f8f9ec0`
