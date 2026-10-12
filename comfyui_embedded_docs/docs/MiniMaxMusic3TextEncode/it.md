# Codifica testo MiniMax Music3

MiniMax Music3 Text Encode utilizza un modello CLIP MiniMax Music3 per convertire didascalie testuali e testi cantati in una sequenza di condizionamento acustico per la generazione musicale. Il nodo restituisce i dati CONDITIONING risultanti, insieme alla durata audio effettiva in secondi calcolata dalla durata massima di input.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `clip` | Il modello CLIP MiniMax Music3, usato per la codifica del testo e la generazione della sequenza di condizionamento. | CLIP | Sì | - |
| `caption` | Testo che descrive la musica da generare. Supporta testo multiriga e prompt dinamici. | STRING | Sì | - |
| `lyrics` | Il testo cantato da usare per generare la musica. Supporta testo multiriga e prompt dinamici. | STRING | Sì | - |
| `seed` | Seme casuale riproducibile per il processo di generazione. Predefinito: 0. È fornito un widget di controllo dopo la generazione. | INT | Sì | 0 to 18446744073709551615 (0xffffffffffffffff) |
| `max_duration` | Durata massima in secondi; il modello può terminare il brano prima. Predefinito: 120.0. | FLOAT | Sì | 0.04 alla durata audio massima del modello (MAX_AUDIO_FRAMES / AUDIO_FRAMES_PER_SECOND), passo 0.04 |
| `cfg_scale` | Scala di guida classifier-free. Predefinito: costante del modello CFG_SCALE. Parametro avanzato. | FLOAT | Sì | 0.0 to 100.0, passo 0.1 (mantiene 2 cifre decimali) |
| `top_k` | Valore di campionamento top-k usato per la selezione dei token acustici. Predefinito: costante del modello CFG_TOP_K. Parametro avanzato. | INT | Sì | 1 alla dimensione del vocabolario del modello (C0_VOCAB_SIZE) |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `conditioning` | La sequenza di condizionamento acustico generata, usata per guidare la successiva generazione musicale. | CONDITIONING |
| `seconds` | La durata effettiva della sequenza di condizionamento, in secondi. | FLOAT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxMusic3TextEncode/it.md)

---
**Source fingerprint (SHA-256):** `c3fbfd189d0358ebf081dd4f9c32be9231a9d0b97fd767401ea4b7955224c25c`
