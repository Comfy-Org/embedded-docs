# VAEDecodeTiled

Il nodo VAEDecodeTiled decodifica le rappresentazioni latenti in immagini utilizzando un approccio a tile per gestire in modo efficiente immagini di grandi dimensioni. Elabora l'input in tile più piccoli per gestire l'utilizzo della memoria mantenendo la qualità dell'immagine. Il nodo supporta anche i VAE video elaborando frame temporali in blocchi con sovrapposizione per transizioni fluide.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `samples` | La rappresentazione latente da decodificare in immagini | LATENT | Sì | - |
| `vae` | Il modello VAE utilizzato per decodificare i campioni latenti | VAE | Sì | - |
| `tile_size` | La dimensione di ciascun tile per l'elaborazione (predefinito: 512) | INT | Sì | 64-4096 (step: 32) |
| `overlap` | La quantità di sovrapposizione tra tile adiacenti (predefinito: 64) | INT | Sì | 0-4096 (step: 32) |
| `temporal_size` | Utilizzato solo per VAE video: quantità di frame da decodificare alla volta (predefinito: 64) | INT | Sì | 8-4096 (step: 4) |
| `temporal_overlap` | Utilizzato solo per VAE video: quantità di frame da sovrapporre (predefinito: 8) | INT | Sì | 4-4096 (step: 4) |

**Nota:** Gli input `tile_size`, `overlap`, `temporal_size` e `temporal_overlap` sono contrassegnati come impostazioni avanzate.

**Nota:** Il nodo regola automaticamente i valori di sovrapposizione se superano i limiti pratici. Se `tile_size` è inferiore a 4 volte `overlap`, la sovrapposizione viene ridotta a un quarto della dimensione del tile. Analogamente, se `temporal_size` è inferiore al doppio di `temporal_overlap`, la sovrapposizione temporale viene dimezzata. Il nodo tiene inoltre conto dei rapporti di compressione interni del VAE quando calcola le dimensioni di tile e sovrapposizione sia per le dimensioni spaziali che temporali. Se il latente di input è un batch annidato di latenti, viene decodificato solo il primo elemento del batch.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `IMAGE` | L'immagine o le immagini decodificate generate dalla rappresentazione latente. Quando si decodificano latenti video, l'output è una sequenza di frame immagine. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeTiled/it.md)

---
**Source fingerprint (SHA-256):** `04136ba1abd0c74e780dc405f916a08b809630ae4f41c183049535488b40fd96`
