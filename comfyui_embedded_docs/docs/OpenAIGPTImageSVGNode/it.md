# OpenAI GPT Image 2.6 SVG

## Panoramica

OpenAI GPT Image 2.6 SVG genera un SVG modificabile da un prompt con i modelli GPT Image di OpenAI. Il risultato è markup vettoriale, quindi forme e testo rimangono modificabili in un editor vettoriale. Sono disponibili due modelli: `gpt-image-2.6-flare` e `gpt-image-2.6-sunburst`.

## Input

### Input comuni

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model` | Il modello GPT Image da usare per l'SVG. | DYNAMIC_COMBO | Sì | `"gpt-image-2.6-flare"`<br>`"gpt-image-2.6-sunburst"` |

### Input di gpt-image-2.6-flare e gpt-image-2.6-sunburst

Entrambi i modelli condividono gli stessi parametri.

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `model.prompt` | Descrizione dell'SVG da disegnare. (predefinito: `""`) | STRING | Sì | N/A |
| `model.size` | Dimensione dell'immagine di riferimento da cui viene disegnato l'SVG. (predefinito: `"1024x1024"`) | COMBO | Sì | `"1024x1024"`<br>`"1024x1536"`<br>`"1536x1024"` |
| `model.background` | Sfondo dell'immagine di riferimento. (predefinito: `"auto"`) | COMBO | Sì | `"auto"`<br>`"opaque"`<br>`"transparent"` |
| `model.quality` | Qualità dell'immagine di riferimento da cui viene disegnato l'SVG. (predefinito: `"low"`) | COMBO | Sì | `"low"`<br>`"medium"`<br>`"high"`<br>`"xhigh"`<br>`"max"` |
| `model.complexity` | Quanto il modello pianifica l'immagine di riferimento prima del rendering. (predefinito: `"high"`) | COMBO | Sì | `"low"`<br>`"medium"`<br>`"high"` |
| `model.seed` | Controlla se il nodo viene rieseguito; i risultati non sono deterministici indipendentemente dal seed. (predefinito: `42`) | INT | Sì | 0 a 2147483647 |

## Output

| Nome output | Descrizione | Tipo di dati |
| --- | --- | --- |
| `svg` | L'immagine vettoriale generata come markup SVG. | SVG |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIGPTImageSVGNode/it.md)

---
**Source fingerprint (SHA-256):** `8ac2f473b265d3b6857e6280a1c017301b124fc6d671ec83a59c677218062c90`
