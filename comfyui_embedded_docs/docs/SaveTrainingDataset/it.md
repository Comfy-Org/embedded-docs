# Salva Dataset di Addestramento

Questo nodo salva su disco un dataset di addestramento codificato per consentirne un caricamento efficiente durante l'addestramento. Prende i latenti delle immagini e il relativo condizionamento testuale, li suddivide in file più piccoli chiamati shard e li archivia in una cartella all'interno della directory datasets. Scrive inoltre un file di metadati che descrive il dataset.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `latents` | Elenco di dizionari di latenti da MakeTrainingDataset. | LATENT | Sì | N/A |
| `conditioning` | Elenco di liste di condizionamento da MakeTrainingDataset. | CONDITIONING | Sì | N/A |
| `folder_name` | Nome della cartella in cui salvare il dataset, all'interno della directory datasets. Sono consentite sottocartelle come 'project/run1'. (predefinito: "training_dataset") | STRING | Sì | N/A |
| `shard_size` | Numero di campioni per file shard. (predefinito: 1000) | INT | Sì | 1 to 100000 |

**Nota:** Il numero di elementi in `latents` deve corrispondere esattamente al numero di elementi in `conditioning`; il nodo genera un errore se questi conteggi non corrispondono. `folder_name` deve indicare una sottocartella della directory datasets (ad esempio `my_dataset`) — non può essere la directory datasets stessa, e i nomi di cartella che risulterebbero al di fuori della directory datasets vengono rifiutati. Il parametro `shard_size` è un'impostazione avanzata.

## Output

Questo nodo non produce alcun dato di output. La sua funzione è salvare file sul disco. Ogni shard viene salvato come file `shard_XXXX.pkl` nella cartella scelta, e un file `metadata.json` registra il numero totale di campioni, il numero di shard e la dimensione dello shard.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveTrainingDataset/it.md)

---
**Source fingerprint (SHA-256):** `6d7b63a24ac42907b0f4a1358712cd0ed085982ecd308bce87e5376d9bbc2274`
