# Codifica testo Qwen Image Edit Plus

Il nodo TextEncodeQwenImageEditPlus elabora un prompt testuale e fino a tre immagini opzionali per produrre dati di condizionamento per attività di generazione o modifica di immagini. Utilizza un template specializzato che chiede prima al modello di descrivere le caratteristiche principali delle immagini di input e poi di spiegare come l'istruzione testuale dell'utente dovrebbe modificarle, così che il risultato codificato comprenda sia le immagini sia la modifica richiesta. Quando viene fornito un VAE, il nodo crea anche latent di riferimento dalle immagini di input.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `clip` | Il modello CLIP utilizzato per la tokenizzazione e la codifica | CLIP | Sì | - |
| `prompt` | Istruzione testuale che descrive la modifica desiderata dell'immagine (supporta input multilinea e prompt dinamici) | STRING | Sì | - |
| `vae` | Modello VAE opzionale per generare latent di riferimento dalle immagini di input | VAE | No | - |
| `image1` | Prima immagine di input opzionale per l'analisi e la modifica | IMAGE | No | - |
| `image2` | Seconda immagine di input opzionale per l'analisi e la modifica | IMAGE | No | - |
| `image3` | Terza immagine di input opzionale per l'analisi e la modifica | IMAGE | No | - |

**Nota:** Quando viene fornito un VAE, il nodo genera latent di riferimento da tutte le immagini di input fornite. È possibile elaborare fino a tre immagini contemporaneamente. Le immagini vengono ridimensionate a un'area target di 384x384 pixel (proporzioni preservate) per l'elaborazione vision-language, e a dimensioni divisibili per 8 (con un'area target di 1024x1024 pixel) per la codifica VAE.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `CONDITIONING` | Dati di condizionamento codificati contenenti token testuali e latent di riferimento opzionali per la generazione di immagini | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEditPlus/it.md)

---
**Source fingerprint (SHA-256):** `5eea53a84045924b44d445244e6149b341188d22573aaaced87bac8a139dac96`
