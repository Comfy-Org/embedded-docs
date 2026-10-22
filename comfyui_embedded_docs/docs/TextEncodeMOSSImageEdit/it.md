# Text Encode MOSS-Image Edit

Codifica un'istruzione di modifica insieme a immagini di riferimento in un conditioning per un LoRA di modifica MOSS-Image. Collega l'output come conditioning positivo ed esegui una seconda istanza con gli stessi riferimenti per quello negativo. I riferimenti vengono usati alla dimensione con cui arrivano, quindi scalali prima di collegarli. Questo nodo è contrassegnato come sperimentale in ComfyUI.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `clip` | Il modello CLIP che tokenizza l'istruzione e la codifica. | CLIP | Sì | - |
| `prompt` | L'istruzione che descrive la modifica. Supporta testo su più righe e prompt dinamici. | STRING | Sì | Qualsiasi testo |
| `vae` | Il VAE usato per codificare le immagini di riferimento in latenti di riferimento. | VAE | Sì | - |
| `edit_format` | Il layout con cui è stato addestrato il LoRA di modifica. Seleziona il metodo dei latenti di riferimento e se il text encoder vede anche i riferimenti. | COMBO | Sì | `"ai-toolkit"`<br>`"ai-toolkit (kv_cache off)"`<br>`"Moss-Image-Edit"` |
| `images` | Slot espandibile: collega una o più immagini di riferimento (`image_1`, `image_2`, ...). Ogni immagine viene usata alla dimensione con cui arriva, il suo canale alpha viene rimosso e viene codificata tramite VAE in un latente di riferimento. | IMAGE | Sì | 1 o più immagini |

**Nota:** Con `"ai-toolkit"` e `"ai-toolkit (kv_cache off)"` il text encoder vede anche ogni riferimento, ridimensionato a un massimo di 384x384 pixel e preceduto da un marcatore `Picture N:` nel prompt, così l'istruzione può farvi riferimento tramite numero. Con `"Moss-Image-Edit"` i riferimenti raggiungono il modello solo come latenti di riferimento e il text encoder vede solo l'istruzione. `"ai-toolkit (kv_cache off)"` mantiene inoltre i riferimenti in attenzione verso l'immagine in fase di generazione, quindi vengono ricalcolati a ogni passo di campionamento.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `conditioning` | L'istruzione codificata con i latenti di riferimento e il metodo dei latenti di riferimento corrispondente allegati. | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeMOSSImageEdit/it.md)

---
**Source fingerprint (SHA-256):** `30e4edbb129f647cdce4ec95f78c002ecdc9a4f8fc5a45f1477fdc555b541dae`
