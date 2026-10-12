# HunyuanRefinerLatent

Il nodo HunyuanRefinerLatent prepara i dati di condizionamento e latenti per il processo di raffinamento video Hunyuan. Collega i dati dell'immagine latente di input sia al condizionamento positivo sia a quello negativo, applica loro un valore di aumento del rumore e crea un nuovo latente riempito di zeri con 32 canali per ulteriori elaborazioni.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `positive` | L'input di condizionamento positivo da elaborare | CONDITIONING | Sì | - |
| `negative` | L'input di condizionamento negativo da elaborare | CONDITIONING | Sì | - |
| `latent` | L'input di rappresentazione latente, utilizzato come dati dell'immagine latente per il condizionamento e per definire le dimensioni del latente di output | LATENT | Sì | - |
| `noise_augmentation` | La quantità di aumento del rumore da applicare (predefinito: 0.10). Questo parametro è mostrato nella sezione avanzata del nodo. | FLOAT | Sì | 0.0 - 1.0 |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `positive` | Il condizionamento positivo elaborato, con i dati dell'immagine latente collegati e l'aumento del rumore applicato | CONDITIONING |
| `negative` | Il condizionamento negativo elaborato, con i dati dell'immagine latente collegati e l'aumento del rumore applicato | CONDITIONING |
| `latent` | Un nuovo latente riempito di zeri, con la stessa dimensione del batch e le stesse ultime tre dimensioni del latente di input, e 32 canali | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanRefinerLatent/it.md)

---
**Source fingerprint (SHA-256):** `4c5669cf2ad5ba00e176876741b7d8d3f092cc58d2163871a10fd769ee4ff84c`
