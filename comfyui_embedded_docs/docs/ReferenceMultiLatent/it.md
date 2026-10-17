# Set Reference Multi Latent

Questo nodo codifica una o più immagini di riferimento e aggiunge i loro latent al condizionamento che un modello di editing utilizza. È la controparte multi-immagine di Set Reference Latent: colleghi un VAE e un insieme di immagini di riferimento, e il nodo collega ogni latent codificato al condizionamento positivo e, quando è collegato un condizionamento negativo, anche a quello negativo. Usalo quando un modello prevede più immagini di riferimento contemporaneamente invece di un singolo latent.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `positive` | Il condizionamento positivo da modificare con i latent di riferimento. | CONDITIONING | Sì | - |
| `negative` | Condizionamento negativo opzionale che riceve gli stessi latent di riferimento. Lascialo scollegato per riutilizzare il condizionamento positivo modificato sull'output `negative`. | CONDITIONING | No | - |
| `vae` | Il VAE utilizzato per codificare le immagini di riferimento collegate. Quando non è collegato alcun VAE, le immagini di riferimento vengono ignorate. | VAE | No | - |
| `resolution` | Come viene preparata ogni immagine di riferimento prima della codifica. `"keep resolution"` la codifica alle dimensioni in ingresso; `"resize"` la ridimensiona a un numero target di megapixel preservando le proporzioni, il che fa comparire `megapixels`. (predefinito: "keep resolution") | DYNAMIC_COMBO | Sì | `"keep resolution"`<br>`"resize"` |
| `images` | Slot espandibile: collega una o più immagini di riferimento (`image_1`, `image_2`, ...) da usare come riferimenti. Le immagini vengono codificate nell'ordine degli slot e aggiunte al condizionamento in quell'ordine. | IMAGE | No | Da 1 a 100 |

### Input di ridimensionamento

Queste opzioni compaiono quando `resolution` è impostato su `"resize"`.

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `megapixels` | Dimensione target di ogni immagine di riferimento, preservando le proporzioni. 1.0 corrisponde a circa 1024 x 1024 pixel. (predefinito: 1.0) | FLOAT | Sì | Da 0.01 a 16.0 |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `positive` | Il condizionamento positivo con i latent di riferimento codificati aggiunti. | CONDITIONING |
| `negative` | Il condizionamento negativo con gli stessi latent di riferimento aggiunti. Restituisce l'output positivo quando non è collegato alcun condizionamento negativo. | CONDITIONING |
| `empty_latent` | Il primo latent di riferimento moltiplicato per 0.0, pronto per inizializzare un sampler. Quando non viene prodotto alcun latent di riferimento, viene restituito invece un latent vuoto quadrato alla risoluzione selezionata. | LATENT |

## Note

- I latent vengono aggiunti anziché sostituiti, quindi concatenando diversi nodi Set Reference Multi Latent si accumulano riferimenti.
- Ogni immagine collegata viene codificata singolarmente, quindi le immagini di riferimento non devono avere le stesse dimensioni.
- Senza un VAE collegato o senza alcuna immagine collegata, `positive` e `negative` vengono restituiti invariati e `empty_latent` è un latent vuoto quadrato: 1024 x 1024, oppure dimensionato da `megapixels` quando `resolution` è `"resize"`.

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReferenceMultiLatent/it.md)

---
**Source fingerprint (SHA-256):** `06f98e7c21e8750a2bdf365cb80fac990bcf01246f183c60ef83bd195fc1225b`
