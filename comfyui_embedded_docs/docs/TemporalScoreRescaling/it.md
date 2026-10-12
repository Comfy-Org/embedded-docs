# TSR - Temporal Score Rescaling

Questo nodo applica il Temporal Score Rescaling (TSR) a un modello di diffusione. Applica una patch al modello affinché, durante il campionamento, lo score previsto o il rumore venga riscalato per guidare la diversità dei risultati generati. Questo è implementato come funzione post-CFG (Classifier-Free Guidance).

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello di diffusione a cui applicare la patch con la funzione TSR. | MODEL | Sì | - |
| `tsr_k` | Controlla la forza di rescaling. Un valore k più basso produce risultati più dettagliati; un valore k più alto produce risultati più levigati nella generazione di immagini. Impostando k = 1 si disabilita il rescaling. (predefinito: 0.95) | FLOAT | Sì | 0.01 - 100.0 |
| `tsr_sigma` | Controlla quanto presto ha effetto il rescaling. Valori più elevati hanno effetto prima. (predefinito: 1.0) | FLOAT | Sì | 0.01 - 100.0 |

Nota: il rescaling viene saltato quando `tsr_k` è impostato a 1, quando il valore sigma è 0 o quando il rapporto segnale-rumore è 0.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `patched_model` | Il modello di input, ora patchato con la funzione Temporal Score Rescaling applicata al suo processo di campionamento. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TemporalScoreRescaling/it.md)

---
**Source fingerprint (SHA-256):** `4d4e3c64fb6e3a3fe4725ea944a361b46d871943a10e65d72d70e0e6d757dfca`
