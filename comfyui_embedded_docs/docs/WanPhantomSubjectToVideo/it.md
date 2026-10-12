# WanPhantomSubjectToVideo

Il nodo WanPhantomSubjectToVideo prepara i dati di condizionamento e un latente per la generazione video Wan. Crea un video latente vuoto dalla larghezza, altezza, lunghezza e dimensione batch richieste e, quando vengono fornite immagini di riferimento, le codifica con il VAE e le aggiunge ai condizionamenti come guida visiva lungo la dimensione temporale.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `positive` | Input di condizionamento positivo per guidare la generazione video | CONDITIONING | Sì | - |
| `negative` | Input di condizionamento negativo per evitare determinate caratteristiche | CONDITIONING | Sì | - |
| `vae` | Modello VAE utilizzato per codificare le immagini di riferimento quando vengono fornite | VAE | Sì | - |
| `width` | Larghezza del video di output in pixel (predefinito: 832) | INT | Sì | 16 a MAX_RESOLUTION (passo 16) |
| `height` | Altezza del video di output in pixel (predefinito: 480) | INT | Sì | 16 a MAX_RESOLUTION (passo 16) |
| `length` | Numero di fotogrammi nel video generato (predefinito: 81) | INT | Sì | 1 a MAX_RESOLUTION (passo 4) |
| `batch_size` | Numero di video da generare simultaneamente (predefinito: 1) | INT | Sì | 1 a 4096 |
| `images` | Immagini di riferimento opzionali usate come guida visiva lungo la dimensione temporale | IMAGE | No | - |

**Nota:** Quando vengono fornite le `images`, vengono automaticamente sottoposte a upscale per corrispondere alla `width` e alla `height` specificate, e per l'elaborazione vengono usate solo le prime `length` immagini. Ogni immagine viene codificata con il `vae` e concatenata lungo la dimensione temporale, e di ciascuna immagine vengono usati solo i canali RGB. Quando le `images` non vengono fornite, tutti e tre gli output di condizionamento vengono restituiti invariati dai condizionamenti di input.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `positive` | Condizionamento positivo con concatenazione lungo la dimensione temporale delle immagini di riferimento codificate quando le immagini sono fornite; altrimenti viene restituito invariato l'input `positive` | CONDITIONING |
| `negative_text` | Condizionamento negativo con concatenazione lungo la dimensione temporale delle immagini di riferimento codificate quando le immagini sono fornite; altrimenti viene restituito invariato l'input `negative` | CONDITIONING |
| `negative_img_text` | Condizionamento negativo con una concatenazione lungo la dimensione temporale azzerata quando le immagini sono fornite; altrimenti viene restituito invariato l'input `negative` | CONDITIONING |
| `latent` | Tensore latente video riempito di zeri con 16 canali; il suo numero di fotogrammi deriva da `length` e le sue dimensioni spaziali da `height` e `width` | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanPhantomSubjectToVideo/it.md)

---
**Source fingerprint (SHA-256):** `a1853382f6e564f66262b69dd7b06cc58e26b93386a460a98e6fcc2ff6acf12b`
