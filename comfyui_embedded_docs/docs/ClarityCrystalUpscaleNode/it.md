# ClarityCrystalUpscaleNode

Esegui l'upscale di un'immagine con Crystal Upscaler di Clarity AI, un upscaler ad alta fedeltà che rimane fedele all'originale mentre ripristina volti, pelle e texture fini. L'immagine viene inviata all'API di Clarity AI e il risultato ingrandito viene restituito come immagine.

Selezionando un `model` vengono mostrati i parametri specifici di quel modello.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Modello da utilizzare. Selezionando un modello vengono mostrati i parametri specifici: `image`, `scale_factor` e `creativity`. | DYNAMIC_COMBO | Sì | `"crystal-upscaler"` |
| `image` | L'immagine da sottoporre a upscale. Deve contenere esattamente un'immagine; i batch di immagini non sono supportati. | IMAGE | Sì | N/A |
| `scale_factor` | Fattore per cui moltiplicare la larghezza e l'altezza dell'immagine. L'output è limitato a 100 megapixel (predefinito: 2.0). | FLOAT | Sì | 1.0 a 200.0 (passo 0.1) |
| `creativity` | Valori più alti consentono al modello di ricostruire più dettagli invece di preservare rigorosamente l'originale. Non ha alcun effetto sulle immagini il cui lato più corto è pari o inferiore a 256 pixel (predefinito: 0). | INT | Sì | 0 a 10 |

**Nota:** L'immagine di input deve essere di almeno 2x2 pixel. L'output è limitato a 100 megapixel e 65535 pixel per lato; un risultato più grande genera un errore, quindi usa un'immagine più piccola o un `scale_factor` inferiore.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `IMAGE` | L'immagine con upscale. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClarityCrystalUpscaleNode/it.md)

---
**Source fingerprint (SHA-256):** `38c90cf7054a93477ee63c356c3fdf8ba38c7edaf1a337da7ac366cd9d746d9e`
