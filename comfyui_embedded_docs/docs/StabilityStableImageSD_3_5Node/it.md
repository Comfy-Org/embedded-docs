# StabilityStableImageSD_3_5Node

Questo nodo genera immagini in modo sincrono utilizzando il modello Stable Diffusion 3.5 di Stability AI. Crea immagini basate su prompt testuali e può anche modificare immagini esistenti quando vengono fornite come input. Il nodo supporta vari rapporti d'aspetto e preset di stile per personalizzare l'output.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | Ciò che desideri vedere nell'immagine di output. Un prompt forte e descrittivo che definisca chiaramente elementi, colori e soggetti porterà a risultati migliori. (predefinito: stringa vuota) | STRING | Sì | - |
| `model` | Il modello Stable Diffusion 3.5 da utilizzare per la generazione. | COMBO | Sì | `sd3.5-large`<br>`sd3.5-large-turbo`<br>`sd3.5-medium` |
| `aspect_ratio` | Rapporto d'aspetto dell'immagine generata. (predefinito: 1:1) | COMBO | Sì | `16:9`<br>`1:1`<br>`21:9`<br>`2:3`<br>`3:2`<br>`4:5`<br>`5:4`<br>`9:16`<br>`9:21` |
| `style_preset` | Stile desiderato opzionale dell'immagine generata. Seleziona `None` per nessun preset di stile. | COMBO | No | `3d-model`<br>`analog-film`<br>`anime`<br>`cinematic`<br>`comic-book`<br>`digital-art`<br>`enhance`<br>`fantasy-art`<br>`isometric`<br>`line-art`<br>`low-poly`<br>`modeling-compound`<br>`neon-punk`<br>`origami`<br>`photographic`<br>`pixel-art`<br>`tile-texture`<br>`None` |
| `cfg_scale` | Quanto rigorosamente il processo di diffusione aderisce al testo del prompt (valori più alti mantengono l'immagine più vicina al prompt). (predefinito: 4.0) | FLOAT | Sì | da 1.0 a 10.0 |
| `seed` | Il seed casuale utilizzato per creare il rumore. (predefinito: 0) | INT | Sì | da 0 a 4294967294 |
| `image` | Immagine di input opzionale per la generazione image-to-image. Quando viene fornita, il nodo passa alla modalità image-to-image e il parametro `aspect_ratio` viene ignorato. | IMAGE | No | - |
| `negative_prompt` | Parole chiave di ciò che non desideri vedere nell'immagine di output. Questa è una funzionalità avanzata. (predefinito: stringa vuota) | STRING | No | - |
| `image_denoise` | Denoise dell'immagine di input; 0.0 restituisce un'immagine identica a quella di input, 1.0 equivale a non aver fornito alcuna immagine. (predefinito: 0.5) Questo parametro viene utilizzato solo quando viene fornita un'`image`. | FLOAT | No | da 0.0 a 1.0 |

**Nota:** Quando viene fornita un'`image`, il nodo passa alla modalità di generazione image-to-image e il parametro `aspect_ratio` viene determinato automaticamente dall'immagine di input. Quando non viene fornita alcuna `image`, il parametro `image_denoise` viene ignorato.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `image` | L'immagine generata o modificata. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityStableImageSD_3_5Node/it.md)

---
**Source fingerprint (SHA-256):** `0ef029d4651fb4a9132899a6df1a2c2de6152dd9091129573f366a2aac39bbae`
