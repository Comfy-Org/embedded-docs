# TextEncodeMageFlowEdit

## Panoramica

Questo nodo codifica un'istruzione di modifica (prompt) insieme a una o più immagini di riferimento per il modello Mage-Flow-Edit. Ridimensiona tutte le immagini di riferimento alla risoluzione di output desiderata, le codifica nello spazio latente se viene fornito un VAE e allega i latenti di riferimento all'output di conditioning. Viene inoltre generato un tensore latente vuoto con le dimensioni corrette per il campionamento, assicurando che la dimensione corrisponda sempre alla larghezza e all'altezza di output.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `clip` | Il modello CLIP utilizzato per tokenizzare e codificare i prompt di testo. | CLIP | Sì | |
| `prompt` | L'istruzione di modifica (prompt positivo) da applicare. | STRING | Sì | multiriga, prompt dinamici abilitati |
| `negative_prompt` | Il prompt negativo da cui allontanarsi. Predefinito: stringa vuota (internamente usa uno spazio quando è vuota). Mostrato nella sezione avanzata dell'interfaccia utente. | STRING | No | multiriga, prompt dinamici abilitati |
| `vae` | Modello VAE per codificare le immagini di riferimento nello spazio latente. Se non fornito, nessun latente di riferimento viene aggiunto al conditioning. | VAE | No | |
| `images` | Immagine/i di riferimento da modificare. Tutti i riferimenti vengono ridimensionati alla risoluzione di output prima della codifica. | IMAGE (autogrow) | No | Fino a 16 immagini (denominate `image_1`…`image_16`), almeno 0 |
| `width` | Larghezza di output in pixel. Se impostata a 0, viene utilizzata la larghezza della prima immagine di riferimento. Viene sempre arrotondata per difetto a un multiplo di 16. Predefinito: 0. | INT | Sì | 0 a 8192 (passo 16) |
| `height` | Altezza di output in pixel. Stesso comportamento di fallback della larghezza. Predefinito: 0. | INT | Sì | 0 a 8192 (passo 16) |
| `batch_size` | Numero di campioni latenti da generare. Predefinito: 1. | INT | Sì | 1 a 4096 |

**Note sulle dipendenze dei parametri:**
- Se `width` e/o `height` sono 0 e non viene fornita alcuna immagine di riferimento, entrambi assumono valore 1024.
- Se solo uno tra `width` o `height` è 0, la dimensione mancante viene presa dalla prima immagine di riferimento, mentre la dimensione impostata esplicitamente viene mantenuta.
- Il parametro `vae` è opzionale; i latenti di riferimento vengono generati e allegati al conditioning solo quando è collegato un VAE.
- Il campo `negative_prompt` è opzionale – se lasciato vuoto, internamente viene utilizzato un singolo spazio come testo negativo.
- Per il conditioning testuale, ogni immagine di riferimento viene ridimensionata in modo che il suo lato più lungo sia al massimo di 384 pixel, coerentemente con la preelaborazione del training. Il ramo di codifica VAE, invece, ridimensiona tutti i riferimenti alla risoluzione di output completa.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `positive` | Output di conditioning contenente i token del prompt positivo, più (se è stato fornito un VAE) i latenti di riferimento codificati. | CONDITIONING |
| `negative` | Output di conditioning contenente i token del prompt negativo, più gli stessi latenti di riferimento (se VAE fornito). | CONDITIONING |
| `latent` | Un tensore latente vuoto con forma `[batch_size, 128, height÷16, width÷16]` da usare come rumore iniziale durante il campionamento. | LATENT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeMageFlowEdit/it.md)

---
**Source fingerprint (SHA-256):** `880d8856b7f6e656bc68ca953fbf892898d05bc5d65290ae3bf7a4405ee09be3`
