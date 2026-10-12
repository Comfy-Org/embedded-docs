# CFGZeroStar

Il nodo CFGZeroStar applica una tecnica specializzata di scaling della guida ai modelli di diffusione. Modifica il processo di guida classifier-free calcolando un fattore di scala ottimizzato basato sulla differenza tra le previsioni condizionali e incondizionali. Questo approccio regola l'output finale per offrire un controllo migliorato sul processo di generazione, mantenendo al contempo la stabilità del modello.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello di diffusione da modificare con la tecnica di scaling della guida CFGZeroStar | MODEL | Sì | - |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `patched_model` | Il modello modificato con lo scaling della guida CFGZeroStar applicato | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CFGZeroStar/it.md)

---
**Source fingerprint (SHA-256):** `4ec70f67eed8aaca964ce3dfb5b650af2f44d34bcde3b74c3886c91e1e8e8cc0`
