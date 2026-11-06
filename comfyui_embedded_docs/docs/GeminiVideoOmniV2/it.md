# Google Gemini Omni (Video)

Google Gemini Omni (Video) genera un video con audio da un prompt testuale utilizzando i modelli Gemini Omni Flash di Google. È possibile allegare facoltativamente immagini e/o video di riferimento per guidare il risultato o modificare filmati esistenti. Descrivi la durata desiderata direttamente nel prompt: da 3 a 10 secondi per Omni Flash e Omni Flash 1.1, da 3 a 15 secondi per Omni Flash 1.2.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello video Gemini utilizzato per generare il video. | DYNAMIC_COMBO | Sì | "Omni Flash 1.2"<br>"Omni Flash 1.1"<br>"Omni Flash" |

### Input di Omni Flash 1.2

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Descrivi il video da generare o la modifica da applicare a un video allegato. Specifica la lunghezza direttamente nel prompt, ad es. "una clip di 6 secondi" oppure, per l'operazione 'extend', "estendi di 5 secondi"; la lunghezza generata può essere da 3 a 15 secondi, e 'extend' aggiunge al massimo 10 secondi. L'output include audio. (predefinito: "") | STRING | Sì | - |
| `resolution` | Risoluzione dell'output. (predefinito: "720p") | COMBO | Sì | "360p"<br>"720p"<br>"1080p"<br>"4k" |
| `aspect_ratio` | Rapporto d'aspetto dell'output: 16:9 (orizzontale) o 9:16 (verticale). Le operazioni 'edit' e 'extend' mantengono invece il rapporto d'aspetto del video di input. (predefinito: "16:9") | COMBO | Sì | "16:9"<br>"9:16" |
| `task_type` | Cosa fare con il prompt e i media allegati. Con 'auto' decide il modello. 'text_to_video' genera solo dal prompt e rifiuta i media allegati. 'image_to_video' anima un'immagine oppure interpola da un fotogramma iniziale a un fotogramma finale quando ne vengono allegate due. 'reference_to_video' tratta i media allegati come riferimenti di soggetto. 'edit' riscrive esattamente un video allegato, mentre 'extend' vi aggiunge nuovo materiale video, così l'output inizia con il video di input. (predefinito: "auto") | COMBO | Sì | "auto"<br>"text_to_video"<br>"image_to_video"<br>"reference_to_video"<br>"edit"<br>"extend" |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. (predefinito: 42) | INT | Sì | 0 a 2147483647 |

### Input di Omni Flash 1.1

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Descrivi il video da generare o la modifica da applicare a un video allegato. Specifica la lunghezza direttamente nel prompt, ad es. "una clip di 6 secondi" oppure, per l'operazione 'extend', "estendi di 5 secondi"; la lunghezza generata può essere da 3 a 10 secondi e il valore predefinito è 10. L'output include audio. (predefinito: "") | STRING | Sì | - |
| `resolution` | Risoluzione dell'output. (predefinito: "720p") | COMBO | Sì | "360p"<br>"720p"<br>"1080p"<br>"4k" |
| `aspect_ratio` | Rapporto d'aspetto dell'output: 16:9 (orizzontale) o 9:16 (verticale). Le operazioni 'edit' e 'extend' mantengono invece il rapporto d'aspetto del video di input. (predefinito: "16:9") | COMBO | Sì | "16:9"<br>"9:16" |
| `task_type` | Cosa fare con il prompt e i media allegati. Con 'auto' decide il modello. 'text_to_video' genera solo dal prompt e rifiuta i media allegati. 'image_to_video' anima un'immagine oppure interpola da un fotogramma iniziale a un fotogramma finale quando ne vengono allegate due. 'reference_to_video' tratta i media allegati come riferimenti di soggetto. 'edit' riscrive esattamente un video allegato, mentre 'extend' vi aggiunge nuovo materiale video, così l'output inizia con il video di input. (predefinito: "auto") | COMBO | Sì | "auto"<br>"text_to_video"<br>"image_to_video"<br>"reference_to_video"<br>"edit"<br>"extend" |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. (predefinito: 42) | INT | Sì | 0 a 2147483647 |

### Input di Omni Flash

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Descrivi il video da generare o la modifica da applicare a un video allegato. Specifica la lunghezza direttamente nel prompt, ad es. "una clip di 6 secondi"; la lunghezza può essere da 3 a 10 secondi. L'output è 720p, 24 FPS, con audio. (predefinito: "") | STRING | Sì | - |
| `aspect_ratio` | Rapporto d'aspetto dell'output: 16:9 (orizzontale) o 9:16 (verticale). L'operazione 'edit' mantiene invece il rapporto d'aspetto del video di input. (predefinito: "16:9") | COMBO | Sì | "16:9"<br>"9:16" |
| `task_type` | Cosa fare con il prompt e i media allegati. Con 'auto' decide il modello. 'text_to_video' genera solo dal prompt e rifiuta i media allegati. 'image_to_video' anima un'immagine oppure interpola da un fotogramma iniziale a un fotogramma finale quando ne vengono allegate due. 'reference_to_video' tratta i media allegati come riferimenti di soggetto. 'edit' riscrive esattamente un video allegato. (predefinito: "auto") | COMBO | Sì | "auto"<br>"text_to_video"<br>"image_to_video"<br>"reference_to_video"<br>"edit" |
| `temperature` | Controlla la casualità. Valori più bassi sono più focalizzati/deterministici, valori più alti sono più vari. (predefinito: 1.0) | FLOAT | Sì | 0.0 a 2.0 (passo 0.01) |
| `top_p` | Campionamento nucleus: campiona dal più piccolo insieme di token la cui probabilità cumulativa raggiunge top_p. (predefinito: 0.95) | FLOAT | Sì | 0.0 a 1.0 (passo 0.01) |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. (predefinito: 42) | INT | Sì | 0 a 2147483647 |

### Input di riferimento

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `images` | Slot espandibile: collega fino a 14 immagini (`image_1`...`image_14`). Immagini di riferimento facoltative per guidare o animare il video. Con l'operazione 'image_to_video' la prima è il fotogramma iniziale e un'eventuale seconda è il fotogramma finale. | IMAGE | No | 0 a 14 immagini |
| `videos` | Slot espandibile: collega fino a 3 video (`video_1`...`video_3`). Video di riferimento facoltativi per guidare o modificare. Ciascuno lungo fino a 10 secondi. | VIDEO | No | 0 a 3 video |

**Note:**
- Il `prompt` non deve essere vuoto; il nodo genera un errore se lo è.
- L'operazione `text_to_video` genera solo dal prompt: allegare immagini o video genera un errore.
- L'operazione `image_to_video` accetta solo immagini (nessun video) e richiede esattamente 1 o 2 immagini: la prima è il fotogramma iniziale e la seconda facoltativa è il fotogramma finale.
- L'operazione `edit` (tutti i modelli) e l'operazione `extend` (solo Omni Flash 1.1 e 1.2) richiedono esattamente un video di input e mantengono il rapporto d'aspetto di quel video di input, sovrascrivendo `aspect_ratio`.
- È possibile allegare al massimo 14 immagini e 3 video. Ogni video allegato deve durare al massimo 10 secondi, 15 secondi con Omni Flash 1.2 e 25 secondi per l'operazione `extend`, il cui risultato può durare al massimo 30 secondi.
- Omni Flash restituisce sempre un video 720p a 24 FPS con audio; la selezione della risoluzione è disponibile solo con Omni Flash 1.1 e 1.2.
- I controlli `temperature` e `top_p` sono disponibili solo con il modello Omni Flash; Omni Flash 1.1 utilizza impostazioni di generazione fisse.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `video` (primo output) | Il video generato con audio. Per Omni Flash: 720p, 24 FPS. Per Omni Flash 1.1 e 1.2: la risoluzione selezionata nell'input `resolution`. | VIDEO |
| `text` (secondo output) | Il contenuto testuale generato dal modello insieme al video (può essere vuoto). | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiVideoOmniV2/it.md)

---
**Source fingerprint (SHA-256):** `1fc6017d4d6fbce8f04b2f0ded496553074b8498e3b7342179550fc768698897`
