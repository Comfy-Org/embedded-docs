# TypeSafe Jev (Pick Image)

Il nodo TypeSafe Jev (Pick Image) seleziona un'immagine da un batch. Collega lo stesso batch di immagini a Get Image from Batch insieme a `index` per mantenere l'immagine selezionata, oppure leggi `confidence` per decidere se la scelta è sufficientemente buona. Questo è un nodo API: viene eseguito sui server di Comfy e richiede un account Comfy.org con crediti.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Modello Jev da usare. Attualmente è disponibile un solo modello: `jev-1.14.0`. | COMBO | Sì | `"jev-1.14.0"` |
| `question` | Quale immagine selezionare. Collega il prompt a `text` per scegliere l'immagine che vi corrisponde meglio (predefinito: `Which image best matches the prompt in text? If there is no text, which image has the best quality?`). | STRING | Sì | 1 a 1000 caratteri |
| `images` | Le immagini tra cui scegliere. Un input in batch conta una volta per immagine, quindi ogni immagine del batch è una candidata. Il lato lungo di ogni immagine viene limitato in base alla dimensione del batch prima del caricamento: 1568 px fino a 4 immagini, 1024 px fino a 8, 768 px fino a 16 e 512 px fino a 32, quindi un batch più grande significa meno dettaglio in ogni immagine. | IMAGE | Sì | 2 a 32 immagini |
| `text` | Il testo a cui si riferisce la domanda, ad esempio il prompt da cui sono state generate le immagini. | STRING | No | 0 a 3000 caratteri |

**Note:**

- Il nodo genera un errore quando sono collegate meno di 2 o più di 32 immagini.
- `index` conta da 0, che è la posizione prevista da Get Image from Batch.
- La fatturazione è basata sui token; il badge del prezzo sul nodo mostra la tariffa approssimativa per 1 milione di token.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `index` | Posizione dell'immagine selezionata nel batch, a partire da 0. | INT |
| `confidence` | Quanto è sicuro Jev, da 0 (nessun vincitore chiaro) a 1 (certo). | FLOAT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TypeSafeJevPickImage/it.md)

---
**Source fingerprint (SHA-256):** `432ee9ba69ebc0b452de4b52e94abdc56a65dc694a463a3654efb62b172c7b93`
