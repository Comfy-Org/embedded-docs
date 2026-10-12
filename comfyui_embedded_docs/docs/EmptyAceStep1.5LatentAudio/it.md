# EmptyAceStep1.5LatentAudio

Il nodo Empty Ace Step 1.5 Latent Audio crea un tensore latente audio vuoto (silenzioso) per i flussi di lavoro di generazione audio. Costruisce un latente con 64 canali la cui lunghezza temporale è calcolata dalla durata richiesta e lo contrassegna come dati audio per l'uso da parte dei nodi audio a valle.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `seconds` | La durata dell'audio da generare, in secondi (predefinito: 120.0). La lunghezza del latente viene calcolata come `seconds * 48000 / 1920`, arrotondata al numero intero più vicino. | FLOAT | Sì | 1.0 - 1000.0 (passo: 0.01) |
| `batch_size` | Il numero di immagini latenti nel batch (predefinito: 1). | INT | Sì | 1 - 4096 |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `LATENT` | Un tensore latente vuoto che rappresenta audio silenzioso. Il tensore ha forma [batch_size, 64, length], dove length è derivato da `seconds`. L'output include anche un identificatore di tipo "audio" e un valore `downscale_ratio_temporal` di 1764, utilizzato per il downscaling temporale nell'elaborazione audio. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStep1.5LatentAudio/it.md)

---
**Source fingerprint (SHA-256):** `bb7120c91ce5d779147cb8553d6f96fa160d87468d4d87550fb6dd4ec89b1557`
