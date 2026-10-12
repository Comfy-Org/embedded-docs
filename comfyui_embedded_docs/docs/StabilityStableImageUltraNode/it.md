# StabilityStableImageUltraNode

Genera immagini in modo sincrono in base al prompt e alla risoluzione. Questo nodo crea immagini utilizzando il modello Stable Image Ultra di Stability AI, elaborando il prompt testuale e generando un'immagine corrispondente con le proporzioni e lo stile specificati.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Cosa desideri vedere nell'immagine di output. Un prompt forte e descrittivo che definisca chiaramente elementi, colori e soggetti porterà a risultati migliori. Per controllare il peso di una determinata parola usa il formato `(word:weight)`, dove `word` è la parola di cui vuoi controllare il peso e `weight` è un valore tra 0 e 1. Ad esempio: `The sky was a crisp (blue:0.3) and (green:0.8)` trasmetterebbe un cielo blu e verde, ma più verde che blu. | STRING | Sì | - |
| `aspect_ratio` | Proporzioni dell'immagine generata (predefinito: "1:1"). | COMBO | Sì | `"1:1"`<br>`"16:9"`<br>`"21:9"`<br>`"2:3"`<br>`"3:2"`<br>`"4:5"`<br>`"5:4"`<br>`"9:16"`<br>`"9:21"` |
| `style_preset` | Stile desiderato opzionale dell'immagine generata. Seleziona "None" per non applicare alcun preset di stile. | COMBO | No | `"3d-model"`<br>`"analog-film"`<br>`"anime"`<br>`"cinematic"`<br>`"comic-book"`<br>`"digital-art"`<br>`"enhance"`<br>`"fantasy-art"`<br>`"isometric"`<br>`"line-art"`<br>`"low-poly"`<br>`"modeling-compound"`<br>`"neon-punk"`<br>`"origami"`<br>`"photographic"`<br>`"pixel-art"`<br>`"tile-texture"` |
| `seed` | Il seed casuale utilizzato per creare il rumore. | INT | Sì | 0 - 4294967294 |
| `image` | Immagine di input opzionale per la generazione image-to-image. | IMAGE | No | - |
| `negative_prompt` | Un testo che descrive ciò che non desideri vedere nell'immagine di output. Questa è una funzionalità avanzata. | STRING | No | - |
| `image_denoise` | Denoise dell'immagine di input; 0.0 produce un'immagine identica all'input, 1.0 equivale a non aver fornito alcuna immagine (predefinito: 0.5). | FLOAT | No | 0.0 - 1.0 |

**Nota:** Quando non viene fornita un'immagine di input, il parametro `image_denoise` viene automaticamente disabilitato e ignorato.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `output` | L'immagine generata in base ai parametri di input. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityStableImageUltraNode/it.md)

---
**Source fingerprint (SHA-256):** `86a9ace60a1f9f2b872865381c695bd0e3e3578e0dd3453f1ab3be58bae2e2f0`
