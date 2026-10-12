# Codifica testo Qwen Image 2.1

Il nodo TextEncodeQwenImage21 codifica un prompt e un negative prompt per il modello Qwen-Image 2.1, allegando facoltativamente immagini di riferimento. Le immagini di riferimento vengono viste dal text encoder e, quando è collegato un VAE, vengono anche codificate come latent che sono inseriti nella sequenza, così il conditioning trasporta sia l'istruzione testuale sia il riferimento visivo. Il nodo restituisce il conditioning positive e negative insieme a un latent vuoto dimensionato sulla prima immagine di riferimento, pronto per il campionamento.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Range |
| --- | --- | --- | --- | --- |
| `clip` | Il text encoder Qwen-Image 2.1 usato per tokenizzare e codificare i prompt. | CLIP | Sì | - |
| `prompt` | Prompt testuale che descrive l'immagine da generare o la modifica da applicare. Supporta input multilinea e prompt dinamici. | STRING | Sì | Qualsiasi testo |
| `negative_prompt` | Prompt testuale che descrive ciò che il risultato deve evitare. Supporta input multilinea e prompt dinamici. | STRING | Sì | Qualsiasi testo |
| `vae` | VAE usato per codificare le immagini di riferimento in latent di riferimento. Se omesso, le immagini di riferimento condizionano il risultato solo tramite il text encoder. | VAE | No | - |
| `resolution` | Le immagini di riferimento vengono ridimensionate a circa `resolution` x `resolution` pixel, in multipli di 32, preservando le proporzioni. 0 mantiene ogni riferimento alla propria dimensione, arrotondata a un multiplo di 32 (predefinito: 1024). | INT | Sì | Da 0 a 4096 (passo 32) |
| `images` | Immagini di riferimento, viste dal text encoder e inserite nella sequenza come latent VAE. Slot espandibile: collega fino a 16 immagini (`image_1` ... `image_16`). | IMAGE | No | Da 0 a 16 immagini |

Il latent vuoto in output è dimensionato sulla prima immagine di riferimento collegata, oppure su `resolution` quando non è collegata alcuna immagine di riferimento. Campiona sul latent restituito da questo nodo: qualsiasi altra dimensione altera la modifica. Quando è collegato un VAE, gli stessi latent di riferimento vengono associati sia al conditioning positive sia a quello negative, così un singolo passo del sampler può eseguire il denoising di entrambi.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `positive` | Conditioning codificato per il prompt, che trasporta i latent di riferimento quando è collegato un VAE. | CONDITIONING |
| `negative` | Conditioning codificato per il negative prompt, con gli stessi latent di riferimento. | CONDITIONING |
| `latent` | Latent vuoto della dimensione della prima immagine di riferimento, oppure 1024 x 1024 quando non è collegata alcuna immagine di riferimento. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImage21/it.md)

---
**Source fingerprint (SHA-256):** `3870f04597d12b593498c12ca139428af2d717b65aa40c889de9373ae9eb475e`
