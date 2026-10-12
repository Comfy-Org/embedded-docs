# Wan Da Immagine a Immagine

Il nodo Wan Image to Image genera un'immagine da una o due immagini di input e da un prompt testuale. Trasforma le immagini di input in base alla descrizione fornita, creando una nuova immagine che mantiene le proporzioni dell'input originale. L'immagine di output è fissata a 1,6 megapixel indipendentemente dalla dimensione dell'input.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Modello da utilizzare (predefinito: "wan2.5-i2i-preview"). | COMBO | Sì | "wan2.5-i2i-preview" |
| `image` | Modifica a immagine singola o fusione multi-immagine. Massimo 2 immagini. | IMAGE | Sì | - |
| `prompt` | Prompt che descrive gli elementi e le caratteristiche visive. Supporta inglese e cinese (predefinito: vuoto). | STRING | Sì | - |
| `negative_prompt` | Prompt negativo che descrive cosa evitare (predefinito: vuoto). | STRING | No | - |
| `seed` | Seed da utilizzare per la generazione (predefinito: 0). | INT | No | da 0 a 2147483647 |
| `watermark` | Indica se aggiungere una filigrana generata dall'IA al risultato (predefinito: false). | BOOLEAN | No | - |

**Nota:** questo nodo accetta esattamente 1 o 2 immagini di input. Se fornisci più di 2 immagini o nessuna immagine, il nodo restituirà un errore.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `image` | L'immagine generata in base alle immagini di input e ai prompt testuali. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToImageApi/it.md)

---
**Source fingerprint (SHA-256):** `e78e5fb43d92c839448d3449b89445fb5db081ee8c947e44edcc048b8740f45d`
