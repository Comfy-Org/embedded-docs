# Google Gemini Decision (Choice)

Scegli una delle tue opzioni per il testo, le immagini, l'audio o il video che colleghi, e ottieni l'opzione scelta, la sua posizione e una confidenza. Collega `choice` a un nodo Branch i cui input portano gli stessi nomi delle opzioni, oppure instrada su `option_index` quando un nodo Branch non è disponibile.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modello da utilizzare (predefinito: `"gemini-decision-1"`). | COMBO | Sì | `"gemini-decision-1"` |
| `question` | La domanda a cui rispondono le opzioni, fino a 5000 caratteri (predefinito: "What style is the image?"). | STRING | Sì | 1 a 5000 caratteri |
| `options` | Un'opzione per riga, utilizzata esattamente come digitata, fino a 128 caratteri ciascuna. Aggiungi un'opzione come `other` per gli input che non rientrano in nessuna di esse (predefinito: `photo`, `illustration`, `3d render`, `anime`, `sketch`, `other`). | STRING | Sì | 2 a 255 opzioni |
| `images` | Immagini da classificare, fino a 16 attraverso gli slot espandibili (`image_1` ... `image_16`). Un'immagine raggruppata in batch conta una volta per immagine. | IMAGE | No | Fino a 16 immagini |
| `audio` | Clip audio da classificare. | AUDIO | No | - |
| `video` | Clip video da classificare. | VIDEO | No | - |
| `text` | Testo a cui si riferisce la domanda, come un prompt o una risposta di un LLM, fino a 20000 caratteri. | STRING | No | Fino a 20000 caratteri |

Fornisci almeno 2 e al massimo 255 opzioni, senza elencarne nessuna due volte; in caso contrario il nodo genera un errore. Collega almeno uno tra `text`, `images`, `audio` o `video` e assegna un nome a più immagini come `image_1`, `image_2` e così via all'interno della domanda.

## Output

| Nome dell'output | Descrizione | Tipo di dato |
|-------------|-------------|-----------|
| `choice` | L'opzione scelta, esattamente come è stata scritta in `options`. | STRING |
| `option_index` | Posizione dell'opzione scelta in `options`, a partire da 0. | INT |
| `confidence` | Confidenza nella scelta, compresa tra 0 e 1. | FLOAT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionChoice/it.md)

---
**Source fingerprint (SHA-256):** `200c63a9197cd95ba0a21da88c5f3117014b37b0651541094a775219381afe43`
