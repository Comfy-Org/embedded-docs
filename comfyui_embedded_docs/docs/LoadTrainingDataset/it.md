# Carica Dataset di Addestramento

Questo nodo carica un dataset di addestramento codificato (latents e conditioning) precedentemente salvato su disco. Legge tutti i file di shard dati `shard_*.pkl` da una cartella dataset selezionata nella directory dei dataset e restituisce i vettori latenti e i dati di conditioning combinati per l'uso nei flussi di lavoro di addestramento.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `folder_name` | Dataset salvato da caricare, dalla directory dei dataset. | COMBO | Sì | Un'opzione per ogni cartella dataset trovata nella directory dei dataset |

Nota: le opzioni di `folder_name` vengono create automaticamente eseguendo la scansione della directory dei dataset. Una sottocartella viene elencata come dataset quando contiene un file `metadata.json` o almeno un file `.safetensors` (la scansione non entra in una cartella che corrisponde). La cartella dataset selezionata viene cercata in tutte le directory radice dei dataset configurate e il nome della cartella deve corrispondere a una sottocartella all'interno di una di tali radici. Il nodo legge tutti i file denominati `shard_*.pkl` nella cartella selezionata, in ordine ordinato, e genera un errore se non viene trovato alcun file shard o se la cartella non può essere individuata.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `latents` | Lista di dizionari latenti (lista di output), in cui ogni dizionario contiene una chiave `"samples"` con un tensore. | LATENT |
| `conditioning` | Lista di liste di conditioning (lista di output), in cui ogni lista interna contiene i dati di conditioning per il campione corrispondente. | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadTrainingDataset/it.md)

---
**Source fingerprint (SHA-256):** `9f914b27f067460f6f3b54f3f2a7bb793c65b99c85e8aa14ab64894be26bd816`
