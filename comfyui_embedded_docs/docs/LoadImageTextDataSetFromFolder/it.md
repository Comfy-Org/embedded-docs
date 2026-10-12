# Carica Immagine-Testo (da Cartella)

Questo nodo carica un dataset di coppie immagine-didascalia da una cartella selezionata e le restituisce come lista. Supporta immagini PNG, JPG, JPEG e WEBP e, per ogni immagine, cerca una didascalia in un file `.txt` con lo stesso nome base. Il nodo supporta anche la struttura di cartelle di kohya-ss/sd-scripts, in cui un nome di sottocartella che inizia con un numero (ad esempio `10_cats`) ripete le immagini contenute in quella sottocartella quel numero di volte nell'output.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `folder` | La cartella da cui caricare immagini e didascalie testuali. | COMBO | Sì | Sottocartelle all'interno della directory di input di ComfyUI (caricate dinamicamente) |

**Nota:** La cartella selezionata deve essere una sottocartella della directory di input di ComfyUI. Il nodo si aspetta un file di didascalia `.txt` per ogni immagine: per ciascun file immagine (`.png`, `.jpg`, `.jpeg`, `.webp`) cerca un file `.txt` con lo stesso nome base nella stessa posizione e usa il suo contenuto ripulito dagli spazi iniziali e finali come didascalia. Se non viene trovato alcun file di didascalia, viene usata una stringa vuota. Il nodo supporta anche la struttura di cartelle di kohya-ss/sd-scripts: le sottocartelle il cui nome inizia con un numero e un underscore (ad esempio `5_cats`) ripetono le immagini al loro interno quel numero di volte nella lista di output finale. Se la cartella selezionata non contiene immagini valide, il nodo genera un errore.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `images` | Lista delle immagini caricate. Le immagini vengono convertite in RGB e normalizzate nell'intervallo float 0–1. | IMAGE |
| `texts` | Lista di didascalie testuali, una per ogni immagine caricata. Le didascalie sono il contenuto ripulito dagli spazi iniziali e finali del file `.txt` corrispondente, oppure una stringa vuota quando non esiste un file di didascalia. | STRING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageTextDataSetFromFolder/it.md)

---
**Source fingerprint (SHA-256):** `d34494d59a65edb38d7e6a5f12c241fb0093371db0b0bf1e52789e84209ad3f5`
