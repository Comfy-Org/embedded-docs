# Krea 3 Image

Krea 3 Image modifica le immagini con Krea 3, oppure genera una nuova immagine da un prompt testuale quando non è connessa alcuna immagine. Collega fino a 8 immagini e descrivi cosa cambiare e cosa mantenere, facendo riferimento a esse nel prompt come `@Image1`, `@Image2`, e così via. Il rapporto d'aspetto e la risoluzione impostano le dimensioni dell'output, mentre la modalità di pensiero privilegia un piano più dettagliato a scapito della velocità.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello Krea 3 da usare. Selezionando un modello vengono mostrati i parametri accettati. | DYNAMIC_COMBO | Sì | `"Krea 3"` |

### Input di Krea 3

Questi input compaiono quando `model` è impostato su `Krea 3`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model.images` | Le immagini da modificare, numerate nell'ordine di connessione. Ogni immagine connessa contribuisce al limite di 8. Lasciare vuoto per generare solo dal testo. | IMAGE | No | da 0 a 8 immagini |
| `model.prompt` | Cosa modificare e cosa mantenere. Fai riferimento alle immagini come `@Image1`, `@Image2`, e così via, oppure come immagine 1, immagine 2, ... Il prompt non può essere vuoto. | STRING | Sì | - |
| `model.aspect_ratio` | Il rapporto d'aspetto del risultato. `"auto"` segue la prima immagine, oppure il prompt quando non è connessa alcuna immagine. (predefinito: `"auto"`) | COMBO | Sì | `"auto"`<br>`"1:1"`<br>`"4:5"`<br>`"3:4"`<br>`"2:3"`<br>`"9:16"`<br>`"5:4"`<br>`"4:3"`<br>`"3:2"`<br>`"16:9"`<br>`"21:9"` |
| `model.resolution` | La risoluzione di output. `"2K"` richiede più tempo e produce un'immagine più grande rispetto a `"1K"`. (predefinito: `"2K"`) | COMBO | Sì | `"1K"`<br>`"2K"` |
| `model.thinking_mode` | Quanto lavoro Krea 3 dedica alla pianificazione della modifica. `"fast"` è consigliato, mentre `"high"` pianifica modifiche complesse in modo più dettagliato e richiede più tempo. `"ultra"` genera diversi candidati e restituisce il migliore; richiede almeno un'immagine, produce sempre in 2K e non supporta `precise_edit`. (predefinito: `"fast"`) | COMBO | Sì | `"fast"`<br>`"high"`<br>`"ultra"` |
| `model.precise_edit` | Mantieni invariato tutto ciò che è esterno all'area modificata. Richiede almeno un'immagine connessa. (predefinito: False) | BOOLEAN | Sì | false<br>true |
| `model.seed` | Il seed per la richiesta (predefinito: 42). Krea riscrive il prompt prima di generare, quindi lo stesso seed non ripete un'immagine. | INT | Sì | da 0 a 2147483647 |

Un riferimento come `@Image3` è accettato solo quando sono connesse almeno tre immagini; in caso contrario il nodo genera un errore. Le immagini di riferimento vengono caricate prima che la richiesta venga inviata.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | L'immagine generata o modificata. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Krea3ImageNode/it.md)

---
**Source fingerprint (SHA-256):** `9e8d036f1ebca81b85e6ef42a015e7e2925bf467fa32e82180ee1b76dcc91c0b`
