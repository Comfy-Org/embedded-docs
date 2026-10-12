# Empty Ace Step 1.0 Latent Audio

Il nodo Empty Ace Step 1.0 Latent Audio crea campioni audio latenti vuoti per una durata scelta. Riempie un batch di latenti audio silenziosi (tutti zero), dove la lunghezza viene calcolata dall'input `seconds` usando i parametri di elaborazione audio. Viene tipicamente utilizzato per inizializzare flussi di lavoro audio che necessitano di una rappresentazione latente come punto di partenza.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `seconds` | La durata dell'audio in secondi (predefinito: 120.0, passo: 0.1) | FLOAT | Sì | 1.0 - 1000.0 |
| `batch_size` | Il numero di immagini latenti nel batch (predefinito: 1) | INT | Sì | 1 - 4096 |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `output` | Restituisce campioni audio latenti vuoti riempiti con zeri. L'output contiene un tensore `samples` e un campo `type` impostato su "audio". | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStepLatentAudio/it.md)

---
**Source fingerprint (SHA-256):** `8268eb582a28c7acc495c52831cc6edd8f8fdd1b294857451ce94abc37ca0d14`
