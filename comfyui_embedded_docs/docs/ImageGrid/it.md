# ImageGrid

Il nodo Image Grid combina più immagini in un'unica griglia o collage organizzato. Prende un elenco di immagini e le dispone in un numero specificato di colonne, ridimensionando ciascuna immagine per adattarla a una dimensione di cella definita e aggiungendo un padding opzionale tra di esse. Il risultato è una singola nuova immagine contenente tutte le immagini di input disposte in una griglia.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `images` | Un elenco di immagini da disporre nella griglia. Il nodo richiede almeno un'immagine per funzionare. | IMAGE | Sì | - |
| `columns` | Il numero di colonne nella griglia (predefinito: 4). | INT | No | 1 - 20 |
| `cell_width` | La larghezza, in pixel, di ciascuna cella nella griglia (predefinito: 256). | INT | No | 32 - 2048 |
| `cell_height` | L'altezza, in pixel, di ciascuna cella nella griglia (predefinito: 256). | INT | No | 32 - 2048 |
| `padding` | La quantità di padding, in pixel, da inserire tra le immagini nella griglia (predefinito: 4). | INT | No | 0 - 50 |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | L'immagine di output singola contenente tutte le immagini di input disposte in una griglia. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageGrid/it.md)

---
**Source fingerprint (SHA-256):** `87bc0af8af33a0fd703f13fec782075502c9562847fa3887a2273afa5b28c47e`
