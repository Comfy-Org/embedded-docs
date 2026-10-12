# StabilityUpscaleCreativeNode

Esegue l'upscale dell'immagine con modifiche minime alla risoluzione 4K. Questo nodo utilizza la tecnologia di upscaling creativo di Stability AI per migliorare la risoluzione dell'immagine preservando il contenuto originale e aggiungendo sottili dettagli creativi.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | L'immagine di input da sottoporre a upscale | IMAGE | Sì | - |
| `prompt` | Ciò che desideri vedere nell'immagine di output. Un prompt forte e descrittivo che definisca chiaramente elementi, colori e soggetti porterà a risultati migliori. (predefinito: stringa vuota) | STRING | Sì | - |
| `creativity` | Controlla la probabilità di creare dettagli aggiuntivi non strettamente condizionati dall'immagine iniziale. (predefinito: 0.3) | FLOAT | Sì | 0.1-0.5 |
| `style_preset` | Stile desiderato opzionale per l'immagine generata. (predefinito: "None") | STRING | Sì | `"3d-model"`<br>`"analog-film"`<br>`"anime"`<br>`"cinematic"`<br>`"comic-book"`<br>`"digital-art"`<br>`"enhance"`<br>`"fantasy-art"`<br>`"isometric"`<br>`"line-art"`<br>`"low-poly"`<br>`"modeling-compound"`<br>`"neon-punk"`<br>`"origami"`<br>`"photographic"`<br>`"pixel-art"`<br>`"tile-texture"` |
| `seed` | Il seed casuale utilizzato per creare il rumore. (predefinito: 0) | INT | Sì | 0-4294967294 |
| `negative_prompt` | Parole chiave di ciò che non desideri vedere nell'immagine di output. Questa è una funzionalità avanzata. (predefinito: stringa vuota) | STRING | No | - |

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `image` | L'immagine sottoposta a upscale alla risoluzione 4K | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityUpscaleCreativeNode/it.md)

---
**Source fingerprint (SHA-256):** `dc9bfacee3bfa663cff22cd0bcef6759f7808e2ae8e19526de28d55a3bef26e6`
