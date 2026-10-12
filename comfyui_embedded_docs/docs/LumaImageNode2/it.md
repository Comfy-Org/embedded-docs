# Luma UNI-1 Immagine

Questo nodo genera immagini a partire da descrizioni testuali utilizzando il modello Luma UNI-1. Accetta un prompt testuale e impostazioni opzionali come rapporto d'aspetto e stile, quindi invia la richiesta all'API Luma per creare un'immagine. Sono disponibili due varianti del modello: `uni-1` e `uni-1-max`.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `prompt` | Descrizione testuale dell'immagine desiderata. Da 1 a 6000 caratteri. (predefinito: "") | STRING | Sì | Da 1 a 6000 caratteri |
| `model` | Modello da utilizzare per la generazione. Selezionando un modello vengono visualizzate impostazioni aggiuntive per quel modello. (predefinito: prima opzione, `"uni-1"`) | DYNAMIC_COMBO | Sì | `"uni-1"`<br>`"uni-1-max"` |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. (predefinito: 0) | INT | Sì | 0 to 2147483647 |

### Input di uni-1 e uni-1-max

Condivisi dalle opzioni del modello `uni-1` e `uni-1-max`. Queste impostazioni compaiono quando è selezionato uno dei due modelli.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `aspect_ratio` | Rapporto d'aspetto dell'immagine di output. `"auto"` lascia che il modello scelga in base al prompt. (predefinito: `"auto"`) | COMBO | Sì | `"auto"`<br>`"3:1"`<br>`"2:1"`<br>`"16:9"`<br>`"3:2"`<br>`"1:1"`<br>`"2:3"`<br>`"9:16"`<br>`"1:2"`<br>`"1:3"` |
| `style` | Preset di stile. `"auto"` sceglie in base al prompt; `"manga"` applica un'estetica manga/anime e richiede un rapporto d'aspetto verticale (2:3, 9:16, 1:2, 1:3). (predefinito: `"auto"`) | COMBO | Sì | `"auto"`<br>`"manga"` |
| `web_search` | Cerca sul web riferimenti visivi prima di generare. (predefinito: False) | BOOLEAN | Sì | True / False |

### Input di riferimento

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `image_ref` | Slot espandibile: collega da 1 a 9 elementi (ad es. da `image_1` a `image_9`). Fino a 9 immagini di riferimento per guidare stile/contenuto. | IMAGE | No | Fino a 9 immagini |

**Nota:** Se `style` è impostato su `"manga"`, `aspect_ratio` deve essere `"auto"` oppure uno dei rapporti verticali `"2:3"`, `"9:16"`, `"1:2"`, `"1:3"`. L'uso di qualsiasi altro rapporto con lo stile `"manga"` causerà un errore. Il numero massimo di immagini di riferimento è 9 sia per `uni-1` che per `uni-1-max`.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | L'immagine generata. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageNode2/it.md)

---
**Source fingerprint (SHA-256):** `27254fe4627fd340426a68f651cab4513ffb6668cafc0accd17f2c442f7d3125`
