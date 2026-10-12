# Applica Wan Uni3C ControlNet

## Panoramica

Questo nodo applica una ControlNet Uni3C a un modello di diffusione video Wan, utilizzando un video di guida renderizzato (ad esempio, render di nuvole di punti deformate) per influenzare l'output del modello. Inietta segnali di controllo in specifici layer a blocchi, consentendo una guida basata sulla traiettoria della camera durante la generazione video.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello di diffusione Wan da patchare. | MODEL | Sì | – |
| `model_patch` | Una patch ControlNet Uni3C (deve essere un'istanza di `comfy.ldm.wan.uni3c.WanUni3CControlnet`). | MODEL_PATCH | Sì | – |
| `vae` | Il VAE utilizzato per codificare il video di guida in latenti. | VAE | Sì | – |
| `render_video` | Il video di guida renderizzato dalla traiettoria della camera, più comunemente render di nuvole di punti deformate dell'immagine di input. | IMAGE | Sì | – |
| `strength` | L'intensità del segnale di controllo applicato. | FLOAT | Sì | da -10.0 a 10.0 (predefinito: 1.0) |
| `start_percent` | La percentuale del processo di denoising in cui inizia il controllo. | FLOAT | Sì | da 0.0 a 1.0 (predefinito: 0.0) |
| `end_percent` | La percentuale del processo di denoising in cui termina il controllo. | FLOAT | Sì | da 0.0 a 1.0 (predefinito: 1.0) |

**Note:**
- Il `model_patch` deve essere una ControlNet Uni3C; in caso contrario, il nodo genera un errore.
- La ControlNet Uni3C funziona solo con modelli Wan; viene generato un errore se il modello non è basato su Wan.
- La dimensione interna della ControlNet deve corrispondere alla dimensione del modello Wan – viene generato un errore se differiscono.
- Si prevede che l'immagine di input `render_video` sia in formato RGB (vengono usati solo i primi 3 canali).
- Questo nodo è sperimentale.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `MODEL` | Il modello Wan patchato con la ControlNet Uni3C applicata. | MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanUni3CControlnetApply/it.md)

---
**Source fingerprint (SHA-256):** `f69253f06aba9208778f713ad36e9995f53a15d2e61243b853b9ac9131637371`
