# OpenAI GPT Image 2.6

Questo nodo genera immagini usando l'API GPT Image di OpenAI. Supporta sei modelli — `gpt-image-2.6-flare`, `gpt-image-2.6-sunburst`, `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst`, `gpt-image-2` e `gpt-image-1.5` — consente di allegare immagini di riferimento per la modifica delle immagini e può usare una maschera per specificare quali parti di un'immagine sostituire.

## Input

### Input comuni

Questi input sono sempre visibili.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `modello` | Il modello OpenAI GPT Image da usare. Selezionando un modello vengono mostrati parametri aggiuntivi specifici per quel modello. | DYNAMIC_COMBO | Sì | `"gpt-image-2.6-flare"`<br>`"gpt-image-2.6-sunburst"`<br>`"gpt-image-2.5-flare"`<br>`"gpt-image-2.5-sunburst"`<br>`"gpt-image-2"`<br>`"gpt-image-1.5"` |
| `prompt` | Prompt testuale per GPT Image (predefinito: `""`). | STRING | Sì | N/D |
| `n` | Quante immagini generare (predefinito: `1`). | INT | Sì | 1 a 8 |
| `seed` | Seed per la riproducibilità (predefinito: `0`). Non ancora implementato nel backend. | INT | Sì | 0 a 2147483647 |

### Input di gpt-image-2.6-flare e gpt-image-2.6-sunburst

Questi input compaiono quando `model` è impostato su `gpt-image-2.6-flare` o `gpt-image-2.6-sunburst`. Entrambi i modelli condividono lo stesso insieme di parametri.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `dimensione` | Dimensione dell'immagine. Seleziona "Custom" per usare larghezza e altezza personalizzate (predefinito: `"auto"`). | COMBO | Sì | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `larghezza_personalizzata` | Usato solo quando `model.size` è "Custom". Deve essere un multiplo di 16 (predefinito: `1024`). | INT | No | 480 a 3840 (passo 16) |
| `altezza_personalizzata` | Usato solo quando `model.size` è "Custom". Deve essere un multiplo di 16 (predefinito: `1024`). | INT | No | 480 a 3840 (passo 16) |
| `sfondo` | Restituisce l'immagine con o senza sfondo (predefinito: `"auto"`). | COMBO | Sì | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `qualità` | Qualità dell'immagine, influisce sul costo e sul tempo di generazione (predefinito: `"low"`). | COMBO | Sì | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.images` | Immagini di riferimento opzionali per la modifica delle immagini. Fino a 16 immagini. Vedi Input di riferimento per i dettagli. | IMAGE | No | 0 a 16 |
| `model.mask` | Maschera opzionale per inpainting (le aree bianche verranno sostituite). Richiede esattamente un'immagine di riferimento. | MASK | No | N/D |
| `model.complexity` | Quanto il modello pianifica l'immagine prima del rendering. Valori più bassi restituiscono più rapidamente, valori più alti pianificano di più. Predefinito: `"high"`. | COMBO | Sì | `"low"`<br>`"medium"`<br>`"high"` |

### Input di gpt-image-2.5-flare e gpt-image-2.5-sunburst

Questi input compaiono quando `model` è impostato su `gpt-image-2.5-flare` o `gpt-image-2.5-sunburst`. Entrambi i modelli condividono lo stesso insieme di parametri.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `dimensione` | Dimensione dell'immagine. Seleziona "Custom" per usare larghezza e altezza personalizzate (predefinito: `"auto"`). | COMBO | Sì | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `larghezza_personalizzata` | Usato solo quando `model.size` è "Custom". Deve essere un multiplo di 16 (predefinito: `1024`). | INT | No | 480 a 3840 (passo 16) |
| `altezza_personalizzata` | Usato solo quando `model.size` è "Custom". Deve essere un multiplo di 16 (predefinito: `1024`). | INT | No | 480 a 3840 (passo 16) |
| `sfondo` | Restituisce l'immagine con o senza sfondo (predefinito: `"auto"`). | COMBO | Sì | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `qualità` | Qualità dell'immagine, influisce sul costo e sul tempo di generazione (predefinito: `"low"`). | COMBO | Sì | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.images` | Immagini di riferimento opzionali per la modifica delle immagini. Fino a 16 immagini. Vedi Input di riferimento per i dettagli. | IMAGE | No | 0 a 16 |
| `model.mask` | Maschera opzionale per inpainting (le aree bianche verranno sostituite). Richiede esattamente un'immagine di riferimento. | MASK | No | N/D |

### Input di gpt-image-2

Questi input compaiono quando `model` è impostato su `gpt-image-2`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `dimensione` | Dimensione dell'immagine. Seleziona "Custom" per usare larghezza e altezza personalizzate (predefinito: `"auto"`). | COMBO | Sì | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `larghezza_personalizzata` | Usato solo quando `model.size` è "Custom". Deve essere un multiplo di 16 (predefinito: `1024`). | INT | No | 480 a 3840 (passo 16) |
| `altezza_personalizzata` | Usato solo quando `model.size` è "Custom". Deve essere un multiplo di 16 (predefinito: `1024`). | INT | No | 480 a 3840 (passo 16) |
| `sfondo` | Restituisce l'immagine con o senza sfondo (predefinito: `"auto"`). | COMBO | Sì | `"auto"`<br>`"opaque"` |
| `qualità` | Qualità dell'immagine, influisce sul costo e sul tempo di generazione (predefinito: `"low"`). | COMBO | Sì | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | Immagini di riferimento opzionali per la modifica delle immagini. Fino a 16 immagini. Vedi Input di riferimento per i dettagli. | IMAGE | No | 0 a 16 |
| `model.mask` | Maschera opzionale per inpainting (le aree bianche verranno sostituite). Richiede esattamente un'immagine di riferimento. | MASK | No | N/D |

### Input di gpt-image-1.5

Questi input compaiono quando `model` è impostato su `gpt-image-1.5`.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `dimensione` | Dimensione dell'immagine (predefinito: `"auto"`). | COMBO | Sì | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"` |
| `sfondo` | Restituisce l'immagine con o senza sfondo (predefinito: `"auto"`). | COMBO | Sì | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `qualità` | Qualità dell'immagine, influisce sul costo e sul tempo di generazione (predefinito: `"low"`). | COMBO | Sì | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | Immagini di riferimento opzionali per la modifica delle immagini. Fino a 16 immagini. Vedi Input di riferimento per i dettagli. | IMAGE | No | 0 a 16 |
| `model.mask` | Maschera opzionale per inpainting (le aree bianche verranno sostituite). Richiede esattamente un'immagine di riferimento. | MASK | No | N/D |

### Input di riferimento

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model.images` | Slot espandibile: collega da 1 a N elementi (ad es. `image_1`...`image_16`); fino a 16 immagini di riferimento per tutti i modelli. | IMAGE | No | 0 a 16 |
| `model.mask` | Maschera opzionale per inpainting (le aree bianche verranno sostituite). Richiede esattamente un'immagine di riferimento. | MASK | No | N/D |

**Vincoli e limitazioni dei parametri:**

- Quando `model.size` è "Custom" (solo `gpt-image-2.6-flare`, `gpt-image-2.6-sunburst`, `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst` e `gpt-image-2`), `model.custom_width` e `model.custom_height` devono essere entrambi multipli di 16, il lato più lungo non deve superare 3840, il rapporto d'aspetto non deve superare 3:1 e il numero totale di pixel deve essere compreso tra 655,360 e 8,294,400.
- `model.mask` richiede esattamente un'immagine di riferimento in `model.images`: non può essere usato senza un'immagine e non può essere usato con più di un'immagine.
- Quando viene usato `model.mask`, la sua altezza e larghezza devono corrispondere all'altezza e alla larghezza dell'immagine di riferimento.
- Quando viene fornito `model.images`, il nodo viene eseguito in modalità modifica immagine; senza `model.images`, genera immagini solo dal prompt.
- Le immagini di riferimento e la maschera vengono ridimensionate verso il basso prima di essere inviate all'API.
- I livelli di qualità `"xhigh"` e `"max"` sono disponibili solo per `gpt-image-2.6-flare`, `gpt-image-2.6-sunburst`, `gpt-image-2.5-flare` e `gpt-image-2.5-sunburst`.
- `model.complexity` è disponibile solo per `gpt-image-2.6-flare` e `gpt-image-2.6-sunburst`; gli altri modelli usano una profondità di pianificazione fissa.
- `seed` al momento non è implementato nel backend.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | L'immagine o le immagini generate. Tutte le immagini restituite vengono impilate in un unico batch; se le loro dimensioni differiscono, vengono ridimensionate per corrispondere alla prima immagine. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV2/it.md)

---
**Source fingerprint (SHA-256):** `36e8dbe4e35d0473ccf16482f640769e8bc30c345bc062a6785a48d7336efa03`
