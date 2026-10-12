# FluxProImageNode

Genera immagini in modo sincrono in base al prompt e alla risoluzione. Questo nodo crea immagini usando il modello Flux 1.1 Pro inviando richieste a un endpoint API e attendendo la risposta completa prima di restituire l'immagine generata.

## Input

| Parametro | Descrizione | Tipo di dato | Obbligatorio | Intervallo |
| --- | --- | --- | --- | --- |
| `prompt` | Prompt per la generazione dell'immagine (predefinito: stringa vuota) | STRING | Sì | - |
| `prompt_upsampling` | Indica se eseguire l'upsampling sul prompt. Se attivo, modifica automaticamente il prompt per una generazione più creativa, ma i risultati non sono deterministici (lo stesso seed non produrrà esattamente lo stesso risultato). (predefinito: False) | BOOLEAN | Sì | - |
| `width` | Larghezza dell'immagine in pixel (predefinito: 1024, passo: 32) | INT | Sì | 256-1440 |
| `height` | Altezza dell'immagine in pixel (predefinito: 768, passo: 32) | INT | Sì | 256-1440 |
| `seed` | Il seed casuale usato per creare il rumore. (predefinito: 0) | INT | Sì | 0-18446744073709551615 |
| `image_prompt` | Immagine di riferimento opzionale per guidare la generazione | IMAGE | No | - |

## Output

| Nome output | Descrizione | Tipo di dato |
| --- | --- | --- |
| `output` | L'immagine generata restituita dall'API | IMAGE |

> Questa documentazione è stata generata dall'IA. Se trovi errori o hai suggerimenti per migliorarla, sentiti libero di contribuire! [Modifica su GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProImageNode/it.md)

---
**Source fingerprint (SHA-256):** `89316d84f364854541157b5b60bae3d4e25024bd4af61a47a1748c6671b463c1`
