# PixVerse V6 Fusione (Riferimento a video)

PixVerse V6 Fusion (Reference to Video) compone un video a partire da soggetti, sfondi e video di riferimento con PixVerse. Colloca un riferimento nella scena nominandolo nel prompt, ad esempio '@Subject1 cammina attraverso @Background1'. Il collegamento di un video di riferimento commuta il modello in modalità Omni, in cui la durata dell'output corrisponde al video di riferimento più lungo.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Impostazioni del modello e della generazione. Seleziona il modello e mostra di seguito le relative impostazioni di generazione. L'unica opzione disponibile è "PixVerse V6". | DYNAMIC_COMBO | Sì | "PixVerse V6" |

### Input di PixVerse V6

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt per la generazione del video. Fai riferimento ai riferimenti collegati come @Subject1, @Background1, @Video1. Predefinito: vuoto. | STRING | Sì | Da 1 a 5000 caratteri |
| `aspect_ratio` | Rapporto d'aspetto dell'output. L'opzione "auto" è consentita solo quando è collegato almeno un video di riferimento. | COMBO | Sì | "auto"<br>più i rapporti d'aspetto predefiniti di PixVerse V6 |
| `quality` | Risoluzione dell'output. Imposta il lato lungo: 360p è 640px, 540p 1024px, 720p 1280px, 1080p 1920px. Predefinito: "720p". | COMBO | Sì | "360p"<br>"540p"<br>"720p"<br>"1080p" |
| `duration_seconds` | Durata del video generato in secondi. Quando sono collegati video di riferimento, la durata dell'output segue invece il video di riferimento più lungo e questa impostazione viene ignorata. Predefinito: 5. | INT | Sì | Da 1 a 15 |
| `generate_audio` | Genera una traccia audio nativa insieme al video. Predefinito: True. | BOOLEAN | Sì | True<br>False |
| `seed` | Seed per la generazione del video. PixVerse lo registra ma non riproduce un'esecuzione a partire da esso. Predefinito: 42. | INT | Sì | Da 0 a 2147483647 |
| `negative_prompt` | Descrizione testuale opzionale degli elementi indesiderati nel video. Predefinito: vuoto. | STRING | No | Fino a 2048 caratteri |
| `style` | Stile visivo opzionale applicato all'intero video. Predefinito: "none". | COMBO | No | "none"<br>più gli stili predefiniti di PixVerse V6 |

### Input di riferimento

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `subjects` | Slot espandibile: collega immagini di riferimento dei soggetti da collocare nella scena. Gli slot sono denominati subject1 fino a subject8; fai riferimento a essi nel prompt come @Subject1, @Subject2 e così via. | IMAGE | No | Da 0 a 8 immagini |
| `backgrounds` | Slot espandibile: collega immagini di riferimento della scena in cui vengono collocati i soggetti. Gli slot sono denominati background1 fino a background2; fai riferimento a essi nel prompt come @Background1, @Background2. | IMAGE | No | Da 0 a 2 immagini |
| `videos` | Slot espandibile: collega video di riferimento da cui prendere in prestito soggetti, movimento, inquadratura o stile. Gli slot sono denominati video1 fino a video2; fai riferimento a essi nel prompt come @Video1, @Video2. Ogni video deve durare al massimo 15 secondi e la durata totale non deve superare i 15 secondi. Collegando almeno un video il nodo passa alla modalità Omni. | VIDEO | No | Da 0 a 2 video<br>Massimo 15 secondi ciascuno<br>15 secondi in totale |

Nota: collega almeno un soggetto, uno sfondo o un video di riferimento. I tag di riferimento nel prompt (ad esempio @Subject1, @Background1, @Video1) devono corrispondere agli slot collegati, altrimenti la richiesta viene rifiutata. Quando è collegato almeno un video di riferimento (modalità Omni), la durata dell'output corrisponde al video di riferimento più lungo, `duration_seconds` viene ignorato, `aspect_ratio` può essere impostato su "auto" e sono accettate fino a 10 immagini di riferimento. Senza un video di riferimento, sono accettate al massimo 7 immagini di riferimento (soggetti e sfondi combinati) e il rapporto d'aspetto "auto" non è consentito.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `video` | Il video fusion generato, scaricato da PixVerse. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6FusionVideoNode/it.md)

---
**Source fingerprint (SHA-256):** `a83ef07f6f1918921e93fa67c2eca351754794f629aa216ccff21ce80901aebd`
