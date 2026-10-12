# HunyuanVideo15SuperResolution

Il nodo HunyuanVideo15SuperResolution prepara i dati di condizionamento per un processo di super-risoluzione video. Prende una rappresentazione latente di un video e, facoltativamente, un'immagine iniziale, e li assembla insieme ai dati di aumento del rumore e ai dati CLIP vision in un formato che può essere utilizzato da un modello per generare un output a risoluzione più elevata.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `positive` | L'input di condizionamento positivo da modificare con i dati latenti e di aumento. | CONDITIONING | Sì | N/A |
| `negative` | L'input di condizionamento negativo da modificare con i dati latenti e di aumento. | CONDITIONING | Sì | N/A |
| `vae` | Il VAE utilizzato per codificare la `start_image` opzionale. Obbligatorio se viene fornita `start_image`. | VAE | No | N/A |
| `start_image` | Un'immagine iniziale opzionale per guidare la super-risoluzione. Se fornita, viene sottoposta a upscale e codificata nel latente di condizionamento. | IMAGE | No | N/A |
| `clip_vision_output` | Embedding CLIP vision opzionali da aggiungere al condizionamento. | CLIP_VISION_OUTPUT | No | N/A |
| `latent` | La rappresentazione latente video di input che viene incorporata nel condizionamento. | LATENT | Sì | N/A |
| `noise_augmentation` | La forza dell'aumento del rumore da applicare al condizionamento (predefinito: 0.70). Questo è un parametro avanzato; un valore viene sempre fornito dall'impostazione predefinita. | FLOAT | Sì | 0.0 - 1.0 (step 0.01) |

**Nota:** Se fornisci una `start_image`, devi anche collegare una `vae` in modo che possa essere codificata. La `start_image` viene automaticamente sottoposta a upscale a 16 volte le dimensioni spaziali (larghezza e altezza) del `latent` di input, quindi codificata e inserita nel latente di condizionamento. Solo i canali RGB della `start_image` vengono utilizzati per la codifica.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `positive` | Il condizionamento positivo modificato, che ora contiene il latente concatenato, l'aumento del rumore e i dati CLIP vision opzionali. | CONDITIONING |
| `negative` | Il condizionamento negativo modificato, che ora contiene il latente concatenato, l'aumento del rumore e i dati CLIP vision opzionali. | CONDITIONING |
| `latent` | Il `latent` di input viene passato invariato. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanVideo15SuperResolution/it.md)

---
**Source fingerprint (SHA-256):** `c9e64092e78423f5e0dc43446a77240e09100242c25e4fccc91491049fe76be5`
