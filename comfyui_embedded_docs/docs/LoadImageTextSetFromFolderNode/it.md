# LoadImageTextSetFromFolderNode

Carica un batch di immagini e le relative didascalie testuali da una directory specificata a scopo di addestramento. Il nodo cerca automaticamente i file immagine e i file di testo delle didascalie associati, elabora le immagini in base alle impostazioni di ridimensionamento specificate e codifica le didascalie usando il modello CLIP fornito.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `folder` | La cartella da cui caricare le immagini. | STRING | Sì | - |
| `clip` | Il modello CLIP usato per codificare il testo. | CLIP | Sì | - |
| `resize_method` | Il metodo usato per ridimensionare le immagini (predefinito: "None"). | COMBO | No | "None"<br>"Stretch"<br>"Crop"<br>"Pad" |
| `width` | La larghezza a cui ridimensionare le immagini. -1 significa usare la larghezza originale (predefinito: -1). | INT | No | da -1 a 10000 |
| `height` | L'altezza a cui ridimensionare le immagini. -1 significa usare l'altezza originale (predefinito: -1). | INT | No | da -1 a 10000 |

**Nota:** L'input CLIP deve essere valido e non può essere None. Se il modello CLIP proviene da un nodo di caricamento del checkpoint, assicurarsi che il checkpoint contenga un modello CLIP o codificatore di testo valido.

**Nota sulla struttura delle cartelle:** Il nodo supporta la struttura di cartelle kohya-ss/sd-scripts. Se il nome di una sottocartella inizia con un numero seguito da un underscore (ad es. `5_myclass`), quel numero viene usato come numero di ripetizioni, e le immagini all'interno di quella sottocartella verranno caricate quel numero di volte.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `IMAGE` | Il batch di immagini caricate ed elaborate. | IMAGE |
| `CONDITIONING` | I dati di condizionamento codificati dalle didascalie testuali. | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageTextSetFromFolderNode/it.md)

---
**Source fingerprint (SHA-256):** `ffd6399783fc281a58bae811112d9ecacb51ab8ea3b512befa9b9fab2c6860de`
