# TypeSafe Jev (Score)

Il nodo TypeSafe Jev (Score) valuta testo, immagini o entrambi collegati, assegnando un punteggio da 1 a 10, e confronta la valutazione con una soglia. Collegare `result` a un nodo If/Else Switch per intervenire sul punteggio, oppure leggere `score` per usare la valutazione non elaborata. Questo è un nodo API: viene eseguito sui server di Comfy e richiede un account Comfy.org con crediti.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Modello Jev da utilizzare. Al momento è disponibile un solo modello: `jev-1.14.0`. | COMBO | Sì | `"jev-1.14.0"` |
| `question` | Cosa valutare, su una scala da 1 a 10. Specificare cosa significano 1 e 10, come nel valore predefinito (predefinito: `Rate the technical quality of the image from 1 (worst) to 10 (best).`). | STRING | Sì | 1 a 1000 caratteri |
| `threshold` | `result` è vero quando il punteggio è almeno pari a questo valore (predefinito: 5.0). | FLOAT | Sì | 1.0 a 10.0 (passo 0.1) |
| `images` | Le immagini a cui si riferisce la domanda. Fino a 32 immagini in totale; un input in batch conta una volta per immagine. Il lato lungo di ogni immagine è limitato dal numero totale di immagini: 1568 px per un massimo di 4 immagini, 1024 px per un massimo di 8, 768 px per un massimo di 16 e 512 px per un massimo di 32, quindi un batch più grande può ridurre il dettaglio in ogni immagine. | AUTOGROW | No | 0 a 32 immagini |
| `text` | Il testo a cui si riferisce la domanda, ad esempio un prompt o una risposta di un LLM. | STRING | No | 0 a 3000 caratteri |

**Note:**

- Collegare il testo o almeno un'immagine; il nodo genera un errore quando entrambi sono vuoti.
- Il punteggio è riportato da 1 a 10 e `result` è vero quando è almeno pari a `threshold`.
- La fatturazione è basata sui token; il badge del prezzo sul nodo mostra la tariffa approssimativa per 1M token.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `result` | Vero quando `score` è almeno pari a `threshold`. | BOOLEAN |
| `score` | La valutazione da 1 (peggiore) a 10 (migliore). | FLOAT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevScore/it.md)

---
**Source fingerprint (SHA-256):** `7e1970e903d2099ab3d7481a758c5291e87614b9eaf116d0ced6a1bcd36dc126`
