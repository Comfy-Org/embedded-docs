# Text Encode MOSS-Image Edit

Codifica un'istruzione di modifica insieme a immagini di riferimento in un conditioning per un LoRA di modifica MOSS-Image. Collega l'output come conditioning positivo ed esegui una seconda istanza con gli stessi riferimenti per quello negativo. I riferimenti vengono usati alla dimensione con cui arrivano, quindi scalali prima di collegarli. Questo nodo è contrassegnato come sperimentale in ComfyUI. Senza VAE, le immagini vanno solo al text encoder.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `clip` | Il modello CLIP che tokenizza l'istruzione e la codifica. | CLIP | Sì | - |
| `prompt` | L'istruzione che descrive la modifica. Supporta testo su più righe e prompt dinamici. | STRING | Sì | Qualsiasi testo |
| `vae` | Il VAE usato per codificare le immagini di riferimento in latenti di riferimento. Opzionale: senza di esso, le immagini vanno solo al text encoder.| VAE | No | - |
| `edit_format` | Il layout con cui è stato addestrato il LoRA di modifica. Seleziona il metodo dei latenti di riferimento e se il text encoder vede anche i riferimenti. | COMBO | Sì | `"ai-toolkit"`<br>`"ai-toolkit (kv_cache off)"`<br>`"Moss-Image-Edit"` |
| `images` | Slot espandibile: collega una o più immagini di riferimento (`image_1`, `image_2`, ...). Ogni immagine viene usata alla dimensione con cui arriva, il suo canale alpha viene rimosso e viene codificata tramite VAE in un latente di riferimento. Con un VAE collegato l’alpha viene rimosso e ogni immagine è codificata in un latente di riferimento; senza VAE le immagini vanno solo al text encoder.| IMAGE | Sì | 1 o più immagini |
| `image_strength` | Scala quanto il modello presta attenzione alle immagini viste dal text encoder (formati ai-toolkit, o senza VAE): 0 le ignora, 1 invariato, sopra 1 le enfatizza. Avanzato. Predefinito: 1.0. | FLOAT | Sì | 0.0 to 100.0 (step 0.05) |

**Nota:** With `"ai-toolkit"` and `"ai-toolkit (kv_cache off)"`, or when no VAE is connected and `image_strength` is above 0, the text encoder also sees every reference, downscaled to at most 384x384 pixels and preceded by a `Picture N:` marker in the prompt, so the instruction can refer to them by number. With `"Moss-Image-Edit"` and a VAE connected, the references reach the model only as reference latents and the text encoder sees the instruction alone. `"ai-toolkit (kv_cache off)"` additionally keeps the references attending to the image being generated, so they are recomputed on every sampling step.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `conditioning` | L'istruzione codificata con i latenti di riferimento e il metodo dei latenti di riferimento corrispondente allegati. | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeMOSSImageEdit/it.md)

---
**Source fingerprint (SHA-256):** `673f098df6a8e466a5c8060009f446eac8f7556311a870de626c5f4bfc3ab196`
