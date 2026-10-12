# Ingrandisci Immagine

Il nodo ImageScale è progettato per ridimensionare le immagini a dimensioni specifiche, offrendo una selezione di metodi di upscaling e la possibilità di ritagliare l'immagine ridimensionata. Astrae la complessità dell'upscaling e del ritaglio delle immagini, fornendo un'interfaccia semplice per modificare le dimensioni dell'immagine in base ai parametri definiti dall'utente.

## Input

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `image` | L'immagine in input da ingrandire. Questo parametro è centrale per il funzionamento del nodo, in quanto rappresenta il dato principale su cui vengono applicate le trasformazioni di ridimensionamento. La qualità e le dimensioni dell'immagine in output sono direttamente influenzate dalle proprietà dell'immagine originale. | `IMAGE` |
| `upscale_method` | Specifica il metodo utilizzato per l'upscaling dell'immagine. La scelta del metodo può influire sulla qualità e sulle caratteristiche dell'immagine ingrandita, influenzando la fedeltà visiva e i potenziali artefatti nell'output ridimensionato. | COMBO[STRING] |
| `width` | La larghezza di destinazione per l'immagine ingrandita. Questo parametro influenza direttamente le dimensioni dell'immagine in output, determinando la scala orizzontale dell'operazione di ridimensionamento. | `INT` |
| `height` | L'altezza di destinazione per l'immagine ingrandita. Questo parametro influenza direttamente le dimensioni dell'immagine in output, determinando la scala verticale dell'operazione di ridimensionamento. | `INT` |
| `crop` | Determina se e come l'immagine ingrandita debba essere ritagliata, offrendo opzioni per il ritaglio disabilitato o il ritaglio centrale. Questo influisce sulla composizione finale dell'immagine, potenzialmente rimuovendo i bordi per adattarla alle dimensioni specificate. | COMBO[STRING] |

## Output

| Parametro | Descrizione | Tipo di dato |
| --- | --- | --- |
| `image` | L'immagine ingrandita (e opzionalmente ritagliata), pronta per ulteriori elaborazioni o visualizzazione. | `IMAGE` |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageScale/it.md)
