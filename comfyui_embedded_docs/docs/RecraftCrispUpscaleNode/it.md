# Recraft Crisp Upscale Image

Questo nodo esegue l'upscaling di un'immagine in modo sincrono utilizzando lo strumento "crisp upscale". Migliora una data immagine raster aumentandone la risoluzione, rendendo l'immagine più nitida e pulita. Quando viene fornito un batch di immagini, ogni immagine viene elaborata indipendentemente e i risultati ottenuti dall'upscaling vengono restituiti come batch.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `image` | L'immagine di input da sottoporre a upscaling. Accetta un batch di immagini; ogni immagine viene elaborata indipendentemente. | IMAGE | Sì | — |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `image` | L'immagine sottoposta a upscaling, con risoluzione e chiarezza migliorate. Restituisce un batch di immagini se in input è stato fornito un batch. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftCrispUpscaleNode/it.md)

---
**Source fingerprint (SHA-256):** `7a60c563504df7a81ce5d50e989bc4a8853f4bb30805a014c9fb567d8ec83e33`
