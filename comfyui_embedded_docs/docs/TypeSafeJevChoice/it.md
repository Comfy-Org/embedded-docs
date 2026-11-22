# TypeSafe Jev (Choice)

Il nodo TypeSafe Jev (Choice) sceglie una delle opzioni definite dall'utente per testo, immagini o entrambi collegati. Collega `choice` a un nodo Branch i cui input riportano i nomi delle opzioni, oppure usa `option_index` per instradare in base alla posizione dell'opzione scelta. Un nodo Branch accetta al massimo 32 input, quindi un elenco con più opzioni di così può essere instradato solo tramite `option_index`. Questo è un nodo API: viene eseguito sui server di Comfy e richiede un account Comfy.org con crediti.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Modello Jev da usare. Attualmente è disponibile un solo modello: `jev-1.14.0`. | COMBO | Sì | `"jev-1.14.0"` |
| `question` | La domanda a cui rispondono le opzioni. Con più socket per immagini, usa i loro nomi, ad esempio `Which season is shown in image_1?` (predefinito: `What style is the image?`). | STRING | Sì | 1 a 1000 caratteri |
| `options` | Le opzioni tra cui scegliere, una per riga. Gli spazi iniziali e finali vengono rimossi da ogni riga e le opzioni devono essere univoche ignorando maiuscole/minuscole, quindi un'opzione ripetuta o due opzioni che differiscono solo per maiuscole/minuscole vengono rifiutate. Aggiungi un'opzione come `other` per input che non rientrano in nessuna di esse (predefinito: `photo`, `illustration`, `3d render`, `anime`, `sketch` e `other`, una per riga). | STRING | Sì | 2 a 50 opzioni, fino a 40 caratteri ciascuna |
| `images` | Le immagini a cui si riferisce la domanda. Fino a 32 immagini in totale; un input in batch conta una volta per immagine. Il lato lungo di ogni immagine è limitato dal numero totale di immagini: 1568 px per un massimo di 4 immagini, 1024 px per un massimo di 8, 768 px per un massimo di 16 e 512 px per un massimo di 32, quindi un batch più grande può ridurre il dettaglio in ogni immagine. | AUTOGROW | No | 0 a 32 immagini |
| `text` | Il testo a cui si riferisce la domanda, come un prompt o una risposta LLM. | STRING | No | 0 a 3000 caratteri |

**Note:**

- Collega del testo o almeno un'immagine; il nodo genera un errore quando entrambi sono vuoti.
- Il nodo genera un errore quando vengono fornite meno di 2 o più di 50 opzioni, quando un'opzione è più lunga di 40 caratteri o quando due opzioni sono uguali ignorando maiuscole/minuscole.
- `option_index` conta da 0, quindi la prima opzione dell'elenco ha indice 0.
- La fatturazione è basata su token; il badge del prezzo sul nodo mostra la tariffa approssimativa per 1M token.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `choice` | L'opzione scelta, con gli spazi iniziali e finali rimossi. Un input del nodo Branch il cui nome conserva quegli spazi non corrisponderà. | STRING |
| `option_index` | Posizione dell'opzione scelta nell'elenco delle opzioni, a partire da 0. | INT |
| `confidence` | Quanto è sicuro Jev, da 0 (nessun chiaro vincitore) a 1 (certo). | FLOAT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevChoice/it.md)

---
**Source fingerprint (SHA-256):** `b1cd36d600f5c07935c455d9e926e6c0a53f172fcc1a6f602c8d4dc70eeffabe`
