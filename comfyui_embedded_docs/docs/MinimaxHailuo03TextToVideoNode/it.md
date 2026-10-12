# MiniMax H3 Testo a Video

Questo nodo genera un video da un prompt testuale utilizzando la famiglia di modelli MiniMax H3: MiniMax H3, MiniMax H3 Max e MiniMax H3 Max Turbo. Selezioni il modello, inserisci un prompt testuale e regoli impostazioni come risoluzione, proporzioni e durata. Il nodo invia la richiesta all'API MiniMax, attende il completamento dell'attività di generazione e restituisce il video risultante.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Richiesto | Intervallo |
|-----------|-------------|--------------|-----------|------------|
| `model` | Modello da utilizzare per la generazione video (predefinito: "MiniMax H3"). Selezionando un modello vengono mostrate anche le impostazioni specifiche del modello descritte nelle sezioni seguenti. | DYNAMIC_COMBO | Sì | "MiniMax H3"<br>"MiniMax H3 Max"<br>"MiniMax H3 Max Turbo" |
| `seed` | Seme casuale. La stessa richiesta con lo stesso seme produce risultati simili, ma non garantiti identici (predefinito: 42). | INT | Sì | da 0 a 4294967295 |
| `watermark` | Indica se aggiungere una filigrana AIGC al video (predefinito: false). Quando abilitato, è supportato solo il modello "MiniMax H3". | BOOLEAN | No | true<br>false |

### Input di MiniMax H3

Queste impostazioni vengono visualizzate quando è selezionato il modello "MiniMax H3".

| Parametro | Descrizione | Tipo di dato | Richiesto | Intervallo |
|-----------|-------------|--------------|-----------|------------|
| `prompt` | Prompt testuale per la generazione video. Deve contenere almeno un carattere non di spaziatura. | STRING | Sì | Qualsiasi testo |
| `resolution` | Risoluzione del video di output. | COMBO | Sì | "768P"<br>"2K" |
| `ratio` | Proporzioni del video di output (predefinito: "16:9"). | COMBO | Sì | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | Durata del video di output in secondi (4-15) (predefinito: 5). | INT | Sì | da 4 a 15 |

### Input di MiniMax H3 Max e MiniMax H3 Max Turbo

Queste impostazioni sono condivise dai modelli "MiniMax H3 Max" e "MiniMax H3 Max Turbo" e vengono visualizzate quando viene selezionato uno dei due modelli.

| Parametro | Descrizione | Tipo di dato | Richiesto | Intervallo |
|-----------|-------------|--------------|-----------|------------|
| `prompt` | Prompt testuale per la generazione video. Deve contenere almeno un carattere non di spaziatura e può essere lungo fino a 50.000 caratteri. | STRING | Sì | Fino a 50000 caratteri |
| `resolution` | Risoluzione del video di output (predefinito: "768P"). | COMBO | Sì | "480P"<br>"768P" |
| `ratio` | Proporzioni del video di output (predefinito: "16:9"). | COMBO | Sì | "16:9"<br>"4:3"<br>"1:1"<br>"3:4"<br>"9:16"<br>"21:9" |
| `duration` | Durata del video di output in secondi (5-15) (predefinito: 5). | INT | Sì | da 5 a 15 |
| `prompt_expansion_mode` | Quanto sforzo viene impiegato per riscrivere il prompt prima della generazione (predefinito: "balanced"). | COMBO | Sì | "balanced"<br>"quality" |

### Note

- Per tutti i modelli, il prompt deve contenere almeno un carattere non di spaziatura.
- L'impostazione `watermark` è supportata solo da "MiniMax H3". Abilitarla con "MiniMax H3 Max" o "MiniMax H3 Max Turbo" causa un errore.
- I modelli "MiniMax H3 Max" e "MiniMax H3 Max Turbo" limitano il prompt a 50.000 caratteri.
- I limiti di risoluzione e durata dipendono dal modello selezionato: "MiniMax H3" supporta risoluzioni "768P" e "2K" e video da 4-15 secondi, mentre "MiniMax H3 Max" e "MiniMax H3 Max Turbo" supportano risoluzioni "480P" e "768P" e video da 5-15 secondi.
- Il prezzo stimato mostrato per questo nodo viene calcolato dal modello, dalla risoluzione e dalla durata selezionati.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `VIDEO` | Il video generato creato dal prompt testuale fornito. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03TextToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `4d3de190d18de4370aff878279755e881841d2ada28320a7c1d7c52061071c05`
