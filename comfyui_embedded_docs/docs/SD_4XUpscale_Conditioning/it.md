# SD_4XUpscale_Conditioning

Il nodo SD_4XUpscale_Conditioning prepara i dati di condizionamento per l'upscaling delle immagini con modelli di diffusione. Ridimensiona le immagini di input in base a un rapporto scelto, aggiunge un'eventuale augmentazione del rumore e restituisce i condizionamenti positivo e negativo modificati insieme a un latent vuoto per la dimensione upscalata.

## Input
| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `images` | Immagini di input da upscalare. | IMAGE | Sì | - |
| `positive` | Dati di condizionamento positivo che guidano la generazione verso il contenuto desiderato. | CONDITIONING | Sì | - |
| `negative` | Dati di condizionamento negativo che allontanano la generazione dal contenuto indesiderato. | CONDITIONING | Sì | - |
| `scale_ratio` | Moltiplicatore applicato alle dimensioni delle immagini di input durante la preparazione del condizionamento e del latent upscalati (predefinito: 4.0). | FLOAT | Sì | 0.0 - 10.0 (step 0.01) |
| `noise_augmentation` | Quantità di rumore da aggiungere durante il processo di upscaling (predefinito: 0.0). | FLOAT | Sì | 0.0 - 1.0 (step 0.001) |

Nota: `noise_augmentation` è un parametro avanzato, mostrato nell'interfaccia del nodo sotto l'interruttore "Avanzate".

## Output
| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `positive` | Condizionamento positivo modificato con i dati dell'immagine scalata e le impostazioni di augmentazione del rumore applicate. | CONDITIONING |
| `negative` | Condizionamento negativo modificato con i dati dell'immagine scalata e le impostazioni di augmentazione del rumore applicate. | CONDITIONING |
| `latent` | Rappresentazione latent vuota corrispondente alle dimensioni upscalate. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SD_4XUpscale_Conditioning/it.md)

---
**Source fingerprint (SHA-256):** `f215e890bd86f42d4da9c6f575fc92e65844e2e2056c5610310d8089e5d61902`
