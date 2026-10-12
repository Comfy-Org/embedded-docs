# Flux2ImageNode

Genera immagini utilizzando il modello Flux.2 [pro] o Flux.2 [max] a partire da un prompt testuale e immagini di riferimento opzionali. Il nodo invia la richiesta all'API BFL, esegue il polling finché il risultato non è pronto e restituisce l'immagine generata.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | La versione del modello Flux.2 da utilizzare. La selezione di un modello sblocca parametri aggiuntivi per larghezza, altezza e immagini di riferimento opzionali. | DYNAMIC_COMBO | Sì | "Flux.2 [pro]"<br>"Flux.2 [max]" |
| `prompt` | Prompt per la generazione o la modifica dell'immagine (predefinito: stringa vuota). | STRING | Sì | N/A |
| `seed` | Il seme casuale utilizzato per creare il rumore (predefinito: 0). Supporta l'opzione control-after-generate per randomizzare il valore dopo ogni esecuzione. | INT | Sì | da 0 a 18446744073709551615 |

### Input di Flux.2 [pro] e Flux.2 [max]

Condivisi da entrambi i modelli — i set di parametri sono identici.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model.width` | La larghezza dell'immagine generata in pixel (predefinito: 1024). | INT | Sì | da 256 a 2048 (passo 32) |
| `model.height` | L'altezza dell'immagine generata in pixel (predefinito: 768). | INT | Sì | da 256 a 2048 (passo 32) |

### Input di riferimento

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model.images` | Immagini di riferimento opzionali per la generazione image-to-image. Fino a 8 immagini. Slot espandibile: collega da 1 a 8 elementi (`image_1`...`image_8`). | IMAGE | No | da 0 a 8 immagini |

**Nota:**
- Il numero massimo di immagini di riferimento è 8. Se vengono fornite più di 8 immagini, viene generato un errore. Le immagini in batch contano ai fini di questo limite, poiché ogni immagine di un batch viene conteggiata individualmente.
- Le immagini di riferimento vengono ridimensionate in modo che il numero totale di pixel non superi 2048 x 2048 prima di essere inviate all'API.
- I valori `model.width` e `model.height` influiscono sul costo di generazione. Il costo dipende anche dal modello selezionato e dalla presenza di immagini di riferimento.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `image` | L'immagine generata come tensore, scaricata dal risultato dell'API BFL. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2ImageNode/it.md)

---
**Source fingerprint (SHA-256):** `2994564757e1c66ac6da7b45d227b27ceb0020ac6fc9e8cbe2b53fe9f70bc195`
