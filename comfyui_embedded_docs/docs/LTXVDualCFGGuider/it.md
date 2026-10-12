# LTXV Dual CFG Guider

Questo nodo crea un oggetto di campionamento guidato (CFG guider) per i modelli LTXV-AV. Applica una scala di guida separata alla parte video e alla parte audio di un latent LTXV-AV packed, consentendoti di controllare l'influenza del condizionamento su ciascuna modalità in modo indipendente. Se le due scale sono uguali, o se il latent non contiene componenti video e audio separati, viene invece usata un'unica scala complessiva.

## Input

| Parametro | Descrizione | Tipo di dato | Richiesto | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Il modello da usare durante il campionamento. | MODEL | Sì | - |
| `positive` | Condizionamento positivo verso cui guidare la generazione. | CONDITIONING | Sì | - |
| `negative` | Condizionamento negativo da cui allontanare la generazione. | CONDITIONING | Sì | - |
| `video_cfg` | Intensità di guida applicata alla modalità video del latent (predefinito: 3.0). | FLOAT | Sì | 0.0 to 100.0 |
| `audio_cfg` | Intensità di guida applicata alla modalità audio del latent (predefinito: 7.0). | FLOAT | Sì | 0.0 to 100.0 |

Nota: quando `video_cfg` e `audio_cfg` sono uguali (o con valori molto vicini), il guider usa quel valore come un'unica scala CFG per l'intero latent. Se il latent non è un latent LTXV-AV packed, viene usato solo il valore di `video_cfg`.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `guider` | Il CFG guider configurato da passare a un nodo sampler. | GUIDER |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVDualCFGGuider/it.md)

---
**Source fingerprint (SHA-256):** `8b5ea32d0e73ab4f9b9f053ac7513d621fcc047e1ff468b6d0b5dd2aa3ff791a`
