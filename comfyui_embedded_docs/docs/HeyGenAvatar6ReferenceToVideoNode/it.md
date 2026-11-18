# HeyGen Avatar 6 Reference to Video

Con HeyGen Avatar 6, fai parlare una persona o un personaggio con l'audio che colleghi, usando una foto o un video come riferimento. Avatar 6 ricostruisce il volto e la scena da quel riferimento, così lo stesso audio può animare una foto statica, una clip esistente o entrambe.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Selettore del modello; selezionando un modello vengono mostrati i suoi input qui sotto. `"heygen-avatar-6-turbo"` è il livello più economico e veloce. | DYNAMIC_COMBO | Sì | `"heygen-avatar-6"`<br>`"heygen-avatar-6-turbo"` |

### Input di `heygen-avatar-6`

`"heygen-avatar-6-turbo"` espone gli stessi input con gli stessi limiti.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `image` | Foto facoltativa della persona o del personaggio da animare. Imposta l'aspetto e la scena e non viene usata come primo fotogramma. | IMAGE | No | Immagine singola |
| `video` | Video facoltativo di un personaggio animato o stilizzato che mostra come parla e si muove. I video più lunghi vengono tagliati ai primi 30 secondi. | VIDEO | No | 2 a 30 secondi |
| `audio` | Parlato per l'avatar. La durata del video segue l'audio. | AUDIO | Sì | 1.5 secondi a 10 minuti |
| `resolution` | Risoluzione del video di output. Predefinito: `"1080p"`. | COMBO | Sì | `"1080p"`<br>`"2k"` |
| `aspect_ratio` | Rapporto d'aspetto del video di output. `"auto"` mantiene la forma dell'immagine o, quando non è collegata alcuna immagine, quella del video; gli altri valori modificano l'inquadratura della scena. Predefinito: `"auto"`. | COMBO | Sì | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"1:1"`<br>`"4:5"`<br>`"5:4"` |
| `motion_prompt` | Indicazioni facoltative per gesti, espressione, postura e movimento della camera. Predefinito: stringa vuota. | STRING | Sì | Testo multiriga, fino a 1200 caratteri |
| `motion_expressiveness` | `"less"` produce meno gesti e di minore ampiezza. Il prompt del movimento ha la precedenza dove i due si sovrappongono. Predefinito: `"default"`. | COMBO | Sì | `"less"`<br>`"default"` |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici a prescindere dal seed. Predefinito: 42. | INT | Sì | 0 a 2147483647 |

**Vincoli e comportamento:**

* Collega un'immagine, un video o entrambi; se non ne è presente nessuno, il nodo genera un errore.
* L'input immagine deve contenere esattamente un'immagine, non un batch.
* I video di riferimento che ritraggono persone realistiche vengono rifiutati. Usa un video di un personaggio animato o stilizzato oppure collega una foto della persona.
* Un video di riferimento deve durare almeno 2 secondi e non superare i 50 MB.
* Il prezzo è calcolato al secondo di video di output e dipende dal modello e dalla risoluzione.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `video` | Il video parlante generato, scaricato da HeyGen al termine del rendering. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenAvatar6ReferenceToVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `1a50342827511e355a1d857c34e8bbfc0b74ca7b003dca783b76fcd151413ff8`
