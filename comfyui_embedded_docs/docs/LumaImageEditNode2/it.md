# Luma UNI-1 Modifica Immagine

Questo nodo modifica un'immagine esistente usando un prompt testuale, tramite il modello Luma UNI-1. Prende un'immagine di origine e una descrizione della modifica desiderata, quindi genera una nuova versione modificata dell'immagine. Puoi scegliere tra i modelli `uni-1` e `uni-1-max`, regolare lo stile, abilitare la ricerca sul web e fornire facoltativamente fino a 8 immagini di riferimento.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `model` | Modello da usare per la modifica. Selezionando un modello vengono mostrate le opzioni specifiche del modello riportate di seguito. | DYNAMIC_COMBO | Sì | `"uni-1"`<br>`"uni-1-max"` |
| `source` | Immagine di origine da modificare. | IMAGE | Sì | - |
| `prompt` | Descrizione della modifica desiderata. 1–6000 caratteri. Predefinito: "" (stringa vuota; la richiesta non è valida finché non viene inserito almeno un carattere). | STRING | Sì | 1 a 6000 caratteri |
| `seed` | Il seed controlla se il nodo deve essere rieseguito; i risultati sono non deterministici indipendentemente dal seed. Predefinito: 0. | INT | Sì | 0 a 2147483647 |

### Input di uni-1 e uni-1-max

Queste opzioni sono condivise da entrambi i modelli `uni-1` e `uni-1-max`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `style` | Preset di stile. `"auto"` sceglie in base al prompt; `"manga"` applica un'estetica manga/anime e richiede un rapporto d'aspetto verticale (2:3, 9:16, 1:2, 1:3). Predefinito: `"auto"`. | COMBO | Sì | `"auto"`<br>`"manga"` |
| `web_search` | Cerca sul web riferimenti visivi prima della generazione. Predefinito: false. | BOOLEAN | Sì | `true`<br>`false` |

### Input di riferimento

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|-----------|----------|-------|
| `image_ref` | Slot espandibile: collega fino a 8 immagini di riferimento (`image_1` fino a `image_8`) per guidare stile/contenuto. Opzionale. | IMAGE | No | 0 a 8 immagini |

**Note:**
- Il `prompt` deve essere compreso tra 1 e 6000 caratteri.
- Gli input `style`, `web_search` e `image_ref` compaiono quando `model` è impostato su `"uni-1"` o `"uni-1-max"`.
- Entrambi i modelli supportano le stesse opzioni specifiche del modello, incluse fino a 8 immagini di riferimento.
- Lo stile `"manga"` richiede un rapporto d'aspetto verticale (2:3, 9:16, 1:2 o 1:3).
- Collegare più di 8 immagini di riferimento genera un errore.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|-----------|
| `image` | L'immagine modificata generata dal modello Luma UNI-1, restituita in formato PNG. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageEditNode2/it.md)

---
**Source fingerprint (SHA-256):** `66f62bb2807759edb405c2caeeefe32c341920924e267c32449a620190b9a7ab`
