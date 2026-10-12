# WaveSpeed Image Upscale

Il nodo WaveSpeed Image Upscale utilizza un servizio AI esterno per aumentare la risoluzione e la qualità di un'immagine. Prende in input una singola foto e la ingrandisce fino a una risoluzione target superiore, come 2K, 4K o 8K, producendo un risultato più nitido e dettagliato.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello AI da utilizzare per l'upscaling. "SeedVR2" e "Ultimate" offrono diversi livelli di qualità e prezzo. | STRING | Sì | `"SeedVR2"`<br>`"Ultimate"` |
| `image` | L'immagine di input da ingrandire. È richiesta esattamente un'immagine. | IMAGE | Sì | |
| `target_resolution` | La risoluzione di output desiderata per l'immagine ingrandita. | STRING | Sì | `"2K"`<br>`"4K"`<br>`"8K"` |

**Nota:** Questo nodo richiede esattamente un'immagine di input. Fornire un batch di immagini comporterà un errore.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `image` | L'immagine di output ingrandita ad alta risoluzione. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WavespeedImageUpscaleNode/it.md)

---
**Source fingerprint (SHA-256):** `1d715431efb690d30d9fc3b4769047a9d568b49c62eb318615e2748c780b8c20`
