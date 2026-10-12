# TextEncodeZImageOmni

TextEncodeZImageOmni codifica un prompt testuale insieme a un massimo di tre immagini di riferimento opzionali in un formato di condizionamento per modelli di generazione di immagini. Il prompt viene tokenizzato e codificato con il modello CLIP, e ogni immagine collegata può essere elaborata opzionalmente da un encoder visivo e/o da un VAE, in modo che i riferimenti visivi siano incorporati insieme al testo. Questo nodo è contrassegnato come sperimentale.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `clip` | Il modello CLIP utilizzato per tokenizzare e codificare il prompt testuale. | CLIP | Sì |  |
| `image_encoder` | Un modello encoder visivo opzionale. Se fornito, viene utilizzato per codificare le immagini di input e gli embedding risultanti vengono aggiunti al condizionamento. | CLIP_VISION | No |  |
| `prompt` | Il prompt testuale da codificare. Supporta input su più righe e prompt dinamici. | STRING | Sì |  |
| `auto_resize_images` | Quando abilitato (predefinito: True), le immagini di input vengono ridimensionate automaticamente prima della codifica VAE, in modo che la loro area totale in pixel sia vicina a 1024x1024, con dimensioni arrotondate a multipli di 8. | BOOLEAN | Sì | True<br>False |
| `vae` | Un modello VAE opzionale. Se fornito, viene utilizzato per codificare le immagini di input in rappresentazioni latenti, che vengono aggiunte al condizionamento come latenti di riferimento. | VAE | No |  |
| `image1` | La prima immagine di riferimento opzionale. | IMAGE | No |  |
| `image2` | La seconda immagine di riferimento opzionale. | IMAGE | No |  |
| `image3` | La terza immagine di riferimento opzionale. | IMAGE | No |  |

**Nota:** Il nodo accetta un massimo di tre immagini (`image1`, `image2`, `image3`). Gli input `image_encoder` e `vae` vengono utilizzati solo quando è fornita almeno un'immagine; quando entrambi sono collegati, ciascuna immagine viene elaborata da entrambi. Quando `auto_resize_images` è True e un `vae` è collegato, le immagini vengono ridimensionate in modo che la loro area totale in pixel sia vicina a 1024x1024 prima della codifica. Se non viene fornita alcuna immagine, viene codificato solo il prompt testuale.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `CONDITIONING` | L'output di condizionamento finale. Contiene il prompt testuale codificato e, quando vengono fornite immagini, può includere embedding di immagini codificati, latenti di riferimento ed embedding di testo aggiuntivi derivati dal template segnaposto per immagini. | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeZImageOmni/it.md)

---
**Source fingerprint (SHA-256):** `b40a3150f536b6f37e2b53e6d9992fcb4fd32dceb540c0a76773a7ba1af9a7b8`
