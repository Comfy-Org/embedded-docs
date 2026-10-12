# LTXV Duration Predictor

Questo nodo prevede la durata naturale dell'inquadratura per un prompt testuale usando un head di durata LTX 2.4 caricato con ModelPatchLoader, quindi allinea il risultato alla griglia di frame 8k+1 del VAE. La previsione viene convertita in un numero di frame utilizzando il frame rate selezionato e i limiti di durata minimo e massimo.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello utilizzato per preprocessare gli embedding di testo ed eseguire l'head di durata. | MODEL | Sì | N/A |
| `positive` | Il conditioning che fornisce gli embedding di testo e i metadati del prompt per la previsione della durata. | CONDITIONING | Sì | N/A |
| `duration_head` | Head di durata LTX 2.4 caricato con ModelPatchLoader. Deve essere un head di durata LTX. | MODEL_PATCH | Sì | N/A |
| `frame_rate` | Frame rate in frame al secondo utilizzato per convertire i secondi in frame (predefinito: 24.0). | FLOAT | Sì | da 1.0 a 120.0 |
| `min_seconds` | Durata minima in secondi utilizzata durante la conversione della previsione in un numero di frame (predefinito: 1.0). | FLOAT | Sì | da 0.5 a 120.0 |
| `max_seconds` | Durata massima in secondi utilizzata durante la conversione della previsione in un numero di frame (predefinito: 20.0). | FLOAT | Sì | da 0.5 a 120.0 |

Nota: l'input `duration_head` deve essere una patch di modello contenente un head di durata LTX. Se la patch di modello collegata non è un head di durata LTX, il nodo solleva un ValueError. Viene utilizzata solo la prima voce di conditioning: se `positive` contiene un batch con più di un prompt, il nodo valuta solo il primo.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `num_frames` | La durata prevista convertita in un numero di frame e allineata alla griglia di frame 8k+1 del VAE. | INT |
| `seconds` | Durata prevista grezza (non limitata). Questo è il valore prima dell'allineamento alla griglia di frame. | FLOAT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVDurationPredictor/it.md)

---
**Source fingerprint (SHA-256):** `a4abb43128b8fe396e4c986d75028aea6bfdd9bb6fda07e24c88f8e04a61669e`
