# TypeSafe Jev (Yes/No)

Il nodo TypeSafe Jev (Sì/No) pone una domanda con risposta sì o no su testo, immagini o entrambi collegati al nodo e restituisce la risposta come valore booleano. Collega `result` a un nodo If/Else Switch per instradare il workflow, oppure leggi `probability` per agire in base a quanto è sicuro il modello. Questo è un nodo API: viene eseguito sui server di Comfy e richiede un account Comfy.org con crediti.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Modello Jev da usare. Attualmente è disponibile un solo modello: `jev-1.14.0`. | COMBO | Sì | `"jev-1.14.0"` |
| `question` | La domanda con risposta sì o no a cui rispondono il testo e le immagini collegati. Formulala in modo che il caso su cui vuoi agire corrisponda a sì; con più socket per le immagini, usa i loro nomi, ad esempio `Does image_2 show the same person as image_1?` (predefinito: `Is there a person in the image?`). | STRING | Sì | 1 a 1000 caratteri |
| `threshold` | La risposta è sì quando la probabilità di sì è almeno questo valore (predefinito: 0.5). | FLOAT | Sì | 0.01 a 0.99 (passo 0.01) |
| `images` | Le immagini a cui si riferisce la domanda. Fino a 32 immagini in totale; un input in batch conta una volta per immagine. Il lato lungo di ogni immagine è limitato in base al numero totale di immagini: 1568 px per un massimo di 4 immagini, 1024 px per un massimo di 8, 768 px per un massimo di 16 e 512 px per un massimo di 32, quindi un batch più grande comporta meno dettaglio in ogni immagine. | AUTOGROW | No | 0 a 32 immagini |
| `text` | Il testo a cui si riferisce la domanda, come un prompt o una risposta di un LLM. | STRING | No | 0 a 3000 caratteri |

**Note:**

- Collega il testo o almeno un'immagine; il nodo genera un errore quando entrambi sono vuoti.
- `result` è vero quando `probability` è almeno `threshold`, e `answer` restituisce lo stesso verdetto come `yes` o `no`.
- La fatturazione si basa sui token; il badge del prezzo sul nodo mostra la tariffa approssimativa per 1 milione di token.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `result` | La risposta come valore booleano: vero quando la probabilità di sì è almeno `threshold`. | BOOLEAN |
| `answer` | La risposta come testo `yes` o `no`. | STRING |
| `probability` | Probabilità di sì, da 0 (decisamente no) a 1 (decisamente sì). | FLOAT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevYesNo/it.md)

---
**Source fingerprint (SHA-256):** `e8c7de5558c61e7c9058b28104a72d8d8961165983d02d63a5c9078c40855385`
