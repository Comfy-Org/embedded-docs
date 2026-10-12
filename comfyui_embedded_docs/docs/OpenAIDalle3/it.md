# OpenAIDalle3

Genera immagini in modo sincrono tramite l'endpoint DALL·E 3 di OpenAI. Questo nodo accetta un prompt testuale e crea immagini corrispondenti utilizzando il modello DALL·E 3 di OpenAI, consentendo di specificare qualità, stile e dimensioni dell'immagine.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt testuale per DALL·E (predefinito: "") | STRING | Sì | - |
| `seed` | Non ancora implementato nel backend (predefinito: 0) | INT | No | 0 to 2147483647 |
| `quality` | Qualità dell'immagine (predefinito: "standard") | COMBO | No | "standard"<br>"hd" |
| `style` | Vivid spinge il modello a tendere verso la generazione di immagini iperrealistiche e drammatiche. Natural induce il modello a produrre immagini più naturali e meno iperrealistiche. (predefinito: "natural") | COMBO | No | "natural"<br>"vivid" |
| `size` | Dimensione dell'immagine (predefinito: "1024x1024") | COMBO | No | "1024x1024"<br>"1024x1792"<br>"1792x1024" |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `IMAGE` | L'immagine generata da DALL·E 3 | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle3/it.md)

---
**Source fingerprint (SHA-256):** `9077628610503d8c0afdd04e30dadac46106bd577d10f2d7aa10864db4430605`
