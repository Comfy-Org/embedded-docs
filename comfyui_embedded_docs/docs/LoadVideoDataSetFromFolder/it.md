# LoadVideoDataSetFromFolder

Carica un dataset di video da una cartella selezionata all'interno della directory di input di ComfyUI e li restituisce come un elenco di riferimenti video lazy. Questo nodo carica un dataset di video: i frame vengono decodificati solo quando un altro nodo ne ha effettivamente bisogno. I formati supportati sono MP4, AVI, MOV, WEBM, MKV e FLV.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `folder` | La cartella contenente i file video. | COMBO | Sì | Tutte le sottocartelle disponibili nella directory di input di ComfyUI (popolate dinamicamente) |

**Nota:** La cartella selezionata deve essere una sottocartella della directory di input di ComfyUI e deve contenere almeno un file video supportato. Le estensioni supportate sono MP4, AVI, MOV, WEBM, MKV e FLV. Se non viene trovato alcun file video supportato, o se il percorso della cartella si risolve al di fuori della directory di input, il nodo genera un errore.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `videos` | Un elenco di riferimenti video lazy, uno per ogni file video supportato nella cartella selezionata, ordinati alfabeticamente per nome file. I frame video vengono decodificati solo quando l'output viene consumato da un altro nodo. | VIDEO (list) |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoDataSetFromFolder/it.md)

---
**Source fingerprint (SHA-256):** `6a7e6115872bb994fa554bb9de84bcd419106485403a3d2db654cbdd6c72bbe5`
