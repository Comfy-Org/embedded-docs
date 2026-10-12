# Codifica testo Ming Image Edit

Text Encode Ming Image Edit codifica un prompt testuale in conditioning per l'editing di immagini Ming, con la possibilità di includere immagini di riferimento. Il prompt e le immagini di riferimento vengono tokenizzati da un modello CLIP e, quando è collegato un VAE, le immagini di riferimento vengono anche codificate in frame latent che vengono aggiunti al conditioning.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `clip` | Il modello CLIP utilizzato per tokenizzare il prompt e le immagini di riferimento. | CLIP | Sì | - |
| `vae` | VAE opzionale che codifica le immagini di riferimento in frame latent aggiunti al conditioning. Senza un VAE, le immagini condizionano solo il text encoder tramite la vision tower. | VAE | No | - |
| `prompt` | Prompt testuale da codificare. Supporta input multilinea e prompt dinamici. | STRING | Sì | Testo multiriga |
| `images` | Slot espandibile: immagini di riferimento opzionali viste dal text encoder e aggiunte alla sequenza latent come frame puliti. Collega da 1 a 8 immagini (`image_1`, `image_2`, ...); le immagini successive vengono ridimensionate sulla prima e il latent campionato dovrebbe corrispondere alle sue dimensioni. Vengono utilizzati solo i canali RGB. | IMAGE | No | 0 to 8 |

**Nota:** Le immagini di riferimento vengono lette in ordine numerico in base ai nomi dei rispettivi slot e gli slot vuoti vengono ignorati. I latent di riferimento vengono prodotti solo quando vengono forniti sia `vae` sia almeno un'immagine.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `CONDITIONING` | Conditioning contenente il prompt codificato, più i latent di riferimento quando vengono forniti un VAE e immagini di riferimento. | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeMingImageEdit/it.md)

---
**Source fingerprint (SHA-256):** `675fb3cc0af006e1284fdb2a5ca2c268c540ee92e1ede90b2359f4e3fc8ba5ea`
