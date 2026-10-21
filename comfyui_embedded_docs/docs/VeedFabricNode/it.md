# VEED Fabric 1.0

Trasforma un'immagine statica e una traccia vocale in un video parlante con sincronizzazione labiale utilizzando VEED Fabric. Funziona con foto, illustrazioni e mascotte purché il viso sia chiaramente visibile; il video mantiene le proporzioni dell'immagine ed è lungo quanto l'audio.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Modello da utilizzare. Selezionando un modello vengono rivelati i parametri specifici: `image`, `audio` e `resolution`. | DYNAMIC_COMBO | Sì | `"fabric-1.0"` |
| `image` | Immagine con un viso chiaramente visibile. Il video mantiene le sue proporzioni. | IMAGE | Sì | - |
| `audio` | Traccia vocale da sincronizzare con le labbra, fino a 300 secondi. Imposta la durata del video. | AUDIO | Sì | Fino a 300 secondi |
| `resolution` | Classe di dimensione dell'output: circa 0,4 megapixel con `"480p"` (864x480 in 16:9) e 0,9 megapixel con `"720p"` (1312x736 in 16:9). (predefinito: `"720p"`) | COMBO | Sì | `"480p"`<br>`"720p"` |

Il nodo si arresta con un errore quando la traccia vocale supera i 300 secondi.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `VIDEO` | Il video parlante: l'immagine di input animata per sincronizzarsi con la traccia vocale. | VIDEO |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeedFabricNode/it.md)

---
**Source fingerprint (SHA-256):** `69cabfa5f03885ce770e8502419305dacee49d7e89a748f31abe3775d682a33a`
