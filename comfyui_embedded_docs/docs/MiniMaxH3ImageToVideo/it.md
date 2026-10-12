# MiniMaxH3ImageToVideo

Questo nodo prepara il condizionamento e il latente vuoto necessari per generare un video con il modello MiniMax H3. Riceve un prompt testuale e, facoltativamente, immagini per il primo e/o l'ultimo fotogramma del video, e le converte in input per il modello. Le immagini keyframe vengono ridimensionate, codificate e associate al condizionamento all'inizio e alla fine del video.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `clip` | Modello CLIP utilizzato per tokenizzare il prompt e codificare le immagini keyframe nel condizionamento. | CLIP | Sì |  |
| `vae` | Modello VAE utilizzato per codificare le immagini keyframe nello spazio latente quando vengono fornite immagini keyframe. | VAE | Sì |  |
| `prompt` | Prompt testuale che descrive il video da generare. Supporta più righe e prompt dinamici. | STRING | Sì |  |
| `width` | Larghezza del video in pixel (predefinito: 1344). | INT | Sì | 32 to MAX_RESOLUTION (step 32) |
| `height` | Altezza del video in pixel (predefinito: 768). | INT | Sì | 32 to MAX_RESOLUTION (step 32) |
| `length` | Numero di fotogrammi a 24 fps, arrotondato per eccesso alla griglia 17k+5 del modello (124 = ~5s; l'intervallo addestrato è ~124-362, valori più lunghi non sono testati) (predefinito: 124). | INT | Sì | 5 to 3600 (step 17) |
| `first_frame` | Immagine facoltativa utilizzata come primo fotogramma del video. Viene estesa alle dimensioni complete della tela, quindi le sue proporzioni non vengono mantenute. Viene utilizzata solo la prima immagine del batch di input. | IMAGE | No |  |
| `last_frame` | Immagine facoltativa utilizzata come ultimo fotogramma del video. Viene ritagliata per coprire la tela mantenendo le sue proporzioni. Viene utilizzata solo la prima immagine del batch di input. | IMAGE | No |  |

Quando vengono forniti `first_frame` e/o `last_frame`, le immagini keyframe vengono codificate con il VAE e associate al condizionamento rispettivamente al fotogramma 0 e al fotogramma finale. Quando non viene fornito nessuno dei due, il nodo lavora solo dal prompt. Il valore `length` richiesto viene arrotondato per eccesso al numero di fotogrammi valido più vicino (17k + 5), quindi il numero effettivo di fotogrammi può essere leggermente superiore a quello richiesto.

Il latente audio-video viene creato come coppia vuota corrispondente a `width`, `height` richiesti e al numero di fotogrammi arrotondato. La porzione audio è dimensionata a partire dallo stesso numero di fotogrammi a 40 fotogrammi audio al secondo.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `positive` | Condizionamento contenente il prompt codificato e, quando vengono fornite immagini keyframe, i keyframe codificati e il numero di fotogrammi per il modello MiniMax H3. | CONDITIONING |
| `latent` | Latente audio-video vuoto che rappresenta il contenuto da generare, con larghezza, altezza e numero di fotogrammi richiesti. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ImageToVideo/it.md)

---
**Source fingerprint (SHA-256):** `d1bdf3f8c66ef20ff11c35203d2c266a88dcf8cc00c65dbb0aea2b1dd16befd6`
