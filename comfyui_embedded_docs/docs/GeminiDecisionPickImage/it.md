# Google Gemini Decision (Pick Image)

Scegli l'immagine migliore da un batch. Collega `index` a Get Image from Batch per mantenere l'immagine scelta, in modo che il resto del workflow venga eseguito solo sull'immagine selezionata.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Modello da utilizzare (predefinito: `"gemini-decision-1"`). | COMBO | Sì | `"gemini-decision-1"` |
| `question` | Quale immagine scegliere (predefinito: "Which image best matches the prompt in text? If there is no text, which image has the best quality?"). | STRING | Sì | 1 a 5000 caratteri |
| `images` | Le immagini tra cui scegliere, come batch o come singolo batch di frame. | IMAGE | Sì | 2 a 64 immagini |
| `text` | Testo a cui si riferisce la domanda, ad esempio il prompt con cui sono state create le immagini, fino a 20000 caratteri. | STRING | No | Fino a 20000 caratteri |

Il nodo richiede da 2 a 64 immagini e genera un errore con una singola immagine. Collega `text` quando la scelta deve seguire un prompt anziché basarsi solo sulla qualità dell'immagine.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `index` | Posizione dell'immagine selezionata nel batch, a partire da 0. | INT |
| `confidence` | Confidenza nella scelta, tra 0 e 1. | FLOAT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiDecisionPickImage/it.md)

---
**Source fingerprint (SHA-256):** `55eb604923cb66b42f23f37d0c710a97033cc2c5d95880d45397bba10e44dab0`
