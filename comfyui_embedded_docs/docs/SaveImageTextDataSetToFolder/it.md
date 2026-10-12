# Salva Immagine-Testo (in Cartella)

Save Image-Text (to Folder) salva un dataset di coppie immagine-didascalia in una cartella all'interno della directory di output di ComfyUI. Ogni immagine viene scritta come file PNG, e la sua didascalia corrispondente viene scritta come file TXT con lo stesso nome base, così ogni immagine risulta abbinata alla sua descrizione.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `images` | Lista di immagini da salvare. | IMAGE | Sì | - |
| `texts` | Lista di didascalie di testo da salvare. Questo input è opzionale. | STRING | No | - |
| `folder_name` | Nome della cartella in cui salvare le immagini (all'interno della directory di output). (predefinito: "dataset") | STRING | Sì | - |
| `filename_prefix` | Prefisso per i nomi dei file delle immagini salvate. (predefinito: "image") | STRING | Sì | - |
| `mode` | Se sovrascrivere i file esistenti o incrementare i nomi dei file per evitare la sovrascrittura. (predefinito: "overwrite") | COMBO | Sì | "overwrite"<br>"increment" |

**Nota:** L'input `images` è una lista, e il nodo riceve sia `images` che `texts` come liste. L'input `texts` è opzionale; se fornito, dovrebbe essere una lista di didascalie di testo e dovrebbe contenere lo stesso numero di elementi di `images`. Ogni didascalia viene salvata come file `.txt` corrispondente alla sua immagine abbinata. In modalità `overwrite`, i file sono nominati `{filename_prefix}_{index}.png` e sostituiscono qualsiasi file esistente con lo stesso nome. In modalità `increment`, un contatore univoco viene aggiunto ai nomi dei file in modo che i file esistenti non vengano sovrascritti. Il `folder_name` deve risolvere in un percorso all'interno della directory di output; i nomi delle cartelle che tentano di uscirne (ad esempio con `..`) vengono rifiutati.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| - | Questo nodo non restituisce dati. Salva i file direttamente nel filesystem. | - |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageTextDataSetToFolder/it.md)

---
**Source fingerprint (SHA-256):** `46c5a04ba1befedf62b75abbff2442dde934048f365fa7e2604ea37e70d8fdcb`
