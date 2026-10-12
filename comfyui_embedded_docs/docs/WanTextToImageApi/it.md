# WanTextToImageApi

Il nodo Wan Text to Image genera immagini basate su descrizioni testuali. Utilizza modelli di IA per creare contenuti visivi a partire da prompt scritti, supportando input testuali sia in inglese che in cinese. Il nodo fornisce vari controlli per regolare dimensioni, qualità e preferenze di stile dell'immagine di output.

## Input

| Parametro | Descrizione | Tipo di dati | Obbligatorio | Intervallo |
|-----------|-------------|--------------|--------------|------------|
| `model` | Modello da usare (predefinito: "wan2.5-t2i-preview") | STRING | Sì | "wan2.5-t2i-preview" |
| `prompt` | Prompt che descrive gli elementi e le caratteristiche visive. Supporta inglese e cinese (predefinito: vuoto) | STRING | Sì | - |
| `negative_prompt` | Prompt negativo che descrive ciò che si desidera evitare (predefinito: vuoto) | STRING | No | - |
| `width` | Larghezza dell'immagine in pixel (predefinito: 1024, passo: 32) | INT | No | 768-1440 |
| `height` | Altezza dell'immagine in pixel (predefinito: 1024, passo: 32) | INT | No | 768-1440 |
| `seed` | Seed da usare per la generazione (predefinito: 0) | INT | No | 0-2147483647 |
| `prompt_extend` | Indica se migliorare il prompt con l'assistenza dell'IA (predefinito: True) | BOOLEAN | No | - |
| `watermark` | Indica se aggiungere una filigrana generata dall'IA al risultato (predefinito: False) | BOOLEAN | No | - |

## Output

| Nome output | Descrizione | Tipo di dati |
|-------------|-------------|--------------|
| `output` | L'immagine generata in base al prompt testuale | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTextToImageApi/it.md)

---
**Source fingerprint (SHA-256):** `208b7c839da45316aeb1a14a3e9d176eeb09b2f931f764fb8a296da15ae3bd4e`
