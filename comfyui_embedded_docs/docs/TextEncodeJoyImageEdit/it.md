# TextEncodeJoyImageEdit

Questo nodo codifica un prompt testuale e immagini opzionali in dati di condizionamento per l'uso con i modelli JoyImage. Combina un codificatore di testo CLIP con input di immagini opzionali per creare un condizionamento ricco che può guidare attività di generazione o modifica delle immagini.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `clip` | Il modello CLIP utilizzato per codificare il prompt testuale | CLIP | Sì | - |
| `prompt` | Il prompt testuale da codificare, con supporto all'input multilinea e ai prompt dinamici | STRING | Sì | - |
| `vae` | Un modello VAE per codificare le immagini nello spazio latente | VAE | No | - |
| `images` | Immagini opzionali da includere nel condizionamento, fino a un massimo di 6 immagini. Ogni immagine si collega come input separato (da image_0 a image_5) | IMAGE | No | da 0 a 6 immagini |

L'input `images` è un gruppo autogrow che accetta da 0 a 6 immagini. Quando non sono collegate immagini, il condizionamento si basa solo sul prompt testuale.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `CONDITIONING` | I dati di condizionamento codificati che combinano il prompt testuale e le eventuali immagini fornite | CONDITIONING |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeJoyImageEdit/it.md)

---
**Source fingerprint (SHA-256):** `ef48523aa9fc990b2839d755cef272bcdfbacef5af8d961736fde5200c6f082d`
