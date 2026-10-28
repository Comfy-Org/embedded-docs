# Carica Modello di Ingrandimento Latent

Il nodo LatentUpscaleModelLoader carica un modello specializzato nell'upscaling delle rappresentazioni latenti da un file memorizzato nella cartella `latent_upscale_models` di ComfyUI. Rileva automaticamente l'architettura del modello dal contenuto del file (Hunyuan Video 720p, Hunyuan Video 1080p o un Latent Upsampler) e configura il modello interno corrispondente, così il risultato è pronto per essere utilizzato da altri nodi.Rileva anche i modelli di upscale latente MiniMax H3 e configura per essi l'upscaler latente MiniMax H3.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model_name` | Il nome del file del modello di upscale latente da caricare. Le opzioni disponibili vengono popolate dinamicamente dai file presenti nella directory `latent_upscale_models` di ComfyUI. | COMBO | Sì | Tutti i file nella cartella `latent_upscale_models` |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `model` | Il modello di upscale latente caricato, configurato e pronto all'uso. A seconda del contenuto del file rilevato, può essere un upscaler per Hunyuan Video 720p, un upscaler per Hunyuan Video 1080p o un modello Latent Upsampler incapsulato.Un modello di upscale latente MiniMax H3 viene caricato come upscaler latente MiniMax H3. | LATENT_UPSCALE_MODEL |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleModelLoader/it.md)

---
**Source fingerprint (SHA-256):** `3de8e009e6ce777815db462117cdebf57842cdc6dd43b6760490e5d9ef8ed138`
