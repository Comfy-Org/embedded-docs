# Carica Video

Il nodo Load Video carica i file video dalla directory di input e li rende disponibili per l'elaborazione nel flusso di lavoro. Legge i file video dalla cartella di input designata e li restituisce come dati video che possono essere collegati ad altri nodi di elaborazione video.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `file` | Il file video da caricare dalla directory di input. L'elenco a discesa viene popolato dinamicamente con tutti i file video trovati nella cartella di input di ComfyUI e nuovi file video possono essere caricati direttamente tramite il selettore file. | COMBO | Sì | Più opzioni disponibili (tutti i file video nella directory di input) |

**Nota:** Le opzioni disponibili per il parametro `file` vengono popolate dinamicamente dai file video presenti nella directory di input. Vengono visualizzati solo i file che corrispondono ai tipi di contenuto video supportati e l'elenco è ordinato alfabeticamente. È inoltre possibile caricare un nuovo file video direttamente tramite l'interfaccia di selezione file del nodo. Se un file video selezionato in precedenza non è più disponibile, il nodo segnala un errore di file non valido.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `video` | I dati video caricati che possono essere passati ad altri nodi di elaborazione video per ulteriori manipolazioni o analisi. | VIDEO |

**Nota:** Il nodo produce anche un'anteprima del video caricato, visualizzata direttamente sul nodo.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideo/it.md)

---
**Source fingerprint (SHA-256):** `dcdd252792ade2a106c11826bbe7344011f0bc08506b80d634043a4dc156e076`
