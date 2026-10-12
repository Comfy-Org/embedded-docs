# LoadVideoTextDataSetFromFolder

Questo nodo carica file video e le relative didascalie testuali corrispondenti da una cartella all'interno della directory di input di ComfyUI, restituendoli come due liste: video e didascalie. Le voci video sono riferimenti lazy, quindi i fotogrammi vengono decodificati solo quando un nodo a valle ne ha bisogno. I formati supportati sono MP4, AVI, MOV, WEBM, MKV e FLV, e sono supportate anche cartelle annidate con un prefisso di conteggio delle ripetizioni (ad esempio `5_classname/`, come usato da strumenti come kohya-ss/sd-scripts).

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `folder` | La cartella contenente file video e didascalie .txt. | COMBO | Sì | Elenca dinamicamente tutte le sottocartelle all'interno della directory di input di ComfyUI |

La cartella selezionata deve essere una sottocartella della directory di input di ComfyUI; un nome di cartella che si risolve al di fuori di tale directory genera un errore. Se la cartella selezionata non contiene file con un'estensione video supportata (MP4, AVI, MOV, WEBM, MKV, FLV), il nodo genera un errore. Per le cartelle annidate il cui nome inizia con un numero seguito da un underscore (ad esempio `5_classname`), ogni video all'interno di quella cartella viene incluso nel dataset il numero di volte indicato da quel prefisso. La didascalia di ogni video viene letta da un file `.txt` con lo stesso nome base; se non esiste un file `.txt` corrispondente, la didascalia è una stringa vuota.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `videos` | Riferimenti video lazy; i fotogrammi vengono decodificati solo quando necessario a valle. Una voce per ogni file video trovato nella cartella. | VIDEO (list) |
| `texts` | Lista di didascalie testuali. Una didascalia per video; se un video non ha un file `.txt` corrispondente, la sua didascalia è una stringa vuota. | STRING (list) |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoTextDataSetFromFolder/it.md)

---
**Source fingerprint (SHA-256):** `21ed21bc3189e96be5c7f0415c65e8749d6591cf19bddf4350a3b0af48b92841`
