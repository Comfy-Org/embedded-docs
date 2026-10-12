# LTXVScheduler

Il nodo LTXVScheduler genera valori sigma per un processo di campionamento personalizzato. Calcola la schedulazione del rumore dal numero di token nel latent fornito, oppure usa un valore predefinito di 4096 token quando nessun latent è collegato, e può facoltativamente estendere i valori sigma affinché il valore finale corrisponda al valore `terminal` specificato.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `steps` | Numero di passaggi di campionamento (predefinito: 20) | INT | Sì | 1-10000 |
| `max_shift` | Valore di shift massimo utilizzato nel calcolo dei sigma (predefinito: 2.05) | FLOAT | Sì | 0.0-100.0 (passo: 0.01) |
| `base_shift` | Valore di shift di base utilizzato nel calcolo dei sigma (predefinito: 0.95) | FLOAT | Sì | 0.0-100.0 (passo: 0.01) |
| `stretch` | Estende i sigma affinché siano nell'intervallo [terminal, 1] (predefinito: True) | BOOLEAN | Sì | True/False |
| `terminal` | Il valore terminale dei sigma dopo l'estensione (predefinito: 0.1). Usato solo quando `stretch` è abilitato. | FLOAT | Sì | 0.0-0.99 (passo: 0.01) |
| `latent` | Input latent opzionale usato per calcolare il numero di token per la regolazione dei sigma. Quando non fornito, viene usato un numero predefinito di token pari a 4096. | LATENT | No | - |

**Nota:** Quando `stretch` è abilitato, i valori sigma diversi da zero vengono ridimensionati in modo che l'ultimo sigma diverso da zero sia uguale al valore `terminal`.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `sigmas` | Valori sigma generati per il processo di campionamento | SIGMAS |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVScheduler/it.md)

---
**Source fingerprint (SHA-256):** `5b4907e905e27a951c332c400e24023ef089df7a5f4a17b1fc8ba42a41302399`
