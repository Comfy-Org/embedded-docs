# LTXVImgToVideo

LTXVImgToVideo converte un'immagine di input in una rappresentazione latente video per modelli di generazione video. Ridimensiona l'immagine alla larghezza e all'altezza richieste, la codifica con il VAE e colloca i frame codificati all'inizio di un latente di dimensione video composto da zeri. Il controllo strength determina quanto contenuto dell'immagine originale viene preservato rispetto a quanto viene modificato durante la generazione del video.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `positive` | Prompt di condizionamento positivo per guidare la generazione del video | CONDITIONING | Sì | - |
| `negative` | Prompt di condizionamento negativo per evitare determinati elementi nel video | CONDITIONING | Sì | - |
| `vae` | Modello VAE utilizzato per codificare l'immagine di input nello spazio latente | VAE | Sì | - |
| `image` | Immagine di input da convertire in frame video | IMAGE | Sì | - |
| `width` | Larghezza del video di output in pixel (predefinito: 768, passo: 32) | INT | Sì | 64 to MAX_RESOLUTION |
| `height` | Altezza del video di output in pixel (predefinito: 512, passo: 32) | INT | Sì | 64 to MAX_RESOLUTION |
| `length` | Numero di frame nel video generato (predefinito: 97, passo: 8) | INT | Sì | 9 to MAX_RESOLUTION |
| `batch_size` | Numero di video da generare simultaneamente (predefinito: 1) | INT | Sì | 1 to 4096 |
| `strength` | Controllo su quanto contenuto dell'immagine originale viene preservato nei primi frame del video generato. Un valore di 1.0 preserva completamente l'immagine originale, mentre 0.0 consente la massima modifica (predefinito: 1.0) | FLOAT | Sì | 0.0 to 1.0 |

Nota: `width` e `height` cambiano con incrementi di 32 pixel, e `length` cambia con incrementi di 8 frame, in base alla compressione del latente video (32x nelle dimensioni spaziali e 8x nella dimensione temporale). Il latente video contiene ((length - 1) // 8) + 1 frame. L'immagine di input viene ridimensionata a `width` x `height` utilizzando un ridimensionamento bilineare con ritaglio centrale, e solo i primi tre canali vengono utilizzati per la codifica.

## Output

| Nome dell'output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `positive` | Il condizionamento positivo passato invariato per l'uso con il latente generato | CONDITIONING |
| `negative` | Il condizionamento negativo passato invariato per l'uso con il latente generato | CONDITIONING |
| `latent` | Rappresentazione latente video contenente i frame immagine codificati e una maschera di rumore che controlla con quanta forza il condizionamento viene applicato durante la generazione del video | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVImgToVideo/it.md)

---
**Source fingerprint (SHA-256):** `4ebc7f80b4d9ac3329e3349c7048885de22b827b5bdd102976687afd7e07a16b`
