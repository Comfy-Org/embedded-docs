# LoadImageDataSetFromFolder

Questo nodo carica più immagini da una sottocartella selezionata all'interno della directory di input principale di ComfyUI e le restituisce come elenco. Scansiona la cartella scelta alla ricerca di file immagine in formato PNG, JPG, JPEG o WEBP, il che lo rende utile per l'elaborazione batch o per preparare dataset di immagini.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `folder` | La cartella da cui caricare le immagini. Le opzioni sono le sottocartelle presenti nella directory di input principale di ComfyUI. | COMBO | Sì | Più opzioni disponibili |

Nota: la cartella selezionata deve essere una sottocartella della directory di input principale di ComfyUI; qualsiasi valore che risolva al di fuori di essa (ad esempio, usando `..`, percorsi assoluti, lettere di unità o symlink) viene rifiutato. Vengono caricati solo i file con estensione .png, .jpg, .jpeg o .webp, e il controllo dell'estensione non distingue tra maiuscole e minuscole. Le immagini caricate vengono convertite in RGB e riscalate nell'intervallo 0-1. Se la cartella selezionata non contiene file immagine validi, il nodo genera un errore. Questo nodo è contrassegnato come sperimentale.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `images` | Elenco delle immagini caricate. Il nodo carica tutti i file immagine validi (PNG, JPG, JPEG, WEBP) trovati nella cartella selezionata. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageDataSetFromFolder/it.md)

---
**Source fingerprint (SHA-256):** `cdee4e372890c126dd5f09654a7dd4103bba97a7901b6f5df8e02f29c4064ed2`
