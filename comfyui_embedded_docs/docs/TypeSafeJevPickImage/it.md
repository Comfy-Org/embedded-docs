# TypeSafe Jev (Pick Image)

Il nodo TypeSafe Jev (Pick Image) seleziona un'immagine da un batch. Collega `index` a Get Image from Batch per mantenere l'immagine selezionata, oppure leggi `confidence` per decidere se la selezione è sufficientemente buona. Questo è un nodo API e richiede un account Comfy.org e una chiave API.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Modello Jev da utilizzare. Al momento è disponibile un solo modello: `jev-1.14.0`. | COMBO | Sì | `"jev-1.14.0"` |
| `question` | Quale immagine selezionare. Collega il prompt a `text` per scegliere l'immagine che vi corrisponde meglio (predefinito: `Which image best matches the prompt in text? If there is no text, which image has the best quality?`). | STRING | Sì | 1 a 1000 caratteri |
| `images` | Le immagini tra cui scegliere. Un input in batch conta una volta per immagine, quindi ogni immagine del batch è una candidata. | IMAGE | Sì | 2 a 32 immagini |
| `text` | Il testo a cui si riferisce la domanda, ad esempio il prompt da cui sono state create le immagini. | STRING | No | 0 a 3000 caratteri |

**Note:**

- Il nodo genera un errore quando sono collegate meno di 2 o più di 32 immagini.
- `index` parte da 0, che è la posizione attesa da Get Image from Batch.
- La fatturazione è basata sui token; il badge del prezzo sul nodo mostra la tariffa approssimativa per 1 milione di token.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `index` | Posizione dell'immagine selezionata nel batch, a partire da 0. | INT |
| `confidence` | Quanto Jev è sicuro, da 0 (nessun vincitore chiaro) a 1 (certo). | FLOAT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevPickImage/it.md)

---
**Source fingerprint (SHA-256):** `432ee9ba69ebc0b452de4b52e94abdc56a65dc694a463a3654efb62b172c7b93`
