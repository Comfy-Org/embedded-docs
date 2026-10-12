# ReveImageEditNode

Il nodo Reve Image Edit modifica un'immagine esistente in base a un'istruzione testuale in linguaggio naturale. Invia l'immagine di input e la tua istruzione all'API di Reve, che restituisce una nuova immagine con le modifiche richieste applicate.

## Input

Il selettore `model` determina quali input specifici del modello vengono mostrati. Il selettore `upscale` controlla se l'input del fattore di upscale è disponibile.

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `image` | L'immagine da modificare. | IMAGE | Sì | - |
| `edit_instruction` | Descrizione testuale di come modificare l'immagine. Massimo 2560 caratteri. | STRING | Sì | - |
| `model` | Versione del modello da usare per la modifica. | DYNAMIC_COMBO | Sì | `"reve-edit@20250915"`<br>`"reve-edit-fast@20251030"` |
| `upscale` | Esegue l'upscale dell'immagine generata. Può comportare un costo aggiuntivo. (predefinito: "disabled") | DYNAMIC_COMBO | No | `"disabled"`<br>`"enabled"` |
| `remove_background` | Rimuove lo sfondo dall'immagine generata. Può comportare un costo aggiuntivo. (predefinito: False) | BOOLEAN | No | `true`<br>`false` |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati non sono deterministici indipendentemente dal seed. (predefinito: 0) | INT | No | da 0 a 2147483647 |

### Input del modello (condivisi da `reve-edit@20250915` e `reve-edit-fast@20251030`)

Entrambe le versioni del modello espongono gli stessi input specifici del modello.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model.aspect_ratio` | Rapporto d'aspetto dell'immagine di output. Se impostato su "auto", il rapporto d'aspetto viene determinato automaticamente. | COMBO | No | `"auto"`<br>`"16:9"`<br>`"9:16"`<br>`"3:2"`<br>`"2:3"`<br>`"4:3"`<br>`"3:4"`<br>`"1:1"` |
| `model.test_time_scaling` | Opzione avanzata. Valori più alti producono immagini migliori ma costano più crediti. (predefinito: 1) | INT | No | da 1 a 5 |

### Input di upscale (quando `upscale` è impostato su "enabled")

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `upscale.upscale_factor` | Fattore di upscale (2x, 3x o 4x). (predefinito: 2) | INT | No | da 2 a 4 |

**Nota:**

- `upscale.upscale_factor` si applica solo quando `upscale` è impostato su "enabled". L'upscaling e la rimozione dello sfondo possono essere abilitati insieme o indipendentemente.
- `edit_instruction` non deve essere vuoto e non può superare 2560 caratteri.
- Quando `model.aspect_ratio` è impostato su "auto", non viene inviato alcun rapporto d'aspetto fisso all'API e il rapporto d'aspetto viene scelto automaticamente.
- `model.test_time_scaling` viene inviato all'API solo quando il suo valore è maggiore di 1; il valore predefinito di 1 mantiene il comportamento predefinito dell'API.
- I risultati non sono deterministici indipendentemente dal valore del seed; il seed controlla solo se il nodo viene rieseguito.
- Questo nodo è contrassegnato come deprecato.
- Costo approssimativo in USD (in base all'indicatore di prezzo del nodo): `$0.01001` per `reve-edit-fast@20251030`; `$0.0572` per `reve-edit@20250915` senza upscaling; `$0.0686` con upscaling 2x, `$0.0819` con upscaling 3x e `$0.0991` con upscaling 4x.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `image` | L'immagine modificata generata in base all'istruzione. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageEditNode/it.md)

---
**Source fingerprint (SHA-256):** `4001f3ab4cc4e705c235f578e90e497bb30d22110ef69b16fb072a91a65d15df`
