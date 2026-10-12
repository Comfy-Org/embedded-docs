# ByteDanceSeedreamNodeV3

ByteDance Seedream 4.5 & 5.0 genera immagini da un prompt testuale (text-to-image) o genera/modifica immagini guidate da immagini di riferimento opzionali, utilizzando i modelli ByteDance Seedream 4.0, 4.5 e 5.0 fino a una risoluzione 4K. Il nodo invia il prompt e le eventuali immagini di riferimento all'API ByteDance, attende il completamento dell'attività di generazione e restituisce il tensore o i tensori dell'immagine risultante.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `prompt` | Prompt testuale per creare o modificare un'immagine. Non deve essere vuoto dopo la rimozione degli spazi bianchi. | STRING | Sì | Testo multiriga |
| `model` | Seleziona il modello Seedream da utilizzare. Ogni modello espone il proprio insieme di sotto-parametri e limiti di seguito. | DYNAMIC_COMBO | Sì | "seedream 5.0 pro"<br>"seedream 5.0 flash"<br>"seedream 5.0 lite"<br>"seedream-4-5-251128"<br>"seedream-4-0-250828" |

### Input di Seedream 5.0 Pro (seedream 5.0 pro)

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `size_preset` | Scegli una dimensione consigliata. Seleziona Custom per usare la larghezza e l'altezza di seguito. Predefinito: primo preset consigliato per questo modello. | COMBO | No | Preset di dimensioni consigliati specifici per modello<br>"Custom" |
| `width` | Larghezza personalizzata per l'immagine. Il valore è valido solo se `size_preset` è impostato su `Custom`. Predefinito: 2048. | INT | No | 1024 a 4514 (passo 2) |
| `height` | Altezza personalizzata per l'immagine. Il valore è valido solo se `size_preset` è impostato su `Custom`. Predefinito: 2048. | INT | No | 1024 a 4514 (passo 2) |
| `prompt_optimization` | Modalità di ottimizzazione del prompt quando vengono fornite immagini di riferimento: 'standard' offre una qualità superiore, 'fast' un tempo di generazione più breve. Predefinito: "standard". | COMBO | No | "standard"<br>"fast" |
| `seed` | Seed da utilizzare per la generazione. Predefinito: 42. | INT | No | 0 a 2147483647 |
| `watermark` | Se aggiungere una filigrana "AI generated" all'immagine. Predefinito: false. | BOOLEAN | No | true / false |
| `thinking` | Abilita il ragionamento di ottimizzazione del prompt del modello ('thinking') per una migliore aderenza. Può aumentare sostanzialmente il tempo di generazione — in particolare su Seedream 5.0 Pro. Può essere disabilitato solo per text-to-image (non quando vengono fornite immagini di riferimento). Predefinito: true. | BOOLEAN | No | true / false |

### Input di Seedream 5.0 Flash (seedream 5.0 flash)

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `size_preset` | Scegli una dimensione consigliata. Seleziona Custom per usare la larghezza e l'altezza di seguito. Predefinito: primo preset consigliato per questo modello. | COMBO | No | Preset di dimensioni consigliati specifici per modello<br>"Custom" |
| `width` | Larghezza personalizzata per l'immagine. Il valore è valido solo se `size_preset` è impostato su `Custom`. Predefinito: 2048. | INT | No | 1024 a 4514 (passo 2) |
| `height` | Altezza personalizzata per l'immagine. Il valore è valido solo se `size_preset` è impostato su `Custom`. Predefinito: 2048. | INT | No | 1024 a 4514 (passo 2) |
| `seed` | Seed da utilizzare per la generazione. Predefinito: 42. | INT | No | 0 a 2147483647 |
| `watermark` | Se aggiungere una filigrana "AI generated" all'immagine. Predefinito: false. | BOOLEAN | No | true / false |

### Input di Seedream 5.0 Lite (seedream 5.0 lite)

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `size_preset` | Scegli una dimensione consigliata. Seleziona Custom per usare la larghezza e l'altezza di seguito. Predefinito: primo preset consigliato per questo modello. | COMBO | No | Preset di dimensioni consigliati specifici per modello<br>"Custom" |
| `width` | Larghezza personalizzata per l'immagine. Il valore è valido solo se `size_preset` è impostato su `Custom`. Predefinito: 2048. | INT | No | 1024 a 6240 (passo 2) |
| `height` | Altezza personalizzata per l'immagine. Il valore è valido solo se `size_preset` è impostato su `Custom`. Predefinito: 2048. | INT | No | 1024 a 4992 (passo 2) |
| `max_images` | Numero massimo di immagini da generare. Con 1, viene prodotta esattamente un'immagine. Con >1, il modello genera tra 1 e max_images immagini correlate (ad es. scene di storie, variazioni di personaggi). Il numero totale di immagini (input + generate) non può superare 15. Predefinito: 1. | INT | No | 1 a 14 |
| `fail_on_partial` | Se abilitato, interrompe l'esecuzione se una qualsiasi immagine richiesta è mancante o restituisce un errore. Predefinito: false. | BOOLEAN | No | true / false |
| `seed` | Seed da utilizzare per la generazione. Predefinito: 42. | INT | No | 0 a 2147483647 |
| `watermark` | Se aggiungere una filigrana "AI generated" all'immagine. Predefinito: false. | BOOLEAN | No | true / false |
| `thinking` | Abilita il ragionamento di ottimizzazione del prompt del modello ('thinking') per una migliore aderenza. Può aumentare sostanzialmente il tempo di generazione — in particolare su Seedream 5.0 Pro. Può essere disabilitato solo per text-to-image (non quando vengono fornite immagini di riferimento). Predefinito: true. | BOOLEAN | No | true / false |

### Input di Seedream 4.5 (seedream-4-5-251128)

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `size_preset` | Scegli una dimensione consigliata. Seleziona Custom per usare la larghezza e l'altezza di seguito. Predefinito: primo preset consigliato per questo modello. | COMBO | No | Preset di dimensioni consigliati specifici per modello<br>"Custom" |
| `width` | Larghezza personalizzata per l'immagine. Il valore è valido solo se `size_preset` è impostato su `Custom`. Predefinito: 2048. | INT | No | 1024 a 6240 (passo 2) |
| `height` | Altezza personalizzata per l'immagine. Il valore è valido solo se `size_preset` è impostato su `Custom`. Predefinito: 2048. | INT | No | 1024 a 4992 (passo 2) |
| `max_images` | Numero massimo di immagini da generare. Con 1, viene prodotta esattamente un'immagine. Con >1, il modello genera tra 1 e max_images immagini correlate (ad es. scene di storie, variazioni di personaggi). Il numero totale di immagini (input + generate) non può superare 15. Predefinito: 1. | INT | No | 1 a 10 |
| `fail_on_partial` | Se abilitato, interrompe l'esecuzione se una qualsiasi immagine richiesta è mancante o restituisce un errore. Predefinito: false. | BOOLEAN | No | true / false |
| `seed` | Seed da utilizzare per la generazione. Predefinito: 42. | INT | No | 0 a 2147483647 |
| `watermark` | Se aggiungere una filigrana "AI generated" all'immagine. Predefinito: false. | BOOLEAN | No | true / false |
| `thinking` | Abilita il ragionamento di ottimizzazione del prompt del modello ('thinking') per una migliore aderenza. Può aumentare sostanzialmente il tempo di generazione — in particolare su Seedream 5.0 Pro. Può essere disabilitato solo per text-to-image (non quando vengono fornite immagini di riferimento). Predefinito: true. | BOOLEAN | No | true / false |

### Input di Seedream 4.0 (seedream-4-0-250828)

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `size_preset` | Scegli una dimensione consigliata. Seleziona Custom per usare la larghezza e l'altezza di seguito. Predefinito: primo preset consigliato per questo modello. | COMBO | No | Preset di dimensioni consigliati specifici per modello<br>"Custom" |
| `width` | Larghezza personalizzata per l'immagine. Il valore è valido solo se `size_preset` è impostato su `Custom`. Predefinito: 2048. | INT | No | 1024 a 6240 (passo 2) |
| `height` | Altezza personalizzata per l'immagine. Il valore è valido solo se `size_preset` è impostato su `Custom`. Predefinito: 2048. | INT | No | 1024 a 4992 (passo 2) |
| `max_images` | Numero massimo di immagini da generare. Con 1, viene prodotta esattamente un'immagine. Con >1, il modello genera tra 1 e max_images immagini correlate (ad es. scene di storie, variazioni di personaggi). Il numero totale di immagini (input + generate) non può superare 15. Predefinito: 1. | INT | No | 1 a 10 |
| `fail_on_partial` | Se abilitato, interrompe l'esecuzione se una qualsiasi immagine richiesta è mancante o restituisce un errore. Predefinito: false. | BOOLEAN | No | true / false |
| `seed` | Seed da utilizzare per la generazione. Predefinito: 42. | INT | No | 0 a 2147483647 |
| `watermark` | Se aggiungere una filigrana "AI generated" all'immagine. Predefinito: false. | BOOLEAN | No | true / false |
| `thinking` | Abilita il ragionamento di ottimizzazione del prompt del modello ('thinking') per una migliore aderenza. Può aumentare sostanzialmente il tempo di generazione — in particolare su Seedream 5.0 Pro. Può essere disabilitato solo per text-to-image (non quando vengono fornite immagini di riferimento). Predefinito: true. | BOOLEAN | No | true / false |

### Input di riferimento

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `images` | Slot espandibile: immagine/i di riferimento opzionale/i per la generazione image-to-image o multi-reference. Collega 1..N immagini (es. `image_1`, `image_2`, ...); il limite di conteggio è per modello (vedi note sotto). Se un'immagine collegata contiene un batch di immagini, ogni immagine nel batch conta ai fini del limite. | IMAGE | No | 0 a 10 (Seedream 5.0 Pro, Seedream 5.0 Flash, Seedream 4.5, Seedream 4.0)<br>0 a 14 (Seedream 5.0 Lite) |

**Note:**

- Il `prompt` non deve essere vuoto dopo la rimozione degli spazi bianchi.
- Numero massimo di immagini di riferimento: 10 per Seedream 5.0 Pro, Seedream 5.0 Flash, Seedream 4.5 e Seedream 4.0; 14 per Seedream 5.0 Lite.
- Ogni immagine di riferimento deve avere un rapporto d'aspetto compreso tra 1:16 e 16:1.
- Quando `max_images` è maggiore di 1 (non disponibile su Seedream 5.0 Pro o Seedream 5.0 Flash), il numero totale di immagini di riferimento più immagini generate non può superare 15.
- `thinking` può essere disabilitato solo per la generazione text-to-image. Quando vengono fornite immagini di riferimento, `thinking` deve essere abilitato. Seedream 5.0 Flash non ha l'input `thinking`.
- `width` e `height` vengono utilizzati solo quando `size_preset` è impostato su "Custom".
- `prompt_optimization` è disponibile solo su Seedream 5.0 Pro.
- `max_images` e `fail_on_partial` sono disponibili solo su Seedream 5.0 Lite, Seedream 4.5 e Seedream 4.0; Seedream 5.0 Pro e Seedream 5.0 Flash richiedono sempre una singola immagine.
- Requisiti di risoluzione (larghezza x altezza):
  - Seedream 5.0 Pro e Seedream 5.0 Flash: tra 0.92MP (921,600 pixel) e 4.62MP (4,624,220 pixel).
  - Seedream 5.0 Lite e Seedream 4.5: almeno 3.68MP (3,686,400 pixel).
  - Seedream 4.0: almeno 0.92MP (921,600 pixel).
  - Seedream 5.0 Lite, Seedream 4.5 e Seedream 4.0: al massimo 16.78MP (16,777,216 pixel).

## Output

| Nome Output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `image` | Il tensore dell'immagine generata. Quando vengono generate più immagini, queste vengono concatenate in un unico tensore IMAGE in batch. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNodeV3/it.md)

---
**Source fingerprint (SHA-256):** `1c1f40b202ccbb3e0f73cd072170e1c16b833e007f26e63505b54c42b004a8a6`
