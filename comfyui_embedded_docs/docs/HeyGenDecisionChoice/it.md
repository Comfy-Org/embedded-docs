# HeyGen Decision (Choice)

Scegli una delle tue opzioni per il testo, le immagini, l'audio o il video che colleghi e ricevi indietro l'opzione scelta, la sua posizione e un livello di confidenza. Collega `choice` a un nodo Branch i cui input hanno gli stessi nomi delle opzioni, oppure instrada su `option_index`.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Modello da utilizzare. `heygen-decision-1-turbo` è più veloce e costa meno di `heygen-decision-1` (predefinito: `"heygen-decision-1"`). | COMBO | Sì | `"heygen-decision-1"`<br>`"heygen-decision-1-turbo"` |
| `question` | La domanda a cui rispondono le opzioni, fino a 5000 caratteri (predefinito: "What style is the image?"). | STRING | Sì | Da 1 a 5000 caratteri |
| `options` | Un'opzione per riga, usata esattamente come digitata, fino a 128 caratteri ciascuna. Aggiungi un'opzione come `other` per gli input che non rientrano in nessuna di esse (predefinito: `photo`, `illustration`, `3d render`, `anime`, `sketch`, `other`). | STRING | Sì | Da 2 a 255 opzioni |
| `images` | Immagini da classificare, fino a 4 in totale, contando ogni frame di un batch. Sono numerate da `image_1` a `image_4` in ordine attraverso i socket. | IMAGE | No | Fino a 4 immagini |
| `audio_1` | Audio da classificare, fino a 30 minuti. | AUDIO | No | Fino a 30 minuti |
| `video_1` | Video da classificare, fino a 60 secondi. | VIDEO | No | Fino a 60 secondi |
| `text` | Testo a cui si riferisce la domanda, ad esempio un prompt o una risposta di un LLM, fino a 20000 caratteri. | STRING | No | Fino a 20000 caratteri |

Fornisci da 2 a 255 opzioni, nessuna duplicata e nessuna che differisca solo per maiuscole/minuscole, altrimenti il nodo genera un errore. Collega almeno un input da classificare e nominalo in base al socket all'interno della domanda, ad esempio "Quale stagione è mostrata in image_1?".

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `choice` | L'opzione scelta, esattamente come scritta in `options`. | STRING |
| `option_index` | Posizione dell'opzione scelta in `options`, a partire da 0. | INT |
| `confidence` | Confidenza nella scelta, tra 0 e 1. | FLOAT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenDecisionChoice/it.md)

---
**Source fingerprint (SHA-256):** `dd21b3b8021b8917e7ee4d120471974634ae6771ff17b0f49e9460f82a2fbe78`
