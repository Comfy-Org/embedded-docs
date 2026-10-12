# EmptyYuE2LatentAudio

Questo nodo crea un latente audio vuoto per YuE2, dimensionato su una durata e un numero di batch scelti. Produce dati audio segnaposto silenziosi che i nodi successivi possono riempire durante la generazione audio.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `seconds` | Lunghezza del latente audio da creare, in secondi (predefinito: 120.0). Il numero di frame latenti viene calcolato da questo valore, con un minimo di 1 frame. | FLOAT | Sì | 0.04 a 1000.0 (passo 0.04) |
| `batch_size` | Numero di latenti audio da creare in un batch (predefinito: 1). | INT | Sì | 1 a 4096 |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `LATENT` | Un latente audio vuoto contenente un tensore di zeri, dimensionato in base a `batch_size` e al numero di frame derivato da `seconds`. È contrassegnato come tipo audio con un rapporto di ridimensionamento temporale di 1920. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyYuE2LatentAudio/it.md)

---
**Source fingerprint (SHA-256):** `3397e3feb534c87d9790bbfe36e8e641476d9b6aa00d75a4e6d0c32f4a948563`
