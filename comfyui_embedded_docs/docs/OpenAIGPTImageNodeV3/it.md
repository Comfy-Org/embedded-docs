# OpenAI GPT Image 2.6

## Panoramica

OpenAI GPT Image 2.6 genera immagini da un prompt e le modifica quando colleghi immagini di riferimento, usando i modelli GPT Image di OpenAI. Il nodo offre quattro modelli: `gpt-image-2.6-flare`, `gpt-image-2.6-sunburst`, `gpt-image-2.5-flare` e `gpt-image-2.5-sunburst`. Disegna annotazioni sulla prima immagine di riferimento e collegale come coppia di markup per mostrare al modello esattamente dove modificare.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello GPT Image da usare. Selezionando un modello vengono mostrati i parametri per quel modello. | DYNAMIC_COMBO | Sì | `"gpt-image-2.6-flare"`<br>`"gpt-image-2.6-sunburst"`<br>`"gpt-image-2.5-flare"`<br>`"gpt-image-2.5-sunburst"` |

### Input di gpt-image-2.6-flare e gpt-image-2.6-sunburst

Questi input compaiono quando `model` è impostato su `gpt-image-2.6-flare` o `gpt-image-2.6-sunburst`. Entrambi i modelli condividono gli stessi parametri.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model.prompt` | Cosa generare, o la modifica da apportare. (predefinito: `""`) | STRING | Sì | N/A |
| `model.size` | Dimensione dell'immagine. Seleziona "Custom" per usare larghezza e altezza personalizzate. (predefinito: `"auto"`) | COMBO | Sì | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `model.custom_width` | Usato solo quando `model.size` è "Custom". Deve essere un multiplo di 16. (predefinito: `1024`) | INT | No | 480 a 3840 (passo 16) |
| `model.custom_height` | Usato solo quando `model.size` è "Custom". Deve essere un multiplo di 16. (predefinito: `1024`) | INT | No | 480 a 3840 (passo 16) |
| `model.background` | Restituisce l'immagine con o senza sfondo. (predefinito: `"auto"`) | COMBO | Sì | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `model.quality` | Qualità dell'immagine. I livelli più alti costano di più e richiedono più tempo. (predefinito: `"low"`) | COMBO | Sì | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.complexity` | Quanto il modello pianifica l'immagine prima del rendering. (predefinito: `"high"`) | COMBO | Sì | `"low"`<br>`"medium"`<br>`"high"` |
| `model.images` | Immagini di riferimento opzionali per la modifica. Fino a 16. | AUTOGROW | No | 0 a 16 |
| `model.markup` | Annotazioni disegnate sopra la prima immagine di riferimento, che mostrano dove modificare. Devono corrispondere alle dimensioni di quell'immagine e devono essere collegate insieme a `model.markup_alpha`. | IMAGE | No | N/A |
| `model.markup_alpha` | Il bianco contrassegna le annotazioni in `model.markup`. L'output MASK del nodo Painter è direttamente compatibile; una maschera di Load Image richiede prima Invert Mask. | MASK | No | N/A |
| `model.seed` | Controlla se il nodo viene rieseguito; i risultati non sono deterministici indipendentemente dal seed. (predefinito: `42`) | INT | Sì | 0 a 2147483647 |

### Input di gpt-image-2.5-flare e gpt-image-2.5-sunburst

Questi input compaiono quando `model` è impostato su `gpt-image-2.5-flare` o `gpt-image-2.5-sunburst`. Corrispondono ai modelli 2.6 tranne per il fatto che `model.complexity` non è offerto.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model.prompt` | Cosa generare, o la modifica da apportare. (predefinito: `""`) | STRING | Sì | N/A |
| `model.size` | Dimensione dell'immagine. Seleziona "Custom" per usare larghezza e altezza personalizzate. (predefinito: `"auto"`) | COMBO | Sì | `"auto"`<br>`"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"`<br>`"2048x2048"`<br>`"2048x1152"`<br>`"1152x2048"`<br>`"3840x2160"`<br>`"2160x3840"`<br>`"Custom"` |
| `model.custom_width` | Usato solo quando `model.size` è "Custom". Deve essere un multiplo di 16. (predefinito: `1024`) | INT | No | 480 a 3840 (passo 16) |
| `model.custom_height` | Usato solo quando `model.size` è "Custom". Deve essere un multiplo di 16. (predefinito: `1024`) | INT | No | 480 a 3840 (passo 16) |
| `model.background` | Restituisce l'immagine con o senza sfondo. (predefinito: `"auto"`) | COMBO | Sì | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `model.quality` | Qualità dell'immagine. I livelli più alti costano di più e richiedono più tempo. (predefinito: `"low"`) | COMBO | Sì | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.images` | Immagini di riferimento opzionali per la modifica. Fino a 16. | AUTOGROW | No | 0 a 16 |
| `model.markup` | Annotazioni disegnate sopra la prima immagine di riferimento, che mostrano dove modificare. Devono corrispondere alle dimensioni di quell'immagine e devono essere collegate insieme a `model.markup_alpha`. | IMAGE | No | N/A |
| `model.markup_alpha` | Il bianco contrassegna le annotazioni in `model.markup`. L'output MASK del nodo Painter è direttamente compatibile; una maschera di Load Image richiede prima Invert Mask. | MASK | No | N/A |
| `model.seed` | Controlla se il nodo viene rieseguito; i risultati non sono deterministici indipendentemente dal seed. (predefinito: `42`) | INT | Sì | 0 a 2147483647 |

**Vincoli e limitazioni dei parametri:**

- Con `model.size` impostato su "Custom", `model.custom_width` e `model.custom_height` devono entrambi essere multipli di 16, il lato più lungo non deve superare 3840, le proporzioni non devono superare 3:1 e il numero totale di pixel deve essere compreso tra 655.360 e 8.294.400.
- `model.markup` e `model.markup_alpha` devono essere collegati insieme. Il markup richiede almeno un'immagine di riferimento e la sua larghezza e altezza devono corrispondere alla prima immagine di riferimento.
- Senza `model.images` il nodo genera immagini solo dal prompt; con immagini di riferimento le modifica e le combina.
- Le immagini di riferimento vengono ridimensionate verso il basso prima di essere inviate all'API.
- `model.complexity` esiste solo su `gpt-image-2.6-flare` e `gpt-image-2.6-sunburst`; i modelli 2.5 usano una profondità di pianificazione fissa.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `image` | L'immagine o le immagini generate. Tutte le immagini restituite vengono impilate in un unico batch; se le loro dimensioni differiscono, vengono ridimensionate per corrispondere alla prima immagine. | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageNodeV3/it.md)

---
**Source fingerprint (SHA-256):** `33f5d91af56c215cc7f7c704f9b123fe1c35bf287012072b818b76b551c04667`
