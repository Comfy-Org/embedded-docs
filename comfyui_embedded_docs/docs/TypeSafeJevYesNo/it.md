# TypeSafe Jev (Yes/No)

Il nodo TypeSafe Jev (Yes/No) pone una domanda con risposta sì o no su testo, immagini o entrambi collegati e restituisce la risposta come valore booleano. Collega `result` a un nodo If/Else Switch per instradare il workflow, oppure leggi `probability` per agire in base a quanto il modello è sicuro. Questo è un nodo API e richiede un account Comfy.org e una chiave API.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Modello Jev da usare. Al momento è disponibile un solo modello: `jev-1.14.0`. | COMBO | Sì | `"jev-1.14.0"` |
| `question` | La domanda sì/no a cui rispondono il testo e le immagini collegati. Formulala in modo che "sì" corrisponda al caso su cui vuoi agire; con più socket immagine, usa i loro nomi, ad esempio `Does image_2 show the same person as image_1?` (predefinito: `Is there a person in the image?`). | STRING | Sì | 1 a 1000 caratteri |
| `threshold` | La risposta è sì quando la probabilità di sì è almeno questo valore (predefinito: 0.5). | FLOAT | Sì | 0.01 a 0.99 (passo: 0.01) |
| `images` | Le immagini a cui si riferisce la domanda. Fino a 32 immagini in totale; un input raggruppato conta una volta per immagine e più di 4 immagini vengono inviate a dimensioni ridotte. | AUTOGROW | No | 0 a 32 immagini |
| `text` | Il testo a cui si riferisce la domanda, come un prompt o una risposta di un LLM. | STRING | No | 0 a 3000 caratteri |

**Note:**

- Collega il testo o almeno un'immagine; il nodo genera un errore quando entrambi sono vuoti.
- `result` è true quando `probability` è almeno `threshold`, e `answer` restituisce lo stesso verdetto come `yes` o `no`.
- La fatturazione è basata sui token; il badge del prezzo sul nodo mostra la tariffa approssimativa per 1 milione di token.

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `result` | La risposta come booleano: true quando la probabilità di sì è almeno `threshold`. | BOOLEAN |
| `answer` | La risposta come testo `yes` o `no`. | STRING |
| `probability` | Probabilità di sì, da 0 (sicuramente no) a 1 (sicuramente sì). | FLOAT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevYesNo/it.md)

---
**Source fingerprint (SHA-256):** `e8c7de5558c61e7c9058b28104a72d8d8961165983d02d63a5c9078c40855385`
