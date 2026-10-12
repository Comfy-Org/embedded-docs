# Dividi Immagine in Elenco di Tasselli

Il nodo Split Image into List of Tiles divide una singola immagine di input in una serie di sezioni rettangolari più piccole e sovrapposte chiamate tile. Crea una lista in batch di queste tile, che possono essere elaborate singolarmente da altri nodi. È possibile specificare la dimensione di ciascuna tile e la quantità di sovrapposizione tra esse.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `image` | L'immagine di input da dividere in tile. | IMAGE | Sì | - |
| `tile_width` | La larghezza di ciascuna tile di output in pixel (predefinito: 1024). | INT | Sì | 64 a 1048576 |
| `tile_height` | L'altezza di ciascuna tile di output in pixel (predefinito: 1024). | INT | Sì | 64 a 1048576 |
| `overlap` | Il numero di pixel di sovrapposizione tra tile adiacenti (predefinito: 128). | INT | Sì | 0 a 4096 |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | Una lista in batch contenente tutte le singole tile dell'immagine. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitImageToTileList/it.md)

---
**Source fingerprint (SHA-256):** `4a04e7042446c2368091ffd051c781f9f0ec8496ab681ee9e0741bb269bb54af`
