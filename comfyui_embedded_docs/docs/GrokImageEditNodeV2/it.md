# GrokImageEditNodeV2

Modifica una o più immagini esistenti in base a un prompt testuale. Il nodo invia le immagini di riferimento collegate e il prompt all'API di modifica immagini Grok utilizzando il modello selezionato, quindi restituisce le immagini modificate.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Il modello di immagini Grok da utilizzare. I sotto-parametri mostrati di seguito cambiano in base al modello selezionato. | DYNAMIC_COMBO | Sì | "grok-imagine-image-2.0"<br>"grok-imagine-image-quality"<br>"grok-imagine-image-pro"<br>"grok-imagine-image" |
| `prompt` | Il prompt testuale utilizzato per generare l'immagine. (predefinito: "") | STRING | Sì | N/D |
| `seed` | Seed per determinare se il nodo deve essere rieseguito; i risultati effettivi sono non deterministici indipendentemente dal seed. (predefinito: 0) | INT | Sì | 0 a 2147483647 |

### Input di grok-imagine-image-2.0

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `resolution` | Risoluzione di output delle immagini modificate. | COMBO | Sì | "1K"<br>"2K" |
| `number_of_images` | Numero di immagini modificate da generare. (predefinito: 1) | INT | Sì | 1 a 10 |
| `quality` | Livello di qualità delle immagini generate. | COMBO | Sì | "medium"<br>"low" |
| `aspect_ratio` | Proporzioni dell'immagine modificata. (predefinito: "auto") | COMBO | Sì | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### Input di grok-imagine-image-quality e grok-imagine-image

Condiviso da grok-imagine-image-quality e grok-imagine-image.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `resolution` | Risoluzione di output delle immagini modificate. | COMBO | Sì | "1K"<br>"2K" |
| `number_of_images` | Numero di immagini modificate da generare. (predefinito: 1) | INT | Sì | 1 a 10 |
| `aspect_ratio` | Consentito solo quando sono collegate più immagini. (predefinito: "auto") | COMBO | Sì | "auto"<br>"1:1"<br>"2:3"<br>"3:2"<br>"3:4"<br>"4:3"<br>"9:16"<br>"16:9"<br>"9:19.5"<br>"19.5:9"<br>"9:20"<br>"20:9"<br>"1:2"<br>"2:1" |

### Input di grok-imagine-image-pro

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `resolution` | Risoluzione di output delle immagini modificate. | COMBO | Sì | "1K"<br>"2K" |
| `number_of_images` | Numero di immagini modificate da generare. (predefinito: 1) | INT | Sì | 1 a 10 |

### Input di riferimento

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `images` | Slot espandibile: collega da 1 a N immagini di riferimento da modificare. Gli slot utilizzano i nomi modello `image_1`, `image_2`, `image_3`; il numero massimo di slot dipende dal modello selezionato. | IMAGE | Sì | 1 immagine per `grok-imagine-image-pro`<br>da 1 a 3 immagini per `grok-imagine-image-2.0`, `grok-imagine-image-quality` e `grok-imagine-image` |

**Nota sui vincoli:**
- `prompt` deve contenere almeno 1 carattere non spazio bianco.
- È richiesta almeno un'immagine di riferimento per la modifica; il nodo genera un errore se non è collegata alcuna immagine.
- Il numero massimo di immagini di input è 1 per `grok-imagine-image-pro` e 3 per `grok-imagine-image-2.0`, `grok-imagine-image-quality` e `grok-imagine-image`. Collegare più immagini di quante il modello supporta genera un errore.
- Il limite di immagini conta ogni immagine negli input collegati, quindi un batch contenente diverse immagini conta come diverse immagini ai fini del limite.
- Per `grok-imagine-image-quality` e `grok-imagine-image`, un `aspect_ratio` personalizzato (qualsiasi cosa diversa da "auto") è consentito solo quando sono collegate più immagini. Con una singola immagine, `aspect_ratio` deve essere "auto".
- Per `grok-imagine-image-2.0`, `aspect_ratio` può essere impostato liberamente anche con una singola immagine.
- Il sotto-parametro `quality` è disponibile solo con `grok-imagine-image-2.0`.

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `IMAGE` | Le immagini modificate restituite dall'API Grok. Se viene generata una singola immagine, viene restituita direttamente. Se vengono generate più immagini, vengono concatenate in un singolo tensore batch. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNodeV2/it.md)

---
**Source fingerprint (SHA-256):** `7d75b1cb8405c5024567b1119bcbd5e4b318152605f74b62bdd5173dda75949f`
