# SaveAnimatedWebp

Questo nodo è progettato per salvare una sequenza di immagini come file WEBP animato. Gestisce l'aggregazione dei singoli fotogrammi in un'animazione coesa, applicando metadati specificati e ottimizzando l'output in base alle impostazioni di qualità e compressione.

## Input

| Campo | Descrizione | Tipo di dato |
| --- | --- | --- |
| `images` | Un elenco di immagini da salvare come fotogrammi nel WEBP animato. Questo parametro è essenziale per definire il contenuto visivo dell'animazione. | `IMAGE` |
| `filename_prefix` | Specifica il nome di base per il file di output, a cui verranno aggiunti un contatore e l'estensione '.webp'. Questo parametro è cruciale per identificare e organizzare i file salvati. | `STRING` |
| `fps` | La frequenza di fotogrammi al secondo per l'animazione, che influenza la velocità di riproduzione. | `FLOAT` |
| `lossless` | Un booleano che indica se usare la compressione senza perdita, influenzando la dimensione del file e la qualità dell'animazione. | `BOOLEAN` |
| `quality` | Un valore tra 0 e 100 che imposta il livello di qualità della compressione, con valori più alti che producono una qualità dell'immagine migliore ma dimensioni del file maggiori. | `INT` |
| `method` | Specifica il metodo di compressione da usare, che può influire sulla velocità di codifica e sulla dimensione del file. | COMBO[STRING] |

## Output

| Campo | Descrizione | Tipo di dato |
| --- | --- | --- |
| `ui` | Fornisce un componente UI che mostra le immagini WEBP animate salvate insieme ai relativi metadati e indica se l'animazione è abilitata. | N/A |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAnimatedWEBP/it.md)
