# SaveAnimatedPng

Il nodo SaveAnimatedPNG è progettato per creare e salvare immagini PNG animate da una sequenza di fotogrammi. Gestisce l'assemblaggio dei singoli fotogrammi in un'animazione coesa, consentendo la personalizzazione della durata dei fotogrammi, del loop e dell'inclusione dei metadati.

## Input

| Campo | Descrizione | Tipo di dati |
| --- | --- | --- |
| `images` | Un elenco di immagini da elaborare e salvare come PNG animato. Ogni immagine nell'elenco rappresenta un fotogramma dell'animazione. | `IMAGE` |
| `filename_prefix` | Specifica il nome di base per il file di output, che verrà utilizzato come prefisso per i file PNG animati generati. | `STRING` |
| `fps` | La frequenza in fotogrammi al secondo dell'animazione, che controlla la rapidità con cui vengono visualizzati i fotogrammi. | `FLOAT` |
| `compress_level` | Il livello di compressione applicato ai file PNG animati, che influisce sulla dimensione del file e sulla chiarezza dell'immagine. | `INT` |

## Output

| Campo | Descrizione | Tipo di dati |
| --- | --- | --- |
| `ui` | Fornisce un componente UI che visualizza le immagini PNG animate generate e indica se l'animazione è a fotogramma singolo o multi-fotogramma. | N/A |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAnimatedPng/it.md)
