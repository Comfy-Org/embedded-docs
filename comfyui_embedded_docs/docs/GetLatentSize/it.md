# Get Image/Video Latent Size

Legge un latente di immagine o video e restituisce la sua larghezza, altezza, numero di fotogrammi e dimensione del batch, così la geometria può essere riutilizzata senza decodificare il latente. Utilizzalo per dimensionare maschere di rumore, allineare le risoluzioni o calcolare le sovrapposizioni quando si esegue il tiling di un sampler. I valori misurati vengono anche stampati sul nodo stesso.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `latent` | Il latente di immagine o video da ispezionare. Quando il latente contiene diversi flussi, viene misurato il primo. | LATENT | Sì | - |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `width` | La larghezza del latente, in celle del latente anziché in pixel. | INT |
| `height` | L'altezza del latente, in celle del latente anziché in pixel. | INT |
| `frames` | Il numero di fotogrammi nel latente. I latenti di immagini hanno un singolo fotogramma. | INT |
| `batch_size` | Il numero di latenti nel batch. | INT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetLatentSize/it.md)

---
**Source fingerprint (SHA-256):** `f75b3347cb1853b035b0bb283d5487ab1532d561d66d3cae3c67f54bf693d31a`
