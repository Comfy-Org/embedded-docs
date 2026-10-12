# OpenAI GPT Image 2.5

Questo nodo genera immagini usando l'API GPT Image di OpenAI. Supporta cinque modelli — `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst`, `gpt-image-2`, `gpt-image-1.5` e `gpt-image-1` — consente di allegare immagini di riferimento per la modifica delle immagini e può usare una maschera per specificare quali parti di un'immagine sostituire.

## Input

### Input comuni

Questi input sono sempre visibili.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello OpenAI GPT Image da usare. Selezionando un modello vengono rivelati parametri aggiuntivi specifici di quel modello. | DYNAMIC_COMBO | Sì | `"gpt-image-2.5-flare"`<br>`"gpt-image-2.5-sunburst"`<br>`"gpt-image-2"`<br>`"gpt-image-1.5"`<br>`"gpt-image-1"` |
| `prompt` | Prompt testuale per GPT Image (predefinito: `""`). | STRING | Sì | N/A |
| `n` | Quante immagini generare (predefinito: `1`). | INT | Sì | da 1 a 8 |
| `seed` | Seed per la riproducibilità (predefinito: `0`). Non ancora implementato nel backend. | INT | Sì | da 0 a 2147483647 |

### Input di gpt-image-2.5-flare e gpt-image-2.5-sunburst

Questi input compaiono quando `model` è impostato su `gpt-image-2.5-flare` o `gpt-image-2.5-sunburst`. Entrambi i modelli condividono lo stesso insieme di parametri.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model.size` | Dimensione immagine. Seleziona `"Custom"` per usare larghezza e altezza personalizzate (predefinito: `"auto"`). | COMBO | Sì | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `model.custom_width` | Usato solo quando `model.size` è `"Custom"`. Deve essere un multiplo di 16 (predefinito: `1024`). | INT | No | da 480 a 3840 (passo 16) |
| `model.custom_height` | Usato solo quando `model.size` è `"Custom"`. Deve essere un multiplo di 16 (predefinito: `1024`). | INT | No | da 480 a 3840 (passo 16) |
| `model.background` | Restituisce l'immagine con o senza sfondo (predefinito: `"auto"`). | COMBO | Sì | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `model.quality` | Qualità dell'immagine; influisce sui costi e sul tempo di generazione (predefinito: `"low"`). | COMBO | Sì | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.images` | Immagini di riferimento opzionali per la modifica delle immagini. Fino a 16 immagini. Vedi Input di riferimento per i dettagli. | IMAGE | No | da 0 a 16 |
| `model.mask` | Maschera opzionale per l'inpainting (le aree bianche verranno sostituite). Richiede esattamente un'immagine di riferimento. | MASK | No | N/A |

### Input di gpt-image-2

Questi input compaiono quando `model` è impostato su `gpt-image-2`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model.size` | Dimensione immagine. Seleziona `"Custom"` per usare larghezza e altezza personalizzate (predefinito: `"auto"`). | COMBO | Sì | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `model.custom_width` | Usato solo quando `model.size` è `"Custom"`. Deve essere un multiplo di 16 (predefinito: `1024`). | INT | No | da 480 a 3840 (passo 16) |
| `model.custom_height` | Usato solo quando `model.size` è `"Custom"`. Deve essere un multiplo di 16 (predefinito: `1024`). | INT | No | da 480 a 3840 (passo 16) |
| `model.background` | Restituisce l'immagine con o senza sfondo (predefinito: `"auto"`). | COMBO | Sì | `"auto"`<br>`"opaque"` |
| `model.quality` | Qualità dell'immagine; influisce sui costi e sul tempo di generazione (predefinito: `"low"`). | COMBO | Sì | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | Immagini di riferimento opzionali per la modifica delle immagini. Fino a 16 immagini. Vedi Input di riferimento per i dettagli. | IMAGE | No | da 0 a 16 |
| `model.mask` | Maschera opzionale per l'inpainting (le aree bianche verranno sostituite). Richiede esattamente un'immagine di riferimento. | MASK | No | N/A |

### Input di gpt-image-1.5 e gpt-image-1

Questi input compaiono quando `model` è impostato su `gpt-image-1.5` o `gpt-image-1`. Entrambi i modelli condividono lo stesso insieme di parametri.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model.size` | Dimensione immagine (predefinito: `"auto"`). | COMBO | Sì | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"` |
| `model.background` | Restituisce l'immagine con o senza sfondo (predefinito: `"auto"`). | COMBO | Sì | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `model.quality` | Qualità dell'immagine; influisce sui costi e sul tempo di generazione (predefinito: `"low"`). | COMBO | Sì | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | Immagini di riferimento opzionali per la modifica delle immagini. Fino a 16 immagini. Vedi Input di riferimento per i dettagli. | IMAGE | No | da 0 a 16 |
| `model.mask` | Maschera opzionale per l'inpainting (le aree bianche verranno sostituite). Richiede esattamente un'immagine di riferimento. | MASK | No | N/A |

### Input di riferimento

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model.images` | Slot espandibile: collega da 1 a N elementi (ad es. `image_1`...`image_16`); fino a 16 immagini di riferimento per tutti i modelli. | IMAGE | No | da 0 a 16 |
| `model.mask` | Maschera opzionale per l'inpainting (le aree bianche verranno sostituite). Richiede esattamente un'immagine di riferimento. | MASK | No | N/A |

**Vincoli e limitazioni dei parametri:**

- Quando `model.size` è `"Custom"` (solo per `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst` e `gpt-image-2`), sia `model.custom_width` sia `model.custom_height` devono essere multipli di 16, il lato più lungo non deve superare 3840, il rapporto d'aspetto non deve superare 3:1 e il numero totale di pixel deve essere compreso tra 655.360 e 8.294.400.
- `model.mask` richiede esattamente un'immagine di riferimento in `model.images`: non può essere usato senza un'immagine e non può essere usato con più di un'immagine.
- Quando si usa `model.mask`, la sua altezza e larghezza devono corrispondere all'altezza e alla larghezza dell'immagine di riferimento.
- Quando viene fornito `model.images`, il nodo viene eseguito in modalità modifica immagine; senza `model.images`, genera immagini solo dal prompt.
- Le immagini di riferimento e la maschera vengono ridimensionate verso il basso prima di essere inviate all'API.
- I livelli di qualità `"xhigh"` e `"max"` sono disponibili solo per `gpt-image-2.5-flare` e `gpt-image-2.5-sunburst`.
- `seed` attualmente non è implementato nel backend.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | L'immagine o le immagini generate. Tutte le immagini restituite vengono impilate in un unico batch; se le loro dimensioni differiscono, vengono ridimensionate per corrispondere alla prima immagine. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV2/it.md)

---
**Source fingerprint (SHA-256):** `9cf1a9fa3e2cd98aff6c42432164ac5e6c55b7bcdc9815043cb359c6968ac172`
