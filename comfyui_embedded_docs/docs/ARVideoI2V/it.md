# ARVideoI2V

Questo nodo prepara una configurazione di generazione image-to-video per modelli video AR (Auto-Regressivi) che utilizzano Causal Forcing o Self-Forcing. Codifica un'immagine iniziale nello spazio latente con un VAE e la memorizza nelle opzioni del transformer del modello, così il processo di campionamento video può inizializzare la cache KV prima del denoising. Utilizza lo stesso checkpoint del modello text-to-video, quindi non è necessaria un'architettura image-to-video separata.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello video AR da utilizzare per la generazione. | MODEL | Sì | - |
| `vae` | Il modello VAE utilizzato per codificare l'immagine iniziale nello spazio latente. | VAE | Sì | - |
| `start_image` | L'immagine iniziale che servirà come primo frame del video generato. Viene utilizzata solo la prima immagine del batch di input e vengono codificati solo i suoi canali RGB. | IMAGE | Sì | - |
| `width` | La larghezza dei frame del video generato (predefinito: 832). | INT | Sì | da 16 a 8192 (passo: 16) |
| `height` | L'altezza dei frame del video generato (predefinito: 480). | INT | Sì | da 16 a 8192 (passo: 16) |
| `length` | Il numero totale di frame del video generato (predefinito: 81). | INT | Sì | da 1 a 1024 (passo: 4) |
| `batch_size` | Il numero di sequenze video da generare in un singolo batch (predefinito: 1). | INT | Sì | da 1 a 64 |

Nota: L'immagine iniziale viene ridimensionata ai valori specificati di `width` e `height` prima di essere codificata. La dimensione temporale latente è calcolata come `((length - 1) // 4) + 1`, mentre le dimensioni spaziali latenti sono `height / 8` e `width / 8`.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `MODEL` | Il modello clonato con l'immagine iniziale codificata memorizzata nelle sue opzioni del transformer (`ar_config.initial_latent`), che il campionatore utilizza per inizializzare la cache KV prima del denoising. | MODEL |
| `LATENT` | Un tensore latente riempito di zeri con forma `[batch_size, 16, lat_t, height // 8, width // 8]`, dove `lat_t = ((length - 1) // 4) + 1`. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ARVideoI2V/it.md)

---
**Source fingerprint (SHA-256):** `984834951b9d5a22aef51c85a5019fd8ba58cdb2d6fff235371ed29f316896d8`
