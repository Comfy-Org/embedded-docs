# TypeSafe Jev (Choice)

Il nodo TypeSafe Jev (Choice) seleziona una delle opzioni definite dall'utente per testo, immagini o entrambi i tipi di input collegati. Collega `choice` a un nodo Branch i cui input riportano i nomi delle opzioni, oppure usa `option_index` per commutare in base alla posizione dell'opzione scelta. Questo è un nodo API e richiede un account Comfy.org e una chiave API.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Modello Jev da usare. Attualmente è disponibile un solo modello: `jev-1.14.0`. | COMBO | Sì | `"jev-1.14.0"` |
| `question` | La domanda a cui rispondono le opzioni. Con più socket per immagini, usa i loro nomi, ad esempio `Which season is shown in image_1?` (predefinito: `What style is the image?`). | STRING | Sì | Da 1 a 1000 caratteri |
| `options` | Le opzioni tra cui scegliere, una per riga. Aggiungi un'opzione come `other` per gli input che non corrispondono a nessuna di esse (predefinito: `photo`, `illustration`, `3d render`, `anime`, `sketch` e `other`, una per riga). | STRING | Sì | Da 2 a 50 opzioni, fino a 40 caratteri ciascuna |
| `images` | Le immagini a cui si riferisce la domanda. Fino a 32 immagini in totale; un input in batch conta una volta per immagine e più di 4 immagini vengono inviate a dimensione ridotta. | AUTOGROW | No | 0 a 32 immagini |
| `text` | Il testo a cui si riferisce la domanda, ad esempio un prompt o una risposta di un LLM. | STRING | No | 0 a 3000 caratteri |

**Note:**

- Collega il testo o almeno un'immagine; il nodo genera un errore quando entrambi sono vuoti.
- Il nodo genera un errore quando vengono fornite meno di 2 o più di 50 opzioni, quando un'opzione è più lunga di 40 caratteri oppure quando due opzioni differiscono solo per maiuscole/minuscole.
- `option_index` parte da 0, quindi la prima opzione dell'elenco ha indice 0.
- La fatturazione si basa sui token; il badge del prezzo sul nodo mostra la tariffa approssimativa per 1M token.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `choice` | L'opzione scelta, scritta esattamente come appare in `options`. | STRING |
| `option_index` | Posizione dell'opzione scelta nell'elenco delle opzioni, a partire da 0. | INT |
| `confidence` | Il livello di certezza di Jev, da 0 (nessun chiaro vincitore) a 1 (certezza). | FLOAT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevChoice/it.md)

---
**Source fingerprint (SHA-256):** `b1cd36d600f5c07935c455d9e926e6c0a53f172fcc1a6f602c8d4dc70eeffabe`
