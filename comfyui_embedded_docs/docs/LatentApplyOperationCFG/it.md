# Applica Operazione Latent CFG

Il nodo LatentApplyOperationCFG applica un'operazione latente all'interno del passaggio di classifier-free guidance (CFG) del processo di campionamento di un modello. Intercetta gli output di condizionamento prodotti prima del CFG, applica l'operazione connessa ai valori latenti e restituisce il modello con questo comportamento di campionamento modificato.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello a cui verrà applicata l'operazione CFG | MODEL | Sì | - |
| `operation` | L'operazione latente da applicare durante il processo di campionamento CFG | LATENT_OPERATION | Sì | - |
| `start_percent` | Frazione della pianificazione di denoising in cui l'operazione inizia a essere applicata; 0 è l'inizio della pianificazione (predefinito: 0.0) | FLOAT | No | 0.0 a 1.0 (passo 0.001) |
| `end_percent` | Frazione della pianificazione di denoising in cui l'operazione smette di essere applicata; 1 è la fine della pianificazione (predefinito: 1.0) | FLOAT | No | 0.0 a 1.0 (passo 0.001) |

Nota: questo nodo è contrassegnato come sperimentale. L'operazione viene applicata agli output di condizionamento del modello durante il processo di campionamento CFG. Quando sono presenti due output di condizionamento, l'operazione viene applicata alla differenza tra il primo e il secondo output, e il secondo output viene riaggiunto al risultato. Quando è presente un solo output di condizionamento, l'operazione viene applicata direttamente a esso. L'operazione viene eseguita solo tra i punti `start_percent` e `end_percent` della pianificazione di denoising, quindi può essere limitata a una parte della pianificazione; al di fuori di tale intervallo gli output di condizionamento vengono restituiti invariati.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il modello modificato con l'operazione CFG applicata al suo processo di campionamento | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentApplyOperationCFG/it.md)

---
**Source fingerprint (SHA-256):** `6a5f59f02eaec38334c63d871e48e89aa983a5ac2ca10801161cdc9e13cacdf2`
