# Comfy Cloud Mage Flow Da testo a immagine [BETA]

Questo nodo genera un'immagine da un prompt testuale inviando la richiesta al workflow text-to-image di Mage-Flow in Comfy Cloud. Esegue il passaggio di generazione completo a 30 step invece del più veloce passaggio turbo distillato e accetta un prompt negativo, così puoi descrivere i contenuti che non vuoi nell'immagine finale. Il prompt negativo è supportato in questa modalità a 30 step; secondo il riepilogo del nodo, la variante turbo distillata non è in grado di sfruttarlo adeguatamente.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `prompt` | La descrizione testuale dell'immagine da generare. | STRING | Sì | Testo libero |
| `negative_prompt` | Testo che descrive il contenuto che non deve apparire nell'immagine generata. Questo input viene usato durante il passaggio di generazione standard a 30 step, ma la variante turbo distillata non sfrutta bene i prompt negativi. | STRING | No | Testo libero |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `image` | L'immagine generata dal prompt testuale e dal prompt negativo forniti. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMageFlowTextToImageNode/it.md)

---
**Source fingerprint (SHA-256):** `80f4ecf1df3f2c46d94138f8ada817e12cc49e69e69a001630776ed644868367`
