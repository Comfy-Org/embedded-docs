# ByteDanceSeedreamNodeV2

Questo nodo genera o modifica immagini utilizzando i modelli Seedream di ByteDance (versioni 4.0, 4.5, 5.0 Lite e 5.0 Pro). Fornisce generazione testo-immagine unificata e modifica precisa di immagini a partire da una singola frase, fino a risoluzione 4K. Questa è la versione legacy (V2) del nodo Seedream.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | La versione del modello Seedream da usare per la generazione. Ogni modello ha capacità e prezzi diversi. | DYNAMIC_COMBO | Sì | `"seedream 5.0 pro"`<br>`"seedream 5.0 lite"`<br>`"seedream-4-5-251128"`<br>`"seedream-4-0-250828"` |
| `prompt` | Prompt testuale per creare o modificare un'immagine (predefinito: stringa vuota). | STRING | Sì | N/A |
| `seed` | Seed da usare per la generazione (predefinito: 0). | INT | Sì | 0 a 2147483647 |
| `watermark` | Indica se aggiungere una filigrana "AI generated" all'immagine (predefinito: False). | BOOLEAN | Sì | True / False |
| `thinking` | Abilita il ragionamento di ottimizzazione del prompt ('thinking') del modello per una migliore aderenza. Può aumentare considerevolmente il tempo di generazione — in particolare su Seedream 5.0 Pro. Può essere disabilitato solo per testo-immagine (non quando vengono fornite immagini di riferimento) (predefinito: True). | BOOLEAN | No | True / False |

### Input di `seedream 5.0 pro`

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `size_preset` | Scegli una dimensione consigliata. Seleziona Custom per usare la larghezza e l'altezza indicate di seguito. | COMBO | Sì | Sono disponibili diversi preset specifici per modello; include `Custom` |
| `width` | Larghezza personalizzata per l'immagine. Il valore è efficace solo se `size_preset` è impostato su `Custom` (predefinito: 2048). | INT | Sì | 1024 a 3136 (passo 2) |
| `height` | Altezza personalizzata per l'immagine. Il valore è efficace solo se `size_preset` è impostato su `Custom` (predefinito: 2048). | INT | Sì | 1024 a 2496 (passo 2) |

### Input di `seedream 5.0 lite`

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `size_preset` | Scegli una dimensione consigliata. Seleziona Custom per usare la larghezza e l'altezza indicate di seguito. | COMBO | Sì | Sono disponibili diversi preset specifici per modello; include `Custom` |
| `width` | Larghezza personalizzata per l'immagine. Il valore è efficace solo se `size_preset` è impostato su `Custom` (predefinito: 2048). | INT | Sì | 1024 a 6240 (passo 2) |
| `height` | Altezza personalizzata per l'immagine. Il valore è efficace solo se `size_preset` è impostato su `Custom` (predefinito: 2048). | INT | Sì | 1024 a 4992 (passo 2) |
| `max_images` | Numero massimo di immagini da generare. Con 1, viene prodotta esattamente un'immagine. Con >1, il modello genera tra 1 e max_images immagini correlate (ad es. scene di una storia, varianti di personaggi). Il numero totale di immagini (input + generate) non può superare 15. (predefinito: 1) | INT | Sì | 1 a 14 |
| `fail_on_partial` | Se abilitato, interrompe l'esecuzione se una qualsiasi delle immagini richieste manca o viene restituito un errore. (predefinito: False) | BOOLEAN | Sì | True / False |

### Input di `seedream-4-5-251128`

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `size_preset` | Scegli una dimensione consigliata. Seleziona Custom per usare la larghezza e l'altezza indicate di seguito. | COMBO | Sì | Sono disponibili diversi preset specifici per modello; include `Custom` |
| `width` | Larghezza personalizzata per l'immagine. Il valore è efficace solo se `size_preset` è impostato su `Custom` (predefinito: 2048). | INT | Sì | 1024 a 6240 (passo 2) |
| `height` | Altezza personalizzata per l'immagine. Il valore è efficace solo se `size_preset` è impostato su `Custom` (predefinito: 2048). | INT | Sì | 1024 a 4992 (passo 2) |
| `max_images` | Numero massimo di immagini da generare. Con 1, viene prodotta esattamente un'immagine. Con >1, il modello genera tra 1 e max_images immagini correlate (ad es. scene di una storia, varianti di personaggi). Il numero totale di immagini (input + generate) non può superare 15. (predefinito: 1) | INT | Sì | 1 a 10 |
| `fail_on_partial` | Se abilitato, interrompe l'esecuzione se una qualsiasi delle immagini richieste manca o viene restituito un errore. (predefinito: False) | BOOLEAN | Sì | True / False |

### Input di `seedream-4-0-250828`

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `size_preset` | Scegli una dimensione consigliata. Seleziona Custom per usare la larghezza e l'altezza indicate di seguito. | COMBO | Sì | Sono disponibili diversi preset specifici per modello; include `Custom` |
| `width` | Larghezza personalizzata per l'immagine. Il valore è efficace solo se `size_preset` è impostato su `Custom` (predefinito: 2048). | INT | Sì | 1024 a 6240 (passo 2) |
| `height` | Altezza personalizzata per l'immagine. Il valore è efficace solo se `size_preset` è impostato su `Custom` (predefinito: 2048). | INT | Sì | 1024 a 4992 (passo 2) |
| `max_images` | Numero massimo di immagini da generare. Con 1, viene prodotta esattamente un'immagine. Con >1, il modello genera tra 1 e max_images immagini correlate (ad es. scene di una storia, varianti di personaggi). Il numero totale di immagini (input + generate) non può superare 15. (predefinito: 1) | INT | Sì | 1 a 10 |
| `fail_on_partial` | Se abilitato, interrompe l'esecuzione se una qualsiasi delle immagini richieste manca o viene restituito un errore. (predefinito: False) | BOOLEAN | Sì | True / False |

### Input di riferimento

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `images` | Slot espandibile: collega da 1 a N elementi (ad es. `image_1`, `image_2`, ...); il limite di conteggio dipende dal modello selezionato (vedi sezioni del modello). Immagine/i di riferimento opzionale/i per la generazione image-to-image o multi-riferimento. Senza immagini di riferimento, il nodo funziona in modalità testo-immagine. | IMAGE | No | da 0 a 10 immagini (`seedream 5.0 pro`, `seedream-4-5-251128`, `seedream-4-0-250828`)<br>da 0 a 14 immagini (`seedream 5.0 lite`) |

### Note sui vincoli

- `width` e `height` hanno effetto solo quando `size_preset` è impostato su `Custom`.
- Il numero totale di immagini di riferimento più le immagini generate non può superare 15.
- `thinking` può essere disabilitato solo per la generazione testo-immagine, non quando vengono fornite immagini di riferimento.
- Seedream 5.0 Pro non supporta la generazione in batch: produce sempre una singola immagine, quindi `max_images` e `fail_on_partial` non sono disponibili per questo modello.

## Output

| Nome output | Descrizione | Tipo di dato |
|-------------|-------------|--------------|
| `image` | L'immagine generata o modificata come tensore. Se sono state richieste più immagini, vengono concatenate in un singolo batch. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedreamNodeV2/it.md)

---
**Source fingerprint (SHA-256):** `f1a84171d94c602ec5417e43857ddf511ab1e54caa089b1928f740d3a38423f8`
