# OpenAI GPT Image 2.6 GIF

## Panoramica

OpenAI GPT Image 2.6 GIF genera una GIF animata da un prompt con i modelli GPT Image di OpenAI e la restituisce come batch di fotogrammi insieme alla frequenza dei fotogrammi, così può essere inviata direttamente a un nodo di salvataggio video o immagini animate. Sono disponibili due modelli: `gpt-image-2.6-flare` e `gpt-image-2.6-sunburst`.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello GPT Image da usare per l'animazione. | DYNAMIC_COMBO | Sì | `"gpt-image-2.6-flare"`<br>`"gpt-image-2.6-sunburst"` |

### Input di gpt-image-2.6-flare e gpt-image-2.6-sunburst

Entrambi i modelli condividono gli stessi parametri.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model.prompt` | Cosa animare. (predefinito: `""`) | STRING | Sì | N/A |
| `model.size` | Dimensione di ciascun fotogramma. Le dimensioni più grandi supportano solo un numero inferiore di fotogrammi. (predefinito: `"512x512"`) | COMBO | Sì | `"384x384"`<br>`"512x512"`<br>`"640x640"`<br>`"720x720"`<br>`"768x768"`<br>`"960x960"`<br>`"512x288"`<br>`"288x512"`<br>`"1024x576"`<br>`"576x1024"`<br>`"1280x720"`<br>`"720x1280"` |
| `model.frame_count` | Numero di fotogrammi. I fotogrammi vengono fatturati a scaglioni: 2 a 8, 9, 10 a 12, 13 a 16. (predefinito: `9`) | INT | Sì | 2 a 16 |
| `model.frame_duration_ms` | Durata di visualizzazione di ciascun fotogramma, in millisecondi. (predefinito: `200`) | INT | Sì | 20 a 2000 (passo 10) |
| `model.background` | Sfondo del fotogramma. La trasparenza viene mantenuta da Save WEBM con vp9, Save Animated WEBP e Save Animated PNG. (predefinito: `"opaque"`) | COMBO | Sì | `"opaque"`<br>`"transparent"` |
| `model.quality` | Qualità dell'immagine. I livelli più alti costano di più e richiedono più tempo. (predefinito: `"low"`) | COMBO | Sì | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.complexity` | Quanto il modello pianifica l'animazione prima del rendering. (predefinito: `"high"`) | COMBO | Sì | `"low"`<br>`"medium"`<br>`"high"` |
| `model.seed` | Controlla se il nodo viene rieseguito; i risultati non sono deterministici indipendentemente dal seed. (predefinito: `42`) | INT | Sì | 0 a 2147483647 |

**Vincoli e limitazioni dei parametri:**

- La frequenza dei fotogrammi viene calcolata da `model.frame_duration_ms`: 200 ms corrispondono a 5 fps.
- Un valore elevato di `model.size` combinato con un `model.frame_count` elevato non è disponibile e mostra "Size too large for this frame count" sul badge del prezzo.

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `frames` | L'animazione come batch di fotogrammi, pronta per un nodo di salvataggio video o immagini animate. | IMAGE |
| `fps` | Fotogrammi al secondo, letti dalla durata dei fotogrammi della GIF restituita. | FLOAT |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageGIFNode/it.md)

---
**Source fingerprint (SHA-256):** `e47ebaef90f8b2618ef3c2659778f75ac9763013dcc515ba5650764ce49da951`
